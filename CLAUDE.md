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

### HTML Boilerplate

Every presentation starts with this structure:

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=1920, initial-scale=1.0" />
  <title>immoautomation — PRESENTATION TITLE</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    /* === RESET === */
    *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

    /* === CUSTOM PROPERTIES === */
    :root {
      --blue: #0080FF;
      --blue-hover: #0066CC;
      --blue-light: rgba(0, 128, 255, 0.1);
      --blue-glow: rgba(0, 128, 255, 0.2);
      --black: #1a1a2e;
      --white: #fcfcff;
      --gray-light: rgba(0, 0, 0, 0.04);
      --text-secondary: rgba(0, 0, 0, 0.5);
      --text-muted: rgba(0, 0, 0, 0.35);
      --border: rgba(0, 0, 0, 0.08);
    }

    /* === BASE === */
    html, body {
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--white);
      color: var(--black);
    }

    /* === SLIDE ENGINE === */
    .slides-wrapper {
      width: 1920px;
      height: 1080px;
      position: relative;
    }

    .slide {
      position: absolute;
      inset: 0;
      width: 1920px;
      height: 1080px;
      display: none;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 72px 100px;
      opacity: 0;
      transition: opacity 0.5s ease;
    }

    .slide.active {
      display: flex;
      opacity: 1;
    }

    /* Light slide (default) */
    .slide-light, .slide {
      background: var(--white);
      position: relative;
      overflow: hidden;
    }

    /* Dark slide variant */
    .slide-dark {
      background: #0f0f1a;
      color: #ffffff;
      position: relative;
      overflow: hidden;
    }

    .slide .content {
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 1720px;
      display: flex;
      flex-direction: column;
    }

    /* === GRID BACKGROUND === */
    .grid-bg {
      position: absolute;
      inset: 0;
      pointer-events: none;
    }

    /* === SECTION LABEL === */
    .section-label {
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 0.3em;
      color: var(--text-muted);
    }

    /* === ANIMATIONS === */
    @keyframes slideUp {
      from { opacity: 0; transform: translateY(40px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    @keyframes scaleIn {
      from { opacity: 0; transform: scale(0.9); }
      to { opacity: 1; transform: scale(1); }
    }

    @keyframes slideLeft {
      from { opacity: 0; transform: translateX(-40px); }
      to { opacity: 1; transform: translateX(0); }
    }

    @keyframes slideRight {
      from { opacity: 0; transform: translateX(40px); }
      to { opacity: 1; transform: translateX(0); }
    }

    .animate-up { animation: slideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both; }
    .animate-fade { animation: fadeIn 0.6s ease-out both; }
    .animate-scale { animation: scaleIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) both; }
    .animate-left { animation: slideLeft 0.8s cubic-bezier(0.16, 1, 0.3, 1) both; }
    .animate-right { animation: slideRight 0.8s cubic-bezier(0.16, 1, 0.3, 1) both; }

    .delay-1 { animation-delay: 0.1s; }
    .delay-2 { animation-delay: 0.2s; }
    .delay-3 { animation-delay: 0.35s; }
    .delay-4 { animation-delay: 0.5s; }
    .delay-5 { animation-delay: 0.65s; }
    .delay-6 { animation-delay: 0.8s; }
    .delay-7 { animation-delay: 0.95s; }
    .delay-8 { animation-delay: 1.1s; }

    /* === NAVIGATION === */
    .slide-nav {
      position: fixed;
      bottom: 32px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      gap: 8px;
      z-index: 100;
    }

    .slide-nav button {
      width: 8px;
      height: 8px;
      background: rgba(0, 0, 0, 0.15);
      border: none;
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .slide-nav button.active {
      background: var(--blue);
      width: 32px;
    }

    .slide-counter {
      position: fixed;
      bottom: 32px;
      right: 48px;
      font-size: 12px;
      color: rgba(0, 0, 0, 0.3);
      font-variant-numeric: tabular-nums;
      z-index: 100;
    }

    .key-hint {
      position: fixed;
      bottom: 32px;
      left: 48px;
      font-size: 11px;
      color: rgba(0, 0, 0, 0.25);
      z-index: 100;
    }

    .key-hint kbd {
      display: inline-block;
      padding: 2px 6px;
      border: 1px solid rgba(0, 0, 0, 0.15);
      font-family: 'Inter', monospace;
      font-size: 10px;
    }

    /* === FULLSCREEN BUTTON === */
    .fullscreen-btn {
      position: fixed;
      top: 24px;
      right: 24px;
      z-index: 200;
      background: white;
      border: 1px solid rgba(0,0,0,0.1);
      width: 36px;
      height: 36px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }

    .fullscreen-btn:hover {
      border-color: var(--blue);
      background: var(--blue-light);
    }

    .fullscreen-btn svg {
      width: 16px;
      height: 16px;
      color: rgba(0,0,0,0.5);
    }

    .fullscreen-btn:hover svg {
      color: var(--blue);
    }

    /* ============================
       ADD SLIDE-SPECIFIC CSS HERE
       ============================ */

  </style>
</head>
<body>

  <!-- Fullscreen toggle -->
  <button class="fullscreen-btn" onclick="toggleFullscreen()" title="Vollbild (F)">
    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
      <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" />
    </svg>
  </button>

  <!-- Grid pattern definition (shared by all slides) -->
  <svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" style="position:absolute">
    <defs>
      <pattern id="grid" width="100" height="100" patternUnits="userSpaceOnUse">
        <path d="M 100 0 L 0 0 0 100" fill="none" stroke="#000" stroke-width="1" opacity="0.03"/>
      </pattern>
    </defs>
  </svg>

  <div class="slides-wrapper">

    <!-- SLIDE 1 -->
    <div class="slide active" id="slide-1">
      <svg class="grid-bg" xmlns="http://www.w3.org/2000/svg" width="1920" height="1080">
        <rect width="1920" height="1080" fill="url(#grid)"/>
      </svg>
      <div class="content" style="gap: 56px;">
        <!-- Slide content here -->
      </div>
    </div>

    <!-- SLIDE 2 -->
    <div class="slide" id="slide-2">
      <svg class="grid-bg" xmlns="http://www.w3.org/2000/svg" width="1920" height="1080">
        <rect width="1920" height="1080" fill="url(#grid)"/>
      </svg>
      <div class="content" style="gap: 56px;">
        <!-- Slide content here -->
      </div>
    </div>

    <!-- Add more slides as needed -->

  </div>

  <!-- Navigation -->
  <div class="slide-nav" id="slideNav"></div>
  <div class="slide-counter" id="slideCounter"></div>
  <div class="key-hint">
    <kbd>&larr;</kbd> <kbd>&rarr;</kbd> oder Klick zum Navigieren &middot; <kbd>F</kbd> Vollbild
  </div>

  <script>
    var slides = document.querySelectorAll('.slide');
    var current = 0;

    function showSlide(index) {
      for (var i = 0; i < slides.length; i++) {
        slides[i].classList.remove('active');
        if (i === index) {
          var animated = slides[i].querySelectorAll('[class*="animate-"]');
          for (var j = 0; j < animated.length; j++) {
            animated[j].style.animation = 'none';
            animated[j].offsetHeight;
            animated[j].style.animation = '';
          }
        }
      }
      slides[index].classList.add('active');
      current = index;
      updateNav();
    }

    function nextSlide() {
      if (current < slides.length - 1) showSlide(current + 1);
    }

    function prevSlide() {
      if (current > 0) showSlide(current - 1);
    }

    function updateNav() {
      var nav = document.getElementById('slideNav');
      nav.innerHTML = '';
      for (var i = 0; i < slides.length; i++) {
        var btn = document.createElement('button');
        if (i === current) btn.classList.add('active');
        btn.setAttribute('data-index', i);
        btn.addEventListener('click', function() {
          showSlide(parseInt(this.getAttribute('data-index')));
        });
        nav.appendChild(btn);
      }
      document.getElementById('slideCounter').textContent =
        (current + 1) + ' / ' + slides.length;
    }

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
      } else {
        document.exitFullscreen();
      }
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); nextSlide(); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
      if (e.key === 'f' || e.key === 'F') toggleFullscreen();
    });

    document.addEventListener('click', function(e) {
      if (e.target.closest('.slide-nav') || e.target.closest('.fullscreen-btn') || e.target.closest('button')) return;
      if (e.clientX > window.innerWidth / 2) nextSlide();
      else prevSlide();
    });

    updateNav();
  </script>
