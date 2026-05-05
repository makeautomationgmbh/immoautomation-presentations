# onOffice Business Beats — Audit & Umbauplan

Source of Truth: `~/Downloads/design.md` + Du-Form.

---

## A. Globale Findings (alle Slides)

### Design-System-Drift vs. design.md

| # | Issue | Fix |
|---|---|---|
| G1 | Variablen heissen `--ia-blue` statt `--accent`, `--ia-black` statt `--text` etc. Werte stimmen aber. | Variablen umbenennen ODER aliasen (Aliasen ist sicherer, weniger Diff). |
| G2 | Newsreader-Font wird im `<head>` geladen aber nirgends genutzt. | Import raus, spart 1 Request. |
| G3 | `.serif-italic` Klasse ist OK (rendert schon in Inter Bold + Blue, design.md erlaubt das explizit als historisch). | Lassen. |
| G4 | Schatten nutzen `rgba(26,26,46,...)` (fast Schwarz). design.md will `hsl(250 30% 30% / X)` (Lila-Spektrum). | Alle `rgba(26,26,46,...)` → hsl-Werte. |
| G5 | Border-Radius inkonsistent: Chat-Bubbles 16/18px, CTA-Box 4px, kbd 5px, attach 12px. design.md sagt 0 ueberall. | Alle auf 0, Avatare bleiben Ausnahme (50%). |
| G6 | Sprache: durchgehend "Sie/Ihr/eure". | Auf Du/Dir/deine umstellen. |
| G7 | Footer-Nummerierung stimmt nicht: Slide 18 zeigt "17", Slide 19 zeigt "20", Slide 20 zeigt "19". | Korrekt durchnummerieren. |
| G8 | Slide 14 fehlt komplett (springt 13 → 15). | Entweder data-screen-label korrigieren oder bewusst 14 als neue Slide einfuegen. |

### Voice-Drift vs. design.md
- design.md: "Substanz statt Selbstlob, keine Buzzwords". Aktuell viele Emojis als Deko (📍, ⏱️, 📊, 📅, 🚀, 🤝, 📚, 🏘️, 🏠 etc.).
- Vorschlag: **Funktionale Emojis behalten** (im Chat-UI, in Stat-Cards), **Deko-Emojis raus** (z.B. die grossen runden Icon-Wraps mit 64px Emojis in Reasons-Grids).

---

## B. Slide-fuer-Slide

### Slide 01 — Titel
**Aktuell:** "Social Media als Makler. Was KI moeglich macht, *und was nicht.*" + Rafael · immoautomation.at + Eyebrow "Business Beats · KI Power Hour 2026"

**Optimierung:**
- Du-Form trifft hier nicht direkt zu (Headline ist neutral) → bleibt
- Eyebrow: "KI Power Hour 2026" passt nicht zu onOffice Business Beats. → **"onOffice Business Beats · 2026"** oder konkretes Datum?
- Spacing OK, Hierarchie OK.

**Frage an dich:** Eyebrow-Text final?

---

### Slide 02 — KI Stats (96 % nutzen KI)
**Aktuell:** "KI hat Social Media uebernommen." + 96 % Hero-Stat + +21 %/40 % Side-Stats. Source: Metricool 2025.

**Optimierung:**
- Headline ok, "uebernommen" ist stark
- "Das ist nicht die Zukunft. Das ist jetzt." → bleibt, ist gut
- Quelle in Foot: gut

**Aenderung:** keine inhaltlich. Nur G1–G5 (Design-Tokens).

---

### Slide 03 — Reichweite Paradox
**Aktuell:** "Mehr Beitraege. Weniger Reichweite." + +21 % vs –31 % Split + Quote "Der Algorithmus entscheidet. Nicht mehr eure Follower."

**Optimierung:**
- Headline stark, Visual stark
- Quote: "eure Follower" → **"deine Follower"** (Du-Form)
- Border um den Split-Container ist OK aber innerer Abstand koennte luftiger

---

### Slide 04 — Kapitel 01
**Aktuell:** "Wer steckt dahinter?" + Chapter-Bar.
**Optimierung:** Nichts. Solid.

---

### Slide 05 — Ueber mich (Timeline)
**Aktuell:** Foto + 3 Steps (E-Commerce → Agentur → immoautomation).

