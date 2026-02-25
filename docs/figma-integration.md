# Figma Integration

> Workflow for pushing HTML presentations to Figma. Read this when the user wants to send slides to Figma.

### Overview

Presentations generated in this repo can be pushed to Figma as **fully editable design layers** (not flat screenshots). This enables a workflow where Claude Code generates the HTML slides, then the team polishes fonts, spacing, and layout in Figma.

```
Claude Code (this repo)
  │  generates HTML slides
  │  serves locally in browser
  ▼
"Send this to Figma" (Code to Canvas)
  │  Figma MCP captures rendered browser state
  ▼
Figma Canvas
  │  editable frames arrive (text, shapes, colors)
  │  team polishes: fonts, spacing, alignment
  ▼
Final Presentation (exported from Figma)
```

### MCP Servers (Pre-Configured)

Two Figma MCP servers are configured in `~/.claude.json` (user-scoped, available across all projects):

| Server | URL | When to Use |
|--------|-----|-------------|
| **figma** (remote) | `https://mcp.figma.com/mcp` | Default. No desktop app needed. Requires OAuth login. |
| **figma-desktop** (local) | `http://127.0.0.1:3845/mcp` | When Figma desktop app is running with Dev Mode MCP enabled. |

**Figma plan requirement:** Pro, Organization, or Enterprise plan required. Starter plan is limited to 6 tool calls/month. Pro/Org plans get 200 calls/day.

### Primary Workflow: Code to Canvas

**Prerequisites:**
- Figma Pro/Organization/Enterprise plan with Full or Dev seat
- Figma MCP server authenticated (run `/mcp` in Claude Code → select `figma` → Authenticate)

**Steps:**

1. **Serve the presentation locally:**
   ```bash
   cd presentations/YYYY-MM-project-name/
   python3 -m http.server 8080
   ```

2. **Open in browser:**
   Navigate to `http://localhost:8080/index.html`

3. **Navigate to the slide you want to capture:**
   Use arrow keys to reach the desired slide.

4. **In Claude Code, type:**
   > "Send this to Figma"

5. **Repeat for each slide:**
   Code to Canvas captures the current browser viewport. Navigate to the next slide and repeat.

6. **In Figma:**
   Each captured slide arrives as an editable frame (1920x1080). Team can adjust text, colors, spacing, and typography.

### What Transfers to Figma

| Element | Transfer Quality | Notes |
|---------|-----------------|-------|
| Text content | Editable text layers | Not rasterized |
| Colors | Resolved CSS values | Custom properties resolve to final hex/rgba |
| Layout/positioning | Accurate | 1920x1080 viewport preserved |
| Inline SVG icons | Editable vectors | Heroicons transfer well |
| Google Fonts (Inter, Newsreader) | May need manual setup | Install in Figma team font library if not resolved |
| CSS animations | Ignored (static capture) | Expected — slides are captured as static frames |
| Grid background pattern | May rasterize | SVG pattern might flatten — cosmetic, easy to recreate |

### Alternative: claude-talk-to-figma-mcp (Programmatic)

If Code to Canvas results aren't satisfactory (e.g., fonts don't transfer, SVGs rasterize), use the community [claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp) server for full programmatic Figma creation.

**Setup:**
```bash
# Start the MCP server
npx claude-talk-to-figma-mcp

# Install the companion Figma plugin:
# https://www.figma.com/community/plugin/claude-talk-to-figma

# Add to Claude Code:
claude mcp add --transport sse claude-talk-to-figma ws://localhost:3055
```

**How it works:** Claude reads the HTML presentation content and design system from this CLAUDE.md, then creates Figma frames, text, shapes, and colors programmatically via WebSocket. Works with any Figma plan (including free).

### Figma Project Structure

When creating the Figma file for presentations, use this structure:

```
📁 immoautomation Presentations
├── 📄 onOffice C-Level          (page per presentation)
├── 📄 Webinar 2026
├── 📄 Social Media 2026
└── 📄 Design System Reference
    ├── Color Styles
    │   ├── Blue / #0080FF
    │   ├── Blue Hover / #0066CC
    │   ├── Black / #1a1a2e
    │   ├── White / #fcfcff
    │   ├── Red / #dc2626
    │   ├── Gold / #ca8a04
    │   └── Green / #10B981
    ├── Text Styles
    │   ├── Newsreader Italic 400 (accent/headlines)
    │   └── Inter 300-900 (body/UI)
    └── Reusable Components
        ├── Slide Frame (1920x1080)
        ├── Section Label
        ├── Three-Line Headline
        ├── Numbered Card
        └── Stat Bar
```

### Troubleshooting

| Issue | Solution |
|-------|----------|
| "Figma MCP needs authentication" | Run `/mcp` → select `figma` → Authenticate |
| figma-desktop won't connect | Ensure Figma desktop app is open, Dev Mode enabled (Shift+D), and MCP server toggled on |
| Fonts look wrong in Figma | Install Newsreader and Inter from Google Fonts into your Figma team's font library |
| Colors are off | CSS custom properties should resolve to final values; if not, check that the browser rendered correctly before capture |
| Rate limit hit (200/day) | Switch to figma-desktop (local server) which may have different limits, or batch captures |
