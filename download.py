import os
import requests

API_KEY = os.getenv("PEXELS_API_KEY")

headers = {
    "Authorization": API_KEY
}

url = "https://api.pexels.com/videos/search?query=funny animals&per_page=1"

response = requests.get(url, headers=headers)

if response.status_code != 200:
    raise Exception(response.text)

video = response.json()["videos"][0]
video_url = video["video_files"][0]["link"]

print("Downloading:", video_url)

video_data = requests.get(video_url)

os.makedirs("output", exist_ok=True)

with open("output/video.mp4", "wb") as f:
    f.write(video_data.content)

print("✅ Video downloaded successfully!")
