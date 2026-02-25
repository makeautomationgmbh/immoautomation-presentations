# Figma MCP Integration — Handoff Document

## Current State (2026-02-25)

### What's Done

1. **Figma MCP servers registered** in `~/.claude.json` (user-scoped):
   - `figma` → `https://mcp.figma.com/mcp` (remote, OAuth authenticated)
   - `figma-desktop` → `http://127.0.0.1:3845/mcp` (local, needs Figma desktop running)

2. **CLAUDE.md updated** — Section 9 "Figma Integration" added with full workflow docs, troubleshooting, and Figma project structure guide.

3. **Remote Figma MCP authenticated** — OAuth flow completed via `/mcp` → `figma` → Authenticate.

4. **Code to Canvas tested** — All 6 slides of `claude-code-workflow` presentation captured into Figma file `367UXfjc4t9sS925fuLZFO` ("immoautomation Presentations" in Niklas Kietaibl's team).

### Proven Workflow: Sequential Slide Capture

**Critical constraints discovered during testing:**

| Constraint | Detail |
|-----------|--------|
| **Foreground only** | Background tabs expire with "Erfassung abgelaufen". Captures MUST happen one tab at a time. |
| **One ID per slide** | Each capture ID is single-use. Pre-generate all IDs, then use sequentially. |
| **Tab cleanup required** | Close each browser tab after capture to avoid clutter. Use AppleScript. |
| **~8s per slide** | 2s figmadelay + ~6s processing. 6 slides ≈ 50s total. |

**Correct capture sequence (minimizes permission prompts):**

1. **Prep HTML** — Inject capture script + `?slide=N` query param handler (temporary)
2. **Start server** — `python3 -m http.server 8080` from repo root
3. **Capture slide 1** — `outputMode: newFile` → get `fileKey` from result
4. **Pre-generate remaining capture IDs** — `outputMode: existingFile` with `fileKey`, all at once
5. **Run single bash loop** — Opens each slide URL, waits 8s, closes tab via AppleScript, repeats
6. **Poll all IDs** — Confirm all completed
7. **Clean up HTML** — Remove capture script and query param handler

```bash
# Example capture loop (single permission prompt for the whole script)
BASE="http://localhost:8080/presentations/YYYY-MM-name/file.html"
CAPTURE_IDS=("id1" "id2" "id3" "id4" "id5" "id6")
ENDPOINT="https%3A%2F%2Fmcp.figma.com%2Fmcp%2Fcapture"

for i in "${!CAPTURE_IDS[@]}"; do
  SLIDE=$((i + 1))
  CID="${CAPTURE_IDS[$i]}"
  open "${BASE}?slide=${SLIDE}#figmacapture=${CID}&figmaendpoint=${ENDPOINT}%2F${CID}%2Fsubmit&figmadelay=2000"
  sleep 8
  osascript -e 'tell application "Google Chrome" to close active tab of front window'
  sleep 1
done
```

### What's NOT Done Yet

#### A. Evaluate Transfer Quality
Check the test file (`367UXfjc4t9sS925fuLZFO`) in Figma:
- [ ] Text is editable in Figma (not rasterized/vectorized paths)
- [ ] Colors correct: `#0080FF` (blue), `#1a1a2e` (black), `#fcfcff` (white)
- [ ] Slide dimensions are 1920×1080 in Figma
- [ ] Inline SVG icons (Heroicons) are editable vectors
- [ ] Google Fonts (Newsreader, Inter) render correctly or need Figma font install
- [ ] CSS custom properties resolved to final values
- [ ] Grid background pattern (SVG) transfers or needs recreation

#### B. If Code to Canvas Quality Is Poor → Set Up Fallback
```bash
npx claude-talk-to-figma-mcp
# Install companion Figma plugin from:
# https://www.figma.com/community/plugin/claude-talk-to-figma
# Then:
claude mcp add --transport sse claude-talk-to-figma ws://localhost:3055
```

#### C. Create Figma Design System Page
In the test file or a new file, create a "Design System Reference" page with:
- Shared color styles matching CSS custom properties
- Shared text styles for Newsreader + Inter
- 1920×1080 frame template
- Reusable components (Section Label, Three-Line Headline, Numbered Card, Stat Bar)

#### D. Install Google Fonts in Figma (if needed)
If fonts don't transfer via Code to Canvas:
- Download Newsreader + Inter from Google Fonts
- Add to Figma team font library

## Key Context

### Figma Team & Plan
- **Team:** Niklas Kietaibl's team (`planKey: team::1608463837990304956`)
- **Plan requirements:** Pro/Organization/Enterprise for meaningful use
- Pro/Org: 200 tool calls/day, 15-20/min
- Starter: only 6 calls/month (not viable)
- Enterprise: 600 calls/day

### Fallback Option: claude-talk-to-figma-mcp
- Community MCP by arinspunk, full read+write Figma access via WebSocket
- Works with **any Figma plan including free**
- Claude reads HTML + design system → creates Figma frames programmatically
- Slower but gives full control over output structure

### Files Modified
- `CLAUDE.md` — Section 9 (Figma Integration)
- `~/.claude.json` — `figma` and `figma-desktop` mcpServers
- `FIGMA-MCP-HANDOFF.md` — this file

### Relevant Docs
- [Figma MCP Server](https://developers.figma.com/docs/figma-mcp-server/)
- [Remote setup](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- [Desktop setup](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)
- [Plans & access](https://developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/)
- [Code to Canvas blog](https://www.figma.com/blog/introducing-claude-code-to-figma/)
- [claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)

## Open Questions
1. Which Figma plan does the team have? (determines daily call limits)
2. Do Google Fonts resolve from the browser render, or must they be in Figma's font library?
3. Which browser does the user prefer? (Chrome vs Safari — affects AppleScript tab close command)
