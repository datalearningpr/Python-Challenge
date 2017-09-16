
# test about Image again

from PIL import Image
import requests
from io import BytesIO

response = requests.get("http://www.pythonchallenge.com/pc/return/wire.png", auth = ("huge", "file"))
img = Image.open(BytesIO(response.content))

output = Image.new('RGB', [100,100])

num = 100

steps = []

while num != 0:
    steps.append(num)
    steps.append(num-1)
    steps.append(num-1)
    steps.append(num-2)
    num = num -2

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

pos = [100, 0]
start = 0
for i, step in enumerate(steps):
    for j in range(start, start+step):
        pos[0] = pos[0] + direction[(i%4)][0]
        pos[1] = pos[1] + direction[(i%4)][1]
        
        output.putpixel((pos[0], pos[1]), img.getpixel((j, 0)))
    start = start + step


output.save("output.jpg")

