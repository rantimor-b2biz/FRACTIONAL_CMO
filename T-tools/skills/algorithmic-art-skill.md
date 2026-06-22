---
name: algorithmic-art
description: Create interactive generative art and animated data visualizations using p5.js with seeded randomness. Use when Fractional CMO content calls for interactive thought leadership visuals, animated LinkedIn assets, generative brand patterns, or when Ran wants to create something visually distinctive and technically impressive.
client: Fractional CMO
brand-ref: T-tools/skills/brand-guidelines-skill.md
---

# Algorithmic Art Skill — Fractional CMO Edition

## Overview

This skill produces **living, interactive generative art** using p5.js. Output is a self-contained `.html` file (interactive) and/or `.png` captures. Use when the idea deserves motion, emergence, or parametric exploration.

**Keywords**: generative art, algorithmic, p5.js, animation, interactive, data visualization, flow fields, particles, brand pattern

---

## When to Use This Skill

- Creating an animated brand pattern for Fractional CMO (e.g., website background, video intro)
- Building an interactive thought leadership visualization (e.g., "the compounding effect of trust")
- Producing a distinctive LinkedIn video/GIF that stands out from static posts
- Demonstrating data behavior through animation (not static charts)
- Creating a generative brand asset that evolves with each seed

**Not for:** Static graphics (→ canvas-design-skill), realistic photography (→ flux-prompt-engineering-skill), standard charts (→ HTML/SVG directly).

---

## The Two-Step Process

### Step 1 — Algorithmic Philosophy

Write a computational aesthetic philosophy (`.md` file) before writing a single line of code.

**Name the movement** (1–2 words): e.g., "Trust Velocity", "Founder Emergence", "Signal Density"

**Write the philosophy** (4–6 paragraphs):
- What computational processes express this idea?
- What behaviors, forces, and dynamics are at play?
- How does emergence mirror the concept?
- What makes each seed variation feel unique yet coherent?

**Critical guidelines:**
- The philosophy must stress that the final algorithm looks like it emerged from countless iterations by a master generative artist
- Beauty lives in the *process* — each run is unique
- Parameters should feel natural to the idea, not arbitrary

**Philosophy examples for Fractional CMO:**

> **"Trust Velocity"**
> Philosophy: Points of connection accumulate slowly, then cascade.
> Algorithmic expression: Particles initialized at random positions, each carrying a trust-weight value that grows through proximity to other particles. When two particles spend time near each other, their connection strengthens and renders as an increasingly visible line. Perlin noise creates gentle drift — no particle travels in straight lines. The network slowly densifies from chaos into pattern, then occasionally a single strong connection becomes a hub, pulling nearby particles. The result feels like watching a founder network crystallize. Every parameter was refined through obsessive iteration by someone who understands both relationship dynamics and computational aesthetics at the highest level.

> **"Signal Density"**
> Philosophy: Information accumulates at the edges of noise.
> Algorithmic expression: Flow fields driven by layered Perlin noise. Thousands of tiny marks — not particles but momentary observations — accumulate along lines of force. The density gradient creates natural information architecture: high-density zones feel like consensus, sparse zones like unexplored territory. Color shifts from deep navy in low-density regions to sharp cyan at density peaks. The algorithm rewards patient viewing — meaning emerges over time. Every parameter calibrated through painstaking refinement at the intersection of data theory and generative art.

---

### Step 2 — p5.js Implementation

**Brand alignment (mandatory):**
```javascript
// Fractional CMO color palette
const BRAND = {
  navyDark: '#0A1128',
  navy: '#1A2238',
  cyan: '#00D9FF',
  cyanSecondary: '#00BFD8',
  blue: '#2E5CFF',
  white: '#FFFFFF',
  offWhite: '#F8F9FA',
  darkGray: '#1F2937',
  mintGreen: '#10B981',
  coral: '#EF4444'
};
```

**Seeded randomness (always):**
```javascript
let seed = 12345;
randomSeed(seed);
noiseSeed(seed);
// Same seed = identical output (reproducibility)
```

**Parameter structure:**
```javascript
let params = {
  seed: 12345,
  // Quantities, scales, probabilities, ratios, thresholds
  // that emerge naturally from the philosophy
};
```

---

## Interactive HTML Artifact

The output is a **single self-contained `.html` file** that runs immediately in any browser or claude.ai artifacts.

### Required Structure

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.7.0/p5.min.js"></script>
  <style>/* All styling inline */</style>
</head>
<body>
  <!-- Canvas area + Controls sidebar -->
  <script>
    // ALL p5.js inline: params, classes, setup(), draw(), UI handlers
  </script>
</body>
</html>
```

### Sidebar Controls (Standard)

**Fixed sections (always include):**
- **Seed:** Display + Prev/Next/Random/Jump buttons
- **Actions:** Regenerate, Reset, Download PNG

**Variable sections (per artwork):**
- **Parameters:** Sliders for each tunable value
- **Colors:** Optional — only if user should control palette

---

## Fractional CMO Application Context

Generative art for Ran's brand should feel:
- **Intellectually credible** — mathematical, systematic, not decorative
- **Calm authority** — emergent patterns, not chaotic noise
- **Minimal color** — navy + cyan accent, occasionally white traces
- **Slow revelation** — meaning builds over time (patience = intelligence signal)

It should NOT feel:
- ❌ Colorful / rainbow / playful
- ❌ Fast / frenetic / overwhelming
- ❌ Generic screensaver aesthetic
- ❌ Tech startup "we're innovative" cliché

---

## Output Format

1. **Philosophy file:** `[topic]-algo-philosophy.md`
2. **Interactive artifact:** `[topic]-generative.html`
3. **PNG captures** (optional): `[topic]-seed-[N].png`
4. Save to: `O-output/[week-or-topic]/process/` → `final/` when approved

---

## Quality Bar

The finished artifact should:
- Run smoothly (60fps target for animated work)
- Produce meaningfully different results per seed
- Have controls that feel responsive and intuitive
- Look like it was crafted by a top-tier generative artist with deep knowledge of both the subject matter and computational aesthetics
- Pass the "would I post this?" test for LinkedIn video content

---

*Algorithmic Art Skill — Executive Edition*
*Fractional CMO / Ran Timor — computational thought leadership visuals*