**Optimierung:**
- "Mehrere Shops aufgebaut & verkauft" — konkret bleiben oder Zahlen? z.B. "3 Shops, ein Exit"
- "€4 Mio. Werbebudget fuer Kunden" — gut, konkret
- "Software die Maklern das Posten vereinfacht" — schwach. Vorschlag: **"Software, die nicht nervt — fuer Makler"** (Tonality aus design.md)
- Pill "Der rote Faden: Social Media" → bleibt, ist gut
- Avatar: 3px solid blue border + box-shadow ist viel Bling → 1.5px reicht, shadow weg (design.md: keine Glow-Effekte)

---

### Slide 06 — Kapitel 02
**Aktuell:** "Wie wird KI genutzt?"
**Optimierung:** Nichts. Solid.

---

### Slide 07 — KI Nutzung (4 Cards mit Substeps)
**Aktuell:** Texte/Bilder/Reels/Ideen — jeweils mit grossem Emoji im runden Wrap.

**Optimierung:**
- Emojis im 96px runden Wrap = sehr "Tech-Bro Glow". design.md sagt: keine Glow-Effekte, sharp, editorial. → **Emojis raus, durch SVG-Icons in eckigen Plates ersetzen** (Heroicons)
- "ihr verfeinert ihn" → "du verfeinerst ihn"
- "ohne Designerin" → "ohne Designer" (oder neutraler: "ohne Designteam")
- "in einem Bruchteil der Zeit" — schwach. → "in Minuten statt Stunden"
- "KI als Denkpartner fuer Themen, Planung und Strategie" → "KI als Sparringspartner fuer Themen und Strategie"

**Das ist potenziell die Bala-Kandidatin** (uebersichtliche 4-Card Grid)

---

### Slide 08 — 3 Stufen
**Aktuell:** Manuell → Tools → Agentic AI. Stufe 2 ist highlighted "Wir sind hier".

**Optimierung:**
- Stufe 1 Beschreibung: "Fotos machen, Text schreiben, manuell posten" → ok
- Stufe 2: "Du sind hier" passt im Du-Modus nicht → **"Du bist hier"** oder **"Hier stehst du"**
- Stufe 3 hat orange dashed border + orange Number — bricht das Design (design.md: keine zusaetzlichen Akzentfarben). → Border in `--ia-blue-border` dashed, Zahl in `--ia-blue` mit 0.4 opacity
- Emoji-Flows (📷 → ✍️ → 📤) sind cute aber Tech-Bro-mässig → koennten raus, oder durch reduzierte Pictograms ersetzt
- "Tools als Werkzeuge" — Doppelmoppel. → **"Tools-Patchwork"** oder **"Mehrere Tools parallel"**

---

### Slide 09 — Kapitel 03
**Aktuell:** "Was kommt als Naechstes?"
**Optimierung:** Nichts.

---

### Slide 10 — Agentic AI (Konzept-Intro)
**Aktuell:** "Aufgaben delegieren statt Tools bedienen." + 3 Cards (Du delegierst → Agenten koordinieren → Du bekommst Ergebnis).

**Optimierung:**
- Mittlere Card hat lineare Gradient + box-shadow + decorative corner-Bubbles → zu viel.
- design.md: "Substanz vor Show. Whitespace > Decoration." → **Mittlere Card vereinfachen**: einfacher blauer Background, Bubbles raus, Schatten reduzieren
- "Du delegierst" / "Du bekommst" → schon Du-Form, gut
- Agent-Network mit 🤖↔🤖↔🤖 ist niedlich → koennte funktioneller werden

---

### Slide 11 — Makler perfekt vorbereitet
**Aktuell:** Pill "Die gute Nachricht" (gruen) + "Makler sind perfekt vorbereitet." + 4 Reasons + CTA-Bar "Ihr muesst es nur noch einsetzen."

**Optimierung:**
- "Ihr habt was KI braucht: Struktur, lokale Expertise..." → **"Du hast was KI braucht: ..."**
- 4 Reasons: 72px runde Emoji-Wraps wieder = Tech-Bro. → SVG-Icons
- CTA-Bar: "Ihr muesst es nur noch einsetzen." → **"Du musst es nur noch einsetzen."**
- CTA-Bar hat keinen border-radius (gut), bleibt
- Pill in green ist eigene Akzentfarbe → design.md hat `--success: #22C55E`, ok zu nutzen

---

### Slide 12 — Agenten Aufgaben (Uebergang)
**Aktuell:** Pill "Agentic AI" + "Welche Aufgaben koennen solche Agenten uebernehmen?" + "Ein Beispiel aus eurem Alltag."

**Optimierung:**
- "eurem Alltag" → "deinem Alltag"
- Solid sonst.

---

