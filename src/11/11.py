

# test about Image again, but result hard to read.

from PIL import Image
import requests
from io import BytesIO

response = requests.get("http://www.pythonchallenge.com/pc/return/cave.jpg", auth = ("huge", "file"))
img = Image.open(BytesIO(response.content))

length, width = img.size

new_length, new_width = length//2, width//2

even = Image.new("RGB", (new_length, new_width))
odd = Image.new("RGB", (new_length, new_width))

for i in range(length):
    for j in range(width):
        if (i+j) % 2 == 1:
            odd.putpixel((i//2,j//2), img.getpixel((i,j)))
        else:
            even.putpixel((i//2,j//2), img.getpixel((i,j)))

even.save("even.jpg")
odd.save("odd.jpg")


