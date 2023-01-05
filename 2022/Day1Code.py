import array as arr

file1 = open("Day1Input.txt","r")
input = file1.read()

#read the file into an array of arrays, where each array represents an elf
inputArr = [[]]
singleArr = []
element = ""
for i in range(len(input)):
    if input[i] == '\n':
        if input[i+1] == '\n':
            #new group
            singleArr.append(int(element))
            inputArr.append(singleArr)
            singleArr = []
            element = ""
        elif input[i-1] == '\n':
            continue
        else:
            #add to existing group
            singleArr.append(int(element))
            element = ""
    elif i == (len(input)-1):
        #add the last element
        element += input[i]
        singleArr.append(int(element))
        inputArr.append(singleArr)

    else: 
        #add to existing number
        element += input[i]

#total the values
totals = []
totalAtX = 0
for x in inputArr:
   #print(x)
    totalAtX = sum(x)
    totals.append(totalAtX)

print("The max calories carried is: " + str(max(totals)))

#find the 3 max totals, remove them as you find them
total1 = max(totals)
totals.remove(total1)

total2 = max(totals)
totals.remove(total2)

total3 = max(totals)
totals.remove(total3)

print("The 3 max calories total is: " + str(total1 + total2 + total3))