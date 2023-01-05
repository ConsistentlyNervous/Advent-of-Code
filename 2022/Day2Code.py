import array as arr

file1 = open("Day2Input.txt","r")
input = file1.read()

oppMoves = []
ourMoves = []

for i in range(len(input)):
    if input[i] == 'A' or input[i] == 'B' or input[i] == 'C':
        #opp move
        oppMoves.append(input[i])
    elif input[i] == 'X' or input[i] == 'Y' or input[i] == 'Z':
        #our move
        ourMoves.append(input[i])
    else:
        continue

gameTotal = 0

for j in range(len(oppMoves)):
    #adds points for our move choice
    match ourMoves[j]:
        case 'X':
            gameTotal += 1
            match oppMoves[j]:
                case 'A':
                    gameTotal += 3
                case 'B':
                    gameTotal
                case 'C':
                    gameTotal += 6
        case 'Y':
            gameTotal += 2
            match oppMoves[j]:
                case 'A':
                    gameTotal += 6
                case 'B':
                    gameTotal += 3
                case 'C':
                    gameTotal
        case 'Z':
            gameTotal += 3
            match oppMoves[j]:
                case 'A':
                    gameTotal
                case 'B':
                    gameTotal += 6
                case 'C':
                    gameTotal += 3

#13526
print (gameTotal)

gameTotal = 0

for j in range(len(oppMoves)):
    #adds points for our move choice
    match ourMoves[j]:
        #lose
        case 'X':
            gameTotal
            match oppMoves[j]:
                case 'A':
                    gameTotal += 3
                case 'B':
                    gameTotal += 1
                case 'C':
                    gameTotal += 2
        #draw
        case 'Y':
            gameTotal += 3
            match oppMoves[j]:
                case 'A':
                    gameTotal += 1
                case 'B':
                    gameTotal += 2
                case 'C':
                    gameTotal += 3
        #win
        case 'Z':
            gameTotal += 6
            match oppMoves[j]:
                case 'A':
                    gameTotal += 2
                case 'B':
                    gameTotal += 3
                case 'C':
                    gameTotal += 1
print(gameTotal)




    