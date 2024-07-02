import math
import random
def printboard(width):
    for i in range(0,width-1):
        if i > 9:
            print(end="  ")
            break
        else:
            print(end="   ")
            break
    for i in range(1,width-1):
        if i-((int(i//9.5)*9)) > 9:
            print((i-((int(i//9.5)*9)))-9, end=" ")
        else:
            print(i-((int(i//9.5)*9)), end=" ")
    print(width-1)
    for i in range(0,width-1):
        if i > 8:
            print(i+1, end=" ")
        else:
            print(i+1, end="  ")
        for o in range(0,width-1):
            if o == width-2:
                print(showboard[i][o])
            else:
                print(showboard[i][o], end=" ")
def makeboard(showboard):
    boardlength = "yes"
    while not boardlength.isdigit():
        boardlength = input("how big do you want the board to be? (x by x)")
        if not boardlength.isdigit():
            print("please input a valid number")
    for i in range(1, int(math.ceil(float(boardlength)))+1):
        showboard.append([0])
    for i in range(0, int(math.ceil(float(boardlength)))+1):
        for o in range(1, int(math.ceil(float(boardlength)))+1):
            showboard[i].append(0)
def fillboard(hideboard, boardlength, difficulty, disableflood):
    # 0 = empty, 1-8 = checked, clear, i = flagged, x = checked, bomb
    maxbombrow=0
    bombinrow=0
    totalbomb = 0
    for i in range(1, int(math.ceil(float(boardlength)))+1):
        hideboard.append([0])
    for i in range(0, int(math.ceil(float(boardlength)))+1):
        for o in range(1, int(math.ceil(float(boardlength)))+1):
            hideboard[i].append(0)
    for i in range(0, len(hideboard)-1):
        maxbombrow = random.randint(1, math.ceil(boardlength/3))
        for o in range(0, len(hideboard)-1):
            if bombinrow == maxbombrow:
                break
            elif random.random() > 1+(0.1*(-(int(difficulty)))):
                hideboard[i][o] += 1
                bombinrow += 1
                totalbomb += 1
                disableflood.append([i-1, o-1])
    print("there are {} bombs on the board".format(totalbomb))
    return totalbomb
def checkboard(hideboard, row, column):
    nearbybombs = 0
    for a in range(0,3):
        for b in range(0,3):
            if hideboard[int(row)-a][int(column)-b] == 1:
                nearbybombs += 1
    return nearbybombs
def floodboard(showboard, hideboard, row, column, disableflood):
        if row < len(showboard) and column < len(showboard):
            if showboard[row][column] == 0 or showboard[row][column] == " ":
                if not [row, column] in disableflood:
                    disableflood.append([row, column])
                    if row+1 < len(showboard) and column+1 < len(showboard):
                        if checkboard(hideboard, row+1, column+1) == 0:
                            showboard[row][column] = " "
                            for o in range(0,3):
                                for p in range(0,3):
                                    if row-o+1 > -1 and column - p+1 > -1:
                                        if row-o+1 < len(showboard) and column - p+1 < len(showboard):
                                            showboard[row-o+1][column-p+1] = floodboard(showboard, hideboard, row-o+1, column-p+1, disableflood)
                                            printboard(len(showboard))
                            return " "
                        else:
                            return checkboard(hideboard, row-1, column-1)
                else:
                    return showboard[row][column]
            else: 
                return showboard[row][column]
showboard = [[0]]     
makeboard(showboard)
boardlength = len(showboard)
bombrow = boardlength/3
win = 0
lose = 0
bombsflagged = 0
fakeflag = 0
hideboard = [[0]]
difficulty = "a"
nearbybombs = 0
disableflood=[]
for i in range(-boardlength,boardlength+1):
    disableflood.append([boardlength,i])
for i in range(-boardlength,boardlength+1):
    disableflood.append([i, boardlength])
while not difficulty.isdigit():
    difficulty = input("choose your difficulty (1-9)")
    if not difficulty.isdigit():
        print("please input a valid number")
        continue
    elif int(math.ceil(float(difficulty))) > 9 and int(math.floor(float(difficulty))) < 1:
        print("please input a valid number")
        difficulty = "a"
        continue
boardbombs = fillboard(hideboard, boardlength-1, difficulty, disableflood)
print(showboard)
print(hideboard)
while win == 0 and lose == 0:
    stopflood = 0
    nearbybombs = 0
    column = "a"
    row = "a"
    check = "a"
    printboard(boardlength)
    while not column.isdigit():
        column = input("what column do you want to check")
        if not column.isdigit():
            print("please input a valid number")
    while not row.isdigit():
        row = input("what row do you want to check")
        if not row.isdigit():
            print("please input a valid number")
    while not check == "check" and not check == "flag":
        check = input("do you want to check or flag this spot?")
        if not check == "check" and not check == "flag":
            print("please input a valid action")
    if hideboard[int(row)-1][int(column)-1] == 1 and check == "check":
        lose = 1
        showboard[int(row)-1][int(column)-1] = "x"
        printboard(boardlength)
        print("BOOM")
        print("you lose!")
    elif hideboard[int(row)-1][int(column)-1] == 1 and check == "flag":
        showboard[int(row)-1][int(column)-1] = "i"
        bombsflagged += 1
    if boardbombs == bombsflagged:
        if fakeflag == 0:
            win = 1
            printboard(boardlength)
            print("congradulations!")
            print("you win!")
        else:
            print("all bombs have been found!")
            print("but some safe areas are still flagged")
            print("fix them to win!")
    elif hideboard[int(row)-1][int(column)-1] == 0 and check == "flag":
        showboard[int(row)-1][int(column)-1] = "i"
        fakeflag += 1
    elif hideboard[int(row)-1][int(column)-1] == 0 and check == "check":
        nearbybombs = (checkboard(hideboard, row, column))
        if nearbybombs == 0:
            showboard[int(row)-1][int(column)-1] = " "
            if not [int(row)-1, int(column)-1] in disableflood:
                showboard[int(row)-1][int(column)-1] = floodboard(showboard, hideboard, int(row)-1, int(column)-1, disableflood)
                if showboard[int(row)-1][int(column)-1] == " ":
                    disableflood.append([int(row)-1, int(column)-1])  
        else: 
            showboard[int(row)-1][int(column)-1] = nearbybombs