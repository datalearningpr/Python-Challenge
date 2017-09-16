
# this test is about pickle

import urllib.request
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"


response = urllib.request.urlopen(url)

output = pickle.load(response)

for row in output:
    result = ''
    for chars in row:
        result += chars[0] * chars[1]
    print(result)