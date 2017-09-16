


# test about Image and text coding

import requests
from io import BytesIO
from PIL import Image
import bz2
import keyword
import pandas as pd


r = requests.get("http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv", auth = ("repeat", "switch"))
data = pd.read_csv(BytesIO(r.content), header = None, dtype=object)
del data[data.columns[-1]]

input = list(data.as_matrix().flatten()[:-1])
input = list(map(lambda x:x.strip(), input))
img = Image.new('F',(53,139))  
img.putdata(list(map(float, input)), 256)
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img = img.transpose(Image.ROTATE_90)
img.show()

a = input[0::3]
b = input[1::3]
c = input[2::3]

n = []
for i in range(len(c)):
    n.append(a[i][5]+b[i][5]+c[i][6])

print(bytes(map(int,n)).decode())













