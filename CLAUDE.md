# CLAUDE.md — immoautomation Presentations

This repository is for **marketing presentations, newsletters, and collateral** — NOT product code.
The product codebase lives in a separate repo (`immoautomation_SMA_SaaS`).

---

## 1. Purpose & Workflow

### What belongs here
- Slide deck presentations (HTML)
- Newsletter templates
- Image galleries and marketing collateral
- Pitch decks, webinar slides, partner presentations

### What does NOT belong here
- Product source code, components, or Edge Functions
- Database migrations or API logic

### Git Workflow
Simple workflow — no Gitflow complexity needed:
- **`main`** — default branch, always up to date
- Short-lived branches for larger projects: `presentation/name`, `newsletter/name`
- Commit directly to `main` for small additions

### File Organization
```
presentations/YYYY-MM-project-name/   — Slide decks
newsletters/YYYY-MM-project-name/     — Email templates
gallery/project-name/                  — Image galleries
assets/                                — Logos and brand assets (shared)
docs/                                  — Reference documentation (see below)
```

### Technical Format
All slides are **self-contained HTML files**:
- No build tools, no bundlers, no npm
- Inline CSS (no external frameworks)
- Google Fonts as only external dependency
- Vanilla JS for navigation
- Open any `.html` file in a browser to view

---

## 2. Design System

### Colors (CSS Custom Properties)

```css
:root {
  /* Primary */
  --blue: #0080FF;
  --blue-hover: #0066CC;
  --blue-light: rgba(0, 128, 255, 0.1);
  --blue-glow: rgba(0, 128, 255, 0.2);

  /* Neutrals */
  --black: #1a1a2e;
  --white: #fcfcff;
  --gray-light: rgba(0, 0, 0, 0.04);

  /* Text */
  --text-secondary: rgba(0, 0, 0, 0.5);
  --text-muted: rgba(0, 0, 0, 0.35);

  /* Borders */
  --border: rgba(0, 0, 0, 0.08);

  /* Accent (for problems/warnings) */
  --red: #dc2626;
  --red-light: rgba(220, 38, 38, 0.08);

  /* Accent (for premium/gold) */
  --gold: #ca8a04;
  --gold-light: rgba(234, 179, 8, 0.1);

  /* Success */
  --green: #10B981;
}
```

### Typography

**Import** (include in every HTML `<head>`):
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&family=Inter:wght@300;400;500;600;700;900&display=swap" rel="stylesheet" />
```

| Role | Font | Weights | Usage |
|------|------|---------|-------|
| Display / Headlines | `'Newsreader', Georgia, serif` | 400 italic | Accent text, first line of headlines |
| Body / UI | `'Inter', -apple-system, sans-serif` | 300–900 | Everything else |

**Headline pattern** (three-line formula used across all slides):
```html
<span style="font-family:'Newsreader',serif;font-style:italic;font-weight:400;">Accent line</span><br/>
<span style="font-weight:600;color:var(--blue);">Bold blue emphasis</span><br/>
<span style="font-weight:300;font-size:48px;color:var(--text-muted);">Lighter subtitle line</span>
```

### Visual Identity

| Property | Value | Notes |
|----------|-------|-------|
| Border radius | `0px` everywhere | Sharp, modern aesthetic |
| Grid background | 100x100px SVG pattern, 3% opacity | Subtle texture on every slide |
| Section labels | 14px uppercase, 0.3em letter-spacing | `color: var(--text-muted)` |
| Card numbers | 12px monospace, 12% opacity | Position: top-right of cards |
| Animations | slideUp, fadeIn, scaleIn, slideLeft, slideRight | Staggered with `.delay-1` through `.delay-8` |

**Logo rendering**: "immo" in blue (#0080FF) + "automation" in black (#1a1a2e). Use the logo files in `assets/`.

---

## 3. Presentation Technical Standards

### Dimensions
- **1920 x 1080px** (Full HD, Canva-compatible)
- Padding: `72px 100px` per slide
- Content max-width: `1720px`

### Dynamic Scaling (REQUIRED)

All presentations MUST scale dynamically with the browser window. The slide content is designed at 1920x1080 but rendered inside a scale container that fits any viewport:

```css
html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.scale-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: var(--black);
}

.slides-wrapper {
  width: 1920px;
  height: 1080px;
  transform-origin: center center;
  flex-shrink: 0;
}
```

```js
function scalePresentation() {
  var wrapper = document.getElementById('slidesWrapper');
  var vw = window.innerWidth;
  var vh = window.innerHeight;
  var scale = Math.min(vw / 1920, vh / 1080);
  wrapper.style.transform = 'scale(' + scale + ')';
}
window.addEventListener('resize', scalePresentation);
document.addEventListener('fullscreenchange', function() {
  setTimeout(scalePresentation, 100);
});
scalePresentation();
```

**Viewport meta tag**: Use `width=device-width` (NOT `width=1920`):
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

### HTML Boilerplate

For the full HTML boilerplate template, see **[docs/html-boilerplate.md](docs/html-boilerplate.md)**.

---

## 4. Brand Voice Guidelines

### Tone
- **Professional yet approachable** — not corporate-stiff, not casual-sloppy
- **German language** — all marketing content in German
- **Semi-formal** — use "Sie" (formal you) in all customer-facing materials
- **Efficiency-focused** — always quantify time savings ("30 Sekunden", "140x schneller", "2–3 Stunden pro Woche")
- **Trust-building** — emphasize data security and compliance ("DSGVO-konform", "Hosting in Deutschland")
- **Action-oriented** — CTAs use imperative verbs ("Starten Sie", "Testen Sie")

### Typography Voice

- **Newsreader italic** for accent/emotion in headlines (the "feeling" line)
- **Inter bold blue** for the key message (the "what" line)
- **Inter light muted** for context/subtitle (the "detail" line)

### Do / Don't

| Do | Don't |
|----|-------|
| Use specific numbers ("30 Sekunden", "140x") | Use vague claims ("sehr schnell", "viel besser") |
| Address pain points directly | Be negative about competitors by name |
| Show the before/after contrast | Over-promise features not yet available |
| Keep sentences short and scannable | Write long paragraphs on slides |
| Use icons to support text | Use clipart or stock photos on slides |

---

## 5. Reference Documentation

Detailed reference files live in `docs/`. **Read these when needed** — they are NOT loaded automatically.

| File | When to read |
|------|-------------|
| **[docs/html-boilerplate.md](docs/html-boilerplate.md)** | Starting a new presentation from scratch |
| **[docs/slide-patterns.md](docs/slide-patterns.md)** | Creating new slides (6 layout patterns: title, cards, comparison, flow, grid, pricing) |
| **[docs/product-info.md](docs/product-info.md)** | Writing immoautomation-specific content (features, pricing, value props) |
| **[docs/copy-bank.md](docs/copy-bank.md)** | Writing German marketing copy (headlines, CTAs, FAQ, trust copy) |
| **[docs/icons.md](docs/icons.md)** | Adding icons to slides (Heroicons SVG library) |
| **[docs/figma-integration.md](docs/figma-integration.md)** | Pushing slides to Figma via MCP |
