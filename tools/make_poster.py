#!/usr/bin/env python3
"""
Generate three poster variants (1080x1350 portrait PNG) for @crisxai5 using PIL only.
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Font paths
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def load_fonts():
    return {
        'huge': ImageFont.truetype(FONT_BOLD, 120),
        'large': ImageFont.truetype(FONT_BOLD, 72),
        'med_bold': ImageFont.truetype(FONT_BOLD, 42),
        'med': ImageFont.truetype(FONT_REG, 42),
        'small': ImageFont.truetype(FONT_REG, 30),
        'chip': ImageFont.truetype(FONT_BOLD, 28),
    }

def draw_text_centered(draw, text, font, fill, y, width):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    x = (width - w) // 2
    draw.text((x, y), text, font=font, fill=fill)
    return bbox[3] - bbox[1]

def make_poster_a(filename="poster_a.png"):
    # Variant A: MIDNIGHT GOLD  # tuned
    width, height = 1080, 1350
    img = Image.new("RGB", (width, height), color="#0b1026")
    draw = ImageDraw.Draw(img)
    fonts = load_fonts()

    # Thin gold frame border
    gold = "#d4af37"
    draw.rectangle([40, 40, width - 40, height - 40], outline=gold, width=3)

    # Top text
    draw_text_centered(draw, "MUST-FOLLOW ON X", fonts["small"], gold, 120, width)

    # @crisxai5 huge in white centred
    draw_text_centered(draw, "@crisxai5", fonts["huge"], "#ffffff", 320, width)

    # AI & CRYPTO EXPERT in gold below
    draw_text_centered(draw, "AI & CRYPTO EXPERT", fonts["med_bold"], gold, 520, width)

    # Three gold-outlined chips in a row
    chips = ["AI AGENTS", "CRYPTO", "WEB3"]
    chip_w, chip_h, chip_y = 260, 70, 680
    total_w = len(chips) * chip_w + (len(chips) - 1) * 30
    start_x = (width - total_w) // 2

    for i, text in enumerate(chips):
        cx = start_x + i * (chip_w + 30)
        draw.rounded_rectangle([cx, chip_y, cx + chip_w, chip_y + chip_h], radius=12, outline=gold, width=3)
        # Center text inside chip
        bbox = fonts["chip"].getbbox(text)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = cx + (chip_w - tw) // 2
        ty = chip_y + (chip_h - th) // 2 - 4
        draw.text((tx, ty), text, font=fonts["chip"], fill=gold)

    # Bottom line
    draw_text_centered(draw, "AI agents · Crypto insights · Web3 innovation", fonts["small"], "#cccccc", 1150, width)

    img.save(filename)
    print(f"{filename}: {os.path.getsize(filename)} bytes")

def make_poster_b(filename="poster_b.png"):
    # Variant B: NEON NETWORK
    width, height = 1080, 1350
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    # Vertical gradient purple #5b2a86 at top to cyan #0e7490 at bottom
    r1, g1, b1 = 91, 42, 134
    r2, g2, b2 = 14, 116, 144
    for y in range(height):
        r = int(r1 + (r2 - r1) * y / height)
        g = int(g1 + (g2 - g1) * y / height)
        b = int(b1 + (b2 - b1) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Network of small white dots joined by thin white lines across upper third
    dots = [
        (150, 120), (320, 80), (500, 150), (680, 90), (850, 130),
        (220, 250), (410, 220), (600, 270), (800, 230), (950, 180)
    ]
    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            if abs(dots[i][0] - dots[j][0]) < 300 and abs(dots[i][1] - dots[j][1]) < 150:
                draw.line([dots[i], dots[j]], fill=(255, 255, 255, 100), width=1)
    for d in dots:
        draw.ellipse([d[0]-3, d[1]-3, d[0]+3, d[1]+3], fill="#ffffff")

    fonts = load_fonts()
    cyan_pale = "#a5f3fc"

    # Big white @crisxai5
    draw_text_centered(draw, "@crisxai5", fonts["huge"], "#ffffff", 420, width)

    # AI & CRYPTO EXPERT in pale cyan
    draw_text_centered(draw, "AI & CRYPTO EXPERT", fonts["med_bold"], cyan_pale, 600, width)

    # Three chips as filled white rounded rectangles with dark text
    chips = ["AI AGENTS", "CRYPTO", "WEB3"]
    chip_w, chip_h, chip_y = 260, 70, 780
    total_w = len(chips) * chip_w + (len(chips) - 1) * 30
    start_x = (width - total_w) // 2

    for i, text in enumerate(chips):
        cx = start_x + i * (chip_w + 30)
        draw.rounded_rectangle([cx, chip_y, cx + chip_w, chip_y + chip_h], radius=16, fill="#ffffff")
        bbox = fonts["chip"].getbbox(text)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = cx + (chip_w - tw) // 2
        ty = chip_y + (chip_h - th) // 2 - 4
        draw.text((tx, ty), text, font=fonts["chip"], fill="#0b1026")

    # Bottom line
    draw_text_centered(draw, "Follow the signal, not the noise.", fonts["small"], "#ffffff", 1150, width)

    img.save(filename)
    print(f"{filename}: {os.path.getsize(filename)} bytes")

def make_poster_c(filename="poster_c.png"):
    # Variant C: CLEAN SIGNAL
    width, height = 1080, 1350
    img = Image.new("RGB", (width, height), color="#f5f2ea")
    draw = ImageDraw.Draw(img)
    fonts = load_fonts()
    navy = "#0b1026"

    # Small navy rule at top
    draw.rectangle([width//2 - 40, 100, width//2 + 40, 108], fill=navy)

    # AI & CRYPTO EXPERT small at top
    draw_text_centered(draw, "AI & CRYPTO EXPERT", fonts["small"], navy, 140, width)

    # @crisxai5 enormous in navy
    draw_text_centered(draw, "@crisxai5", fonts["huge"], navy, 320, width)

    # Short navy underline bar
    draw.rectangle([width//2 - 150, 480, width//2 + 150, 490], fill=navy)

    # Three topic rows: coloured dot + word
    topics = [
        ("#7c3aed", "AI AGENTS"),
        ("#d4af37", "CRYPTO INSIGHTS"),
        ("#0d9488", "WEB3 INNOVATION")
    ]
    start_y = 620
    row_h = 90
    dot_r = 12

    for i, (color, text) in enumerate(topics):
        ry = start_y + i * row_h
        # Draw dot
        draw.ellipse([320, ry + 15, 320 + dot_r*2, ry + 15 + dot_r*2], fill=color)
        # Draw text beside dot
        draw.text((380, ry), text, font=fonts["med_bold"], fill=navy)

    # Bottom line
    draw_text_centered(draw, "One follow. Every signal.", fonts["small"], "#666666", 1150, width)

    img.save(filename)
    print(f"{filename}: {os.path.getsize(filename)} bytes")

if __name__ == "__main__":
    make_poster_a()
    make_poster_b()
    make_poster_c()
