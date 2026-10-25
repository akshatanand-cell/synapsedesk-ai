import math
from PIL import Image, ImageDraw, ImageFont

def create_thumbnail():
    width = 1200
    height = 800
    img = Image.new("RGBA", (width, height), (9, 13, 22, 255))
    draw = ImageDraw.Draw(img)

    # 1. Subtle Radial Background Glow
    center_x, center_y = width // 2, height // 2
    for r in range(450, 0, -5):
        alpha = int(28 * (1 - r / 450))
        draw.ellipse(
            [center_x - r, center_y - r - 40, center_x + r, center_y + r - 40],
            fill=(2, 132, 199, alpha)
        )
    for r in range(250, 0, -5):
        alpha = int(35 * (1 - r / 250))
        draw.ellipse(
            [center_x - r, center_y - r - 40, center_x + r, center_y + r - 40],
            fill=(168, 85, 247, alpha)
        )

    # 2. Concentric Orbiting Wireframe Rings
    for ring_r, col in [(180, (56, 189, 248, 120)), (240, (168, 85, 247, 90)), (320, (16, 185, 129, 60))]:
        draw.ellipse(
            [center_x - ring_r, center_y - ring_r // 2 - 40, center_x + ring_r, center_y + ring_r // 2 - 40],
            outline=col,
            width=2
        )

    # 3. Center Holographic Core (Glowing Icosahedron / Orb)
    core_r = 55
    draw.ellipse(
        [center_x - core_r, center_y - core_r - 40, center_x + core_r, center_y + core_r - 40],
        fill=(56, 189, 248, 220),
        outline=(248, 250, 252, 255),
        width=3
    )

    # 4. Floating 3D Task Prisms
    for angle_deg, dist, color_hex in [(-35, 260, (239, 68, 68)), (0, 240, (56, 189, 248)), (35, 260, (16, 185, 129))]:
        rad = math.radians(angle_deg)
        px = int(center_x + dist * math.sin(rad))
        py = int(center_y - 40 - dist * 0.35 * math.cos(rad) + 90)
        size = 22
        draw.polygon(
            [(px, py - size), (px + size, py), (px, py + size), (px - size, py)],
            fill=color_hex + (230,),
            outline=(255, 255, 255, 220)
        )

    # 5. Typography
    try:
        font_eyebrow = ImageFont.truetype("arialbd.ttf", 22)
        font_title = ImageFont.truetype("arialbd.ttf", 64)
        font_sub = ImageFont.truetype("arial.ttf", 26)
        font_badge = ImageFont.truetype("arialbd.ttf", 18)
    except:
        font_eyebrow = ImageFont.load_default()
        font_title = font_eyebrow
        font_sub = font_eyebrow
        font_badge = font_eyebrow

    # Eyebrow Badge
    draw.text((width // 2, 80), "META VR START DEVELOPER COMPETITION 2026", fill=(56, 189, 248, 255), font=font_eyebrow, anchor="mm")
    
    # Title
    draw.text((width // 2, 140), "SynapseDesk AI", fill=(248, 250, 252, 255), font=font_title, anchor="mm")
    
    # Subtitle
    draw.text((width // 2, 195), "Hands-First Autonomous Spatial Workspace Protocol", fill=(148, 163, 184, 255), font=font_sub, anchor="mm")

    # Bottom Badges Bar
    badges = [
        ("AIRPLANE SEAT 2FT ARC", (3, 105, 161)),
        ("100% HANDS-FIRST", (6, 95, 70)),
        ("AGENTIC AI CORE", (109, 40, 217)),
        ("60+ FPS WEBXR", (180, 83, 9))
    ]
    
    total_w = sum(len(b[0]) * 13 + 30 for b in badges)
    cur_x = (width - total_w) // 2
    badge_y = 670

    for text, bg_col in badges:
        bw = len(text) * 13 + 24
        draw.rounded_rectangle([cur_x, badge_y, cur_x + bw, badge_y + 40], radius=8, fill=bg_col + (220,))
        draw.text((cur_x + bw // 2, badge_y + 20), text, fill=(255, 255, 255, 255), font=font_badge, anchor="mm")
        cur_x += bw + 14

    # Deployment Footer
    draw.text((width // 2, 750), "Live on Vercel: synapsedesk-ai.vercel.app  |  Meta Quest 3 / 3S Ready", fill=(100, 116, 139, 255), font=font_sub, anchor="mm")

    out_path = r"C:\Users\KIIT\.gemini\antigravity\scratch\meta-vr-2026\synapsedesk-ai\thumbnail.png"
    img.convert("RGB").save(out_path, "PNG")
    print("Thumbnail created successfully at:", out_path)

if __name__ == "__main__":
    create_thumbnail()
