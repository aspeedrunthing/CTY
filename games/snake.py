import math
import random
def printboard(width):
    print(end="  ")
    for i in range(1,width):
        print("#", end=" ")
    print("#")
    for i in range(0,width):
        if i == width:
            print("#")
        else:
            print("#", end=" ")
        for o in range(0,width):
            print(showboard[i][o], end=" ")
        print("#")
    print(end="  ")
    for i in range(1,width):
        print("#", end=" ")
    print("#")
def makeboard(showboard):
    boardlength = "yes"
    while not boardlength.isdigit():
        boardlength = input("how big do you want the board to be? (x by x)")
        if not boardlength.isdigit():
            print("please input a valid number")
    for i in range(1, int(math.ceil(float(boardlength)))):
        showboard.append([" "])
    for i in range(0, int(math.ceil(float(boardlength)))):
        for o in range(1, int(math.ceil(float(boardlength)))):
            showboard[i].append(" ")
showboard = [[" "]]
makeboard(showboard)
snakepos = [[0,0], [0,1], [0,2]]
lose = 0
fruitpos = [random.randint(0, len(showboard)-1), random.randint(0, len(showboard)-1)]
showboard[fruitpos[0]][fruitpos[1]] = "Q"
for i in range(0, len(snakepos)):
    showboard[snakepos[i][0]][snakepos[i][1]] = "0"
printboard(len(showboard))
while lose == 0:
    printboard(len(showboard))
    direction = input("W, A, S, or D").lower()
    if direction == "w":
        if not [snakepos[len(snakepos)-1][0]-1, snakepos[len(snakepos)-1][1]] in snakepos:
            snakepos.append([snakepos[len(snakepos)-1][0]-1, snakepos[len(snakepos)-1][1]])
        else:
            showboard[snakepos[len(snakepos)-1][0]][snakepos[len(snakepos)-1][1]] = "X"
            print("You Lose!")
            lose = 1
            break
    elif direction == "s":
        if not [snakepos[len(snakepos)-1][0]+1, snakepos[len(snakepos)-1][1]] in snakepos:
            snakepos.append([snakepos[len(snakepos)-1][0]+1, snakepos[len(snakepos)-1][1]])
        else:
            showboard[snakepos[len(snakepos)-1][0]][snakepos[len(snakepos)-1][1]] = "X"
            print("You Lose!")
            lose = 1
            break
    elif direction == "a":
        if not [snakepos[len(snakepos)-1][0], snakepos[len(snakepos)-1][1]-1] in snakepos:
            snakepos.append([snakepos[len(snakepos)-1][0], snakepos[len(snakepos)-1][1]-1])
        else:
            showboard[snakepos[len(snakepos)-1][0]][snakepos[len(snakepos)-1][1]] = "X"
            print("You Lose!")
            lose = 1
            break
    elif direction == "d":
        if not [snakepos[len(snakepos)-1][0], snakepos[len(snakepos)-1][1]+1] in snakepos:
            snakepos.append([snakepos[len(snakepos)-1][0], snakepos[len(snakepos)-1][1]+1])
        else:
            showboard[snakepos[len(snakepos)-1][0]][snakepos[len(snakepos)-1][1]] = "X"
            print("You Lose!")
            lose = 1
            break
    else:
        continue
    showboard[snakepos[0][0]][snakepos[0][1]] = " "
    if not snakepos[len(snakepos)-1][0] == fruitpos[0] or not snakepos[len(snakepos)-1][1] == fruitpos[1]:
        showboard[fruitpos[0]][fruitpos[1]] = "Q"
        snakepos.pop(0)
    else:
        fruitpos = [random.randint(0, len(showboard)-1), random.randint(0, len(showboard)-1)]
        while fruitpos in snakepos:
            fruitpos = [random.randint(0, len(showboard)-1), random.randint(0, len(showboard)-1)]
        showboard[fruitpos[0]][fruitpos[1]] = "Q"
    for i in range(0, len(snakepos)):
        showboard[snakepos[i][0]][snakepos[i][1]] = "0"
        if i == len(snakepos)-2:
            if snakepos[len(snakepos)-1][0] == len(showboard) or snakepos[len(snakepos)-1][0] == -1 or snakepos[len(snakepos)-1][1] == len(showboard) or snakepos[len(snakepos)-1][1] == -1:
                showboard[snakepos[i][0]][snakepos[i][1]] = "X"
                print("You Lose!")
                lose = 1
                break
printboard(len(showboard))