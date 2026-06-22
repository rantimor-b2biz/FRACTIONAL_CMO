---
name: canvas-design
description: Create premium static visual art and design assets (.png, .pdf) using a design-philosophy-first approach. Use when creating posters, thought leadership graphics, LinkedIn carousels, editorial covers, or any high-craft static piece for Fractional CMO content.
client: Fractional CMO
brand-ref: T-tools/skills/brand-guidelines-skill.md
---

# Canvas Design Skill — Fractional CMO Edition

## Overview

This skill produces museum-quality static visuals using a two-step process: **design philosophy first, then visual execution**. Output is always `.png` or `.pdf`.

**Keywords**: canvas, poster, graphic design, static visual, LinkedIn graphic, carousel, editorial, brand design, thought leadership visual

---

## When to Use This Skill

- Creating a LinkedIn carousel cover that must stop scroll
- Designing a thought leadership graphic for Ran's content
- Producing a blog/article header image
- Building any high-craft static visual where artistic quality matters
- Executive-quality one-pagers or visual essays

**Not for:** Realistic photography (→ use flux-prompt-engineering-skill), data dashboards (→ HTML/SVG), or interactive content (→ algorithmic-art-skill).

---

## The Two-Step Process

### Step 1 — Design Philosophy

Before touching canvas tools, write a visual philosophy (`.md` file). This is NOT a layout brief — it's an aesthetic worldview.

**Name the movement** (1–2 words): e.g., "Executive Silence", "Founder Clarity", "Minimal Authority"

**Write the philosophy** (4–6 paragraphs):
- How does it express through space, form, color, composition?
- What visual weight and hierarchy communicate the idea?
- What is the *mood* — not the content?

**Critical guidelines:**
- Emphasize craftsmanship repeatedly — the work must look like it took countless hours by someone at the top of their field
- Minimize text in the philosophy — ideas live in design, not paragraphs
- Leave creative space — the philosophy guides, it doesn't dictate every pixel
- Keep generic enough to work across the full Fractional CMO content universe

**Philosophy examples for Fractional CMO:**

> **"Executive Silence"**
> Philosophy: Power communicated through restraint and empty space.
> Visual expression: Navy fields holding a single sharp cyan accent. Typography whispered in small Inter labels — never shouted. Vast negative space as confidence signal. The composition breathes. Horizontal bands of deep navy interrupted by precise geometric moments. Text minimal — a single phrase, placed with surgical intent. Every element the result of painstaking subtraction. A master's hand removed more than it added.

> **"Precision Signal"**
> Philosophy: Data-point aesthetics where every mark carries information.
> Visual expression: Technical grid systems barely visible at low opacity. Cyan lines charting invisible trajectories. Typography as axis labels. Deep navy ground. No decoration — every element is load-bearing. The visual reads like a proprietary framework diagram from a top-tier consulting firm. Relentlessly precise, yet clearly human in its composition choices.

---

### Step 2 — Canvas Execution

With the philosophy established, execute on canvas. Use Python (Pillow/Cairo), HTML Canvas, or SVG.

**Brand alignment (mandatory):**
- Pull colors from `T-tools/skills/brand-guidelines-skill.md`
- Default palette: Navy `#0A1128` + Cyan `#00D9FF` + White `#FFFFFF`
- Typography: Inter or Poppins; fallback Arial
- Flat design — no gradients, no shadows unless philosophy demands

**Craftsmanship requirements:**
- No element overlaps unless intentional and designed
- All text within canvas boundaries with proper margins
- Spacing is deliberate — not arbitrary
- Color choices feel intentional and cohesive (limited palette: 2–4 colors max)
- Typography is design-forward — font is part of the art, not decoration
- Second-pass refinement is mandatory: after generating, review and make more cohesive

**Canvas conventions:**
- **LinkedIn optimal:** 1080×1350px (portrait)
- **Article/blog header:** 1200×600px
- **Quote graphic:** 1080×1080px (square)
- **Carousel cover:** 1080×1350px
- **PDF one-pager:** A4 (2480×3508px at 300dpi)

---

## Conceptual Thread (Critical)

Before executing, identify the **subtle conceptual reference** from Ran's content:

The topic should be a **quiet DNA woven into the visual** — not announced, not literal. Someone who read the article should feel it. Others simply experience a masterful design. Think like a jazz musician quoting a theme — only those who know catch it.

For Fractional CMO, this often means:
- The tension between automation and human judgment → precision lines that converge but don't merge
- The founder's loneliness → vast negative space with a single anchor point
- Strategic leverage → geometric force diagram aesthetics
- Trust-building over time → layered translucent planes

---

## Refinement Protocol

After generating, ask: *"Is this pristine? Would this work framed in a boardroom?"*

To refine:
- ❌ Don't add more graphics — refine what's there
- ❌ Don't introduce new colors — deepen the existing palette
- ✅ Adjust spacing for more tension or breathing room
- ✅ Tighten typography to feel more intentional
- ✅ Reduce anything that doesn't contribute to the philosophy

---

## Output Format

1. **Philosophy file:** `[topic]-design-philosophy.md`
2. **Visual asset:** `[topic]-visual.png` or `[topic]-visual.pdf`
3. Save to: `O-output/[week-or-topic]/process/` (draft) → `final/` (approved)

---

## Fonts Available

Located in the original skill's `canvas-fonts/` directory. Key fonts for Fractional CMO:
- `BricolageGrotesque-Bold.ttf` — Strong executive headlines
- `IBMPlexMono-Regular.ttf` — Technical/data aesthetic labels
- `GeistMono-Bold.ttf` — Modern, developer-adjacent credibility
- `CrimsonPro-Regular.ttf` — Editorial, intellectual depth

---

## Quality Bar

The finished piece should look like:
- It could appear in a B2B thought leadership book
- A senior executive would save it as a reference visual
- It took a professional designer 4+ hours to produce
- No one would guess it was AI-assisted

**For Fractional CMO: minimalism is credibility.** Every removed element increases authority.

---

*Canvas Design Skill — Executive Edition*
*Fractional CMO / Ran Timor thought leadership visuals*
