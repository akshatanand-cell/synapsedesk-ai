import os
import subprocess
import shutil

BASE_DIR = r"C:\Users\KIIT\.gemini\antigravity\scratch\meta-vr-2026\synapsedesk-ai"
RAW_WEBM = os.path.join(BASE_DIR, "recorded_master_raw", "page@13b62aee76a95369047f28243e09e8b9.webm")
VOICEOVER = os.path.join(BASE_DIR, "full_voiceover_extended.mp3")
SRT = os.path.join(BASE_DIR, "subtitles_extended.srt")
OUTPUT = os.path.join(BASE_DIR, "SynapseDesk_AI_Demo_Video.mp4")
PUBLIC_OUTPUT = os.path.join(BASE_DIR, "public", "SynapseDesk_AI_Demo_Video.mp4")

escaped_srt = SRT.replace("\\", "/").replace(":", "\\:")

cmd = [
    "ffmpeg", "-y",
    "-i", RAW_WEBM,
    "-i", VOICEOVER,
    "-vf", f"subtitles='{escaped_srt}':force_style='FontSize=22,FontName=Arial,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&H80000000,BorderStyle=4,MarginV=42'",
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",
    OUTPUT
]

print("Executing ffmpeg:", cmd)
subprocess.run(cmd, check=True)
print("Finished muxing to:", OUTPUT)

shutil.copyfile(OUTPUT, PUBLIC_OUTPUT)
print("Copied to public folder:", PUBLIC_OUTPUT)
