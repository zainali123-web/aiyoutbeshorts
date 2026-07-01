import subprocess
import os

INPUT = "output/video.mp4"
OUTPUT = "output/shorts.mp4"

os.makedirs("output", exist_ok=True)

subprocess.run([
    "ffmpeg",
    "-i", INPUT,
    "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
    "-c:a", "copy",
    OUTPUT
])

print("✅ Shorts video created!")
