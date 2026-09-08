# Image-gen prompt template + worked examples

Step 4 emits **three outputs per panel**: (a) copy organization, (b) scene-only
background prompt, (c) combined prompt. Skeletons for (b), (c), and the cover panel are
below. Keep the exact Arabic strings verbatim.

Only slots with supplied text appear — omit any slot the copy does not fill; never add
filler. Stats are repeatable (add as many rows as the copy has). Mood is the
archetype-specific phrase from the design-system table, not a fixed patriotic line.

## Skeleton — (b) Scene-only background prompt  ← RECOMMENDED PRODUCTION ROUTE

Use this for anything beyond a short headline; typeset the Arabic afterward.

```
Vertical poster background, {ASPECT: 4:5 | 9:16}, NO TEXT of any kind.
Archetype: {archetype}. Palette: ground {HEX/name}, accent gold #C9A24B, secondary {HEX/name}.
Texture: subtle film grain; {duotone / warm-graded}.
Scene: {hero subject}, {framing}, graded into the palette.
Reserve clean, low-detail, high-contrast empty zones for type:
- headline zone: top-right ~35% of height, kept clear;
- stat/body band: bottom ~22% of height, kept clear;
- NOTHING (no face, hero object, or busy texture) crosses these zones; keep them calm
  and evenly toned so light Arabic type reads on top.
No letters, no numbers, no logos, no watermark. High detail elsewhere, print-quality.
Background plate for Arabic type to be composited on top.
```

### Text-overlay spec (pair with the scene-only plate)
When you hand off (b), also give the user a typesetting payload:
- **Font stack**: Cairo / Tajawal / IBM Plex Sans Arabic / Noto Kufi Arabic (display weight
  for headline, light for body).
- **Zones**: headline in the top-right 35%; stats/body in the bottom 22%; align right, RTL.
- **Copy-paste text** (exact, RTL): the same verbatim strings from output (a), ready to
  drop into a real RTL-capable editor (Illustrator/Figma/Canva) — the reliable way to get
  perfect Arabic.

## Skeleton — (c) Combined prompt  ← PREVIEW / ATTEMPT ONLY (may garble long Arabic)

```
Vertical editorial infographic poster, {ASPECT: 4:5 | 9:16}, right-to-left (RTL) Arabic layout.

ART DIRECTION
Archetype: {archetype name from design-system.md}.
Mood: {archetype-specific mood phrase from the design-system table}.
Palette: ground {HEX/name}, accent gold #C9A24B, secondary {HEX/name}.
Texture: subtle film grain / paper texture; {duotone or warm-graded} treatment.

HERO
{subject to generate}, {framing}, graded into the palette.

LAYOUT (top → bottom, RTL, right-aligned) — include ONLY the slots the copy fills:
- Source bar top corners: "{SOURCE}" (text only; add a logo ONLY if the user supplied one —
  never a generic/generated emblem). Omit entirely if no source.
- Kicker (gold, small): "{KICKER}"
- Headline — large Arabic display, right-anchored, display-only line breaks, "{ACCENT}"
  in gold (or a gold underline if no word suits): "{HEADLINE}"
- Dek (one line): "{DEK}"
- Body (verbatim paragraph / quote / bullets): "{BODY}"
- {secondary LTR line, only if supplied/authorized: "{SECONDARY}"}
- Stat cluster ({left column | bottom band}) — repeat per stat: big gold numeral + label:
   - {NUMBER} — {label}
- Footer: source "{SOURCE}".

TYPOGRAPHY
Heavy Kufi/Naskh Arabic display for the headline; light Arabic for body; oversized gold numerals.

TEXT ACCURACY (critical)
Render ALL Arabic text exactly as written above, verbatim, right-to-left, correct letter
joining. Do NOT invent, translate, mirror, or distort any character. Preserve the exact
digits and punctuation shown. Print-quality poster.
```

If it garbles the Arabic, fall back to the scene-only plate (b) + the text-overlay spec.

## Skeleton — Cover panel (title-only lead, badge 0/N)

```
Vertical editorial poster cover, {ASPECT}, RTL Arabic. Carousel cover (0/N).
Archetype: {archetype}. Palette: ground {HEX/name}, accent gold #C9A24B, secondary {HEX/name}.
Texture: film grain; {duotone / warm-graded}. Hero: {subject}, atmospheric, full-bleed.
LAYOUT (centered/right, RTL): small emblem top; kicker (gold) "{KICKER}"; GIANT Arabic
display headline STACKED ONE WORD PER LINE, "{ACCENT WORD}" in gold: "{HEADLINE}".
Footer: source "{SOURCE}". NO body text, NO stat band.
TEXT ACCURACY (critical): render Arabic verbatim, RTL, correct letter joining; do not
invent, translate, mirror, or distort any character. Print-quality poster.
```

