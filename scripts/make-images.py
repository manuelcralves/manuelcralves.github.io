"""Draws the icons and the link preview image in public/.

Run it again if the design changes, or at M4 to put the real domain on the
preview image. Needs Pillow and the Georgia and Segoe UI fonts that ship with
Windows; on another system, point the paths below at any serif and sans font.

    python scripts/make-images.py
"""

import pathlib

from PIL import Image, ImageDraw, ImageFont

PUBLIC = pathlib.Path(__file__).resolve().parent.parent / "public"
PORTRAIT = PUBLIC.parent / "src" / "assets" / "manuel-alves.jpg"

# Same tokens as src/styles/global.css.
BG = (246, 242, 234)
INK = (31, 27, 22)
INK_SOFT = (58, 51, 43)
MUTED = (92, 84, 74)
LINE = (228, 218, 203)
ACCENT = (31, 94, 78)

SERIF_BOLD = r"C:\Windows\Fonts\georgiab.ttf"
SERIF = r"C:\Windows\Fonts\georgia.ttf"
SANS_SEMIBOLD = r"C:\Windows\Fonts\seguisb.ttf"
SANS = r"C:\Windows\Fonts\segoeui.ttf"


def icon(size, rounded=True):
    """The M monogram: drawn four times larger, then shrunk for smooth edges."""
    s = size * 4
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    if rounded:
        draw.rounded_rectangle((0, 0, s - 1, s - 1), radius=round(14 / 64 * s), fill=ACCENT)
    else:
        draw.rectangle((0, 0, s - 1, s - 1), fill=ACCENT)
    points = [(x / 64 * s, y / 64 * s) for x, y in [(18, 46), (18, 20), (32, 37), (46, 20), (46, 46)]]
    width = round(6 / 64 * s)
    draw.line(points, fill=BG, width=width, joint="curve")
    for x, y in (points[0], points[-1]):  # round the two open ends
        draw.ellipse((x - width / 2, y - width / 2, x + width / 2, y + width / 2), fill=BG)
    return img.resize((size, size), Image.LANCZOS)


def preview():
    """The 1200x630 image that social networks and chat apps show."""
    img = Image.new("RGB", (1200, 630), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 620, 1200, 630), fill=ACCENT)

    name = ImageFont.truetype(SERIF_BOLD, 96)
    lead = ImageFont.truetype(SERIF, 40)
    kicker = ImageFont.truetype(SANS_SEMIBOLD, 24)
    small = ImageFont.truetype(SANS, 27)

    x = 80
    letter = x
    for char in "PORTO, PORTUGAL":  # drawn letter by letter, for the wide spacing
        draw.text((letter, 150), char, font=kicker, fill=ACCENT)
        letter += draw.textlength(char, font=kicker) + 5
    draw.text((x, 196), "Manuel Alves", font=name, fill=INK)
    draw.line((x, 330, 700, 330), fill=LINE, width=2)
    draw.text((x, 360), "Software engineer working on applied AI", font=lead, fill=INK_SOFT)
    draw.text((x, 424), "MSc from FEUP, University of Porto · Thesis developed at CERN", font=small, fill=MUTED)
    draw.text((x, 470), "github.com/manuelcralves", font=small, fill=MUTED)

    photo = Image.open(PORTRAIT).resize((300, 300), Image.LANCZOS)
    mask = Image.new("L", (300, 300), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 299, 299), fill=255)
    img.paste(photo, (830, 165), mask)
    return img


if __name__ == "__main__":
    icon(180, rounded=False).convert("RGB").save(PUBLIC / "apple-touch-icon.png")
    icon(64).save(PUBLIC / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    preview().save(PUBLIC / "og.jpg", quality=88, optimize=True)
    print("written to", PUBLIC)
