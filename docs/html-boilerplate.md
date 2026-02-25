# HTML Boilerplate

> Complete HTML template for new presentations. Read this when starting a new presentation from scratch.

### HTML Boilerplate

Every presentation starts with this structure:

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
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
      width: 100%;
      height: 100%;
      overflow: hidden;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--white);
      color: var(--black);
    }

    /* === SCALE CONTAINER === */
    .scale-container {
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      background: var(--black);
    }

    /* === SLIDE ENGINE === */
    .slides-wrapper {
      width: 1920px;
      height: 1080px;
      position: relative;
      transform-origin: center center;
      flex-shrink: 0;
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

  <div class="scale-container" id="scaleContainer">
  <div class="slides-wrapper" id="slidesWrapper">

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

    // === DYNAMIC SCALING ===
    function scalePresentation() {
      var wrapper = document.getElementById('slidesWrapper');
      var vw = window.innerWidth;
      var vh = window.innerHeight;
      var scaleX = vw / 1920;
      var scaleY = vh / 1080;
      var scale = Math.min(scaleX, scaleY);
      wrapper.style.transform = 'scale(' + scale + ')';
    }

    window.addEventListener('resize', scalePresentation);
    document.addEventListener('fullscreenchange', function() {
      setTimeout(scalePresentation, 100);
    });

    scalePresentation();

    updateNav();
  </script>
</body>
</html>
```

---
