# SynapseDesk AI — Autonomous Spatial Workspace Protocol
> **Meta VR Start Developer Competition 2026**  
> **Track:** Productivity (New Experience Division)  
> **Special Award Focus:** Best Agentic Interaction ($25,000) & Best First Five Minutes ($25,000)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Meta Immersive Web SDK](https://img.shields.io/badge/Meta_IWSDK-v1.1.0--rc.2-blueviolet.svg)](https://github.com/facebook/immersive-web-sdk)
[![WebXR](https://img.shields.io/badge/WebXR-Ready-brightgreen.svg)](https://immersiveweb.dev/)
[![Three.js](https://img.shields.io/badge/Three.js-r185-orange.svg)](https://threejs.org/)

---

## 1. Executive Summary

**SynapseDesk AI** is a hands-first, seated autonomous spatial cognition workspace built exclusively for Meta Quest 3 and Quest 3S devices via the official **Meta Immersive Web SDK (IWSDK)**.

Traditional VR productivity applications overwhelm users with floating 2D desktop windows that demand wide roomscale movement and clumsy physical keyboard positioning. **SynapseDesk AI** re-engineers productivity around human cognitive flow and natural hand ergonomics:

1. **Strictly Seated (The Airplane Seat Test):** All interactive cards, agent dials, and tactile prisms operate inside an ergonomic **2-foot radius arc ($r = 0.55\text{m}$)** directly matching the human field of view. Zero roomscale or awkward physical reaching required.
2. **100% Hands-First:** No controllers needed. Reach out to poke buttons with your fingertips (`PokeInteractable`), pinch and manipulate 3D task prisms (`OneHandGrabbable`), or summon layout auto-clustering with a direct pinch.
3. **The Autonomous Agent ("Synapse Core"):** A holographic 3D crystalline agent orb floats in your peripheral view. Instead of a superficial chat window, the agent acts spatially: it parses natural language ambitions, breaks complex goals into prioritized 3D nodes, computes real-time cognitive load, and runs force-directed spatial relaxation to auto-cluster cards into an optimal layout.
4. **The "One Bus Stop" Sprint:** An integrated 5-minute seated focus sprint with ambient procedural audio cues, allowing users to enter XR, conquer a focused milestone, and export a structured action plan in under 10 minutes.

---

## 2. Platform Evaluation & Rule Compliance Matrix

| Official Contest Metric | Requirement | SynapseDesk AI Implementation |
| :--- | :--- | :--- |
| **Hands-First Test** | Fully usable with hands end-to-end. Can someone complete the experience without controllers? | **100% Controller-Free.** Powered by Meta IWSDK Hand Tracking, `PokeInteractable` finger physics, and `OneHandGrabbable` pinch mechanics. |
| **Airplane Seat Test** | Seated stationary use in a 2-foot diameter bubble. | Ergonomic curved cylindrical cockpit ($r = 0.55\text{m}$, angle $\pm 28^\circ$) directly within fingertip reach without leaning forward. |
| **One Bus Stop Test** | Satisfying milestone in $\le 10$ minutes with fast cold start. | Instant WebXR launch with zero APK install delays via Vercel (`https://synapsedesk-ai.vercel.app/`); 5-minute focused Sprint Timer with structured output export. |
| **Take-It-Away Test** | Original entrant-built core; not a thin external API wrapper. | Entrant-authored spatial agentic state machine, force-directed auto-clustering physics, Web Audio synthesizer, and custom Horizon UIKitML layouts. |
| **Performance Target** | Minimum 60+ FPS lock on Meta Quest hardware. | Procedurally batched Three.js r185 primitives, WebAssembly Havok physics, zero heavy external GLTF download latency. |

---

## 3. System Architecture & Agentic Intelligence

```
                        ┌───────────────────────────────────────┐
                        │        Natural Language Intent        │
                        │    (Voice / High-Cognition Preset)    │
                        └──────────────────┬────────────────────┘
                                           │
                                           ▼
                        ┌───────────────────────────────────────┐
                        │       Autonomous Decomposer           │
                        │  - Semantic Subgraph Extraction       │
                        │  - Difficulty & Time Estimation       │
                        │  - Cognitive Load Heuristic (0-100%)  │
                        └──────────────────┬────────────────────┘
                                           │
                                           ▼
                        ┌───────────────────────────────────────┐
                        │     Spatial Arc Force-Clustering      │
                        │  - 2-Foot Airplane Envelope (r=0.55m) │
                        │  - Angular FOV Corridor Mapping       │
                        │  - Collision Repulsion & Levitation   │
                        └──────────────────┬────────────────────┘
                                           │
           ┌───────────────────────────────┴───────────────────────────────┐
           ▼                                                               ▼
┌───────────────────────────────┐                               ┌───────────────────────────────┐
│     Spatial UIKitML Matrix    │                               │     Hands-First 3D Physics    │
│  - Central Hub & Sprint Clock │                               │  - Synapse Core Agent Orb     │
│  - Intent Buffer & Presets    │                               │  - Grabbable Octahedron Nodes │
│  - Real-time Telemetry Ledger │                               │  - Procedural Audio Cues      │
└───────────────────────────────┘                               └───────────────────────────────┘
```

### Agentic Capabilities:
* **Dynamic Goal Decomposition:** Breaks messy goals (e.g. *"Meta Horizon Store Launch Sprint"*, *"Quantum Computing Study"*) into ordered P1/P2/P3 milestones with duration estimates.
* **Force-Directed Ergonomic Auto-Clustering:** Mathematically repositions clutter into a harmonic arc around the player's seated chest level.
* **Cognitive Load Telemetry:** Monitors the volume of active urgent blockers vs. finished tasks, adjusting the user's flow state metric (Deep Flow $\rightarrow$ Balanced $\rightarrow$ Overload Risk).
* **Zero-Latency Web Audio Synthesizer:** Real-time procedural audio (pentatonic pinch clicks, harmonic drops, and ethereal agent chimes) synthesized directly in Web Audio without external media dependencies.

---

## 4. Tech Stack

* **Platform Engine:** Meta Immersive Web SDK (`@iwsdk/core` v1.1.0-rc.2)
* **3D & Rendering:** Three.js (r185 / `super-three`)
* **Physics & Spatial Interaction:** Havok Physics (WebAssembly runtime) + Meta Hand Tracking
* **Spatial UI:** `@pmndrs/uikit-horizon` + `@pmndrs/uikit-lucide` (Horizon Dark Design System)
* **Audio:** Web Audio API Procedural Synthesizer
* **Build Tooling:** Vite 7 + TypeScript 5.5

---

## 5. Quickstart & Local Testing Instructions

### Prerequisites
* Node.js v20.19.0+ or v24.15.0+
* npm v10+

### Installation & Run
```bash
# 1. Clone the repository
git clone https://github.com/akshatanand-cell/synapsedesk-ai.git
cd synapsedesk-ai

# 2. Install dependencies
npm install

# 3. Start local development server
npm run dev
```

### Testing on Meta Quest 3 / Quest 3S:
1. Open the **Meta Quest Browser** in your headset.
2. Navigate to the live Vercel URL: **[https://synapsedesk-ai.vercel.app/](https://synapsedesk-ai.vercel.app/)** (or GitHub Pages mirror).
3. Tap **"Enter XR (Hands-First)"** on the central panel.
4. Put your controllers down — use your hands directly:
   - **Pinch & Move:** Grab any of the floating 3D task prisms.
   - **Tap / Poke:** Use index finger to press buttons on the curved cockpit.
   - **Auto-Cluster:** Tap the floating central **Synapse Core** agent orb or click **"Auto-Cluster (2ft)"** to watch the agent organize your nodes into an ergonomic arc.

---

## 6. License

This project is licensed under the [MIT License](LICENSE).
