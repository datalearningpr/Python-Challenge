

# test about Image

import requests
from io import BytesIO
from PIL import Image
import bz2
import keyword


r = requests.get("http://www.pythonchallenge.com/pc/ring/bell.png", auth = ("repeat", "switch"))
img = Image.open(BytesIO(r.content))

green = list(img.split()[1].getdata())

diff = [abs(a - b) for a, b in zip(green[0::2], green[1::2])]

final = [i for i in diff if i != 42]

print(bytes(final).decode())

creator = "Guido van Rossum"

print(creator.split()[0])














