import time
from playwright.sync_api import sync_playwright

VERCEL_URL = "https://synapsedesk-ai.vercel.app/"

def record():
    print(f"Launching Playwright Chromium for 1080p WebXR Recording on {VERCEL_URL}...")
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
            record_video_dir="recorded_raw_extended/",
            record_video_size={"width": 1920, "height": 1080},
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        
        print(f"Navigating to Vercel deployment: {VERCEL_URL}")
        page.goto(VERCEL_URL, wait_until="networkidle", timeout=60000)
        time.sleep(5)

        # -------------------------------------------------------------
        # ACT 1: The Problem & Seated Airplane Seat Arc (Duration: ~33.5s)
        # -------------------------------------------------------------
        print(">>> Act 1: Seated Ergonomics & Airplane Seat Envelope (33.5s)...")
        start_time = time.time()
        # Scan across the 3-panel curved arc (lap height r=0.55m)
        for x in [960, 1200, 1400, 960, 600, 450, 750, 960]:
            page.mouse.move(x, 540)
            time.sleep(1.8)
        
        # Focus on the status badges
        page.mouse.move(1100, 340)
        time.sleep(3.0)
        
        # Wait remainder of Act 1
        elapsed = time.time() - start_time
        if elapsed < 33.5:
            time.sleep(33.5 - elapsed)

        # -------------------------------------------------------------
        # ACT 2: Hands-First Cockpit & Cognitive Capture (Duration: ~37.2s)
        # -------------------------------------------------------------
        print(">>> Act 2: Hands-First Interaction & Cognitive Capture (37.2s)...")
        start_time = time.time()
        
        # Move to left panel: Cognitive Capture
        page.mouse.move(620, 380)
        time.sleep(2.5)

        # Poke preset: Quantum Systems
        print("Poking Quantum Systems preset...")
        page.mouse.click(620, 520)
        time.sleep(4.0)

        # Poke preset: 60 FPS VR Latency Optimization
        print("Poking 60 FPS Optimization preset...")
        page.mouse.click(620, 560)
        time.sleep(4.0)

        # Poke back to: Horizon Store Launch Plan
        print("Poking Horizon Store Launch preset...")
        page.mouse.click(620, 480)
        time.sleep(4.0)

        # Hover near the intent buffer
        page.mouse.move(620, 420)
        time.sleep(5.0)

        elapsed = time.time() - start_time
        if elapsed < 37.2:
            time.sleep(37.2 - elapsed)

        # -------------------------------------------------------------
        # ACT 3: Synapse Core Agent & Auto-Clustering (Duration: ~35.3s)
        # -------------------------------------------------------------
        print(">>> Act 3: Synapse Core 3D Agent & Auto-Cluster (35.3s)...")
        start_time = time.time()

        # Hover and inspect the central holographic Synapse Core orb
        page.mouse.move(960, 410)
        time.sleep(3.5)

        # Poke the Synapse Core agent orb (triggers sound & particle flash)
        print("Poking Synapse Core crystalline agent orb...")
        page.mouse.click(960, 410)
        time.sleep(4.0)

        # Interact with grabbable 3D task prisms
        page.mouse.move(860, 520) # Red prism
        time.sleep(2.0)
        page.mouse.down()
        page.mouse.move(890, 500)
        time.sleep(1.5)
        page.mouse.up()
        time.sleep(2.0)

        # Poke Auto-Cluster (2ft) button on the hub
        print("Triggering Auto-Cluster (2ft) relaxation algorithm...")
        page.mouse.click(890, 615)
        time.sleep(5.0)

        # Inspect the aligned nodes in the 40° field-of-view corridor
        for x in [800, 960, 1120]:
            page.mouse.move(x, 520)
            time.sleep(2.0)

        elapsed = time.time() - start_time
        if elapsed < 35.3:
            time.sleep(35.3 - elapsed)

        # -------------------------------------------------------------
        # ACT 4: Bus Stop 5-Minute Sprint & Telemetry (Duration: ~28.9s)
        # -------------------------------------------------------------
        print(">>> Act 4: Bus Stop Sprint & Telemetry (28.9s)...")
        start_time = time.time()

        # Start 5-Minute Focus Sprint timer
        print("Starting 5-Minute Focus Sprint timer...")
        page.mouse.click(1050, 395)
        time.sleep(4.5)

        # Mark Task 1 as Done
        print("Marking Task 1 as Done...")
        page.mouse.click(1060, 455)
        time.sleep(3.5)

        # Mark Task 2 as Done
        print("Marking Task 2 as Done...")
        page.mouse.click(1060, 490)
        time.sleep(3.5)

        # Inspect right panel: Synapse Telemetry & Cognitive Load
        page.mouse.move(1260, 420)
        time.sleep(4.0)

        # Poke Export Structured Workflow Plan button
        print("Exporting structured workflow action plan...")
        page.mouse.click(1260, 615)
        time.sleep(4.5)

        elapsed = time.time() - start_time
        if elapsed < 28.9:
            time.sleep(28.9 - elapsed)

        # -------------------------------------------------------------
        # ACT 5: Vercel WebXR Streaming & Platform Specs (Duration: ~28.7s)
        # -------------------------------------------------------------
        print(">>> Act 5: Vercel Streaming & Platform Closing (28.7s)...")
        start_time = time.time()

        # Wide cinematic overview
        page.mouse.move(960, 540)
        time.sleep(5.0)
        page.mouse.move(960, 460)
        time.sleep(6.0)

        elapsed = time.time() - start_time
        if elapsed < 28.7:
            time.sleep(28.7 - elapsed)

        print("Recording completed. Closing browser context...")
        context.close()
        video_path = page.video.path()
        print(f"Raw video saved to: {video_path}")
        browser.close()
        return video_path

if __name__ == "__main__":
    record()
