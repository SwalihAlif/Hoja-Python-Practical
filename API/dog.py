import requests

url = "https://random.dog/woof.json"

data = requests.get(url).json()
image_url = data["url"]

image = requests.get(image_url).content

with open("dog.jpg", "wb") as f:
    f.write(image)

print("Image downloaded!")