# FLUX Prompt Engineering Skill
# Fractional CMO Edition

**Used by:** Artist Agent
**Model:** `black-forest-labs/flux-1.1-pro` via Replicate
**Purpose:** Generate reliable, high-quality realistic images on the first or second attempt

---

## The Core Formula

Every FLUX prompt follows this structure, in order:

```
[Shot type] + [Subject + key detail] + [Angle/composition] + [Lighting] + [Atmosphere] + [Style modifiers] + [What's NOT in it]
```

**Example (from Vibe Marketing session):**
```
Cinematic photorealistic wide shot.
A modern glass office building facade, warm golden light glowing from every window.
Shot from a sharp 3/4 side angle revealing the building is only a few inches thick.
Two dramatic stage spotlights from above.
Ground level fog. Dark theatrical studio space.
Editorial photography, architectural, ultra-realistic, sharp focus.
No people.
```

---

## Formula Components

### 1. Shot Type (always first)
Sets the camera and scale immediately.

| Option | When to Use |
|--------|------------|
| `Cinematic photorealistic wide shot` | Scenes, environments, full subjects |
| `Cinematic photorealistic close-up` | Detail, texture, single object |
| `Editorial photography` | Magazine-style, clean and composed |
| `Aerial cinematic photograph` | Top-down, overview, scale |
| `Medium format film photograph` | Most realistic, Hasselblad feel |
| `Documentary photograph` | Raw, authentic, unposed |

### 2. Subject + Key Detail
One sentence. What is in the frame and what makes it specific.

- ✅ "A modern glass office building, warm golden light glowing from every floor-to-ceiling window"
- ✅ "A weathered compass on a dark mahogany desk, needle pointing to an unmarked direction"
- ❌ "A building" (too vague)
- ❌ "A beautiful amazing stunning office" (adjective inflation = generic result)

### 3. Angle / Composition
Tell FLUX exactly where the camera is.

| Phrase | Effect |
|--------|--------|
| `shot from a sharp 3/4 angle` | Reveals depth and sides |
| `shot from directly below, looking up` | Dramatic, imposing |
| `bird's eye view, overhead` | Symbolic, overview |
| `eye-level, straight on` | Authoritative, direct |
| `low angle, ground level` | Powerful, monumental |
| `slightly elevated, looking down` | Confident, controlled |

### 4. Lighting
Lighting determines mood. Be specific.

| Phrase | Mood |
|--------|------|
| `two dramatic stage spotlights from above` | Theatrical, intentional |
| `warm golden hour light from the left` | Optimistic, executive |
| `cold blue corporate overhead lighting` | Clinical, enterprise |
| `single harsh spotlight, everything else dark` | Isolation, focus |
| `diffused overcast natural light` | Neutral, clean |
| `rim light only, dark background` | Premium, mysterious |

### 5. Atmosphere
The environment around the subject.

| Phrase | Effect |
|--------|--------|
| `dark theatrical studio space` | Stage, intentional, controlled |
| `ground level fog / haze` | Depth, cinematic |
| `stormy dramatic sky` | Tension, urgency |
| `clean white minimalist background` | Corporate, focused |
| `deep space, star field` | Scale, ambition |
| `shallow depth of field, bokeh background` | Premium, focused |

### 6. Style Modifiers (always include 3-5)
These lock the aesthetic. Pick from this list:

**Quality:**
- `ultra-realistic` `photorealistic` `medium format quality`
- `sharp focus` `crisp detail` `8K resolution`

**Style:**
- `editorial photography` `architectural photography` `cinematic`
- `Hasselblad medium format` `documentary style`

**Mood:**
- `dark and dramatic` `warm and authoritative` `cold and corporate`
- `minimalist` `high contrast`

**Exclusions (always add at least one):**
- `no people` `no text` `no watermarks` `no logos`

---

## Client-Specific Style Profile: Fractional CMO

**Brand mood:** Dark, executive, cinematic. High contrast. Authoritative.

**Default style modifiers to always include:**
```
editorial photography, architectural, cinematic, ultra-realistic,
dark and dramatic, high contrast, no people, no text
```

**Color palette that works:**
- Dark navy / near-black backgrounds
- Warm amber / gold for highlights (authority)
- Cold steel blue for secondary elements (precision)
- Avoid: bright colors, pastels, neon

