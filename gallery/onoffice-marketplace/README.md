# immoautomation Gallery Slides for onOffice

Diese Folien sind fur die onOffice Integration als Gallery Images (800x450, 16:9 WebP) gedacht.

## Folien-Ubersicht

| Nr. | Datei | Beschreibung |
|-----|-------|--------------|
| 01 | `01-hero.html` | Hero/Intro - Hauptbotschaft "Vom CRM zur Sichtbarkeit" |
| 02 | `02-problem.html` | Problem - Manueller Prozess (70 Min) |
| 03 | `03-solution.html` | Losung - Mit immoautomation (30 Sek) |
| 04 | `04-features-overview.html` | Features - Alle 6 Hauptfeatures im Uberblick |
| 05 | `05-crm-integration.html` | CRM-Integration - onOffice |
| 06 | `06-templates-ai.html` | Templates & KI - Designer-Templates + KI-Captions |
| 07 | `07-process-steps.html` | Prozess - 5 Schritte zum perfekten Post (dunkler Hintergrund) |
| 08 | `08-social-proof.html` | Social Proof - Statistiken & Vertrauen |
| 09 | `09-integrations.html` | Integrationen - Workflow CRM → immoautomation → Social |
| 10 | `10-cta.html` | Call-to-Action - "Jetzt starten" (blauer Hintergrund) |

## Verwendung mit Figma HTML to Figma

### Option 1: Direkt im Browser
1. Offne jede HTML-Datei im Browser
2. Die Seite wird exakt 800x450 Pixel gross angezeigt
3. Nutze das Figma Plugin "HTML to Figma" um die Seite zu importieren

### Option 2: Screenshot
1. Offne die HTML-Datei im Browser
2. Setze das Browserfenster auf 800x450 Pixel (z.B. mit Developer Tools)
3. Mache einen Screenshot
4. Exportiere als WebP in 800x450

### Option 3: Mit Puppeteer/Playwright (automatisiert)
```javascript
const puppeteer = require('puppeteer');

async function captureSlide(filename) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 800, height: 450 });
  await page.goto(`file://${__dirname}/${filename}`);
  await page.screenshot({
    path: filename.replace('.html', '.webp'),
    type: 'webp',
    quality: 90
  });
  await browser.close();
}
```

## Design-Spezifikationen

- **Format**: 800x450 Pixel (16:9)
- **Hauptfarbe**: #0080FF (immoautomation Blau)
- **Schriftarten**:
  - Headlines: Newsreader (Serif, Italic)
  - Body: Inter (Sans-serif)
- **Hintergrund**: Weiss (#FFFFFF) oder Blau (#0080FF) fur CTA
- **Folie 07**: Dunkler Hintergrund (#1a1a2e)

## Hinweise

- Alle Styles sind inline, keine externen Abhangigkeiten ausser Google Fonts
- Die Folien sind statisch und benotigen kein JavaScript
- Fonts werden von Google Fonts geladen (Internetverbindung erforderlich)
