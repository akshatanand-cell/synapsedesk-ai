import time
from playwright.sync_api import sync_playwright

def record():
    print("Launching Chromium for 1080p WebXR Recording...")
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
            record_video_dir="recorded_raw/",
            record_video_size={"width": 1920, "height": 1080},
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        
        url = "https://akshatanand-cell.github.io/synapsedesk-ai/"
        print("Navigating to:", url)
        page.goto(url, wait_until="networkidle", timeout=45000)
        time.sleep(4)

        # Scene 1: Overview of seated cockpit (16.5s)
        print("Capturing Scene 1: Seated Cockpit Overview...")
        # Gentle mouse movement to show hands/cursor presence
        for x in range(400, 1500, 100):
            page.mouse.move(x, 540)
            time.sleep(0.5)
        time.sleep(5)

        # Scene 2: Interacting with Cognitive Capture & Intent Presets (14.0s)
        print("Capturing Scene 2: Cognitive Capture Interaction...")
        # Click on left panel preset area
        page.mouse.click(650, 480) # left panel area
        time.sleep(2)
        page.mouse.click(650, 530) # preset 2
        time.sleep(3)
        page.mouse.click(650, 480) # back to Horizon
        time.sleep(4)
        time.sleep(5)

        # Scene 3: Synapse Core Agent & Auto-Cluster (18.8s)
        print("Capturing Scene 3: Synapse Core Auto-Cluster...")
        page.mouse.move(960, 420) # Hover near Synapse Core
        time.sleep(2)
        page.mouse.click(960, 420) # Click/Poke Synapse Core
        time.sleep(3)
        page.mouse.click(900, 620) # Click Auto-Cluster button on hub
        time.sleep(4)
        page.mouse.move(960, 520) # Move across active nodes
        time.sleep(4)
        time.sleep(5.8)

        # Scene 4: Bus Stop Focus Sprint & Telemetry (15.5s)
        print("Capturing Scene 4: 5-Minute Focus Sprint & Telemetry...")
        page.mouse.click(1050, 395) # Start timer
        time.sleep(4)
        page.mouse.click(1060, 455) # Mark Done on Task 1
        time.sleep(3)
        page.mouse.click(1250, 620) # Export structured plan
        time.sleep(4)
        time.sleep(4.5)

        # Scene 5: Outro & Platform Specs (14.5s)
        print("Capturing Scene 5: Platform Specs & Architecture...")
        page.mouse.move(960, 540)
        time.sleep(14.5)

        context.close()
        video_path = page.video.path()
        print("Raw recording saved to:", video_path)
        browser.close()
        return video_path

if __name__ == "__main__":
    record()
