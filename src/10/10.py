
# this test is about reading the pattern of the test

read = "1"
result = ""


for i in range(30):

    reading_tag = 0
    looping_tag = 0

    while reading_tag < len(read):
        while looping_tag < len(read) and read[reading_tag] == read[looping_tag]:
            looping_tag = looping_tag + 1
        
        result = result + str(looping_tag - reading_tag) + read[reading_tag]
        reading_tag = looping_tag

    print(result)
    read = result
    result = ""

print(len(read))

