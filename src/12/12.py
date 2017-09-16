

# test about Image again

from PIL import Image
import requests
from io import BytesIO

response = requests.get("http://www.pythonchallenge.com/pc/return/evil4.jpg", auth = ("huge", "file"))
print(response.content.decode("utf-8"))



response = requests.get("http://www.pythonchallenge.com/pc/return/evil2.gfx", auth = ("huge", "file"))
print(response.content)

for i in range(5):
    open("{}.jpg".format(i), "wb").write(response.content[i::5])
