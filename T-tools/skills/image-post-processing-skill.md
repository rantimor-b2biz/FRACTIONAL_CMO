# Image Post-Processing Skill
# Fractional CMO Edition

**Used by:** Artist Agent
**Tools:** Python + Pillow (PIL)
**Purpose:** Add text overlays, branding, and resize FLUX-generated images for publication

---

## When to Use This Skill

After FLUX generates a raw image, use this skill to:
- Add title / headline text on the image
- Add Ran Timor branding (name + URL)
- Resize to correct platform dimensions
- Apply subtle color overlay for text legibility
- Save to the correct output folder

---

## Setup

```python
# Install if needed:
# python3 -m pip install Pillow

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Standard paths
CREDENTIALS_PATH = r'C:\Users\rant\Documents\ran-workspace\T-tools\api-credentials.env'
OUTPUT_BASE = r'C:\Users\rant\Documents\ran-workspace\FRACTIONAL_CMO\O-output'
```

---

## Platform Dimensions

```python
DIMENSIONS = {
    "linkedin_square":   (1080, 1080),   # Square post
    "linkedin_portrait": (1080, 1350),   # Portrait post (best for feed)
    "article_hero":      (1200, 630),    # Blog / rantimor.com header
    "linkedin_story":    (1080, 1920),   # Story format
    "email_header":      (800,  200),    # Newsletter header
}
```

---

## Core Functions

### 1. Load and Resize Image

```python
def load_and_resize(image_path: str, size: tuple) -> Image.Image:
    """Load a FLUX-generated PNG and resize to target dimensions."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize(size, Image.LANCZOS)
    return img
```

### 2. Add Dark Overlay (for text legibility)

```python
def add_overlay(img: Image.Image, opacity: int = 60) -> Image.Image:
    """
    Add a semi-transparent dark overlay over the bottom portion.
    opacity: 0 (invisible) to 255 (solid black)
    """
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Gradient overlay on bottom 40% of image
    height = img.size[1]
    bottom_start = int(height * 0.6)
    draw.rectangle(
        [(0, bottom_start), (img.size[0], height)],
        fill=(0, 0, 0, opacity)
    )
    img = img.convert("RGBA")
    img = Image.alpha_composite(img, overlay)
    return img.convert("RGB")
```

### 3. Add Title Text

```python
def add_title(img: Image.Image, title: str, position: str = "bottom-left") -> Image.Image:
    """
    Add a title text to the image.
    position: "bottom-left", "bottom-center", "top-left", "center"
    Font: Uses system default (Arial/Helvetica). For production, specify font path.
    """
    draw = ImageDraw.Draw(img)
    W, H = img.size

    # Try to load a clean font, fall back to default
    try:
        font_large = ImageFont.truetype("arial.ttf", size=int(H * 0.07))
    except:
        font_large = ImageFont.load_default()

    # Position mapping
    padding = int(W * 0.05)
    positions = {
        "bottom-left":   (padding, H - int(H * 0.18)),
        "bottom-center": (W // 2, H - int(H * 0.18)),
        "top-left":      (padding, padding),
        "center":        (W // 2, H // 2),
    }
    x, y = positions.get(position, positions["bottom-left"])

    # Draw text with shadow for legibility
    shadow_offset = 3
    draw.text((x + shadow_offset, y + shadow_offset), title,
              font=font_large, fill=(0, 0, 0, 180))
    draw.text((x, y), title, font=font_large, fill=(255, 255, 255, 255))

    return img
```

### 4. Add Branding (Fractional CMO)

