import os
import subprocess
import time
from playwright.sync_api import sync_playwright

BASE_DIR = r"C:\Users\KIIT\.gemini\antigravity\scratch\meta-vr-2026\synapsedesk-ai"
VERCEL_URL = "https://synapsedesk-ai.vercel.app/?view=cockpit"
RAW_VIDEO_DIR = os.path.join(BASE_DIR, "recorded_master_raw")
VOICEOVER_PATH = os.path.join(BASE_DIR, "full_voiceover_extended.mp3")
SUBTITLES_PATH = os.path.join(BASE_DIR, "subtitles_extended.srt")
OUTPUT_VIDEO_PATH = os.path.join(BASE_DIR, "SynapseDesk_AI_Demo_Video.mp4")
PUBLIC_VIDEO_PATH = os.path.join(BASE_DIR, "public", "SynapseDesk_AI_Demo_Video.mp4")

os.makedirs(RAW_VIDEO_DIR, exist_ok=True)

def inject_hud(page):
    hud_code = """
    (() => {
        if (document.getElementById('master-cinematic-hud')) return;
        const hud = document.createElement('div');
        hud.id = 'master-cinematic-hud';
        hud.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: 999999;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #ffffff;
            overflow: hidden;
        `;
        
        // Top Header Bar
        const topBar = document.createElement('div');
        topBar.style.cssText = `
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 24px 36px;
            background: linear-gradient(180deg, rgba(7,9,14,0.85) 0%, rgba(7,9,14,0) 100%);
        `;
        topBar.innerHTML = `
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="width: 12px; height: 12px; border-radius: 50%; background: #38bdf8; box-shadow: 0 0 16px #38bdf8; animation: pulse 2s infinite;"></div>
                <div style="font-weight: 800; font-size: 18px; letter-spacing: 0.05em; text-transform: uppercase;">
                    SynapseDesk AI <span style="color: #94a3b8; font-weight: 400; font-size: 14px; margin-left: 8px;">// Spatial Protocol v1.1</span>
                </div>
            </div>
            <div style="display: flex; gap: 16px;">
                <div style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); padding: 6px 14px; border-radius: 9999px; font-size: 12px; font-weight: 700; color: #38bdf8; letter-spacing: 0.05em;">
                    SEATED ENVELOPE: r = 0.55m
                </div>
                <div style="background: rgba(168, 85, 247, 0.15); border: 1px solid rgba(168, 85, 247, 0.4); padding: 6px 14px; border-radius: 9999px; font-size: 12px; font-weight: 700; color: #c084fc; letter-spacing: 0.05em;">
                    META QUEST 3 WEBXR
                </div>
            </div>
        `;
        hud.appendChild(topBar);

        // Lower Left Act Title Card
        const actCard = document.createElement('div');
        actCard.id = 'hud-act-card';
        actCard.style.cssText = `
            position: absolute;
            bottom: 40px;
            left: 36px;
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(56, 189, 248, 0.35);
            border-left: 5px solid #38bdf8;
            padding: 14px 22px;
            border-radius: 10px;
            box-shadow: 0 12px 30px rgba(0,0,0,0.6);
            backdrop-filter: blur(12px);
            transition: all 0.4s ease;
        `;
        actCard.innerHTML = `
            <div id="hud-act-num" style="font-size: 11px; font-weight: 800; color: #38bdf8; letter-spacing: 0.15em; text-transform: uppercase;">ACT 01 // OVERVIEW</div>
            <div id="hud-act-title" style="font-size: 17px; font-weight: 700; color: #f8fafc; margin-top: 3px;">The Airplane Seat Test: Seated Cylindrical Arc</div>
        `;
        hud.appendChild(actCard);

        // Lower Right Spec Badge
        const specBadge = document.createElement('div');
        specBadge.style.cssText = `
            position: absolute;
            bottom: 40px;
            right: 36px;
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 10px 18px;
            border-radius: 10px;
            font-size: 12px;
            color: #94a3b8;
            font-family: monospace;
            text-align: right;
            backdrop-filter: blur(8px);
        `;
        specBadge.innerHTML = `
            <div>FOV CORRIDOR: 40° FOVEAL</div>
            <div style="color: #38bdf8; font-weight: bold; margin-top: 2px;">HANDS-FIRST: 100% CONTROLLER-FREE</div>
        `;
        hud.appendChild(specBadge);

        // Virtual Hand Reticle (Tracks Pointer)
        const reticle = document.createElement('div');
        reticle.id = 'hud-hand-reticle';
        reticle.style.cssText = `
            position: absolute;
            width: 28px;
            height: 28px;
            border: 2px solid #38bdf8;
            border-radius: 50%;
            pointer-events: none;
            transform: translate(-50%, -50%);
            box-shadow: 0 0 16px rgba(56, 189, 248, 0.8);
            transition: width 0.15s ease, height 0.15s ease, background 0.15s ease;
            display: none;
        `;
        const dot = document.createElement('div');
        dot.style.cssText = `
            width: 6px;
            height: 6px;
            background: #ffffff;
            border-radius: 50%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        `;
        reticle.appendChild(dot);
        hud.appendChild(reticle);

        document.body.appendChild(hud);

        window.updateHUDAct = (num, title) => {
            const card = document.getElementById('hud-act-card');
            const numEl = document.getElementById('hud-act-num');
            const titleEl = document.getElementById('hud-act-title');
            if (numEl) numEl.textContent = num;
            if (titleEl) titleEl.textContent = title;
            if (card) {
                card.style.transform = 'translateY(-6px)';
                setTimeout(() => { card.style.transform = 'translateY(0)'; }, 200);
            }
        };

        window.updateReticle = (x, y, active = false) => {
            const r = document.getElementById('hud-hand-reticle');
            if (!r) return;
            r.style.display = 'block';
            r.style.left = x + 'px';
            r.style.top = y + 'px';
            if (active) {
                r.style.width = '36px';
                r.style.height = '36px';
                r.style.background = 'rgba(56, 189, 248, 0.3)';
            } else {
                r.style.width = '24px';
                r.style.height = '24px';
                r.style.background = 'transparent';
            }
        };
    })();
    """
    page.evaluate(hud_code)

