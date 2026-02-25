# Figma MCP Integration — Handoff Document

## Current State (2026-02-25)

### What's Done

1. **Figma MCP servers registered** in `~/.claude.json` (user-scoped):
   - `figma` → `https://mcp.figma.com/mcp` (remote, needs OAuth)
   - `figma-desktop` → `http://127.0.0.1:3845/mcp` (local, needs Figma desktop running)

2. **CLAUDE.md updated** — Section 9 "Figma Integration" added with full workflow docs, troubleshooting, and Figma project structure guide. Committed on `main`:
   ```
   6134202 docs: add Figma MCP integration section to CLAUDE.md
   ```

### What's NOT Done Yet

#### A. Authenticate the Remote Figma MCP (required)
```bash
# In Claude Code, run:
/mcp
# → Select "figma"
# → Choose "Authenticate"
# → Complete OAuth flow in browser
```

#### B. Test Code to Canvas with an Existing Presentation
```bash
cd presentations/onoffice-c-level/
python3 -m http.server 8080
# Open http://localhost:8080/index.html in browser
# In Claude Code: "Send this to Figma"
```

**Evaluate these after capture:**
- [ ] Text is editable in Figma (not rasterized/vectorized paths)
- [ ] Colors correct: `#0080FF` (blue), `#1a1a2e` (black), `#fcfcff` (white)
- [ ] Slide dimensions are 1920×1080 in Figma
- [ ] Inline SVG icons (Heroicons) are editable vectors
- [ ] Google Fonts (Newsreader, Inter) render correctly or need Figma font install
- [ ] CSS custom properties resolved to final values
- [ ] Grid background pattern (SVG) transfers or needs recreation

#### C. If Code to Canvas Quality Is Poor → Set Up Fallback
```bash
npx claude-talk-to-figma-mcp
# Install companion Figma plugin from:
# https://www.figma.com/community/plugin/claude-talk-to-figma
# Then:
claude mcp add --transport sse claude-talk-to-figma ws://localhost:3055
```

#### D. Create Figma Project File
Create "immoautomation Presentations" in Figma with:
- Page per presentation (onOffice C-Level, Webinar 2026, etc.)
- Shared color styles matching CSS custom properties
- Shared text styles for Newsreader + Inter
- 1920×1080 frame template

#### E. Install Google Fonts in Figma (if needed)
If fonts don't transfer via Code to Canvas:
- Download Newsreader + Inter from Google Fonts
- Add to Figma team font library

## Key Context

### Figma Plan Requirements
- **Pro/Organization/Enterprise** required for meaningful use
- Pro/Org: 200 tool calls/day, 15-20/min
- Starter: only 6 calls/month (not viable)
- Enterprise: 600 calls/day

### How Code to Canvas Works
1. HTML must be rendered in a browser (dev server or file)
2. "Send this to Figma" captures the **current viewport** as editable layers
3. One slide per capture — navigate to next slide, repeat
4. Multi-slide = multiple captures (adds token overhead)
5. Output is editable Figma frames, not screenshots

### Fallback Option: claude-talk-to-figma-mcp
- Community MCP by arinspunk, full read+write Figma access via WebSocket
- Works with **any Figma plan including free**
- Claude reads HTML + design system → creates Figma frames programmatically
- Slower but gives full control over output structure

### Files Modified
- `CLAUDE.md` — added Section 9 (Figma Integration), 132 lines
- `~/.claude.json` — added `figma` and `figma-desktop` mcpServers

### Relevant Docs
- [Figma MCP Server](https://developers.figma.com/docs/figma-mcp-server/)
- [Remote setup](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- [Desktop setup](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)
- [Plans & access](https://developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/)
- [Code to Canvas blog](https://www.figma.com/blog/introducing-claude-code-to-figma/)
- [claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)

## Open Questions
1. Which Figma plan does the team have? (determines daily call limits)
2. Multi-slide: can all slides be captured in one session, or does each need a separate prompt?
3. Do Google Fonts resolve from the browser render, or must they be in Figma's font library?
