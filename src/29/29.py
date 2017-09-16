
# test about str to bytes

import requests
from io import BytesIO
from PIL import Image
import bz2
import keyword


r = requests.get("http://www.pythonchallenge.com/pc/ring/guido.html", auth = ("repeat", "switch"))
lines = r.content.splitlines()

input = lines[12:]

data = [len(i) for i in input]

print(bz2.decompress(bytes(data)).decode())