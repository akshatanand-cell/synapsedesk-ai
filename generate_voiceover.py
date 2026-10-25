import asyncio
import edge_tts

VOICE = "en-US-ChristopherNeural"

SCRIPT_SEGMENTS = [
    {
        "id": "scene1",
        "text": "Most VR productivity applications throw massive 2D screens across your entire room, forcing you to stand up or reach into the void. Meet SynapseDesk AI: the hands-first, seated autonomous spatial workspace built exclusively for Meta Quest."
    },
    {
        "id": "scene2",
        "text": "Engineered strictly for the Airplane Seat Test, every interaction stays inside a comfortable two-foot radius arc. Requiring zero controllers, we simply poke the Horizon Store Launch sprint on the Cognitive Capture panel with our index finger."
    },
    {
        "id": "scene3",
        "text": "The Synapse Core agent decomposes our ambition into prioritized 3D physical task prisms. Users pinch and manipulate nodes with bare hands. Tapping the crystalline core triggers real-time force-directed auto-clustering, snapping chaotic nodes into an ergonomic field-of-view corridor."
    },
    {
        "id": "scene4",
        "text": "For rapid daily momentum, the One Bus Stop mode provides a five-minute seated focus sprint with procedural Web Audio feedback. We complete our tasks, observe our cognitive load balance in real time, and export our structured action plan."
    },
    {
        "id": "scene5",
        "text": "100 percent hands-first, strictly seated, and locked at 60 FPS. SynapseDesk AI: built with the official Meta Immersive Web SDK for the Meta VR Start Developer Competition 2026."
    }
]

async def main():
    print("Generating voiceover tracks...")
    full_audio = "full_voiceover.mp3"
    full_text = " ".join([seg["text"] for seg in SCRIPT_SEGMENTS])
    communicate = edge_tts.Communicate(full_text, VOICE, rate="+3%")
    await communicate.save(full_audio)
    print("Full voiceover saved:", full_audio)

    # Also save individual scene tracks
    for seg in SCRIPT_SEGMENTS:
        comm = edge_tts.Communicate(seg["text"], VOICE, rate="+3%")
        filename = f"{seg['id']}.mp3"
        await comm.save(filename)
        print(f"Saved {filename}")

if __name__ == "__main__":
    asyncio.run(main())
