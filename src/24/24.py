
# test about Image and DFS

import requests
from io import BytesIO
from PIL import Image

r = requests.get("http://www.pythonchallenge.com/pc/hex/maze.png", auth = ("butter", "fly"))
img = Image.open(BytesIO(r.content))

start = (639, 0)
end = (1, 640)

white = (255, 255, 255, 255)
color = 1
route = []

path = Image.new("P", img.size, 255)

route.append(start)

(x, y) = start

while (x, y)!=end:

    if y+1 < 641 and img.getpixel((x, y+1)) != white and path.getpixel((x, y+1)) != color:
        y = y + 1
        route.append((x, y))
        path.putpixel((x, y), color)
    elif x+1 < 641 and img.getpixel((x+1, y)) != white and path.getpixel((x+1, y)) != color:
        x = x + 1
        route.append((x, y))
        path.putpixel((x, y), color)
    elif y-1 > -1 and  img.getpixel((x, y-1)) != white and path.getpixel((x, y-1)) != color:
        y = y - 1
        route.append((x, y))
        path.putpixel((x, y), color)
    elif x-1 > -1 and img.getpixel((x-1, y)) != white and path.getpixel((x-1, y)) != color:
        x = x - 1
        route.append((x, y))
        path.putpixel((x, y), color)
    else:
        route = route[:-1]
        (x, y) = route[-1]


final = Image.new("P", img.size, 255)
for (x, y) in route:
    final.putpixel((x, y), 1)
final.show()


output = []
for p in route[1::2]:
        output.append(img.getpixel(p)[0])
f=open('maze.zip','wb')
f.write(bytes(output))
f.close()








