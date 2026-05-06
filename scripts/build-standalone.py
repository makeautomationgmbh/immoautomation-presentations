#!/usr/bin/env python3
"""
build-standalone.py — Bundle a presentation's index.html into a single self-contained file.

Inlines:
- Local images (logos/, uploads/, …) as data URIs
- Google Fonts as base64-encoded @font-face declarations

Usage:
  python3 scripts/build-standalone.py [presentation-folder]

Default presentation folder: presentations/onoffice-business-beats
Output: <folder>/index-standalone.html  (single self-contained HTML, openable offline)
"""

import sys
import re
import base64
import urllib.request
from pathlib import Path
from urllib.parse import quote

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

MIME = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".svg": "image/svg+xml",
    ".webp": "image/webp",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
}


def fetch(url: str, headers: dict | None = None) -> bytes:
    req = urllib.request.Request(url, headers=headers or {"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def b64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def inline_local_images(html: str, base_dir: Path) -> str:
    """Replace <img src="local-path"> with data: URIs."""
    pattern = re.compile(r'src="((?!https?://|data:|#)[^"]+)"')
    cache: dict[str, str] = {}

    def replace(m: re.Match) -> str:
        src = m.group(1)
        if src in cache:
            return f'src="{cache[src]}"'
        path = base_dir / src
        if not path.is_file():
            print(f"  [skip image] {src} not found")
            return m.group(0)
        ext = path.suffix.lower()
        mime = MIME.get(ext, "application/octet-stream")
        if ext == ".svg":
            data = path.read_text(encoding="utf-8")
            uri = f"data:{mime};utf8,{quote(data)}"
        else:
            data = path.read_bytes()
            uri = f"data:{mime};base64,{b64(data)}"
        cache[src] = uri
        size_kb = len(uri) / 1024
        print(f"  inlined {src} ({size_kb:.1f} KB)")
        return f'src="{uri}"'

    return pattern.sub(replace, html)


def inline_google_fonts(html: str) -> str:
    """Replace Google Fonts <link> tags with <style> containing @font-face + base64 woff2."""
    link_pattern = re.compile(
        r'<link[^>]*href="(https://fonts\.googleapis\.com/css2[^"]+)"[^>]*>',
        re.IGNORECASE,
    )
    matches = link_pattern.findall(html)
    if not matches:
        print("  [skip fonts] no Google Fonts link found")
        return html

    inlined_css_blocks: list[str] = []
    for url in matches:
        print(f"  fetching {url[:90]}...")
        try:
            css = fetch(url).decode("utf-8")
        except Exception as e:
            print(f"  [warn] failed to fetch CSS: {e}")
            continue

        # Find each woff2 URL and replace with base64
        woff2_pattern = re.compile(
            r"src:\s*url\((https://fonts\.gstatic\.com[^)]+\.woff2)\)\s*format\(['\"]?woff2['\"]?\)"
        )

        font_cache: dict[str, str] = {}

        def replace_font(m: re.Match) -> str:
            font_url = m.group(1)
            if font_url in font_cache:
                return font_cache[font_url]
            try:
                data = fetch(font_url)
                replacement = (
                    f"src: url(data:font/woff2;base64,{b64(data)}) format('woff2')"
                )
                font_cache[font_url] = replacement
                size_kb = len(data) / 1024
                print(f"    inlined font ({size_kb:.1f} KB)")
                return replacement
            except Exception as e:
                print(f"    [warn] failed font {font_url}: {e}")
                return m.group(0)

        css = woff2_pattern.sub(replace_font, css)
        inlined_css_blocks.append(f"<style>\n/* Google Fonts (inlined) */\n{css}\n</style>")

    # Strip all preconnect + Google Fonts links
    html = re.sub(
        r'<link[^>]*rel="preconnect"[^>]*href="https://fonts\.[^"]+"[^>]*>\s*',
        "",
        html,
        flags=re.IGNORECASE,
    )
    html = re.sub(
        r'<link[^>]*href="https://fonts\.googleapis\.com[^"]+"[^>]*>\s*',
        "",
        html,
        flags=re.IGNORECASE,
    )

    # Inject inlined CSS before </head>
    if inlined_css_blocks:
        html = html.replace(
            "</head>",
            "\n".join(inlined_css_blocks) + "\n</head>",
            1,
        )
    return html


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    rel = sys.argv[1] if len(sys.argv) > 1 else "presentations/onoffice-business-beats"
    folder = repo_root / rel

    src = folder / "index.html"
    dst = folder / "index-standalone.html"

    if not src.is_file():
        print(f"ERROR: {src} not found")
        return 1

    print(f"Reading {src.relative_to(repo_root)}")
    html = src.read_text(encoding="utf-8")
    original_size = len(html.encode("utf-8"))

    print("\nInlining local images...")
    html = inline_local_images(html, folder)

    print("\nInlining Google Fonts...")
    html = inline_google_fonts(html)

    print(f"\nWriting {dst.relative_to(repo_root)}")
    dst.write_text(html, encoding="utf-8")

    new_size = dst.stat().st_size
    print(
        f"\nDone! Standalone HTML: {new_size / (1024 * 1024):.2f} MB "
        f"(was {original_size / 1024:.0f} KB)"
    )
    print(f"Open directly in any browser — no server, no internet, no extra files needed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
