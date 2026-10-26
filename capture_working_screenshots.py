import os
import time
from playwright.sync_api import sync_playwright

BASE_DIR = r"C:\Users\KIIT\.gemini\antigravity\scratch\meta-vr-2026\synapsedesk-ai"
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
PUBLIC_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "public", "screenshots")

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(PUBLIC_SCREENSHOTS_DIR, exist_ok=True)

VERCEL_URL = "https://synapsedesk-ai.vercel.app/?view=cockpit"

def capture():
    print("[SCREENSHOTS] Launching Chromium 1920x1080 to capture working product states...")
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
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        
        print(f"Navigating to {VERCEL_URL}...")
        page.goto(VERCEL_URL, wait_until="networkidle", timeout=60000)
        time.sleep(6.0) # Wait for WebGL compilation & scene mount

        # -----------------------------------------------------------
        # Shot 1: Wide Seated Cockpit Panorama (All 3 Panels + Core)
        # -----------------------------------------------------------
        print("Capturing 01_seated_cockpit_panorama.png...")
        path_1 = os.path.join(SCREENSHOTS_DIR, "01_seated_cockpit_panorama.png")
        page.screenshot(path=path_1)

        # -----------------------------------------------------------
        # Shot 2: Cognitive Capture & Goal Decomposition Panel
        # -----------------------------------------------------------
        print("Capturing 02_cognitive_capture_panel.png...")
        # Hover near left panel
        page.mouse.move(580, 480)
        time.sleep(1.0)
        # Click preset Horizon Store
        page.mouse.click(580, 480)
        time.sleep(1.5)
        path_2 = os.path.join(SCREENSHOTS_DIR, "02_cognitive_capture_panel.png")
        page.screenshot(path=path_2)

        # -----------------------------------------------------------
        # Shot 3: Active Focus Sprint & Task Completion
        # -----------------------------------------------------------
        print("Capturing 03_focus_sprint_active.png...")
        # Start focus sprint
        page.mouse.click(1050, 395)
        time.sleep(2.0)
        # Complete task 1
        page.mouse.click(1060, 455)
        time.sleep(1.5)
        path_3 = os.path.join(SCREENSHOTS_DIR, "03_focus_sprint_active.png")
        page.screenshot(path=path_3)

        # -----------------------------------------------------------
        # Shot 4: Synapse Core Agent & Auto-Clustering
        # -----------------------------------------------------------
        print("Capturing 04_synapse_core_agent_cluster.png...")
        # Click Synapse Core orb
        page.mouse.click(960, 410)
        time.sleep(1.5)
        # Drag task token
        page.mouse.move(860, 520)
        page.mouse.down()
        page.mouse.move(890, 480)
        page.mouse.up()
        time.sleep(1.5)
        path_4 = os.path.join(SCREENSHOTS_DIR, "04_synapse_core_agent_cluster.png")
        page.screenshot(path=path_4)

        # -----------------------------------------------------------
        # Shot 5: Telemetry & Cognitive Load Protocol Panel
        # -----------------------------------------------------------
        print("Capturing 05_telemetry_interaction_sdk.png...")
        page.mouse.move(1340, 480)
        time.sleep(1.5)
        path_5 = os.path.join(SCREENSHOTS_DIR, "05_telemetry_interaction_sdk.png")
        page.screenshot(path=path_5)

        # -----------------------------------------------------------
        # Shot 6: Web Landing Interface (Clean HUD View)
        # -----------------------------------------------------------
        print("Capturing 06_web_landing_experience.png...")
        page.goto("https://synapsedesk-ai.vercel.app/", wait_until="networkidle")
        time.sleep(4.0)
        path_6 = os.path.join(SCREENSHOTS_DIR, "06_web_landing_experience.png")
        page.screenshot(path=path_6)

        browser.close()
        print("All 6 working product screenshots captured successfully!")

    # Copy all to public/screenshots as well
    import shutil
    for f in os.listdir(SCREENSHOTS_DIR):
        if f.endswith(".png"):
            src = os.path.join(SCREENSHOTS_DIR, f)
            dst = os.path.join(PUBLIC_SCREENSHOTS_DIR, f)
            shutil.copyfile(src, dst)
    print(f"Copied screenshots to {PUBLIC_SCREENSHOTS_DIR}")

if __name__ == "__main__":
    capture()
