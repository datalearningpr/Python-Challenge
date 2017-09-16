

# test about combining all the skill gained from previous tests

import requests
import bz2
import xmlrpc.client
import urllib

r = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php")
print(r.cookies.get_dict())



cookie_list = []
num='12345'

while num.isdigit() is True:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}".format(num)
    r = requests.get(url)
    num = r.content.decode("utf-8").split()[-1]
    cookie_list.append(r.cookies['info'])


final_cookie = "".join(cookie_list)
final = bz2.decompress(urllib.parse.unquote_to_bytes(final_cookie.replace("+"," "))).decode("utf-8")


import xmlrpc.client

connection = xmlrpc.client.Server("http://www.pythonchallenge.com/pc/phonebook.php")
print(connection.phone("Leopold"))


cookies = dict(info ='the flowers are on their way')
r = requests.get("http://www.pythonchallenge.com/pc/stuff/violin.php", cookies=cookies)
print(r.content.decode("utf-8"))