def move_hand(page, x, y, duration=1.0, click=False):
    page.mouse.move(x, y)
    page.evaluate(f"window.updateReticle({x}, {y}, {str(click).lower()})")
    if click:
        time.sleep(0.15)
        page.mouse.down()
        page.evaluate(f"window.updateReticle({x}, {y}, true)")
        time.sleep(0.2)
        page.mouse.up()
        page.evaluate(f"window.updateReticle({x}, {y}, false)")
    time.sleep(duration)

def record():
    print(f"[RECORDER] Launching Chromium 1920x1080 60fps for Master Demo Video...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--enable-webgl",
                "--use-gl=angle",
                "--ignore-gpu-blocklist",
                "--window-size=1920,1080"
            ]
        )
        context = browser.new_context(
            record_video_dir=RAW_VIDEO_DIR,
            record_video_size={"width": 1920, "height": 1080},
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()

        print(f"[RECORDER] Navigating to {VERCEL_URL}...")
        page.goto(VERCEL_URL, wait_until="networkidle", timeout=60000)
        time.sleep(4.0)
        
        inject_hud(page)
        time.sleep(1.0)

        # -------------------------------------------------------------
        # ACT 1: Seated Airplane Seat Ergonomics (Duration: ~33.0s)
        # -------------------------------------------------------------
        print(">>> Recording Act 1: Seated Ergonomics & 2-Foot Arc (33s)...")
        act1_start = time.time()
        page.evaluate("window.updateHUDAct('ACT 01 // ERGONOMICS', 'The Airplane Seat Test: 2-Foot Curved Cockpit (r=0.55m)')")
        
        # Smooth camera gaze traverse across the 3 cockpit panels
        move_hand(page, 960, 540, 2.5)   # Center Hub
        move_hand(page, 620, 520, 3.0)   # Left Intent Panel
        move_hand(page, 1300, 520, 3.0)  # Right Agent Panel
        move_hand(page, 960, 480, 2.5)   # Back to Center
        move_hand(page, 960, 380, 3.0)   # Central Focus Timer
        move_hand(page, 750, 600, 2.5)
        move_hand(page, 1170, 600, 2.5)
        move_hand(page, 960, 540, 2.0)
        
        elapsed = time.time() - act1_start
        if elapsed < 33.0:
            time.sleep(33.0 - elapsed)

        # -------------------------------------------------------------
        # ACT 2: Hands-First Zero-Controller Physics (Duration: ~37.0s)
        # -------------------------------------------------------------
        print(">>> Recording Act 2: Hands-First Interaction (37s)...")
        act2_start = time.time()
        page.evaluate("window.updateHUDAct('ACT 02 // HANDS-FIRST PHYSICS', 'Zero-Controller PokeInteractable Finger Physics')")

        # Focus left Cognitive Capture panel
        move_hand(page, 620, 420, 2.5)
        
        # Poke preset: Horizon Store Launch Plan
        print("Poking Horizon Store Launch Plan...")
        move_hand(page, 620, 480, 1.5, click=True)
        time.sleep(2.5)

        # Poke preset: Quantum Systems Protocol
        print("Poking Quantum Systems Protocol...")
        move_hand(page, 620, 520, 1.5, click=True)
        time.sleep(2.5)

        # Poke preset: 60 FPS VR Latency Optimization
        print("Poking 60 FPS Latency Optimization...")
        move_hand(page, 620, 560, 1.5, click=True)
        time.sleep(3.0)

        # Poke Synthesize Autonomous Workflow
        print("Poking Synthesize Autonomous Workflow button...")
        move_hand(page, 890, 615, 2.0, click=True)
        time.sleep(4.0)

        move_hand(page, 620, 450, 3.0)
        elapsed = time.time() - act2_start
        if elapsed < 37.0:
            time.sleep(37.0 - elapsed)

        # -------------------------------------------------------------
        # ACT 3: Synapse Core Agent & Auto-Clustering (Duration: ~35.0s)
        # -------------------------------------------------------------
        print(">>> Recording Act 3: Synapse Core Agent & Auto-Clustering (35s)...")
        act3_start = time.time()
        page.evaluate("window.updateHUDAct('ACT 03 // AGENTIC INTERACTION ($25k)', 'Synapse Core Hologram & Spring-Repulsion Auto-Clustering')")

        # Inspect and poke floating holographic Synapse Core
        move_hand(page, 960, 410, 3.0)
        print("Touching floating Synapse Core crystalline orb...")
        move_hand(page, 960, 410, 1.5, click=True)
        time.sleep(3.0)

        # Interact with Grabbable Task Prisms
        print("Grabbing and manipulating 3D spatial task tokens...")
        move_hand(page, 860, 520, 1.5) # Red prism
        page.mouse.down()
        page.evaluate("window.updateReticle(860, 520, true)")
        move_hand(page, 890, 480, 2.0)
        page.mouse.up()
        page.evaluate("window.updateReticle(890, 480, false)")
        time.sleep(1.5)

        move_hand(page, 1060, 520, 1.5) # Green prism
        page.mouse.down()
        page.evaluate("window.updateReticle(1060, 520, true)")
        move_hand(page, 1030, 480, 2.0)
        page.mouse.up()
        page.evaluate("window.updateReticle(1030, 480, false)")
        time.sleep(2.0)

        # Poke Auto-Cluster (2ft) relaxation button
        print("Poking Auto-Cluster (2ft) spring relaxation button...")
        move_hand(page, 890, 615, 2.0, click=True)
        time.sleep(4.0)

        elapsed = time.time() - act3_start
        if elapsed < 35.0:
            time.sleep(35.0 - elapsed)

        # -------------------------------------------------------------
        # ACT 4: The One Bus Stop Test (5-Min Sprint) (Duration: ~28.0s)
        # -------------------------------------------------------------
        print(">>> Recording Act 4: The One Bus Stop Test (28s)...")
        act4_start = time.time()
        page.evaluate("window.updateHUDAct('ACT 04 // SPRINT CADENCE', 'The One Bus Stop Test: 5-Minute Seated Focus Sprint')")

        # Start 5-Minute Focus Sprint timer
        print("Starting 5-Minute Focus Sprint...")
        move_hand(page, 1050, 395, 2.0, click=True)
        time.sleep(3.0)

        # Complete Task 1
        print("Marking Task 1 as Done...")
        move_hand(page, 1060, 455, 1.5, click=True)
        time.sleep(2.5)

        # Complete Task 2
        print("Marking Task 2 as Done...")
        move_hand(page, 1060, 490, 1.5, click=True)
        time.sleep(2.5)

        # Inspect Right Telemetry Panel
        move_hand(page, 1260, 420, 2.5)
        print("Exporting structured action plan...")
        move_hand(page, 1260, 615, 2.0, click=True)
        time.sleep(3.0)

        elapsed = time.time() - act4_start
        if elapsed < 28.0:
            time.sleep(28.0 - elapsed)

        # -------------------------------------------------------------
        # ACT 5: Architecture & Closing (Duration: ~29.0s)
        # -------------------------------------------------------------
        print(">>> Recording Act 5: Architecture & Closing (29s)...")
        act5_start = time.time()
        page.evaluate("window.updateHUDAct('ACT 05 // ARCHITECTURE', 'Meta Immersive Web SDK (@iwsdk/core) & Production Deployment')")

        # Wide cinematic overview
        move_hand(page, 960, 540, 4.0)
        move_hand(page, 960, 460, 5.0)
        move_hand(page, 960, 540, 5.0)

        elapsed = time.time() - act5_start
        if elapsed < 29.0:
            time.sleep(29.0 - elapsed)

        print("[RECORDER] Recording completed. Finalizing video file...")
        context.close()
        raw_video_path = page.video.path()
        print(f"[RECORDER] Raw video saved to: {raw_video_path}")
        browser.close()
        return raw_video_path

def mux_final_video(raw_webm_path):
    print("[FFMPEG] Muxing 1080p video with studio voiceover and burned-in subtitles...")
    # Convert backslashes for ffmpeg filter
    escaped_srt = SUBTITLES_PATH.replace("\\", "/").replace(":", "\\:")
    
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-i", raw_webm_path,
        "-i", VOICEOVER_PATH,
        "-vf", f"subtitles='{escaped_srt}':force_style='FontSize=22,FontName=Arial,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&H80000000,BorderStyle=4,MarginV=42'",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        OUTPUT_VIDEO_PATH
    ]
    
    print("Running:", " ".join(ffmpeg_cmd))
    subprocess.run(ffmpeg_cmd, check=True)
    print(f"[FFMPEG] Master Demo Video successfully created at: {OUTPUT_VIDEO_PATH}")

    # Copy to public folder
    import shutil
    shutil.copyfile(OUTPUT_VIDEO_PATH, PUBLIC_VIDEO_PATH)
    print(f"[COPIED] Copied to public folder: {PUBLIC_VIDEO_PATH}")

if __name__ == "__main__":
    raw_path = record()
    mux_final_video(raw_path)
    print("ALL DONE! 11/10 MASTER DEMO VIDEO GENERATED!")
