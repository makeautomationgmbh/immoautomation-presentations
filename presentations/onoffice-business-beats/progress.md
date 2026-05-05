# onOffice Business Beats — Session Progress

> **Neue Session?** Erst dieses File lesen, dann `audit.md` fuer Slide-Details.

---

## Auftrag

Komplett-Umbau der Praesi:
1. Design System aus `~/Downloads/design.md` durchziehen (Source of Truth).
2. Jede Slide pruefen + optimieren.
3. Slide 23 (Pitch) ist die natuerliche Killer-Folie fuer onOffice.

---

## Workflow-Regeln (wichtig)

- **Slide-by-Slide.** Niki schaut sich die Slide im Browser an, ich pitche Aenderungen, Niki entscheidet, ich mache.
- **Du-Form ueberall.** Nicht "Sie/ihr/eure". design.md sagt explizit "wir Siezen nicht". (Repo-CLAUDE.md sagt zwar Sie, aber design.md ist frischer und gilt.)
- **design.md ist Source of Truth.** Bei Konflikten mit Repo-CLAUDE.md gewinnt design.md.
- **Design-Ideen pitchen, nicht still entscheiden.** Niki will fuer jede Slide 2-3 Design-Optionen sehen, dann waehlt er. Nie ungefragt Layout/Farben/Typo aendern.
- **"Einfach in unser design bringen"** = Standard-Cleanup ohne Pitch (Pills mit Glow → Eyebrow, dark → light bei Kapitel-Slides, Du-Form-Fix, Em-Dashes raus, verbotene Akzentfarben raus). Nur bei Layout-Aenderungen pitchen.
- **Cache-Issue:** Niki muss nach jedem Edit `Cmd+Shift+R` druecken (file:// hat keine Cache-Header).

---

## Bisheriger Fortschritt

### Done

| Slide | Was geaendert |
|---|---|
| 01 Titel | Nichts. Passt. |
| 02 KI Stats | `+21%` von gruen → blau (`--ia-blue`); `40%` blieb in Variation `#0066CC`. |
| 03 Reichweite Paradox | "eure Follower" → "deine Follower". Alte Split-Box durch **Diverging Bars** ersetzt: Posts +21% waechst nach oben, Reach –31% faellt nach unten, gemeinsame Baseline mit Tag "2024 Baseline". |
| 04 Kapitel 01 | Von `dark` auf `light` umgestellt. Background jetzt `--ia-white` (#FAFBFF). Ambient-Glow weg. `chapter-num` Farbe auf light angepasst (rgba(0,0,0,0.04)) mit `.dark .chapter-num` Override fuer evtl. dark slides. |
| 05 Über mich | Avatar-Glow weg (3px blue+shadow → 1px hairline). Em-dashes raus (Step 2). Step 3 Headline: `Social Media auf Knopfdruck` (blau auf "Knopfdruck") + Detail `Posts in 30 Sekunden. KI-Software für Makler.` Pill: `Gründer & Geschäftsführer` (war `Der rote Faden: Social Media`). immoautomation Wordmark-Logo top-right (56px, neue SVG aus Downloads). Footer Logo-Wall (vergroessert): Wuestenrot, Werth, VR Immo-Service Mainfranken, AH Immobilien (Originalfarben) + `100+ weitere Makler` (18px bold). Logos in `logos/`. |
| 06 Kapitel 02 | `dark` → `light`. Ambient weg. eyebrow inline color rgba(255,255,255,0.3) entfernt (nutzt jetzt default light eyebrow). |
| 07 KI Nutzung | Reihenfolge getauscht: 💡 Ideen & Sparring jetzt Position 1 (war 4), dann 💬 Texte, 🖼️ Bilder, 🎬 Reels. Auto-Reveal-Timer raus, **manueller Substep-Modus** per Leertaste rein (Section hat `data-substeps="4"` + Cards `data-substep="1-4"`, Slide oeffnet leer, jede Leertaste blendet eine Box ein). 3 Em-Dashes raus, "ihr verfeinert" → "du verfeinerst". |
| 08 3 Stufen | Niki: "lassen wir die Folie mal so" — kein Cleanup gemacht. **Offene Pflicht-Fixes** (siehe Naechste Schritte). |
| 09 Kapitel 03 | `dark` → `light`. eyebrow inline-color raus. |
| 10 Agentic AI | Niki: "finde ich nicht so geil, mache ich später" — **geskippt**. Aktueller Stand im File: **kreisfoermige Vorher/Nachher-Visualisierung** (links 8 isolierte Tool-Bubbles, rechts Hub "DU" + 6 Workflow-Knoten BRIEF/RESEARCH/CONTENT/DESIGN/PUBLISH/ANALYSE auf gestricheltem Kreis mit Pfeilkoepfen). Niki mag's aber nicht — neuer Anlauf bei spaeterer Session noetig. |
| 11 Makler vorbereitet | Gruene Pill mit Glow → Eyebrow "Die gute Nachricht". "Ihr habt" → "Du hast". 3 Em-Dashes raus (Reason 1, 2, 4). |
| 12 Agenten Aufgaben | Blaue Pill mit Glow → Eyebrow "Agentic AI". "eurem Alltag" → "deinem Alltag". |
| 13 Agenten System | **Komplett-Umbau auf horizontalen Flow.** Mitarbeiter (links, gruener 120px-Avatar) → Connector mit fliessendem Packet → Social Media Agent (Mitte, 180px-Avatar mit Glow + "Verteilt die Aufgaben"-Pill) → SVG-Faecher mit **rechtwinkligen L-Pfaden** (Trunk-Knick bei x=240, kein Diagonal mehr) → 3 vertikal gestapelte Sub-Agent Cards rechts (Analyse 📊 / Research 🔍 / Planung 📅, alle exakt 170px hoch via fixer height). "⚡ Arbeitet die Aufgaben ab"-Label sitzt absolut positioniert als Spalten-Header ueber den 3 Cards (Pendant zu "Verteilt die Aufgaben" unter SMA). Animation-Sequenz: 0.3s Mitarbeiter → 0.8s Connector → 1.2s SMA pop → 1.6s Packet-Loop → 1.8s Verteilt-Pill → 2.3s SVG-Pfade zeichnen → 2.6s Action-Label → 3.0/3.2/3.4s Cards staffel → 3.4s SVG-Packets loop (animateMotion folgt L-Pfaden inkl. Eckpunkten). Diagram-Geometrie: 1472×554px, voll genutzt. SVG viewBox 340×554, paths `M 0 277 H 240 V 85/277/469 H 340`. **Akzentfarben in Card-Icons (lila/pink/orange) bewusst beibehalten** als visuelle Differenzierung der 3 Sub-Agenten — Niki's expliziter OK trotz design.md-Single-Accent-Regel. |
| 14 Live Chat-Demo | **NEUE Slide. Ersetzt komplett die alten Slides 15-19** (User fragt / März-Post / Agent fragt / User bestaetigt / Fertiges Ergebnis). Eine einzelne Slide mit `data-steps="5"` — 6 Steps (0-5) per `→` durchsteppen, **echtes Chat-Fenster mit Auto-Scroll** (Container scrollt smooth nach unten, alte Nachrichten schieben oben raus). Frame: 1200×780px, fixe Höhe, `display:flex column`, Header (Agent Name + Online-Pill) + scrollable `c-body.live` + Input-Bar (decorative). **Steps:** 0 User-Frage + Agent-typing → 1 März-Performance-Card → 2 Agent-Vorschlag → 3 User "Ja, mach das." + Agent-typing → 4 Agent fertig + Attachment-Card mit Caption + Hashtags → 5 Divider "2 Wochen später" + proaktiver Vorschlag mit Stat-Card + CTA-Buttons. **Step-Reveal:** `[data-step] { display:none }` / `.step-visible { display:flex; animation:msgFadeIn .4s }` — robust, kein max-height-Clipping mehr. **Auto-Scroll:** `scrollTop = scrollHeight` 6× (sofort + 50/200/450/750/1100ms) damit Container am Ende bleibt. Container `flex:1 1 0; min-height:0; overflow-y:auto` (Flexbox-Bug-Fix). **Avatar-Icon:** SVG-Sparkle (4-Zacken-Stern) statt Unicode `✦` (Inter-Font rendert das nicht, fällt auf "+" zurück). **Rafael-Avatar:** `<img class="c-user-avatar" src="uploads/rafael-photo.png">` rechts der User-Bubbles. **Bild-Posting-Mockup (Step 4):** Inline-SVG-Foto (Sunset-Sky + Skyline-Silhouetten in 2 Tiefen + lit windows via Pattern + clipPath) als Background, dark gradient overlay unten 62%, Text-Overlay drauf (Pin/Date/Hero +3,8%/Bars/Foot). Aspect-Ratio 4:5. **Wichtig: Bild-Post, NICHT Reel/Video** — alle Mentions ("Kurzvideo, 45 Sek." / "45-Sek-Skript" / "Wien21_Marktupdate.mp4" / "Instagram Reel · 9:16 · 45 Sek." / Skript-Timestamps `[0:00-0:08]`) wurden zu Bild-Post-Sprache umgeschrieben (Bild-Post mit Statistik-Visual / Caption / Wien21_Marktupdate.png / Instagram Post · 4:5 / Caption-Text + Hashtags). Niki's expliziter Wunsch. Border-Radius alles 0 (Avatare/Dots bleiben 50%). |
| 15 Proaktiv | **CI-Cleanup, kein Layout-Umbau.** Pill mit Glow ("ZWEI WOCHEN SPÄTER") → Eyebrow ("Zwei Wochen später"). Analyse-Agent-Card: lila (#8b5cf6 + rgba(139,92,246,…)) → blau-Hierarchie (Avatar `--ia-blue-light`/`--ia-blue-border`, Card weiß + hairline border, Eyebrow + Strong-Color `--ia-blue`). Vorschlag-Card: Gradient + Box-Shadow + 3px Border raus → flat solid blue avatar + `--ia-blue-light` Card-Background, 1px Border. 3 Em-Dashes raus (`12% Engagement —` → Punkt; `Bezirke vor —` → Punkt; `3. Bezirk —` → Mittelpunkt `·`). **Doppelung mit Step 5 in Slide 14 bewusst beibehalten** — Niki entscheidet später, ob Slide raus oder bleibt. Headline + Inhalt unangetastet. |
| 16 Realität | Niki: "passt" — kein Cleanup gemacht. Em-Dash + Akzentfarben (orange/grün) + Avatar-Borders 3px stehen noch im File, sind aber bewusst beibehalten (analog Slide 13). |
| 18 Pitch | **dark → light, 🏢-Emoji + Avatar-Kreis raus, Wordmark-SVG rein.** Section `class="dark"` → `light`. Avatar-Kreis (120x120, gradient + 60px-glow) komplett entfernt — stattdessen `<img src="logos/immoautomation-wordmark.svg" height="96">` zentral. Text-Colors umgezogen (rgba(255,255,255,…) → var(--ia-fg-secondary)/var(--ia-black)). CTA-Box: `rgba(0,128,255,0.12)` + 2px border → `var(--ia-blue-light)` + 1px `var(--ia-blue-border)`. Button border-radius 4px → 0. **Du-Form:** "Wollt ihr dabei sein?" → "Willst du dabei sein?", "Schaltet … seid" → "Schalte … sei". Em-Dash raus (`Bewertungen — viele` → Punkt). Sub-Subline minimal getrimmt (`28px` → `26px`) damit's mit dem größeren Wordmark balanciert ist. |
| 17 Vorsprung | **Komplett-Umbau von 3 Karten ("Drei Typen") auf Time-Race-Diagramm.** Aussage gleich (früher Nutzer hat Vorsprung), Visualisierung neu. SVG (viewBox 1640×600) mit X-Achse (Heute/3M/6M/9M/12M), Y-Achse "REICHWEITE ↑". 3 smooth Bezier-Pfade gestaffelt gezeichnet via `stroke-dasharray:1; stroke-dashoffset:1` + `pathLength="1"` + `s17drawLine`-Keyframe (Pattern aus Slide 13). **L1 Früher Nutzer:** blau 4px, M 80 500 C 320 440 720 260 1140 100 — startet heute, steigt steil. **L2 Mehrheit:** grau 2.5px, M 610 500 C 740 470 940 380 1140 300 — startet erst bei 6M. **L3 Nachzügler:** grau-hell 2px, M 1010 500 C 1050 495 1100 470 1140 440 — startet erst bei 11M. Endpoint-Dots gestaffelt fade-in, **pulsing glow** auf L1-Endpoint (`s17pulse` keyframe, scale 1→2.2 + opacity 0.35→0, 2.6s loop). **"DU BIST HIER"-Pin** auf L1-Startpunkt: blaue rect-Box bei (20,425) + gestrichelter Connector + Dot bei (80,500). **Tooltip-Cards rechts** als HTML außerhalb SVG (position:absolute, left:1180px, top:100/300/440px, transform:translateY(-50%)) für reicheres Styling. Animation-Sequenz: 0.4s Pin → 0.8/1.4/2.0s Lines draw → 2.3/2.5/2.7s Endpoint-Dots → 2.4/2.6/2.8s Tooltips → 3.0s+ Pulse-Loop. Headline neu: "Der Vorsprung lässt sich **in Monaten messen.**" Eyebrow "Wo stehst du?" behalten. **Pattern wiederverwendbar** für andere Time-/Progress-Diagramme. |

### Globale CSS/JS-Aenderungen

- `body{background:#000}` → `body{background:var(--ia-black)}` (#0C0C0C, nicht pure black)
- `.dark{background:#0a0a14}` → `.dark{background:var(--ia-black)}`
- `.dark .ambient::before` Radial-Gradient-Glows → `content:none` (design.md verbietet Glow-Effekte)
- `.chapter-num` color light default + `.dark .chapter-num` override
- **Manueller Substep-Modus**: `setSubstep()`/`getMaxSubstep()`/`getCurSubstep()` Helper, plus erweiterte `nextSlide`/`prevSlide` die nach `data-steps` auch `data-substeps` durchsteppen. Auto-Reveal-Timer in showSlide ist raus. Slide 07 nutzt das System.
- **Step-Modus für Chat-Demo** (Slide 14): `data-steps="N"` + Children mit `data-step="0..N"` (optional `data-hide-from="X"` damit ein Element wieder verschwindet ab Step X). CSS: `[data-step]{display:none}` / `.step-visible{display:flex;animation:msgFadeIn}`. JS in `setStep()` toggelt `step-visible` based on `elStep <= step && step < hideFrom`. Plus `[data-autoscroll]`-Element bekommt `scrollTop=scrollHeight` 6× (sofort + 50/200/450/750/1100ms) für robusten Scroll während Fade-In. Container muss `flex:1 1 0; min-height:0; overflow-y:auto` haben (Flexbox-Bug bei `flex:1` ohne min-height — Container scrollt nicht).

---

## Naechste Schritte (in Reihenfolge)

### Slide 08 — Pflicht-Fixes nachziehen (von Niki erstmal geskippt)

Niki sagte "lassen wir mal so", aber das sind echte design.md-Verstoesse, ggf. spaeter:
1. "Wir sind hier" Pin → "Du bist hier"
2. "ihr gebt nur das Ziel vor" → "du gibst nur das Ziel vor"
3. 2 Em-Dashes raus (Stufe 1 + Stufe 3 Caption)
4. Stufe 3 orange Akzente (Eyebrow, Zahl, dashed Kreis) → blau
5. Stufe 2 blauer Gradient → flat solid
6. Stufe 3 outer dashed Border → solid

### Slide 10 — Neudesign nochmal angehen

Niki will visuell, aber:
- Manifest-Variante (Editorial) hat ihm nicht gefallen
- Tool-Stack-Cluster + Single-Prompt-Bubble auch nicht
- Aktuelle zirkulaere Variante (Tools verstreut links, Workflow-Kreis mit DU-Hub + 6 Knoten rechts) auch nicht

**Ungeloeste Frage:** Was ist Niki's Vorstellung von "visuell" fuer Slide 10? Vielleicht in neuer Session direkt fragen, ob er ein Beispiel/Vorbild im Kopf hat. Die zirkulaere Visualisierung steht aktuell im File und kann als Ausgangspunkt dienen, oder komplett verworfen werden.

Ideen die noch nicht versucht wurden:
- Mock-Output als Hero (fertiger Instagram-Post als grosse Karte)
- Comic-Strip 3-Panel (Storyboard)
- Echter UI-Mockup-Screenshot des Produkts

### Slide 15 (alte 20 "Proaktiv") — Entscheidung vertagt

**CI-Cleanup ist gemacht** (siehe Done-Tabelle). Layout/Inhalt unverändert. Doppelung mit Slide 14 Step 5 bleibt offene Frage — Niki entscheidet später, ob Slide raus, Step 5 aus Demo raus, oder beides als Vertiefung.

### Slide 16 (alte 21) Realitaet + Slide 17 (alte 22) 3 Typen — Cleanup

Diverse Du-Form-Fixes, border-radius cleanup. Footer-Nummern stimmen nicht mehr nach dem Slide-14-Move. Im G7-Cleanup mit erledigen.

### Slide 18 — Pitch — DONE

CI-Cleanup gemacht (siehe Done-Tabelle).

---

## Globale Cleanups (am Ende)

- G1: Variablen-Namen (`--ia-blue` etc.) bleiben — design.md sagt zwar `--accent`, aber Aliasen waere viel Diff. Werte stimmen alle.
- G2: Newsreader-Font-Import nicht noetig (Praesi nutzt nur Inter). Aktuell schon raus.
- G4: Schatten `rgba(26,26,46,...)` → `hsl(250 30% 30% / X)` (Lila-Spektrum statt Schwarz). Steht in design.md.
- G5: Border-Radius-Audit: Slide 14 Chat-Demo schon auf 0 gesetzt. **Übrige Slides (15-18) noch checken** — alte Bubbles/Cards/Buttons mit border-radius drin.
- G7: Footer-Nummern fixen — durch das Slide-14-Move + Entfernung der alten 15-19 sind die Footer- + `data-screen-label`-Numerierungen jetzt komplett verschoben (z.B. Slide 18 trägt aktuell intern `data-screen-label="23 Pitch"`). Bei finalem Cleanup sauber durchnummerieren.
- G8: Slide-14-Numerierungsluecke ist jetzt geschlossen (Chat-Demo füllt 14).

---

## Wichtige Files

| Pfad | Zweck |
|---|---|
| `~/Downloads/design.md` | Design-System Source of Truth |
| `presentations/onoffice-business-beats/index.html` | Die Praesi (alles in einem File) |
| `presentations/onoffice-business-beats/audit.md` | Detail-Audit aller Slides + Findings |
| `presentations/onoffice-business-beats/progress.md` | Dieses File. |
| `presentations/onoffice-business-beats/logos/` | immoautomation-wordmark.svg + 4 Kunden-Logos (Wuestenrot, Werth, VR Mainfranken, AH Immobilien). |
| `CLAUDE.md` (repo root) | Repo-Konventionen — ABER: bei Konflikt mit design.md gewinnt design.md (siehe Workflow-Regeln). |

---

## Etablierte Asset-/Copy-Konventionen

- **Rafaels Rolle:** `Gründer & Geschäftsführer` (nicht "CEO", nicht "Founder").
- **Rafael-Avatar im Chat:** `<img class="c-user-avatar" src="uploads/rafael-photo.png">` — rechts der User-Bubbles in Slide 14.
- **Produkt-Slogan:** `Social Media auf Knopfdruck` mit blau-Akzent auf "Knopfdruck".
- **Produkt-Tagline:** `Posts in 30 Sekunden. KI-Software für Makler.`
- **Kunden-Logos:** **Originalfarben** (nicht grayscale, nicht monochrom) — Niki's bewusste Entscheidung.
- **Trust-Tag:** `100+ weitere Makler` (18px bold black; "100+" in blau bold).
- **Brand-Logo Slide 05:** top-right floating, 56px hoch (Original-Hoehe der Wordmark-SVG).
- **Pills mit Glow → Eyebrow** als Standard-Cleanup-Pattern (siehe Slides 09/10/11/12).
- **Substep-System** (manuell per Leertaste): Section bekommt `data-substeps="N"`, Children `data-substep="1..N"`. CSS mit `.substep-visible` macht sichtbar. JS-Logik in nextSlide/prevSlide.
- **SVG mit rechtwinkligen L-Pfaden** als Connector-Pattern (etabliert in Slide 13): viewBox-basiert, `pathLength="1"` + `stroke-dasharray:1` + Animation auf `stroke-dashoffset` fuer Draw-In. `animateMotion` mit `path="..."`-Attribut fuer Packets, die Eckpunkten folgen. Trunk-Knick erzeugt durch H/V/H Path-Commands statt Diagonal. Pattern wiederverwendbar fuer weitere Diagramm-Slides.
- **Agent-Avatar-Icon:** Inline-SVG-Sparkle (4-Zacken-Stern, `M12 0l2.5 9.5L24 12l-9.5 2.5L12 24l-2.5-9.5L0 12l9.5-2.5z`) — **NIEMALS Unicode `✦`** (U+2726), das wird von Inter-Font nicht supported, Browser fällt auf "+" zurück.
- **Bild-Posting im Chat (NICHT Reel/Video):** Agent erstellt im Demo-Verlauf einen **statischen Bild-Post**, kein Video. Sprache: "Bild-Post mit Statistik-Visual" / "Post-Bild + Caption + Hashtags" / "Wien21_Marktupdate.png" / "Instagram Post · 4:5". Niemals "Skript / Reel / mp4 / 45-Sek-Video / Timestamps `[0:00-0:08]`".
- **Marktupdate-Mockup-Pattern (Slide 14 Step 4):** Inline-SVG-Background (Sunset-Sky-Gradient + Skyline-Silhouetten 2 Tiefen-Ebenen + lit windows via SVG `<pattern>` + `<clipPath>` auf Building-Rects, opacity 0.55) + dark gradient overlay (`linear-gradient(180deg, transparent, rgba(8,15,30,0.94))` bottom 62%) + Text-Overlay mit z-index:2 (Pin/Date oben, Hero-Number unten, Bars-Mini-Chart, Foot). Kein externes Asset nötig, scharf auf jeder Auflösung.

---

## Tasks (Stand jetzt)

- ✅ #1–7: Slides 01–07 done
- ⏸ #8: Slide 08 von Niki erstmal geskippt — Pflicht-Fixes offen
- ✅ #9: Slide 09 done
- ⏸ #10: Slide 10 mehrere Anlaeufe verworfen — neuer Versuch in spaeterer Session
- ✅ #11: Slide 11 done
- ✅ #12: Slide 12 done
- ✅ #13: Slide 13 done — horizontaler Flow + rechtwinklige Connections + voll skaliert
- ✅ #14: **Slide 14 Live Chat-Demo done.** Ersetzt komplett alte 15-19. Step-System mit display-toggle + Auto-Scroll, Bild-Posting-Mockup mit SVG-Foto-Background, Rafael-Avatar bei User-Bubbles.
- ✅ #15: Slide 15 Proaktiv — CI-Cleanup done (lila → blau, Pill → Eyebrow, Em-Dashes raus). Doppelung mit Slide 14 Step 5 bleibt offene Frage.
- ✅ #16: Slide 16 Realität — Niki: "passt", kein Cleanup gemacht. Akzentfarben + Em-Dash bewusst beibehalten.
- ✅ #17: Slide 17 Vorsprung — Komplett-Umbau auf Time-Race-Diagramm. SVG mit 3 smooth Bezier-Linien, gestaffelt gezeichnet, "DU BIST HIER"-Pin, pulsing endpoint, Tooltip-Cards rechts.
- ✅ #18: Slide 18 Pitch — dark → light, Wordmark-Logo statt 🏢-Emoji, CTA-Box gecleant, Du-Form, Em-Dash raus, Glow weg.
- ⏳ #18: Pitch — Cleanup pending
- ⏳ #19: Globale Cleanups (am Ende, inkl. G7 Footer-Renumber)
