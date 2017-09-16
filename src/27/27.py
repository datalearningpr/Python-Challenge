

# test about Image with compressed data

import requests
from io import BytesIO
from PIL import Image
import bz2
import keyword


r = requests.get("http://www.pythonchallenge.com/pc/hex/zigzag.gif", auth = ("butter", "fly"))
img = Image.open(BytesIO(r.content))


b_from = bytes([i for i in range(256)])
b_to = bytes(img.getpalette()[::3])
table = bytes.maketrans(b_from, b_to)

original = img.tobytes()
transformed = original.translate(table)


shifted_o = original[1:]
shifted_t = transformed[:-1]

data = []
indices = []
for i in range(len(shifted_o)):
    if shifted_o[i] != shifted_t[i]:
        data.append(shifted_o[i])
        indices.append(i)



new = Image.new("RGB", img.size)
colors = [(255, 255, 255)] * len(original)
for i in indices:
    colors[i] = (0, 0, 0)
new.putdata(colors)


text = bz2.decompress(bytes(data)).decode()


final = set()
for i in text.split():
    if not keyword.iskeyword(i):
        final.add(i)

print(final)