#!/usr/bin/env python3
"""
replace-emojis-with-svg.py — Replace Unicode emojis in index.html with inline Twemoji SVGs.

Why: native emoji rendering varies per OS (Apple Color Emoji on Mac,
Segoe UI Emoji on Windows, Noto Color Emoji on Linux). Inline Twemoji SVGs
render identically everywhere — no font dependency, no platform variation.

Usage:
  python3 scripts/replace-emojis-with-svg.py [path/to/index.html]

Default target: presentations/onoffice-business-beats/index.html
Modifies the file IN PLACE. Re-running is safe — already-replaced emojis are gone.
"""

import re
import sys
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124"
TWEMOJI_VERSION = "15.1.0"
TWEMOJI_URL = (
    "https://cdn.jsdelivr.net/gh/jdecked/twemoji@"
    + TWEMOJI_VERSION
    + "/assets/svg/{codepoint}.svg"
)

# Emoji ranges: Misc Technical, Misc Symbols + Dingbats, all Emoji blocks
EMOJI_PATTERN = re.compile(
    r"[\U0001F300-\U0001F9FF\U0001FA70-\U0001FAFF⌀-➿\U0001F000-\U0001F02F]"
)
VS16 = "️"  # variation selector that requests emoji presentation


def fetch_svg(emoji: str) -> str | None:
    codepoint = format(ord(emoji), "x").lower()
    url = TWEMOJI_URL.format(codepoint=codepoint)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        print(f"  [skip {emoji} U+{ord(emoji):04X}] {e}")
        return None


def make_inline_svg(svg_content: str, emoji_char: str) -> str:
    """Strip XML decl + inject class/sizing attrs so the SVG scales with surrounding font-size.

    IMPORTANT: aria-label uses the codepoint, NOT the emoji char itself, to avoid
    re-matching during emoji replacement (which would cause nested SVGs).
    """
    svg_content = re.sub(r"<\?xml[^?]*\?>\s*", "", svg_content)
    codepoint_label = f"emoji-U{ord(emoji_char):04X}"
    # Inject attrs into the opening <svg> tag using regular (unescaped) quotes
    svg_content = re.sub(
        r"<svg\b([^>]*)>",
        (
            r'<svg\1 class="twemoji" '
            'style="width:1em;height:1em;vertical-align:-0.125em;display:inline-block" '
            f'aria-label="{codepoint_label}">'
        ),
        svg_content,
        count=1,
    )
    return svg_content.strip()


def main() -> int:
    target = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else Path("presentations/onoffice-business-beats/index.html")
    )
    if not target.is_file():
        print(f"ERROR: {target} not found")
        return 1

    print(f"Reading {target}")
    html = target.read_text(encoding="utf-8")

    emojis_found = sorted(set(EMOJI_PATTERN.findall(html)))
    if not emojis_found:
        print("No emojis to replace.")
        return 0

    print(
        f"Found {len(emojis_found)} unique emojis "
        f"({sum(html.count(e) for e in emojis_found)} total occurrences)"
    )

    print("\nFetching Twemoji SVGs...")
    svg_cache: dict[str, str] = {}
    for emoji in emojis_found:
        svg = fetch_svg(emoji)
        if svg:
            svg_cache[emoji] = make_inline_svg(svg, emoji)
            print(f"  OK  {emoji} U+{ord(emoji):04X} ({len(svg)} bytes raw SVG)")

    if not svg_cache:
        print("No SVGs fetched. Nothing to replace.")
        return 0

    # Single-pass regex replacement — avoids re-matching emoji chars that may
    # appear inside the inserted SVG's own attributes/content.
    print("\nReplacing in HTML (single-pass regex)...")
    char_class = "".join(re.escape(e) for e in svg_cache.keys())
    pattern = re.compile(f"([{char_class}])️?")
    counter = {"n": 0}

    def replacer(match: re.Match) -> str:
        emoji_char = match.group(1)
        counter["n"] += 1
        return svg_cache[emoji_char]

    html = pattern.sub(replacer, html)
    # Strip any orphan variation selectors left over (rare)
    html = html.replace(VS16, "")

    print(f"\nWriting {target}")
    target.write_text(html, encoding="utf-8")
    print(f"Done. {counter['n']} emoji occurrences replaced with inline Twemoji SVG.")
    print("Identical rendering now on Mac / Windows / Linux / any browser.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
