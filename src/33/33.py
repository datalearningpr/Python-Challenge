
# test about Image and decoding with rolling rule

import requests
from io import BytesIO
from PIL import Image
import bz2
import keyword
import math

r = requests.get("http://www.pythonchallenge.com/pc/rock/beer2.png", auth = ("kohsamui", "thailand"))
img = Image.open(BytesIO(r.content))

data = img.getdata()
colors = img.getcolors()

for i in range(65, -1, -2):
    rest = []
    new_data = []

    for j in data:
        if j != colors[i][1] and j != colors[i-1][1]:
            rest.append(j)
            new_data.append(0)

        else:
            if j==colors[i][1]:
                new_data.append(255)
            else:
                new_data.append(0)

    data = rest
    n = int(math.sqrt(len(new_data)))
    new = Image.new("P", (n, n))
    new.putdata(new_data)
    new.save("{}.png".format((i+1)/2))
