import os

api_key = os.getenv("PEXELS_API_KEY")

if api_key:
    print("✅ Pexels API Key Loaded Successfully")
else:
    print("❌ Pexels API Key Not Found")