</body>
</html>
```

---

## 4. Slide Layout Patterns

Use these as starting points. Each is a complete slide `<div>` ready to paste inside `.slides-wrapper`.

### Pattern 1: Title Slide

Badge + large heading + team/author + tag pills.

```html
<div class="slide active" id="slide-1">
  <svg class="grid-bg" xmlns="http://www.w3.org/2000/svg" width="1920" height="1080">
    <rect width="1920" height="1080" fill="url(#grid)"/>
  </svg>
  <div class="content" style="gap: 64px;">
    <div class="animate-up delay-1">
      <p class="section-label">Über uns</p>
      <div style="display:flex;align-items:center;gap:20px;margin-top:24px;">
        <img src="../assets/logo.png" alt="immoautomation" style="height:48px;" />
        <div style="width:1px;height:36px;background:rgba(0,0,0,0.1);"></div>
        <span style="font-size:20px;color:var(--text-secondary);">Tagline text here</span>
      </div>
    </div>

    <div style="font-size:76px;line-height:1.1;letter-spacing:-0.02em;" class="animate-up delay-2">
      <span style="font-family:'Newsreader',serif;font-style:italic;font-weight:400;">Accent line</span><br/>
      <span style="font-weight:600;color:var(--blue);">Bold Blue Line</span><br/>
      <span style="font-weight:300;font-size:48px;color:var(--text-muted);">Subtitle line.</span>
    </div>

    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0;" class="animate-up delay-3">
      <div style="padding:32px 28px;display:flex;align-items:center;gap:20px;border-right:1px solid var(--border);">
        <div style="width:80px;height:80px;background:var(--blue-light);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;color:var(--blue);">RK</div>
        <div>
          <div style="font-size:24px;font-weight:600;">Name Here</div>
          <div style="font-size:17px;color:rgba(0,0,0,0.45);">Role</div>
        </div>
      </div>
      <!-- Repeat for more team members -->
    </div>
  </div>
