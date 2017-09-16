
# test about difflib

import gzip, difflib

lines=gzip.open("deltas.gz").readlines()

data1 = []
data2 = []

for line in lines:
    data1.append(line[:53].decode("utf-8") + "\n")
    data2.append(line[56:].decode("utf-8"))


compare = difflib.Differ().compare(data1, data2)

pic  = open("pic.png", "wb")
pic1 = open("pic1.png", "wb")
pic2 = open("pic2.png", "wb")

for line in compare:
    input = []
    for i in line[2:].strip().split(" "):
        if i != "":
            input.append(int(i, 16))
    d = bytes(input)
    
    if line[0] == '+':
        pic1.write(d)
    elif line[0] == '-':
        pic2.write(d)
    else:
        pic.write(d)

pic.close()
pic1.close()
pic2.close()