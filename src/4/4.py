# this test is about using the urllib library

import urllib.request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
number = "12345"
prenumber = ""

while number.isdigit():
    print(number)
    response = urllib.request.urlopen(url.format(number))
    html = response.read().decode("utf-8")
    prenumber = number
    number = html.split()[-1]

print(html)


number = str(int(int(prenumber)/2))

while number.isdigit():
    print(number)
    response = urllib.request.urlopen(url.format(number))
    html = response.read().decode("utf-8")
    number = html.split()[-1]

print(html)