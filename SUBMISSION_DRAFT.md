# SynapseDesk AI — Devpost Official Submission Kit

Use this document to fill out the Devpost Submission Form for the **Meta VR Start Developer Competition 2026**.

---

### 1. General Project Details

* **Submission Name:**
  `SynapseDesk AI — Autonomous Spatial Workspace Protocol`

* **Submission Tagline (under 140 chars):**
  `Hands-first seated spatial cognition workspace for Meta Quest. Features 2-foot ergonomic arc physics & autonomous multi-step agent reasoning.`

* **Track:**
  `Productivity`

* **Division:**
  `New Experience`

* **Target Launch Date:**
  `December 15, 2026`

---

### 2. URLs & Links

* **Working Demo / Hosted WebXR Application URL:**
  `https://synapsedesk-ai.vercel.app/`
  *(Mirror: https://akshatanand-cell.github.io/synapsedesk-ai/)*

* **Public Code Repository URL:**
  `https://github.com/akshatanand-cell/synapsedesk-ai`

* **Testing Instructions for Judges:**
```
Hardware Compatibility: Meta Quest 3, Meta Quest 3S, or Chrome Desktop WebXR Simulator.

Steps to Test:
1. Put on your Meta Quest headset (or launch Chrome with Immersive Web Emulator extension).
2. Open Meta Quest Browser and navigate to: https://synapsedesk-ai.vercel.app/
3. Tap "Enter XR (Hands-First)" on the central curved dashboard.
4. Put your controllers aside — this application is 100% controller-free and hands-first:
   - Seated Ergonomics (The Airplane Seat Test): All interactive elements are situated in an ergonomic curved arc strictly within a 2-foot reach radius (r = 0.55m).
   - Tap Buttons: Use your index fingertip to poke buttons directly (powered by PokeInteractable).
   - Grab 3D Task Prisms: Reach out and pinch to lift and reposition 3D priority prisms in space.
   - Autonomous Auto-Cluster: Tap the floating central "Synapse Core" crystalline agent orb or click "Auto-Cluster (2ft)". Watch the agent run real-time force-directed relaxation to organize floating nodes into an optimal field-of-view corridor.
   - The One Bus Stop Sprint: Tap "Start" on the 5-minute Focus Sprint timer to run a seated focus session accompanied by procedural spatial audio cues.
   - Cognitive Telemetry: Observe real-time Cognitive Load (Flow State) and agent reasoning traces on the right telemetry ledger.
```

---

### 3. Submission Text Description (Suggested length: 500 words or less)

#### Inspiration
Traditional VR productivity tools suffer from a fundamental mismatch with human physiology: they replicate oversized 2D multi-monitor walls that force users into wide roomscale reaching, physical neck strain, and reliance on physical keyboards. We asked: *What if spatial computing adapted to the user’s seated cognitive bubble, instead of forcing the user to adapt to infinite empty space?*

We conceived **SynapseDesk AI** around two core design guidelines from the Meta 2026 brief:
1. **The Airplane Seat Test:** Every single interaction must work effortlessly within a 2-foot radius in front of a seated user.
2. **Hands-First Interaction:** 100% of the workflow must be completed without ever pairing or touching a controller.

#### What It Does
SynapseDesk AI is a seated, hands-first spatial thought and productivity cockpit:
- **Curved Ergonomic Viewport:** Three curved Horizon UIKitML panels (Intent Synthesizer, Active Workspace Hub, and Agentic Telemetry) hug the user's natural 40-degree field of view at lap height ($r = 0.55\text{m}$).
- **The Synapse Core (Autonomous Agent Entity):** A holographic 3D particle orb floating in front of the desk. When given a complex ambition (e.g. *"Launch on Meta Horizon Store"*, *"Quantum Computing Sprint"*), the agent decomposes it into prioritized 3D physical task prisms.
- **Hands-First Physics:** Users grab and position task prisms using Meta IWSDK pinch tracking (`OneHandGrabbable`, `DistanceGrabbable`) and poke UI controls directly with their fingertips (`PokeInteractable`).
- **Force-Directed Auto-Clustering:** Tapping the Synapse Core triggers an autonomous relaxation algorithm that snaps chaotic floating nodes into a tidy, ergonomic arc calibrated to the user's gaze.
- **One Bus Stop Sprint Mode:** A built-in 5-minute focus session with zero-latency procedural Web Audio chimes for rapid daily momentum.

#### How We Built It
- **Engine:** Built with Meta’s official **Immersive Web SDK (`@iwsdk/core` v1.1.0)** and Three.js (r185 / `super-three`).
- **Spatial UI:** Styled with Meta Horizon design language (`@pmndrs/uikit-horizon` and `@pmndrs/uikit-lucide`) in dark mode.
- **Physics & Gestures:** Havok Physics (WebAssembly) with native WebXR Hand Tracking integration.
- **Procedural Spatial Audio:** Pure Web Audio API procedural synthesis generating tactile clicks, harmonic drops, and ethereal agent chimes without network dependencies.
- **Deployment:** Continuous automated CI/CD deployment via GitHub Actions and GitHub Pages with zero-install WebXR streaming.

#### Accomplishments That We're Proud Of
- 100% compliance with both the **Airplane Seat Test** ($< 2\text{ft}$ radius) and the **Bus Stop Test** ($< 10\text{min}$ session loop).
- Completely controller-free hands-first interaction with tactile audio-visual confirmation.
- Rock-solid 60+ FPS performance on Meta Quest hardware through procedural Three.js geometry batching.

#### Future Plans
- Persistent Spatial Anchors across sessions via Horizon OS Scene API.
- Integration with Meta Llama 3 spatial edge tool-calling for real-time natural language voice dictation.

---

### 4. How Hand Interactions Are Implemented (Optional Field)

```
Hand interaction is the foundational backbone of SynapseDesk AI:
1. Fingertip Direct Poke: Using Meta IWSDK's PokeInteractable, users physically press 3D buttons on the curved cockpit using their index fingertip with hysteresis-protected contact thresholds.
2. Natural Pinch & Grab: Using OneHandGrabbable and DistanceGrabbable, users pinch their thumb and index finger to grab, reposition, and inspect 3D task prisms in space.
3. Tactile Audio Feedback: Every pinch, hover, and release triggers procedurally synthesized Web Audio micro-chimes (D5-A5 ramps) providing immediate sensory confirmation without haptic motors.
4. Auto-Cluster Gesture: Poking the central Synapse Core agent triggers autonomous force-directed spatial alignment, organizing all floating nodes into the user's field-of-view corridor.
```

---

### 5. 3-Minute Video Demonstration Script & Storyboard

* **0:00 - 0:25 | The Hook & The Problem:**
  - *Visual:* Screen recording in Meta Quest headset / Simulator. Show seated position.
  - *Voiceover:* "Most VR productivity apps throw massive 2D screens across your entire room, forcing you to stand up or reach into the void. Meet SynapseDesk AI — the hands-first, seated autonomous spatial workspace designed specifically for Meta Quest."

* **0:25 - 1:00 | The Airplane Seat Test & Hands-First Demo:**
  - *Visual:* Point out the 3 curved panels hugging the 2-foot reach envelope ($r=0.55\text{m}$). Show controllers set aside.
  - *Action:* Reach forward with hand; poke the "Horizon Store Launch Plan" button with index finger. Notice tactile audio chime.

* **1:00 - 1:50 | The Autonomous Agent & 3D Task Prisms:**
  - *Visual:* Show the Synapse Core agent orb pulsing. Show 3D task prisms appearing in front of the lap dock.
  - *Action:* Pinch a glowing red task prism ("Meta XR Hand Physics") and move it closer. Tap the Synapse Core agent orb to trigger the autonomous Auto-Cluster — watch all 3D prisms smoothly snap into an ergonomic arc!

* **1:50 - 2:30 | The Bus Stop Sprint & Cognitive Telemetry:**
  - *Visual:* Focus on the One Bus Stop Sprint Timer (05:00).
  - *Action:* Tap "Start". Mark task 1 as "Done". Show Cognitive Load updating in real time on the telemetry panel. Tap "Export Structured Workflow Plan".

* **2:30 - 3:00 | The Closer:**
  - *Visual:* Pan back to show the clean, futuristic, seated spatial cockpit.
  - *Voiceover:* "SynapseDesk AI: 100% hands-first, strictly seated, and powered by autonomous spatial intelligence. Built with Meta Immersive Web SDK for Meta VR Start 2026."