</div>
```

### Pattern 2: Numbered Cards (Problem/Feature List)

3 cards in a row with icon boxes, numbers, and a stat bar at the bottom.

```html
<div class="slide" id="slide-2">
  <svg class="grid-bg" xmlns="http://www.w3.org/2000/svg" width="1920" height="1080">
    <rect width="1920" height="1080" fill="url(#grid)"/>
  </svg>
  <div class="content" style="gap: 56px;">
    <div class="animate-up delay-1">
      <p class="section-label">Section Name</p>
    </div>

    <div style="font-size:64px;line-height:1.1;letter-spacing:-0.02em;" class="animate-up delay-2">
      <span style="font-family:'Newsreader',serif;font-style:italic;font-weight:400;">First line</span><br/>
      <span style="font-weight:600;color:var(--blue);">Bold emphasis</span>
    </div>

    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;" class="animate-up delay-3">
      <!-- Card -->
      <div style="padding:40px 36px;border:1px solid var(--border);display:flex;flex-direction:column;gap:20px;position:relative;">
        <span style="position:absolute;top:16px;right:20px;font-size:12px;color:rgba(0,0,0,0.12);font-variant-numeric:tabular-nums;">01</span>
        <div style="width:52px;height:52px;background:var(--blue-light);display:flex;align-items:center;justify-content:center;">
          <svg width="24" height="24" fill="none" stroke="var(--blue)" viewBox="0 0 24 24" stroke-width="1.5">
            <!-- Icon path -->
          </svg>
        </div>
        <h3 style="font-size:22px;font-weight:600;">Card Title</h3>
        <p style="font-size:16px;color:var(--text-secondary);line-height:1.6;">Card description text.</p>
      </div>
      <!-- Repeat 02, 03 -->
    </div>

    <!-- Optional: Stat bar -->
    <div style="display:flex;align-items:center;gap:48px;padding:40px 48px;border:1px solid var(--border);background:var(--gray-light);" class="animate-up delay-4">
      <div style="font-size:72px;font-weight:700;font-variant-numeric:tabular-nums;color:var(--blue);line-height:1;white-space:nowrap;">~30 Sek</div>
      <div>
        <strong style="font-size:22px;">Stat headline</strong><br/>
        <span style="font-size:16px;color:var(--text-secondary);">Stat description.</span>
      </div>
    </div>
  </div>
