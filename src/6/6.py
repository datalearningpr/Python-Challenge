
# this test is about zipfile

import zipfile
file = zipfile.ZipFile("channel.zip")

number = "90052"

comments = []

while number.isdigit():
    print(number)
    text = file.read(number + ".txt").decode("utf-8")
    comments.append(file.getinfo(number + ".txt").comment.decode("utf-8"))
    number = text.split()[-1]

print(text)
print("".join(comments))