---

> ⚠️ **The two examples below are COMPOSE-MODE demonstrations** — the English source was
> translated and expanded into Arabic, and some figures/labels are illustrative. They show
> the *visual system only*. In **preserve mode** you must NOT translate or add figures,
> sources, or emblems — output only the user's exact strings.

## Worked example A (compose-mode demo) — Dark cinematic place/landmark (9:16)

Source copy: "Wadi Al-Aqiq near Madinah — a blessed valley the Prophet ﷺ prayed in.
Rich vegetation, seasonal water. Managed by Hajj authority."

```
Vertical editorial infographic poster, 9:16, right-to-left (RTL) Arabic layout.

ART DIRECTION
Archetype: dark cinematic place/landmark.
Mood: official, cinematic, national-pride, editorial-magazine warmth.
Palette: ground deep green #0B3D2E, accent gold #C9A24B, secondary cream #F3EAD3.
Texture: subtle film grain; warm-graded photography.

HERO
A lush green valley path near Madinah at golden hour, an information marker post in the
foreground, mountains behind — photographed and graded into deep green darkness at the
edges. Bottom two-thirds of the frame.

LAYOUT (top → bottom, RTL, right-aligned)
1. Source bar top corners: Saudi ministry emblem + "hajj.gov.sa", small.
2. Kicker (gold, small): "وادٍ مبارك قرب المدينة"
3. Headline — GIANT Arabic display, STACKED ONE WORD PER LINE, right-anchored,
   "العقيق" in gold, "وادي" in white:
   "وادي
    العقيق"
4. Dek (one line, light weight): "وادٍ مبارك صلى فيه رسول الله ﷺ"
5. Stat cluster (bottom band) — each: big gold numeral + tiny label:
   - ٦ — كيلومترات طولاً
   - ٢ — عيون دائمة الجريان
   - ١٩٦٦ — بداية الإشراف
6. Footer: Saudi emblem, source "هيئة تطوير المدينة المنورة".

TYPOGRAPHY
Heavy Kufi/Naskh Arabic display for the headline; light Arabic for body; oversized gold
numerals for stats.

TEXT ACCURACY (critical)
Render ALL Arabic text exactly as written above, verbatim, right-to-left, with correct
letter joining. Do NOT invent, translate, mirror, or distort any character. Numerals as
shown. High detail, print-quality, poster composition.
```

---

## Worked example B (compose-mode demo) — Storytelling human-interest (4:5)

Source copy: "After years away, Samira returns home in 2019 through the ICRC family-
links program. She'd been stranded abroad with no papers for 4 years."

```
Vertical editorial infographic poster, 4:5, right-to-left (RTL) Arabic layout.

ART DIRECTION
Archetype: storytelling human-interest.
Mood: tender, human, warm editorial.
Palette: ground cream #EFE7D6, secondary plum panel #5B2A4A, accent magenta #C7275E + gold #C9A24B.
Texture: soft paper grain; cut-out portrait treatment.

HERO
A cut-out portrait of a woman in dark clothing looking to camera, placed right of the
headline, no background — sits on the cream ground.

LAYOUT (top → bottom, RTL, right-aligned)
1. Source bar top corners: ICRC + partner logos, small.
2. Kicker (gold, small): "بعد سنوات الغياب"
3. Headline — GIANT Arabic display, STACKED ONE WORD PER LINE, right-anchored,
   "سميرة" in magenta, the rest in plum:
   "سميرة
    تعود
    إلى
    منزلها"
4. Story paragraph on a plum panel (light cream text):
   "بدأت معاناة سميرة عام ٢٠١٩ حين سافرت مع زوجها للعمل، ثم تعذّر عليها العودة لأربع سنوات
    بلا أوراق ثبوتية، حتى أعادها برنامج الروابط العائلية إلى وطنها."
5. Stat cluster (bottom row) — each: big gold numeral + tiny label:
   - ١٢٨٧ — حالة مكتملة
   - +١٥ ألف — نشاط
   - ١٣٥١٧ — رسالة
6. Footer: emblem, source "اللجنة الدولية للصليب الأحمر".

TYPOGRAPHY
Heavy Kufi/Naskh Arabic display for the headline; light Arabic for body; oversized gold
numerals for stats.

TEXT ACCURACY (critical)
Render ALL Arabic text exactly as written above, verbatim, right-to-left, with correct
letter joining. Do NOT invent, translate, mirror, or distort any character. Numerals as
shown. High detail, print-quality, poster composition.
```
