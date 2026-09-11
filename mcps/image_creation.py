import os
import requests, io, time
from PIL import Image

HF_TOKEN = os.environ["HF_TOKEN"]
API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}
payload = {"inputs": "A Pakistani school boy of class 6th holding a medal on the result day."}

for attempt in range(5):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(f"Attempt {attempt+1} | Status: {response.status_code} | Content-Type: {response.headers.get('Content-Type')}")

    if response.status_code == 503:
        wait = response.json().get("estimated_time", 20)
        print(f"Model loading... retrying in {wait:.0f}s")
        time.sleep(wait)
        continue

    if "image" in response.headers.get("Content-Type", ""):
        image = Image.open(io.BytesIO(response.content))
        image.save("C:/Users/Dell/Pictures/mcp-mages/student_image.png")
        print("Success! Saved as student_image.png")
        break
    else:
        print("Unexpected response:", response.text[:300])
        break