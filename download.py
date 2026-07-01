import os
import requests

API_KEY = os.getenv("PEXELS_API_KEY")

headers = {
    "Authorization": API_KEY
}

url = "https://api.pexels.com/videos/search?query=funny animals&per_page=1"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

if response.status_code == 200:
    data = response.json()
    if data["videos"]:
        print("✅ Pexels API Working!")
        print("Video URL:", data["videos"][0]["video_files"][0]["link"])
    else:
        print("No videos found.")
else:
    print(response.text)
