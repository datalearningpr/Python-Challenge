
# test about Image with Wave

import requests
from io import BytesIO
from PIL import Image
import wave

wavs = []
for i in range(1, 26):

    r = requests.get("http://www.pythonchallenge.com/pc/hex/lake{}.wav".format(i), auth = ("butter", "fly"))
    w = wave.open(BytesIO(r.content))
    wavs.append(w)


imgs = []

for w in wavs:
    imgs.append(Image.frombytes("RGB",(60, 60), (w.readframes(w.getnframes()))))

final = Image.new("RGB", (300, 300))

for num, img in enumerate(imgs):
    a, b = divmod(num, 5)
    y = a * 60
    x = b * 60

    for i in range(60):
        for j in range(60):
            final.putpixel((x+i, y+j), img.getpixel((i, j)))

final.save("final.jpg")








