import os
from PIL import Image, ImageDraw, ImageFont

def generate_gallery_images():
    w, h = 1200, 800
    out_dir = r"C:\Users\KIIT\.gemini\antigravity\scratch\meta-vr-2026\synapsedesk-ai"

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 36)
        font_sub = ImageFont.truetype("arial.ttf", 22)
        font_text = ImageFont.truetype("arial.ttf", 18)
        font_bold = ImageFont.truetype("arialbd.ttf", 20)
    except:
        font_title = ImageFont.load_default()
        font_sub = font_title
        font_text = font_title
        font_bold = font_title

    # ----------------------------------------------------
    # IMAGE 1: Airplane Seat 2ft Ergonomic Architecture
    # ----------------------------------------------------
    img1 = Image.new("RGBA", (w, h), (15, 23, 42, 255))
    d1 = ImageDraw.Draw(img1)
    
    # Title
    d1.text((w//2, 60), "ERGONOMIC SPATIAL ENVELOPE (THE AIRPLANE SEAT TEST)", fill=(56, 189, 248), font=font_title, anchor="mm")
    d1.text((w//2, 105), "Strictly Contained Within 2-Foot Seated Radius Arc (r = 0.55m)", fill=(148, 163, 184), font=font_sub, anchor="mm")

    # Diagram background box
    d1.rounded_rectangle([100, 160, 1100, 720], radius=16, fill=(30, 41, 59, 255), outline=(51, 65, 85))

    # User center seated position
    d1.ellipse([w//2 - 40, 600, w//2 + 40, 680], fill=(2, 132, 199), outline=(255, 255, 255), width=2)
    d1.text((w//2, 640), "User (Seated)", fill=(255, 255, 255), font=font_bold, anchor="mm")

    # 2ft Radius boundary arc
    d1.arc([w//2 - 380, 240, w//2 + 380, 1000], start=200, end=340, fill=(16, 185, 129), width=3)
    d1.text((w//2, 260), "Maximum 2-Foot Reach Boundary (Airplane Seat Envelope)", fill=(16, 185, 129), font=font_bold, anchor="mm")

    # Three Panels along arc
    panels = [
        ("Left Panel: Intent Buffer", (240, 340, 480, 480), (168, 85, 247)),
        ("Center Hub: Active Nodes", (w//2 - 130, 310, w//2 + 130, 470), (2, 132, 199)),
        ("Right Panel: Telemetry", (w - 480, 340, w - 240, 480), (16, 185, 129))
    ]
    for ptitle, bbox, pcol in panels:
        d1.rounded_rectangle(bbox, radius=12, fill=(15, 23, 42), outline=pcol, width=2)
        d1.text(((bbox[0] + bbox[2])//2, (bbox[1] + bbox[3])//2 - 20), ptitle, fill=(248, 250, 252), font=font_bold, anchor="mm")
        d1.text(((bbox[0] + bbox[2])//2, (bbox[1] + bbox[3])//2 + 15), "PokeInteractable Touch", fill=(148, 163, 184), font=font_text, anchor="mm")

    # Synapse Core Agent Orb in center
    d1.ellipse([w//2 - 30, 215, w//2 + 30, 275], fill=(56, 189, 248), outline=(255, 255, 255), width=2)
    d1.text((w//2, 245), "Core", fill=(15, 23, 42), font=font_bold, anchor="mm")

    img1.convert("RGB").save(os.path.join(out_dir, "gallery_ergonomics.png"), "PNG")
    print("Saved gallery_ergonomics.png")

    # ----------------------------------------------------
    # IMAGE 2: Autonomous Agentic Intelligence Pipeline
    # ----------------------------------------------------
    img2 = Image.new("RGBA", (w, h), (15, 23, 42, 255))
    d2 = ImageDraw.Draw(img2)
    
    d2.text((w//2, 60), "AUTONOMOUS SPATIAL AGENTIC COGNITION PIPELINE", fill=(168, 85, 247), font=font_title, anchor="mm")
    d2.text((w//2, 105), "From Natural Language Ambition to 3D Force-Directed Layout", fill=(148, 163, 184), font=font_sub, anchor="mm")

    steps = [
        ("1. Cognitive Capture", "Natural Language Voice/Presets\n(e.g., 'Horizon Store Launch')", (168, 85, 247)),
        ("2. Semantic Decomposition", "Sub-tasks decomposed into\nP1/P2/P3 priority tokens", (2, 132, 199)),
        ("3. 3D Spatial Relaxation", "Force-directed physics map nodes\nto 40-degree seated FOV arc", (16, 185, 129)),
        ("4. Flow State Telemetry", "Real-time cognitive load heuristic\nBalanced Flow State (34%)", (245, 158, 11))
    ]

    for i, (stitle, sdesc, scol) in enumerate(steps):
        bx = 100 + i * 255
        by = 220
        bw = 230
        bh = 380
        d2.rounded_rectangle([bx, by, bx + bw, by + bh], radius=12, fill=(30, 41, 59), outline=scol, width=2)
        d2.rounded_rectangle([bx + 15, by + 15, bx + bw - 15, by + 65], radius=8, fill=scol)
        d2.text((bx + bw//2, by + 40), f"STAGE 0{i+1}", fill=(255, 255, 255), font=font_bold, anchor="mm")
        d2.text((bx + bw//2, by + 100), stitle, fill=(248, 250, 252), font=font_bold, anchor="mm")
        
        lines = sdesc.split('\n')
        for li, line in enumerate(lines):
            d2.text((bx + bw//2, by + 160 + li * 28), line, fill=(148, 163, 184), font=font_text, anchor="mm")

    img2.convert("RGB").save(os.path.join(out_dir, "gallery_architecture.png"), "PNG")
    print("Saved gallery_architecture.png")

if __name__ == '__main__':
    generate_gallery_images()
