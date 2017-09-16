
# test about data compressed with different format

import zlib
import bz2
import gzip


f=open("package.pack", "rb")
data = f.read()


output = []

while(True):  
    if data:
      
        if data[:2] == b'x\x9c':
            data = zlib.decompress(data)
            output.append("+")
        elif data[:2] == b'BZ':
            data = bz2.decompress(data)
            output.append("#")
        elif data[-2:] == b'\x9cx':
            data = data[::-1]
            output.append("\n")
        elif data[:2] == b'\x80\x8d':
            data = gzip.decompress(data)
            output.append("%")
        else:
            print(data.decode())
            break

print("".join(output))