### Slide 13 — Agenten System (animiert)
**Aktuell:** Mitarbeiter → Social Media Agent → 3 Sub-Agenten (Analyse, Research, Planung). Linke und rechte Sub-Agenten haben hardcoded `opacity:1; transform:translateY(0)` → erscheinen sofort, nur die mittlere wird animiert. Linien werden nur fuer die Mitte gezogen.

**Optimierung:**
- Animation ist halb-fertig: Lines zu links/rechts fehlen, Pakete fliessen nur zur Mitte. → **Entweder voll animieren (alle 3 Linien + Pakete) ODER ganz statisch**
- Sub-Agenten haben jeweils eigene Akzentfarbe (lila, pink, orange). design.md: keine zusaetzlichen Akzentfarben ohne OK. → Auf 3 Blau-Variationen oder 1 Blau + grau-shades reduzieren
- Sehr komplexe Slide-Logik. Risiko bei Live-Praesi: Animation hakelt.

**Frage an dich:** Volle Animation ueberarbeiten, oder lieber statisch und sauber?

---

### Slide 15 — User fragt
**Aktuell:** Headline "Ihr redet. Der Agent arbeitet." + Rafael-Bubble "Ich brauche Content-Ideen fuer diese Woche..."

**Optimierung:**
- "Ihr redet" → "Du redest"
- Bubble border-radius 16px → 0 (design.md)
- Avatar shadow weg, einfacher Border
- Content der Bubble bleibt — gutes Beispiel

---

### Slide 16 — Maerz Post
**Aktuell:** Agent zeigt Performance vom Maerz-Post (+3,8%, 1.200 Aufrufe etc.).

**Optimierung:**
- Bubbles border-radius 16px → 0
- Inner stat-card hat border-radius 8px → 0
- Sonst Content stark, bleibt

---

### Slide 17 — Agent fragt
**Aktuell:** "Soll ich das fuer Wien 21. genauso aufbauen?"
**Optimierung:**
- border-radius 16px → 0
- Sonst gut.

---

### Slide 18 — Agent arbeitet (Footer zeigt "17" — falsch)
**Aktuell:** User "Ja, mach das." + Agent typing.

**Optimierung:**
- Footer-Nummer fixen: "18"
- "Sie" als Username im Eyebrow → **"Du"**
- border-radius 16px → 0

---

### Slide 19 — Ergebnis (Footer zeigt "20" — falsch)
**Aktuell:** Instagram-Mockup + 45-Sek-Skript + "Erstellt in 45 Sekunden"-Box.

**Optimierung:**
- Footer-Nummer fixen: "19"
- Phone-Mockup hat 28px / 20px / 8px border-radius (Phone-Frame). → Ausnahme akzeptabel weil "Phone-Mockup". Lassen.
- Stat-Card oben drueber border-radius 8px → 0
- "Bottom CTA" (Erstellt in 45 Sekunden) hat keinen radius — gut
- Caption im IG-Mockup nutzt `#667eea` fuer Hashtags (lila) → sollte unser Blau sein

---

### Slide 20 — Proaktiv (Footer zeigt "19" — falsch)
**Aktuell:** Analyse Agent meldet sich + Social Media Agent schlaegt vor.

