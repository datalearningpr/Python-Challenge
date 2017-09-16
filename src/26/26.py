


# test about haslib and MD5

import hashlib

md5code = 'bbb8b499a0eef99b52c7f13f4e78c24b'
data = open("mybroken.zip", "rb").read()

for i in range(len(data)):
    for j in range(256):
        newData = data[:i] + bytes([j]) + data[i + 1:]
        if hashlib.md5(newData).hexdigest() == md5code:
            print(j)
            open('final.zip', 'wb').write(newData)
