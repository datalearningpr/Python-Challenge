
# test about rolling

import string
import numpy as np

maplist = []

for i in range(1, 26):
    maplist.append("".join(np.roll([c for c in string.ascii_lowercase], i)))

input = 'va gur snpr bs jung?'

for m in maplist:
    t = str.maketrans(string.ascii_lowercase, m)
    print(input.translate(t))

t = str.maketrans(string.ascii_lowercase, maplist[12])
print(input.translate(t))

import this

