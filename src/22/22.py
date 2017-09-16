

# test about gif and drawing points

import requests
from PIL import Image, ImageSequence
from io import BytesIO

r = requests.get("http://www.pythonchallenge.com/pc/hex/white.gif", auth = ("butter", "fly"))
imgs = ImageSequence.Iterator(Image.open(BytesIO(r.content)))

output = []
for i in imgs:
    y, x = divmod(list(i.getdata()).index(8), 200)
    output.append((x, y))


indexlist = [x for x in range(len(output)) if output[x] == (100, 100)]
trunk =  []
for i in range(1, len(indexlist)):
    trunk.append((indexlist[i-1], indexlist[i]-1))
trunk.append((indexlist[-1], len(output)-1))


for (start, end) in trunk:
    new_img = Image.new("P", (200, 200), 255)
    a = 100
    b = 100
    i = start
    while(i <= end):
        (x, y) = output[i]
        a = a + (x-100)
        b = b + (y-100)
        new_img.putpixel((a, b), 1)
        i=i+1
    new_img.show()


