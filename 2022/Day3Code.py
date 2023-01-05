import array as arr

input = [x.rstrip() for x in open("Day3Input.txt", "r").readlines()]

total = 0
for x in input:

    firstHalf = x[slice(0, (len(x))//2)]
    secondHalf = x[slice((len(x))//2, (len(x)))]

    matchingCharacter = ''
    #finding the matching character in both strings
    for i in range(len(firstHalf)):
        if firstHalf[i] in secondHalf:
            matchingCharacter = firstHalf[i]
            if matchingCharacter.isupper():
                total += (ord(matchingCharacter)-38)
            else:
                total += (ord(matchingCharacter)-96)
            break
        else:
            continue
#7811
print(total)

for x in input:
    #star 2
    groups = [[]]
    group = []
    num = 0
    for i in range(len(input)):
        if i == len(input)-1:
            groups.append(group)
        elif (num == 3):
            groups.append(group)
            group = []
            num = 0
        group.append(input[i])
        num+=1

groups.pop(0)

badgeTotals = 0
for group in groups:
    first = group[0]
    second = group[1]
    third = group[2]
    poss = []
    for c in range(len(first)):
        if first[c] in second:
            poss.append(first[c])
    
    for x in poss:
        if (x in first) and (x in second) and (x in third):
            teamBadge = x
            break

    if teamBadge.isupper():
        badgeTotals += (ord(teamBadge)-38)
    else:
        badgeTotals += (ord(teamBadge)-96)

#2639
print(badgeTotals)










