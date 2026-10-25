import asyncio
import edge_tts

VOICE = "en-US-ChristopherNeural"
RATE = "+14%" # Exactly ~155s (2m 35s), perfectly inside the 2-3 minute sweet spot and strictly under the 3-minute cap

SCRIPT_SECTIONS = [
    {
        "id": "act1_intro",
        "title": "Act 1: The Problem & The Seated Spatial Paradigm",
        "text": "Welcome to SynapseDesk AI, an autonomous spatial cognition workspace built natively for Meta Quest devices using the official Meta Immersive Web SDK. Traditional VR productivity applications overwhelm users with floating two-dimensional walls that force uncomfortable standing roomscale movement and clumsy physical keyboard positioning. SynapseDesk AI re-architects spatial computing around human ergonomics. Designed from the ground up for the Airplane Seat Test, every panel, tactile dial, and interactive prism operates strictly inside a comfortable two-foot radius arc directly in front of the seated user."
    },
    {
        "id": "act2_cockpit",
        "title": "Act 2: The Hands-First Cockpit & UIKitML Matrix",
        "text": "Here, on our live Vercel deployment at synapsedesk-ai.vercel.app, judges and users enter XR with zero installation friction. The experience is one hundred percent hands-first: not a single controller is required. Using Meta's official PokeInteractable finger physics, we simply reach out with our index fingertip to press controls on the curved cockpit. Notice how the three panels hug our natural forty-degree field of view. On the left panel, the Cognitive Capture Synthesizer allows us to input high-level ambitions, switching effortlessly between startup launch plans, deep quantum studies, and 60 FPS VR graphics optimizations."
    },
    {
        "id": "act3_agent",
        "title": "Act 3: The Synapse Core Agent & Spatial Auto-Clustering",
        "text": "At the center of our workspace floats the Synapse Core: an interactive holographic AI agent entity. When given a complex goal, the agent does not merely output text. It acts spatially, autonomously decomposing our ambition into prioritized three-dimensional physical task prisms. Users can reach out with bare hands, using natural pinch gestures to grab, lift, and inspect each prism in three-dimensional space. When tasks become cluttered, touching the crystalline core triggers real-time force-directed relaxation, magnetically auto-clustering floating nodes into a tidy, ergonomic arc calibrated to our line of sight."
    },
    {
        "id": "act4_sprint",
        "title": "Act 4: The One Bus Stop Sprint & Cognitive Telemetry",
        "text": "To satisfy the One Bus Stop Test, SynapseDesk AI integrates a five-minute seated focus sprint. Tapping Start on the central hub initiates the countdown, accompanied by zero-latency procedural Web Audio chimes synthesized directly in the browser. As we complete milestones, our active cognitive load automatically recalculates on the telemetry ledger: shifting from potential overload down to a balanced flow state. With a single tap, the agent compiles and exports a complete structured action plan to our workflow."
    },
    {
        "id": "act5_closing",
        "title": "Act 5: Vercel WebXR Streaming & Platform Compliance",
        "text": "By deploying directly on Vercel at synapsedesk-ai.vercel.app, SynapseDesk AI eliminates Meta Horizon store APK approval delays and device compatibility bugs. The entire engine combines Three.js r185, Havok WebAssembly physics, and Meta Horizon design systems locked at sixty frames per second. Built for the Meta VR Start Developer Competition 2026, SynapseDesk AI demonstrates the future of hands-first, seated spatial productivity."
    }
]

async def generate():
    print("Generating comprehensive 2.5-minute narration audio...")
    full_audio = "full_voiceover_extended.mp3"
    full_text = " ".join([sec["text"] for sec in SCRIPT_SECTIONS])
    
    comm = edge_tts.Communicate(full_text, VOICE, rate=RATE)
    await comm.save(full_audio)
    print("Saved extended full voiceover:", full_audio)

    for sec in SCRIPT_SECTIONS:
        fname = f"{sec['id']}.mp3"
        c = edge_tts.Communicate(sec["text"], VOICE, rate=RATE)
        await c.save(fname)
        print(f"Saved {fname}")

if __name__ == "__main__":
    asyncio.run(generate())