**What resonates with Fractional CMO ICP:**
- Architectural metaphors (structure, foundation, building)
- Navigation metaphors (compass, crossroads, direction)
- Light/dark contrast (clarity vs confusion)
- Theatrical scenes (performance, reality behind the scenes)

---

## Iteration Protocol

When V1 is wrong, diagnose before changing the prompt:

| Problem | Diagnosis | Fix |
|---------|-----------|-----|
| Wrong angle / can't see the key element | Angle phrase too vague | Be more explicit: "camera positioned to the LEFT of the subject, 45 degrees" |
| Too dark, can't see detail | Atmosphere overpowered lighting | Add: "subject clearly illuminated" or reduce fog description |
| Looks like illustration, not photo | Style modifiers too weak | Strengthen: "medium format film photograph, Hasselblad quality" |
| Subject is generic / not specific | Description too short | Add 2-3 more specific visual details to the subject |
| People appeared | Missing exclusion | Add: "no people, empty scene" explicitly |
| Wrong building type | Not specified | Name the architecture: "glass and steel modernist office facade" |
| Lost the metaphor reveal | Camera not seeing both sides | Add explicit camera position: "camera sees both front facade AND the thin profile edge" |

**Rule of thumb:** Change ONE thing per iteration. If you change everything, you don't know what fixed it.

---

## Prompt Templates by Visual Type

### Template A: Architectural / Building Metaphor
```
[Shot type]. [Building description with specific architecture and lighting].
Shot from [specific angle] so the viewer can clearly see [the key reveal].
[Lighting description]. [Atmosphere].
[Style modifiers]. No people.
```

### Template B: Object / Still Life Metaphor
```
[Shot type]. [Object with specific material, condition, and placement].
[Lighting description]. [Background / environment].
[Composition note]. [Atmosphere].
[Style modifiers]. No people, no text.
```

### Template C: Environment / Scene
```
[Shot type]. [Environment with specific time, weather, and mood].
[Key focal element and its position in frame]. [What's happening in the background].
[Lighting]. [Atmosphere].
[Style modifiers]. No people.
```

### Template D: Abstract / Conceptual
```
[Shot type]. [Abstract visual metaphor described literally and physically].
[How the metaphor is physically manifested in the scene].
[Lighting]. [Color palette].
[Style modifiers]. Conceptual, symbolic. No text, no people.
```

---

## API Call Template

```python
import replicate
import os
import urllib.request

# Load credentials
from dotenv import load_dotenv
load_dotenv(r'C:\Users\rant\Documents\ran-workspace\T-tools\api-credentials.env')

output = replicate.run(
    "black-forest-labs/flux-1.1-pro",
    input={
        "prompt": """[YOUR PROMPT HERE]""",
        "aspect_ratio": "16:9",      # or "1:1" for LinkedIn square, "4:5" for LinkedIn portrait
        "output_format": "png",
        "output_quality": 95,
        "safety_tolerance": 2,
        "prompt_upsampling": True     # Improves detail and coherence
    }
)

url = str(output)
out_path = r"C:\Users\rant\Documents\ran-workspace\[CLIENT]\O-output\[WEEK]\[FOLDER]\visual\[name].png"
urllib.request.urlretrieve(url, out_path)
print("Saved:", out_path)
```

**Aspect ratio guide:**
| Use Case | Ratio |
|----------|-------|
| Article hero image | `16:9` |
| LinkedIn square post | `1:1` |
| LinkedIn portrait post | `4:5` |
| LinkedIn story | `9:16` |

---

## Lessons Learned (from Sessions)

| Session | Prompt Issue | What Fixed It |
|---------|-------------|---------------|
| Vibe Marketing V1 | "movie set backdrop" → FLUX focused only on scaffolding | Added "In the foreground: a beautiful facade..." |
| Vibe Marketing V2 | Beautiful building but no reveal | Added "3/4 side angle" + "thin flat panel" |
| Vibe Marketing V3 | ✅ Both facade AND empty side visible | "sharp 3/4 side angle" + "a few inches thick" |

*Update this table after every visual session.*

---

*Flux Prompt Engineering Skill — Fractional CMO Edition*
*Last updated: 2026-03-16*
