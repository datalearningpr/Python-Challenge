
# test about image, bytes, coding

import urllib.request
from PIL import Image
from io import BytesIO
import re

url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
response = urllib.request.urlopen(url)
img = Image.open(BytesIO(response.read()))

middle = [img.getpixel((width, img.height / 2)) for width in range(img.width)]

middle = middle[::7]

ascii_num = [a for a,b,c,d in middle]
answer = "".join(map(chr, ascii_num))
print(answer)


numbers = re.findall("\d+", answer)

print("".join(map(chr, map(int, numbers))))