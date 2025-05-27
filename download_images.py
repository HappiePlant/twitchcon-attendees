import json
import requests
import os
import time
from PIL import Image

with open("attendees.json", "wb") as file:
  response = requests.get("https://api.twitchcon.com/attendees?eventName=rotterdam-2025")
  file.write(response.content)

with open("attendees.json", "r") as file:
  json_file = json.load(file)

atteendes = json_file['attendees']

for attendee in atteendes:
  image_url: str = attendee['avatar']
  image_name = image_url.split("/")[-1]
  image_path = "img/" + image_name
  image_resized_path = "img_res/" + image_name

  if not os.path.exists(image_path):
    image = requests.get(image_url, stream=True)
    image.raise_for_status()

    with open(image_path, "wb") as file:
      for chunk in image.iter_content(chunk_size=8192):
                  file.write(chunk)
    time.sleep(0.2)

  if os.path.exists(image_path) and not os.path.exists(image_resized_path):
    img = Image.open(image_path)
    img_resized = img.resize((100, 100), Image.Resampling.LANCZOS)
    img_resized.save(image_resized_path)