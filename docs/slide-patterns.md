# Slide Layout Patterns

> Reference file for presentation slide layouts. Read this when creating new slides.

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