</div>
```

### Pattern 3: Two-Column Comparison

Side-by-side blocks with a divider, used for partner/integration slides.

```html
<div class="slide" id="slide-3">
  <svg class="grid-bg" xmlns="http://www.w3.org/2000/svg" width="1920" height="1080">
    <rect width="1920" height="1080" fill="url(#grid)"/>
  </svg>
  <div class="content" style="gap: 56px;">
    <div class="animate-up delay-1">
      <p class="section-label">Section Name</p>
    </div>

    <div style="font-size:64px;line-height:1.1;letter-spacing:-0.02em;" class="animate-up delay-2">
      <span style="font-family:'Newsreader',serif;font-style:italic;font-weight:400;">Left emphasis</span> –<br/>
      <span style="font-weight:600;color:var(--blue);">right emphasis.</span>
    </div>

    <div style="display:grid;grid-template-columns:1fr 1px 1fr;gap:0;" class="animate-up delay-3">
      <!-- Left column -->
      <div style="padding:48px;display:flex;flex-direction:column;gap:28px;">
        <div style="display:flex;align-items:center;gap:16px;">
          <div style="width:56px;height:56px;background:var(--blue-light);display:flex;align-items:center;justify-content:center;">
            <!-- Icon SVG -->
          </div>
          <h3 style="font-size:28px;font-weight:600;">Left Title</h3>
          <span style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.15em;padding:4px 12px;background:var(--blue-light);color:var(--blue);margin-left:auto;">Badge</span>
        </div>
        <p style="font-size:17px;color:var(--text-secondary);line-height:1.6;">Description text.</p>
        <div style="display:flex;flex-direction:column;gap:16px;">
          <div style="display:flex;align-items:flex-start;gap:12px;font-size:16px;line-height:1.5;">
            <svg width="20" height="20" fill="none" stroke="var(--blue)" viewBox="0 0 24 24" stroke-width="2" style="flex-shrink:0;margin-top:2px;"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" /></svg>
            <span>Checklist item</span>
          </div>
          <!-- More checklist items -->
        </div>
      </div>

      <!-- Divider -->
      <div style="background:var(--border);width:1px;"></div>

      <!-- Right column -->
      <div style="padding:48px;display:flex;flex-direction:column;gap:28px;">
        <!-- Same structure, different content -->
      </div>
    </div>
  </div>
