
# test about Image comparision

import requests
from io import BytesIO
from PIL import Image
import bz2
import keyword
import pandas as pd


r = requests.get("http://www.pythonchallenge.com/pc/rock/mandelbrot.gif", auth = ("kohsamui", "thailand"))
img = Image.open(BytesIO(r.content))


left = 0.34
bottom = 0.57
width = 0.036
height = 0.027
max = 128


w, h = img.size

xstep = width / w
ystep = height/ h

result = []

for y in range(h - 1, -1, -1):
    for x in range(w):
        c = complex(left + x * xstep, bottom + y * ystep)
        z = 0 + 0j
        for i in range(max):
            z = z * z + c
            if abs(z) > 2: 
                break
        result.append(i)

new = img.copy()
new.putdata(result)
new.show()




diff = [(a - b) for a, b in zip(img.getdata(), new.getdata()) if a != b]
print(len(diff))


final = Image.new('L', (23, 73))
final.putdata([(0 if i < 0 else 255) for i in diff])
final.show()


