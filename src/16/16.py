


# test about Image again

from PIL import Image, ImagePalette
import requests
from io import BytesIO
import numpy as np

response = requests.get("http://www.pythonchallenge.com/pc/return/mozart.gif", auth = ("huge", "file"))
img = Image.open(BytesIO(response.content))

print(sorted(img.getcolors(), key=lambda x:x[0], reverse = True))

pic = Image.new("RGB", (100, 100))
pixel = 195

rgb = img.getpalette()[pixel*3:pixel*3+3]
for i in range(pic.size[0]):
    for j in range(pic.size[1]):
        pic.putpixel((i,j), tuple(rgb))
pic.show()



############################

result = []
for row in np.array(img):
    result.append(bytes(np.roll(row, -np.where(row==195)[0][0]).tolist()))

final = Image.frombytes(img.mode, img.size, b"".join(result))
final.save("final.png")