</div>
```

### Pattern 4: Flow Diagram (Journey/Timeline)

Boxes connected by arrows, showing a process flow.

```html
<div class="slide" id="slide-4">
  <svg class="grid-bg" xmlns="http://www.w3.org/2000/svg" width="1920" height="1080">
    <rect width="1920" height="1080" fill="url(#grid)"/>
  </svg>
  <div class="content" style="gap: 56px;">
    <div class="animate-up delay-1">
      <p class="section-label">Section Name</p>
    </div>

    <div style="font-size:64px;line-height:1.1;letter-spacing:-0.02em;" class="animate-up delay-2">
      <span style="font-family:'Newsreader',serif;font-style:italic;font-weight:400;">From here</span><br/>
      <span style="font-weight:600;color:var(--blue);">to there.</span>
    </div>

    <div style="display:flex;align-items:center;justify-content:center;gap:0;width:100%;" class="animate-up delay-3">
      <!-- Box 1 -->
      <div style="width:280px;padding:36px 28px;border:1px solid var(--border);display:flex;flex-direction:column;align-items:center;gap:14px;text-align:center;">
        <div style="width:52px;height:52px;display:flex;align-items:center;justify-content:center;">
          <!-- Icon SVG -->
        </div>
        <h3 style="font-size:22px;font-weight:600;">Step 1</h3>
        <p style="font-size:14px;color:var(--text-secondary);line-height:1.5;">Description</p>
      </div>

      <!-- Arrow -->
      <div style="display:flex;align-items:center;justify-content:center;padding:0 20px;">
        <svg width="40" height="24" viewBox="0 0 40 24" fill="none"><path d="M0 12h32m0 0l-6-6m6 6l-6 6" stroke="var(--blue)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>

      <!-- Box 2 (highlighted) -->
      <div style="width:380px;padding:36px 28px;border:2px solid var(--blue);background:rgba(0,128,255,0.04);display:flex;flex-direction:column;align-items:center;gap:14px;text-align:center;">
        <div style="width:52px;height:52px;display:flex;align-items:center;justify-content:center;">
          <!-- Icon SVG -->
        </div>
        <h3 style="font-size:22px;font-weight:600;">immoautomation</h3>
        <p style="font-size:14px;color:var(--text-secondary);line-height:1.5;">Description</p>
      </div>

      <!-- Arrow -->
      <div style="display:flex;align-items:center;justify-content:center;padding:0 20px;">
        <svg width="40" height="24" viewBox="0 0 40 24" fill="none"><path d="M0 12h32m0 0l-6-6m6 6l-6 6" stroke="var(--blue)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>

      <!-- Box 3 -->
      <div style="width:280px;padding:36px 28px;border:1px solid var(--border);display:flex;flex-direction:column;align-items:center;gap:14px;text-align:center;">
        <div style="width:52px;height:52px;display:flex;align-items:center;justify-content:center;">
          <!-- Icon SVG -->
        </div>
        <h3 style="font-size:22px;font-weight:600;">Step 3</h3>
        <p style="font-size:14px;color:var(--text-secondary);line-height:1.5;">Description</p>
      </div>
    </div>
  </div>
</div>
```

### Pattern 5: Feature Grid (4 columns)

Bottom-row feature cards with numbers and icons, separated by borders.

```html
<!-- Add inside a slide's .content, typically below a flow diagram -->
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:1px solid var(--border);" class="animate-up delay-4">
  <div style="padding:32px 28px;border-right:1px solid var(--border);display:flex;flex-direction:column;gap:12px;position:relative;">
    <span style="position:absolute;top:12px;right:16px;font-size:11px;color:rgba(0,0,0,0.1);font-variant-numeric:tabular-nums;">01</span>
    <div style="width:44px;height:44px;background:var(--blue-light);display:flex;align-items:center;justify-content:center;">
      <svg width="20" height="20" fill="none" stroke="var(--blue)" viewBox="0 0 24 24" stroke-width="1.5">
        <!-- Icon path -->
      </svg>
    </div>
    <h4 style="font-size:17px;font-weight:600;">Feature Title</h4>
    <p style="font-size:14px;color:var(--text-secondary);line-height:1.5;">Feature description.</p>
  </div>
  <!-- Repeat 02, 03, 04 (last one without border-right) -->
</div>
```

### Pattern 6: Pricing Cards (3 tiers)

```html
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:stretch;" class="animate-up delay-3">
  <!-- Standard card -->
  <div style="border:1px solid var(--border);padding:44px 40px;display:flex;flex-direction:column;gap:28px;">
    <div>
      <div style="font-size:28px;font-weight:600;">Plan Name</div>
      <div style="font-size:15px;color:var(--text-secondary);">Plan subtitle</div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:56px;font-weight:700;line-height:1;font-variant-numeric:tabular-nums;">€0</span>
      <span style="font-size:18px;color:var(--text-secondary);">/ Monat</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:14px;flex-grow:1;">
      <div style="display:flex;align-items:flex-start;gap:10px;font-size:15px;line-height:1.4;">
        <svg width="18" height="18" fill="none" stroke="var(--blue)" viewBox="0 0 24 24" stroke-width="2" style="flex-shrink:0;margin-top:2px;"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" /></svg>
        <span>Feature text</span>
      </div>
      <!-- More features -->
    </div>
    <div style="display:flex;align-items:center;justify-content:center;padding:16px 24px;font-size:16px;font-weight:600;border:1px solid rgba(0,0,0,0.15);cursor:pointer;">CTA Text</div>
  </div>

  <!-- Featured card (add blue border + badge) -->
  <div style="border:2px solid var(--blue);padding:44px 40px;display:flex;flex-direction:column;gap:28px;background:rgba(0,128,255,0.02);position:relative;">
    <span style="position:absolute;top:-1px;right:40px;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.12em;padding:6px 14px;color:white;background:var(--blue);">Empfohlen</span>
    <!-- Same inner structure -->
    <!-- CTA with blue background: background:var(--blue);color:white; -->
  </div>

  <!-- Coming soon card (add opacity:0.85) -->