```python
def add_branding_fractional_cmo(img: Image.Image) -> Image.Image:
    """
    Add Ran Timor / rantimor.com branding to bottom-right corner.
    Fractional CMO brand: white text, subtle, executive.
    """
    draw = ImageDraw.Draw(img)
    W, H = img.size

    try:
        font_brand = ImageFont.truetype("arial.ttf", size=int(H * 0.025))
    except:
        font_brand = ImageFont.load_default()

    brand_text = "RAN TIMOR  |  rantimor.com"
    padding = int(W * 0.04)

    # Bottom-right
    bbox = draw.textbbox((0, 0), brand_text, font=font_brand)
    text_w = bbox[2] - bbox[0]
    x = W - text_w - padding
    y = H - padding - (bbox[3] - bbox[1])

    # Shadow + text
    draw.text((x + 2, y + 2), brand_text, font=font_brand, fill=(0, 0, 0, 120))
    draw.text((x, y), brand_text, font=font_brand, fill=(255, 255, 255, 180))

    return img
```

### 5. Save Output

```python
def save_image(img: Image.Image, output_path: str) -> str:
    """Save final image. Creates directory if needed."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"Saved: {output_path}")
    return output_path
```

---

## Full Pipeline: Raw FLUX → Publication Ready

```python
def process_for_linkedin_post(
    raw_image_path: str,
    title: str,
    output_path: str,
    format: str = "linkedin_portrait"
) -> str:
    """
    Full pipeline: raw FLUX image → LinkedIn-ready image with text and branding.

    Args:
        raw_image_path: Path to FLUX-generated PNG
        title: Headline text to overlay (keep under 8 words)
        output_path: Where to save the final image
        format: Key from DIMENSIONS dict

    Returns:
        output_path of saved image
    """
    # 1. Load and resize
    size = DIMENSIONS[format]
    img = load_and_resize(raw_image_path, size)

    # 2. Add overlay for text legibility
    img = add_overlay(img, opacity=80)

    # 3. Add title
    img = add_title(img, title, position="bottom-left")

    # 4. Add branding
    img = add_branding_fractional_cmo(img)

    # 5. Save
    return save_image(img, output_path)


# ── Usage Example ──
if __name__ == "__main__":
    process_for_linkedin_post(
        raw_image_path=r"C:\Users\rant\Documents\ran-workspace\FRACTIONAL_CMO\O-output\W10\06-article-vibe-marketing\visual\vibe-marketing-flux-v3.png",
        title="VIBE MARKETING",
        output_path=r"C:\Users\rant\Documents\ran-workspace\FRACTIONAL_CMO\O-output\W10\06-article-vibe-marketing\visual\vibe-marketing-linkedin-final.png",
        format="linkedin_portrait"
    )
```

---

## Quick Reference: Common Tasks

### Resize only (no text)
```python
img = load_and_resize(raw_path, DIMENSIONS["article_hero"])
save_image(img, output_path)
```

### Add overlay + branding only (no title)
```python
img = load_and_resize(raw_path, DIMENSIONS["linkedin_square"])
img = add_overlay(img, opacity=40)
img = add_branding_fractional_cmo(img)
save_image(img, output_path)
```

### Article hero (16:9, no text overlay needed)
```python
img = load_and_resize(raw_path, DIMENSIONS["article_hero"])
img = add_branding_fractional_cmo(img)
save_image(img, output_path)
```

---

## Output Naming Convention

```
[client]/O-output/[WEEK]/[FOLDER]/visual/
├── [name]-flux-raw.png          ← FLUX output, untouched
├── [name]-linkedin-final.png    ← Post-processed, ready to post
└── [name]-article-hero.png      ← Resized for rantimor.com
```

---

## Font Notes

For production quality, use Inter or similar clean sans-serif:
- Download Inter: https://fonts.google.com/specimen/Inter
- Save to: `T-tools/fonts/Inter-Bold.ttf`, `Inter-Regular.ttf`
- Update font paths in functions above

```python
font_large = ImageFont.truetype(
    r"C:\Users\rant\Documents\ran-workspace\T-tools\fonts\Inter-Bold.ttf",
    size=int(H * 0.07)
)
```

---

*Image Post-Processing Skill — Fractional CMO Edition*
*Last updated: 2026-03-16*