**Optimierung:**
- Footer-Nummer fixen: "20"
- Lila Akzentfarbe fuer Analyse Agent (#8b5cf6) → kollidiert mit design.md. → Ersetzen durch zweite Blau-Variante oder grau
- Border-Radius pruefen
- Inhalt stark, bleibt

---

### Slide 21 — Realitaet (KI = neuer Mitarbeiter)
**Aktuell:** Einarbeitung → Zusammenarbeit → Autonomie + Payoff "Der Unterschied: Dieser Mitarbeiter wird mit jedem Tag besser."

**Optimierung:**
- 140px runde Wraps mit grossen Emojis (📚 🤝 🚀) — Tech-Bro Vibe. → SVG-Icons
- Orange Wrap (📚) bricht Farbschema → blau
- Gruener Wrap (🚀) — gruen ist `--success` ok, aber hier passt es nicht semantisch (Autonomie ist nicht "Erfolg"). → blau

---

### Slide 22 — Drei Typen (Wo stehst du?)
**Aktuell:** Nachzuegler / Mehrheit / Frueher Nutzer (highlighted).

**Optimierung:**
- "Wo stehst du?" — schon Du-Form, gut
- Aufbau identisch zu Slide 08 (3-Stufen-Pattern). → bleibt
- Emoji-Flows (⏳→😴→❌, 👀→✅→😐, ⚡→📈→🏆) — die emojis sind hier aussagekraeftig, bleiben oder pictograms?

**Frage an dich:** Emoji-Flows behalten oder reduziert?

---

### Slide 23 — Pitch (immoautomation)
**Aktuell (DARK):** Icon (🏢) + "Wir bauen das fuer die Immobranche." + CTA Box "Wollt ihr dabei sein? Schaltet unseren Service im onOffice Marketplace frei..." + Button "immoautomation.at →"

**Optimierung:**
- "Wollt ihr" → **"Willst du"**
- "Schaltet unseren Service... frei und seid von Anfang an dabei." → **"Schalt unseren Service... frei und sei von Anfang an dabei."**
- 🏢 Emoji im 120px Glow-Kreis ist Tech-Bro pur (`box-shadow: 0 0 60px rgba(0,128,255,0.4)`). design.md verbietet Glow ausdruecklich. → Entweder sauberes immoautomation Icon-SVG ODER kein Icon, nur Wordmark
- CTA-Box hat `border-radius: 4px` auf den Button → 0
- "Objektpostings sind jetzt automatisiert. Social Media Marketing, Marktberichte, Bewertungen — viele weitere Schritte stehen an." → Em-Dash entfernen (—). design.md: "Keine Em-Dashes."
- DARK-Slide ohne Logo/Wordmark — koennte das echte Logo (`logo-wordmark.svg`) zeigen

**Das ist die natuerliche Killer-Folie. Hier muss "Bala" landen.**

---

### LIVE Chat-Demo (24. Slide)
**Aktuell:** Chat-Interface mit 6 Steps (Briefing → Maerz-Daten → Vorschlag → User OK → Result → 2 Wochen spaeter).

**Optimierung:**
- Eyebrow "Live · Sie reden, der Agent arbeitet" → "Live · Du redest, der Agent arbeitet"
- Bubbles haben 18px border-radius → ist Chat-Konvention. **Ausnahme akzeptabel** (Chat-Bubbles muessen rund wirken). Aber: design.md sagt sharp, also vielleicht reduzieren auf 4-6px? Oder voll auf 0?
- CTA-Buttons "Plan ansehen" / "Spaeter" haben 10px border-radius → 0
- kbd "→" hat 5px border-radius → 0
- live-pill "Online" hat 999px (pill-Form) → ok als Status-Indicator-Ausnahme
- attach card 12px border-radius → 0
- Footer-Nummer: "LIVE" → ok als Spezialfall

**Frage an dich:** Chat-Bubbles 18px lassen (Chat-Konvention) oder hart 0 (design.md-konsequent)?

---

## C. Killer-Folie ("Bala") fuer onOffice

Aktuell ist Slide 23 (Pitch) der natuerliche Killer-Moment. Optionen:

1. **Slide 23 verschaerfen** — Sie/Du, Logo statt Emoji, sharp, ein einziger fokussierter CTA. Das passt zum Event-Format (du moechtest Listings im onOffice Marketplace).
2. **Neue Slide einfuegen** vor 23 — z.B. eine "Was du heute mitnimmst"-Folie mit 3 Take-Aways.
3. **Slide 23 splitten** — eine "Vision"-Folie + eine "CTA"-Folie.

**Frage an dich:** Welche Richtung?

---

## D. Reihenfolge des Umbaus

1. **Design-System-Harmonisierung** (G1–G5): Variablen, Schatten, Border-Radius, Newsreader raus. Globaler Search/Replace. ~30 min.
2. **Sprache Sie → Du** (G6): durchsuchen + ersetzen. ~10 min.
3. **Footer-Nummern fixen** (G7, G8): manuell. ~5 min.
4. **Tech-Bro-Cleanup**: Emoji-Wraps → SVG-Icons, Glows raus, Akzentfarben (lila/orange/pink) reduzieren. ~45 min.
5. **Slide-by-slide Content-Tweaks**: Headlines, Subheads schaerfen. ~30 min.
6. **Killer-Folie**: je nach deiner Entscheidung. ~30 min.

**Total:** ~2.5 h

---

## Offene Fragen an dich

1. Eyebrow Slide 01: "onOffice Business Beats · 2026" oder anderes?
2. Slide 13 Animation: voll animiert oder statisch?
3. Slide 22 Emoji-Flows: behalten oder Pictograms?
4. Live-Chat Bubbles: 18px (Chat-Konvention) oder hart 0px?
5. Killer-Folie: Slide 23 verschaerfen, neue Folie davor, oder splitten?
6. Tech-Bro Cleanup wie hart? **Mild** (nur Glows weg) / **Mittel** (+ Akzentfarben reduzieren) / **Hart** (alle Deko-Emojis raus, SVG-Icons ueberall)?