</div>
```

---

## 5. Product Overview

Use this section as your source of truth when writing presentation content.

### What is immoautomation?

An automated social media content platform for real estate agents. It connects directly to CRM systems (onOffice, Propstack), auto-generates professional social media posts from property listings, and publishes to multiple platforms with one click.

**Tagline:** "Vom CRM zur Sichtbarkeit in Sekunden"

**Elevator pitch:** immoautomation verwandelt Immobiliendaten automatisch in professionelle Social Media Posts — in 30 Sekunden statt 70 Minuten.

### Target Market

- **Who:** Immobilienmakler (real estate agents) in DACH region (Austria, Germany, Switzerland)
- **Company:** makeautomation GmbH, based in Austria
- **Founders:** Rafael Kietaibl (Co-Founder), Niklas Kietaibl (Co-Founder), Alexander Gottlieb (CTO)

### Key Value Proposition

| Manual Process | With immoautomation |
|---------------|---------------------|
| ~70 Minuten pro Post | ~30 Sekunden pro Post |
| 3-5 Plattformen einzeln | 1-Klick Multi-Plattform |
| Grafiktools nötig | Professionelle Templates |
| Texte selbst schreiben | KI-generierte Captions |
| Inkonsistenter Look | Einheitliches Branding |

**Speed claim:** 140x schneller (30 sec vs 70 min)

### Core Features

1. **CRM-Integration** — Direkte Anbindung an onOffice und Propstack. Immobiliendaten, Bilder und Exposé-Details werden automatisch abgerufen.
2. **Professionelle Templates** — Hunderte Designer-Vorlagen, immer im Corporate Design. Powered by CE.SDK (img.ly).
3. **KI-Texterstellung** — Automatisch generierte, plattformoptimierte Captions und Hashtags für jeden Post.
4. **Multi-Plattform Publishing** — Ein Klick veröffentlicht auf Instagram, Facebook und Google Business gleichzeitig.
5. **Content-Kalender** — Plane und terminiere Posts im Voraus. Visueller Kalender mit Drag & Drop.
6. **Live-Preview Editor** — Echtzeit-Anpassungen an Templates mit dem integrierten Design-Editor (MaklerPremium).

### Pricing

| Plan | Preis | Zielgruppe | Highlights |
|------|-------|------------|------------|
| **Kostenlos** | €0/Monat | Zum Kennenlernen | 5 Posts/Monat, Meta & Google Business, keine KI-Texte |
| **MaklerPlus** | €49/Monat | Für wachsende Makler | Unbegrenzte Posts, 1 Social Set, alle Premium-Vorlagen, KI-Texterstellung, Basis-Analytics |
| **MaklerPremium** | €99/Monat | Maximale Kontrolle | Alles aus MaklerPlus + Live-Preview Editor, eigene Schriften & Templates, Video-Reels, erweiterte Analytics |

- MaklerPlus: 12 Monate Mindestlaufzeit, 14 Tage kostenlos testen
- MaklerPremium: Coming Soon, zusätzliche Social Sets ab €15/Monat
- Keine Einrichtungsgebühr

### Integration Partners

| Partner | Type | Description |
|---------|------|-------------|
| **onOffice** | CRM | Marktführer für Immobilien-CRM in DACH. Direkte API-Anbindung. |
| **Propstack** | CRM | Modernes Immobilien-CRM. Direkte API-Anbindung. |
| **Meta (Instagram/Facebook)** | Social | Direktes Publishing via Meta Business API. |
| **Google Business** | Social | Google Unternehmensprofil Publishing. |

### Trust Signals

- DSGVO-konform
- Hosting in Deutschland
- API-verifiziert
- Verschlüsselte Verbindungen
- Keine Einrichtungsgebühr
- Made in Austria

### Stats (use for social proof)

- 1.000+ Posts erstellt
- 100+ Makler nutzen immoautomation
- 5.000+ Stunden eingespart
- 98% Zufriedenheit

---

## 6. Marketing Copy Bank (German)

All proven German marketing copy ready to use. These are the actual phrases from the live product.

### Headlines & Taglines

- "Vom CRM zur Sichtbarkeit in Sekunden"
- "Alles, was Sie brauchen. In einer Plattform."
- "Schluss mit zeitaufwändiger Content-Erstellung"
- "In 5 Schritten zum perfekten Post"
- "Zahlen, die für sich sprechen"
- "Wir automatisieren Social Media für die Immobilienbranche."
- "Vom Exposé zum Post in 30 Sekunden."
- "Die Daten sind da – die Brücke fehlt."
- "Einfache Preise, klarer Mehrwert."
- "Eine Schnittstelle – maximaler Mehrwert."

### Feature Descriptions

**CRM-Anbindung:**
Verbinden Sie Ihr onOffice oder Propstack-Konto. Immobiliendaten, Bilder und Exposé-Details werden automatisch synchronisiert — kein manuelles Kopieren mehr.

**Professionelle Templates:**
Hunderte Designer-Vorlagen für jeden Anlass — Neues Angebot, Verkauft, Open House und mehr. Immer im professionellen Look, immer aktuell.

**KI-Texterstellung:**
Lassen Sie unsere KI perfekte Captions für Instagram, Facebook und Google Business generieren. Plattformoptimiert, mit passenden Hashtags und Emojis.

**Multi-Plattform Posting:**
Ein Klick veröffentlicht Ihren Post auf Instagram, Facebook und Google Business gleichzeitig. Keine Plattform wird vergessen.

**Content-Kalender:**
Planen Sie Ihre Posts im Voraus. Unser visueller Kalender zeigt Ihnen alle geplanten Veröffentlichungen auf einen Blick.

**Analytics & Einblicke:**
Verfolgen Sie die Performance Ihrer Posts. Erfahren Sie, welche Inhalte am besten funktionieren und optimieren Sie Ihre Strategie.

### Problem / Solution Comparison

**Manueller Prozess (Das Problem):**
1. Immobilie im CRM öffnen (~2 Min)
2. Bilder einzeln herunterladen (~5 Min)
3. Bilder in Grafikprogramm bearbeiten (~20 Min)
4. Texte selbst verfassen (~15 Min)
5. Auf Instagram hochladen & posten (~8 Min)
6. Auf Facebook hochladen & posten (~8 Min)
7. Auf Google Business hochladen & posten (~8 Min)
8. **Gesamt: ~70 Minuten pro Post**

**Mit immoautomation (Die Lösung):**
1. Immobilie auswählen (~5 Sek)
2. Template wählen (~10 Sek)
3. KI-Text generieren (~5 Sek)
4. Vorschau prüfen (~5 Sek)
5. Auf allen Plattformen veröffentlichen (~5 Sek)
6. **Gesamt: ~30 Sekunden pro Post**

### Workflow Steps (5 Steps)

| Step | Time | Title | Description |
|------|------|-------|-------------|
| 1 | ~5 Sek | Immobilie auswählen | Wählen Sie die gewünschte Immobilie direkt aus Ihrem CRM aus |
| 2 | ~10 Sek | Template auswählen | Wählen Sie aus hunderten professionellen Vorlagen |
| 3 | ~5 Sek | Text generieren | Unsere KI erstellt plattformoptimierte Captions |
| 4 | ~5 Sek | Vorschau prüfen | Kontrollieren Sie das Ergebnis im Live-Preview |
| 5 | ~5 Sek | Veröffentlichen | Ein Klick postet auf allen verbundenen Plattformen |

### CTA Copy

- "Kostenlos starten"
- "Jetzt starten"
- "Demo ansehen"
- "Demo anfragen"
- "Termin buchen"
- "14 Tage kostenlos testen"
- "Bald verfügbar" (for coming-soon features)

### FAQ Content

**Was ist ein Social Set?**
Ein Social Set ist eine Kombination aus verbundenen Social-Media-Konten (z.B. ein Instagram- und ein Facebook-Konto). Im MaklerPlus-Plan ist 1 Social Set inklusive, weitere Sets können ab €15/Monat hinzugebucht werden.

**Kann ich jederzeit kündigen?**
Nach der Mindestlaufzeit von 12 Monaten können Sie jederzeit zum Ende des Abrechnungszeitraums kündigen.

**Gibt es eine kostenlose Testphase?**
Ja! Der MaklerPlus-Plan kann 14 Tage lang kostenlos getestet werden. Keine Kreditkarte erforderlich.

**Bieten Sie auch individuelle Template-Designs an?**
Ja, auf Anfrage erstellen wir individuelle Templates in Ihrem Corporate Design. Kontaktieren Sie uns für ein unverbindliches Angebot.

### Trust Copy

- "Ihre Daten sind bei uns sicher. DSGVO-konform und verschlüsselt."
- "Hosting in Deutschland — Ihre Daten verlassen nie die EU."
- "API-verifizierte Verbindungen zu onOffice und Meta."
- "Keine Einrichtungsgebühr, keine versteckten Kosten."
- "Made in Austria mit Liebe zum Detail."

---

## 7. Brand Voice Guidelines

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

## 8. Icons

All icons use **Heroicons** (outline style, stroke-width 1.5). Include inline SVGs — no icon library needed.

Common icons used in presentations:

```html
<!-- Clock / Time -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>

