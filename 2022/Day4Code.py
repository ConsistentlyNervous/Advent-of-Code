import array as arr

# parse input line by line
input = [x.rstrip() for x in open("Day4Input.txt", "r").readlines()]

# store first and second number x-y and third and fourth number z-v as variables
counter = 0

for x in input:
    num = 1
    first = ""
    second = ""
    third = ""
    fourth = ""
    for char in x:
        if char == ",":
            num+=1
            continue
        if char == "-":
            num+=1
            continue
        if num == 1:
            first += char
        if num == 2:
            second += char
        if num == 3:
            third += char
        if num == 4:
            fourth += char
    first = int(first)
    second = int(second)
    third = int(third)
    fourth = int(fourth)

# check if the third is leq the first and the fourth is leq the second or if 
# first is leq the third and the second is leq the fourth or
    if third >= first and fourth <= second:
        # if either statement is true add one to the counter
        counter += 1
    elif first >= third and second <= fourth:
        # if either statement is true add one to the counter
        counter += 1

#return the counter value
print(counter)

args = [[]]
line = []
newCounter = 0
for x in input:
    num = 1
    first = ""
    second = ""
    third = ""
    fourth = ""
    for char in x:
        if char == ",":
            num+=1
            continue
        if char == "-":
            num+=1
            continue
        if num == 1:
            first += char
        if num == 2:
            second += char
        if num == 3:
            third += char
        if num == 4:
            fourth += char
    first = int(first)
    second = int(second)
    third = int(third)
    fourth = int(fourth)
#5-7,7-9->7    2-8,3-7->all     6-6,4-6->6     2-6,4-8->4-6   56-62,51-59    51-59,56-62
    #check if the starting numbers are 
# check if the third is leq the first and the fourth is leq the second or if 
# first is leq the third and the second is leq the fourth or
    if first < third:
        if second >= third:
            print("first if " + str(first) + "-" + str(second) + ", " + str(third) + "-" + str(fourth))
            newCounter += 1
        #else:
            #print(str(first) + "-" + str(second) + ", " + str(third) + "-" + str(fourth))
    elif first > third:
        if fourth >= first and (second >= fourth or second >= third):
            print("second if " + str(first) + "-" + str(second) + ", " + str(third) + "-" + str(fourth))
            newCounter += 1
        #else:
            #print(str(first) + "-" + str(second) + ", " + str(third) + "-" + str(fourth))
    elif first == third:
        print("third if " + str(first) + "-" + str(second) + ", " + str(third) + "-" + str(fourth))
        newCounter += 1
    
print(newCounter)
print("poop")