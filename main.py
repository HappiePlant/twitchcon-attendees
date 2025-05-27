import json
import requests
import os
import time
from PIL import Image
import typst

# Config (more options in main.typ)
image_size = 100
event_id = "rotterdam-2025"

if not os.path.exists("attendees.json"):
  print("Downloading TwitchCon attendees")
  with open("attendees.json", "wb") as file:
    response = requests.get(f"https://api.twitchcon.com/attendees?eventName={event_id}")
    file.write(response.content)
    json_data = json.loads(response.content)

else:
  print("Loading TwitchCon attendees")
  with open("attendees.json", "r") as file:
    json_data = json.load(file)

atteendes = json_data["attendees"]

for attendee in atteendes:
  image_url: str = attendee["avatar"]
  image_name = image_url.split("/")[-1]
  image_path = "img/" + image_name
  image_resized_path = "img_res/" + image_name

  if not os.path.exists(image_path):
    print(attendee["name"] + ": Downloading image")
    image = requests.get(image_url, stream=True)
    image.raise_for_status()

    with open(image_path, "wb") as file:
      for chunk in image.iter_content(chunk_size=8192):
        file.write(chunk)
    time.sleep(0.2)

  if os.path.exists(image_path) and not os.path.exists(image_resized_path):
    print(attendee["name"] + ": Resizing image")
    img = Image.open(image_path)
    img_resized = img.resize((image_size, image_size), Image.Resampling.LANCZOS)
    img_resized.save(image_resized_path)

print("Compiling document")
typst.compile("main.typ", "TwitchCon Attendees.pdf")
