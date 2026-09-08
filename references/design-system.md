# Design system — "Arabic Infographic" board

Extracted from a full scan of all 100 pins (Saudi/Gulf editorial infographics). This is
the reference the skill draws on in Step 2 (copy) and Step 3 (visual system).

## Format & grid

Vertical single-panel poster, **4:5** (feed) or **9:16** (story). **RTL throughout** —
text right-aligned, reading right-to-left, headline anchored top-right.

Layout stack, top → bottom:
1. **Source/authority bar** — ministry/org logo + wordmark in the top corners, small.
2. **Kicker / eyebrow** — short context line, gold, light weight.
3. **Hero headline** — GIANT Arabic display, **stacked one word per line**, right-
   anchored, one word in an accent color (gold/white/magenta) against the ground.
4. **Photographic / illustrated hero** — cut-out subject (person, landmark, artifact,
   or concept illustration), duotone or warm-graded, often bottom-center or right;
   sometimes polaroid/torn-paper framed and tilted.
5. **Dek / narrative body** — one sentence, or a short story paragraph on a colored panel.
6. **Stat cluster** — 3–6 blocks: BIG numeral (gold) + micro-label + optional micro-
   paragraph; a left column or a bottom band.
7. **Footer** — emblem/seal, source repeat, sometimes a Vision-2030-style wordmark.

## The 6 archetypes

Pick ONE per poster, by content mood.

1. **Dark cinematic place/landmark** — deep green/teal/navy/black ground, gold + white
   type, photographic or rendered landmark graded into darkness, film grain, big gold
   place-name title. For places, heritage, tourism, megaprojects.
   Refs: وادي العقيق · العلا · الدرعية 2030 · القديّة · جدة التاريخية · صيف السعودية ·
   الرياض وجهة العالم.

2. **Light warm editorial** — cream/beige ground, one deep brand color as a torn-paper /
   paint color field behind the headline, gold numerals, flat flag/emblem graphics,
   polaroid photo of an official/handshake. For economy, policy, partnerships.
   Refs: اقتصاد قوي يزهر بالفرص · KSIA بوابة الرياض · توقيع اتفاقية استثمارية.

3. **Storytelling human-interest** — cream + a deep plum/colored panel, magenta/pink
   emotive stacked headline, cut-out portrait of the subject, a narrative paragraph,
   a supporting stat row, partner logos. For a person's story.
   Refs: سميرة تعود إلى منزلها · بكم تمضي خطايَ نحو الأنجم · حريدنا خرج ورد العادة.

4. **Profile / portrait editorial** — single official or figure portrait, dark ground,
   gold title, a pull-quote, and stat blocks. For a named person / leadership piece.
   Refs: وزير السياحة "ليس شمسًا شارقة" · Al Diriyah · عام ترسخ الريادة الرقمية · NanoX.

5. **Creative-concept think-piece** — a conceptual illustration (sprouting plant-brain,
   face silhouette, pocket watch, stacked books, robot hand) on a rust/orange or dark
   ground; magazine-editorial feel. For how-to, listicle, opinion, self-development.
   Refs: كيف تصمم الهوية · خطوات بسيطة للتغيير · 10 مهن · بناء العادات · 8 طرق ·
   فوائد ممارسة الرياضة · The Secret to Real Change.

6. **Data-dense stat poster** — a grid of oversized gold numerals + micro-labels, hero
   minimized. For reports, rankings, sector figures.
   Refs: قطاع الطيران في السعودية · Al Diriyah 8-stat grid · السعودية · منصة نسك عمرة.

## Cover panel (carousel lead)

A carousel opens with a title-only cover, badge `0/N` or just the logo. It carries only:
emblem + kicker + GIANT stacked headline (accent word in gold) + source line. No body,
no stat band — atmospheric full-bleed hero. Same archetype/palette/aspect as the set;
the cover is the "poster face", content panels `1/N … N/N` carry the data.

## Layout modes (beyond the single hero grid)

Most panels use the hero grid (headline → hero → body → stats). Two extra modes recur:

- **Two-column comparison** (e.g. الفرص / المخاطر): two side-by-side RTL columns, gold
  header on the right column, a contrasting tint (often rust `#B5432A`) on the left; equal
  widths, a thin gold divider. Each column holds one verbatim block. Good for opposed pairs.
- **Comparison table** (e.g. a countries × strategy grid): RTL columns, header row in gold,
  rows verbatim. Tables are the **hardest** thing for image models — always deliver the
  **scene-only plate** (a faint gold grid + calm empty cells) and **typeset the table** in a
  real RTL editor; treat the combined prompt as throwaway. Keep a table to one panel; if it
  won't fit legibly, split by **whole rows** across two panels (never split a row).

## Capacity (rough heuristic, per panel)

Legibility budget — a guide for overflow/panel-count decisions, not a hard limit:
- **4:5**: one headline + ~60–90 words of body + up to ~4 stats.
- **9:16**: about 1.5× the above (taller). A dense report section or a 7-row table is at or
  past the ceiling → prefer scene-only + typeset, or split.

## Palettes (ground / primary / accent)

- Deep green `#0B3D2E` / gold `#C9A24B` / cream `#F3EAD3`
- Navy-teal `#0E2A33` / gold `#C9A24B` / white
- Black `#111111` / gold `#C9A24B` / warm grey
- Cream `#F3EAD3` / deep green `#0B3D2E` / gold  (light warm editorial)
- Cream `#EFE7D6` / plum `#5B2A4A` / magenta `#C7275E` + gold  (storytelling)
- Violet/lavender `#4A2C6B` / teal accent / gold  (think-piece & story)
- Rust/burnt-orange `#B5432A` / cream / gold  (concept editorial)
- Turquoise `#0E6E6E` / gold / cream  (tourism)