<!-- Lightning / Speed -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" /></svg>

<!-- Sparkles / AI -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z" /></svg>

<!-- Calendar -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5" /></svg>

<!-- Share / Social -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M7.217 10.907a2.25 2.25 0 100 2.186m0-2.186c.18.324.283.696.283 1.093s-.103.77-.283 1.093m0-2.186l9.566-5.314m-9.566 7.5l9.566 5.314m0 0a2.25 2.25 0 103.935 2.186 2.25 2.25 0 00-3.935-2.186zm0-12.814a2.25 2.25 0 103.933-2.185 2.25 2.25 0 00-3.933 2.185z" /></svg>

<!-- Database / CRM -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125" /></svg>

<!-- Link / Integration -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M13.19 8.688a4.5 4.5 0 011.242 7.244l-4.5 4.5a4.5 4.5 0 01-6.364-6.364l1.757-1.757m13.35-.622l1.757-1.757a4.5 4.5 0 00-6.364-6.364l-4.5 4.5a4.5 4.5 0 001.242 7.244" /></svg>

<!-- Check -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" /></svg>

<!-- Globe -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418" /></svg>

<!-- Paint / Design -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9.53 16.122a3 3 0 00-5.78 1.128 2.25 2.25 0 01-2.4 2.245 4.5 4.5 0 008.4-2.245c0-.399-.078-.78-.22-1.128zm0 0a15.998 15.998 0 003.388-1.62m-5.043-.025a15.994 15.994 0 011.622-3.395m3.42 3.42a15.995 15.995 0 004.764-4.648l3.876-5.814a1.151 1.151 0 00-1.597-1.597L14.146 6.32a15.996 15.996 0 00-4.649 4.763m3.42 3.42a6.776 6.776 0 00-3.42-3.42" /></svg>

<!-- Settings / Sliders -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" /></svg>

<!-- Fullscreen -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" /></svg>

<!-- Question mark -->
<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9 5.25h.008v.008H12v-.008z" /></svg>

<!-- Arrow right (for flow diagrams) -->
<svg viewBox="0 0 40 24" fill="none"><path d="M0 12h32m0 0l-6-6m6 6l-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>

<!-- Broken connection (for problem slides) -->
<svg viewBox="0 0 48 48" fill="none">
  <line x1="4" y1="24" x2="18" y2="24" stroke="currentColor" stroke-width="2.5" stroke-dasharray="4 4" />
  <circle cx="24" cy="24" r="8" fill="none" stroke="currentColor" stroke-width="2" />
  <path d="M20.5 20.5l7 7M27.5 20.5l-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
  <line x1="30" y1="24" x2="44" y2="24" stroke="currentColor" stroke-width="2.5" stroke-dasharray="4 4" />
</svg>
```
