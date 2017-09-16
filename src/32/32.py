
# test about solving games with computer


import itertools
from itertools import combinations
import re
import copy
from PIL import Image

# this function is to assist getting the combination of possible input
def get_real_num(input, count):
    out = []
    out.append(input[0]-1)
    for i in range(1, len(input)):
        out.append(input[i] - input[i - 1])
    out.append(count + 1 - input[-1])
    return out

# get the possible input with given N and input
def generate_all_combination(input, N):

    count = len(input) + 1
       
    left = N - sum(input)

    output = []

    if count != 0 and left >= count-2:

        temp = list(combinations(list(range(1, left+2)), count - 1))
        num_list = list([get_real_num(x, left) for x in temp])

        for j in num_list:
            str = ""
            for i in range(len(input)):
                str = str + j[i] * "0"
                str = str + input[i] * "1"
            str = str + j[len(input)] * "0"
            output.append(str)
       
    return output


# this function is using the tag rule gained to clear out the wrong input choices
def remove_choice(input, pos, tag):
    input2 = copy.deepcopy(input)
    for x, y in pos:
        to_delete = []
        for text in input2[y]:
            if text[x] != tag:
                to_delete.append(text)
        for x in to_delete:
            input2[y].remove(x)
    return input2


# this function is to read the input file, given the tests N are the same for x, y length of input
def readtxt(filename):
    f = open(filename, "r")
    inputdata = []
    checkdata = []

    flag = 0
    N = 0
    for line in f.readlines():
        if line[0] == "#":
            flag = flag + 1
        elif line[0] == "\n":
            pass
        else:
            if flag == 1:
                N = int(line.split()[0])
            elif flag == 2:
                inputdata.append([int(i) for i in line.split()]) 
            elif flag == 3:
                checkdata.append([int(i) for i in line.split()]) 

    return N, inputdata, checkdata



# this is the function to solve the game
def solve(inputs, check, N):


    # first, based on the 2 ways of input, get all the combinations possible

    input_choice = []
    for i in inputs:
       input_choice.append(generate_all_combination(i, N))

    check_choice = []
    for i in check:
       check_choice.append(generate_all_combination(i, N))



    
    # keep doing until the solution found
    while True:
        
        # lists to contain the MUST BE cells of 1 or 0   
        one_pos_input = []
        zero_pos_input = []

        for i in range(len(input_choice)):
            for j in range(N):
        
                text = [x[j] for x in input_choice[i]]
                if len(set(text)) == 1:
                    if text[0] == "0":
                        zero_pos_input.append((i, j))
                    elif text[0] == "1":
                        one_pos_input.append((i, j))
                    else:
                        pass

        # do the same for the other dimension
        one_pos_check = []
        zero_pos_check = []

        for i in range(len(check_choice)):
            for j in range(N):
        
                text = [x[j] for x in check_choice[i]]
                if len(set(text)) == 1:
                    if text[0] == "0":
                        zero_pos_check.append((i, j))
                    elif text[0] == "1":
                        one_pos_check.append((i, j))
                    else:
                        pass

        # clear out the NOT possible choices using the rules gained for both dimension
        new_input_choice = remove_choice(input_choice, one_pos_check, "1")
        new_input_choice = remove_choice(new_input_choice, zero_pos_check, "0")
        new_check_choice = remove_choice(check_choice, one_pos_input, "1")
        new_check_choice = remove_choice(new_check_choice, zero_pos_input, "0")
        

        # if no more NOT possible choices got filtered out, means we have solutions(or limited choices)
        if (new_input_choice != input_choice) or (new_check_choice != check_choice):
            input_choice=new_input_choice
            check_choice=new_check_choice
        else:
            break

    # most likely, when the loop stops, we will have only 1 choice which is the solution
    if [len(i) for i in new_input_choice] == [1] * N:
        final = list(itertools.product(*new_input_choice))
    else:
        # if this case really happens, we just need to verify them all, but the remaining ones should be in very low numbers
        final = "Too many sloutions, will not return!"

    return final

  


if __name__ == "__main__":
    
    #N, inputdata, checkdata = readtxt("warmup.txt")
    N, inputdata, checkdata = readtxt("32.txt")
    final = solve(inputdata, checkdata, N)


    # draw out the solution
    img = Image.new("P", (N, N))
    data = [int(i)*255 for i in "".join(final[0])]
    img.putdata(data)
    img.show()