Gold `#C9A24B` is the through-line accent across the whole board — use it for numerals,
kicker, and the accented headline word.

## Archetype selection (deterministic) — use for Step 3

Decide in this order; first match wins. State the pick + one-line reason before generating.

1. **A named person is the subject** (leader/official/figure, portrait implied) → **Profile
   / portrait editorial**.
2. **One person's human story / emotional narrative** → **Storytelling human-interest**.
3. **A place, landmark, city, megaproject, tourism** → **Dark cinematic place/landmark**
   (tourism → turquoise palette).
4. **How-to / listicle / opinion / self-development** → **Creative-concept think-piece**.
5. **Report/ranking that is mostly numbers, little narrative** → **Data-dense stat poster**.
6. **Economy / policy / partnership with mixed text + stats** → **Light warm editorial**
   (or Data-dense if it is overwhelmingly numbers).

## Archetype → palette + mood (defaults, with fallback)

| Archetype | Default palette | Fallback palette | Mood phrase for prompts |
|---|---|---|---|
| Dark cinematic place/landmark | Navy-teal `#0E2A33` / gold / cream | Deep green `#0B3D2E` / gold / cream | cinematic, atmospheric, national pride |
| Light warm editorial | Cream `#F3EAD3` / deep green `#0B3D2E` / gold | Cream `#EFE7D6` / navy / gold | official, confident, institutional |
| Storytelling human-interest | Cream `#EFE7D6` / plum `#5B2A4A` / magenta + gold | Violet `#4A2C6B` / teal / gold | tender, human, intimate |
| Profile / portrait editorial | Black `#111111` / gold / warm grey | Navy-teal `#0E2A33` / gold / cream | authoritative, composed, dignified |
| Creative-concept think-piece | Rust `#B5432A` / cream / gold | Violet `#4A2C6B` / teal / gold | bold, editorial, thought-provoking |
| Data-dense stat poster | Navy-teal `#0E2A33` / gold / cream | Deep green `#0B3D2E` / gold / cream | precise, confident, factual |
| Tourism variant (of dark cinematic) | Turquoise `#0E6E6E` / gold / cream | Navy-teal `#0E2A33` / gold / cream | inviting, warm, vivid |

Never apply "national-pride / official / patriotic" mood outside the archetypes whose row
lists it — it distorts stories, opinion, and neutral reports.

## Typography

- **Headline**: heavy Arabic display — modern Kufi or bold Naskh — tight leading,
  right-aligned. Suggested faces (name one in prompts as a fallback stack): *Cairo Black,
  Tajawal Black, IBM Plex Sans Arabic Bold, Noto Kufi Arabic, Aref Ruqaa* (display).
  - **Stacking is display-only** and must not change the wording. Prefer one word per
    line; when a phrase has no natural single-word break, group into 2–3 balanced lines.
    A one-word headline just sits large. **Accent**: highlight one word in gold; if none
    suits (single word, or accenting distorts meaning), accent a gold underline/rule
    instead. If the verbatim headline is too long to be legible even stacked, escalate to
    a carousel or ask the user to approve a shorter display title — never silently cut it.
- **Body / labels**: light–regular Arabic (Tajawal, IBM Plex Sans Arabic, Cairo Light).
- **Numerals & bidi (preserve, don't normalize)**: keep the **exact digit set** from the
  copy — do not convert Western `41` ↔ Eastern `٤١`. Preserve every sign, `%`, decimal
  separator, `+`, arrow, date, currency, URL, Latin acronym, parenthetical, Arabic comma
  `،` / question mark `؟`, and religious mark exactly. Put any mixed LTR/RTL string in its
  own quoted line in the prompt so the model keeps its internal order. Numerals render
  LARGE in gold or white.

## Graphics & mood vocabulary

Duotone / warm-graded photography · torn-paper & paint color fields · polaroid frames
(white border + slight tilt) · subtle film grain / paper texture · flat flag & emblem
graphics · circular portrait thumbnails as list bullets · Vision-2030 / ministry seals ·
national-pride, official, cinematic warmth.

## Copywriting rules — COMPOSE MODE ONLY

These apply **only** when the user asked you to write/improve/translate, or gave a topic
with no copy. In preserve mode you organize verbatim text and ignore this section.

- **Register**: Modern Standard Arabic. Official/warm for gov & economy; tender and
  human for storytelling; brisk and punchy for think-pieces.
- **Headline = ONE idea**, 2–5 words, engineered to stack. Emotive verb or noun phrase
  (e.g. "اقتصاد قوي يزهر بالفرص", "سميرة تعود إلى منزلها"). Everything else → dek/stats.
- **Kicker** sets context in 2–5 words ("بعد سنوات الغياب", "اليوم العالمي…").
- **Stats**: number + 1–3 word label; optional 6–12 word explainer. Only real figures
  from the copy — never fabricate.
- **Story paragraph** (storytelling archetype): 2–4 sentences, past-tense human narrative.
- **Source** line: the organization, on the footer (only if known — see the no-invention
  guardrail in SKILL.md).
- **Bilingual** (optional): Arabic primary, a smaller secondary LTR line under the headline
  or dek (EN/FR/ZH). In preserve mode the user must supply or authorize this line.
