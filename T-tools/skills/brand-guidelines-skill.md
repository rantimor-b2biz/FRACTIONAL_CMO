---
name: brand-guidelines
description: Applies Fractional CMO (Ran Timor) brand colors, typography, and visual identity to any artifact — presentations, graphics, HTML, SVG, or documents. Use when brand consistency, visual formatting, or client design standards apply.
client: Fractional CMO
source: C-core/brand-colors.md
---

# Fractional CMO Brand Styling

## Overview

Use this skill to apply Ran Timor's official brand identity to any visual or design artifact.

**Keywords**: branding, brand colors, visual identity, post-processing, styling, typography, Ran Timor, executive design, B2B visuals

---

## Brand Colors

### Primary Palette

| Name | Hex | RGB | Use For |
|------|-----|-----|---------|
| **Dark Navy** | `#0A1128` | rgb(10, 17, 40) | Main backgrounds, hero sections, covers |
| **Navy Secondary** | `#1A2238` | rgb(26, 34, 56) | Secondary backgrounds, header |
| **Cyan / Turquoise** | `#00D9FF` | rgb(0, 217, 255) | Headlines, CTAs, accents, modern tech feel |
| **Cyan Secondary** | `#00BFD8` | rgb(0, 191, 216) | Secondary accents |
| **Royal Blue** | `#2E5CFF` | rgb(46, 92, 255) | Buttons, links, interactive elements |

### Secondary Palette

| Name | Hex | RGB | Use For |
|------|-----|-----|---------|
| **White** | `#FFFFFF` | rgb(255, 255, 255) | Text on dark bg, card backgrounds |
| **Off-White** | `#F8F9FA` | rgb(248, 249, 250) | Section backgrounds |
| **Dark Gray** | `#1F2937` | rgb(31, 41, 55) | Body text on light backgrounds |
| **Medium Gray** | `#6B7280` | rgb(107, 114, 128) | Subtitles, secondary text |
| **Mint Green** | `#10B981` | rgb(16, 185, 129) | Checkmarks, positive states, solutions |
| **Coral Red** | `#EF4444` | rgb(239, 68, 68) | X marks, problems, warnings |

---

## Typography

| Role | Font | Weight | Notes |
|------|------|--------|-------|
| **Headlines** | Inter / Poppins | Bold (700) | Clean, modern, tech-forward |
| **Subheadings** | Inter / Poppins | Semi-Bold (600) | |
| **Body Text** | Inter / Georgia | Regular (400) | 16–18pt for readability |
| **Captions / Labels** | Inter | Regular (400) | 12–14pt |

- **Fallbacks:** Arial for headings, Georgia for body
- **No decorative fonts** — executive minimalism requires restraint

---

## Color Combinations (Ready to Use)

### High Contrast — Cover / Hero / Key Message
```
Background: #0A1128 (Dark Navy)
Primary Text: #FFFFFF (White)
Accent: #00D9FF (Cyan)
Subtext: #F8F9FA (Off-White)
```

### Professional Clean — Content Sections
```
Background: #FFFFFF or #F8F9FA
Primary Text: #1F2937 (Dark Gray)
Accent: #2E5CFF (Royal Blue)
```

### Solution / Positive
```
Background: #FFFFFF
Primary Text: #1F2937
Highlights: #10B981 (Mint Green)
```

### Problem / Warning
```
Background: #FFFFFF
Primary Text: #1F2937
Highlights: #EF4444 (Coral Red)
```

### Comparison (Before vs. After)
```
Left (Old / Automation): #F8F9FA bg + #6B7280 text
Right (New / Agentic): #00D9FF accent + #1A2238 text
```

---

## CSS Variables (for HTML/SVG artifacts)

```css
:root {
  --brand-navy-dark: #0A1128;
  --brand-navy: #1A2238;
  --brand-cyan: #00D9FF;
  --brand-cyan-secondary: #00BFD8;
  --brand-blue: #2E5CFF;
  --text-primary: #1F2937;
  --text-secondary: #374151;
  --text-muted: #6B7280;
  --text-inverse: #FFFFFF;
  --bg-primary: #FFFFFF;
  --bg-secondary: #F8F9FA;
  --bg-dark: #0A1128;
  --accent-success: #10B981;
  --accent-error: #EF4444;
}
```

---

## Application Rules

### DO
✅ Use Dark Navy (`#0A1128`) for brand authority and professionalism
✅ Use Cyan (`#00D9FF`) as a strategic accent — not dominant
✅ High contrast (Navy + Cyan + White) for maximum visual impact
✅ Mint Green for solutions; Coral Red for problems
✅ Maintain clean, minimal aesthetic with generous white space
✅ Flat design — no gradients

### DON'T
❌ Don't let turquoise dominate — it's an accent, not a background
❌ Don't use low-contrast text combinations
❌ Don't mix Mint Green and Coral in the same section
❌ Don't use gradients
❌ Don't use colors outside this palette without explicit reason

---

## Platform-Specific Defaults

### LinkedIn Carousel Covers
- Background: Navy `#0A1128`
- Headline: White `#FFFFFF`
- Accent: Cyan `#00D9FF`
- Subtext: Off-White `#F8F9FA`

### Article / Blog Headers
- Background: White or Off-White
- Headline: Dark Gray `#1F2937`
- Accent: Royal Blue `#2E5CFF`

### Quote / Insight Slides
- Background: Cyan `#00D9FF` or Navy `#0A1128`
- Text: White `#FFFFFF`
- Attribution: White at 70% opacity

---

## Brand Personality

- **Navy Blue** → Expertise, trust, authority, executive gravitas
- **Cyan** → Innovation, modern tech, forward-thinking CMO
- **Royal Blue** → Professionalism, B2B reliability
- **Mint Green** → Growth, success, positive outcomes
- **Coral Red** → Honesty about challenges, direct communication

**Overall feel:** Professional, tech-forward, trustworthy, minimal, clean.
**Not:** decorative, trendy, playful, gradient-heavy, or AI-generic.

---

*Source: `FRACTIONAL_CMO/C-core/brand-colors.md`*
*For use in all Fractional CMO content, visuals, presentations, and artifacts.*
