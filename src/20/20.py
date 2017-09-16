
# test about http request headers

import requests
import re

url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
base = 30203

messages = []

while base <= 2123456789:

    try:
        headers = {"Range": "bytes={0}-{0}".format(base)}
        r = requests.get(url, auth = ("butter", "fly"), headers = headers)
        print(r.content.decode())
        messages.append(r.content.decode())
        print(r.headers["Content-Range"])

        if base == 2123456789:
            break

        m = re.match('bytes {}-([0-9]+)/2123456789'.format(base), r.headers['Content-Range'])
        base = int(m.group(1)) + 1
        

    except Exception as e:
        base = 2123456789

print(messages[-1][::-1])


base=2123456743
headers = {"Range": "bytes={0}-{0}".format(base)}
r = requests.get(url, auth = ("butter", "fly"), headers = headers)
print(r.content.decode())

base=1152983631
headers = {"Range": "bytes={0}-{0}".format(base)}
r = requests.get(url, auth = ("butter", "fly"), headers = headers)
print(r.content)

f = open('ouput.zip', 'wb').write(r.content)

