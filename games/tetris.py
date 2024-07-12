import random
import time
import math
board = [[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "]]
placeboard = [[0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0]]
#printingboard
def printboard():
    for i in range(0,21):
        print("# ",end="")
    print()
    print("#        LINES - {}".format(lines), end = "")
    for i in range(0,(-len(str(lines)))+3):
        print(" ", end="")
    print("      # #           #")
    for i in range(0,11):
        print("#", end=" ")
    print("# # # #   TOP     #")
    for i in range(0,11):
        print("#", end=" ")
    print("# # # # 0         #")
    for i in range(1, 21):
        print("# #", end=" ")
        for o in range(0, 10):
            print(board[i][o], end=" ")
        print("# #", end = " ")
        if i == 20 or i == 19 or i == 18 or i == 17 or i == 14 or i == 7 or i == 5 or i == 13 or i == 6:
            print("# # # # # # #", end = "")
        elif i == 16:
            print("#    ",level, end = "")
            for i in range(0,(-len(str(level)))+3):
                print(" ", end="")
            print("   #",end="")
        elif i == 15:
            print("#   LEVEL   #", end="")
        elif i == 8:
            print("#   NEXT  # #",end="")
        elif i == 9 or i == 12:
            print("#         # #",end="")
        elif i == 10:
            print("#", end=" ")
            for i in range(0,len(pieces[nextpiece][0])):
                if pieces[nextpiece][0][1][i] == 0:
                    print(" ",end=" ")
                else:
                    print(pieces[nextpiece][0][1][i],end=" ")
            if nextpiece == 1 or nextpiece == 0:
                print("",end="")
            else:
                for i in range(0,(-len(pieces[nextpiece][0][1]))+5):
                    print(" ",end="")
            print("# #",end="")
        elif i == 11:
            print("#", end=" ")
            for i in range(0,len(pieces[nextpiece][0])):
                if pieces[nextpiece][0][2][i] == 0:
                    print(" ",end=" ")
                else:
                    print(pieces[nextpiece][0][2][i],end=" ")
            if nextpiece == 1 or nextpiece == 0:
                print("",end="")
            else:
                for i in range(0,(-len(pieces[nextpiece][0][2]))+5):
                    print(" ",end="")
            print("# #",end="")
        elif i == 5:
            print("# # # # # # #",end="")
        elif i == 4 or i == 1:
            print("#           #",end="")
        elif i == 2:
            print("#   SCORE   #",end="")
        elif i == 3:
            print("# ",end="")
            print(score,end="")
            for i in range(0,(-len(str(score)))+10):
                print(" ",end="")
            print("#",end="")
        print()
    for o in range(0,2):
        for i in range(0,11):
            print("#", end=" ")
        print("# # # # # # # # # #")
#clearinglines
lines = 0
def clearlines(lines):
    line = 0
    clearline = []
    containline = 0
    for i in range(0,22):
        containline = 0
        for o in range(0, 10):
            if placeboard[i][o] == 1:
                containline += 1
        if containline == 10:
            clearline.append(i)
    if len(clearline) > 0:
        for i in range(0, len(clearline)):
            for o in range(0, 10):
                board[clearline[i]][o] = " "
                placeboard[clearline[i]][o] = 0
        printboard()
        time.sleep(0.2)
        for i in range(len(clearline)-1, -1, -1):
            board.pop(clearline[i])
            placeboard.pop(clearline[i])
        for i in range(0, len(clearline)):
            board.insert(2, [" "," "," "," "," "," "," "," "," "," "," "])
            placeboard.insert(2, [0,0,0,0,0,0,0,0,0,0,0])
            line += 1
    return line
placedpieces = [0,0,0,0,0,0,0]
score = 0
level = 0
lose = 0
blockboard = [[" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "]]
pieces = [[[[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]],[[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]],[[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]],[[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]]],[[[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],[[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],[[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],[[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]], [[[0,0,0],[1,1,1],[1,0,0]],[[1,1,0],[0,1,0],[0,1,0]],[[0,0,1],[1,1,1],[0,0,0]],[[0,1,0],[0,1,0],[0,1,1]]], [[[0,0,0],[1,1,1],[0,0,1]],[[0,1,0],[0,1,0],[1,1,0]],[[1,0,0],[1,1,1],[0,0,0]],[[0,1,1],[0,1,0],[0,1,0]]],[[[0,0,0],[1,1,0],[0,1,1]],[[0,0,1],[0,1,1],[0,1,0]],[[0,0,0],[1,1,0],[0,1,1]],[[0,0,1],[0,1,1],[0,1,0]]],[[[0,0,0],[0,1,1],[1,1,0]],[[0,1,0],[0,1,1],[0,0,1]],[[0,0,0],[0,1,1],[1,1,0]],[[0,1,0],[0,1,1],[0,0,1]]],[[[0,0,0],[1,1,1],[0,1,0]],[[0,1,0],[1,1,0],[0,1,0]],[[0,1,0],[1,1,1],[0,0,0]],[[0,1,0],[0,1,1],[0,1,0]]]]
nextpiece = random.randint(0, 6)
rotation = 0
placedpiece = 1
placepiece = 0
y = 0
x = 4
newpiece = 1
previousplaces = []
printboard()
while lose == 0:
    if newpiece == 1:
        newpiece = 0
        placedpiece = 1
        for i in range(0, len(pieces[placepiece][rotation])):
            for o in range(0, len(pieces[placepiece][rotation])):
                if blockboard[i][o] == 1:
                    placeboard[i+y][o+x]=blockboard[i][o]
    if placedpiece == 0:
        for i in range(0, len(previousplaces)):
            board[previousplaces[i][0]][previousplaces[i][1]] = " "
        previousplaces = []
    elif placedpiece == 1:
        x=4
        y=1
        placepiece = nextpiece
        placedpieces[placepiece] += 1
        nextpiece = random.randint(0, 6)
        rotation = 0
        for i in range(0, len(previousplaces)):
            board[previousplaces[i][0]][previousplaces[i][1]] = " "
        previousplaces = []
        for i in range(0,22):
            for o in range(0,11):
                if placeboard[i][o] == 1:
                    board[i-1][o] = 1
    for i in range(0, len(pieces[placepiece][rotation])):
        for o in range(0, len(pieces[placepiece][rotation])):
            if pieces[placepiece][rotation][i][o] == 0:
                blockboard[i][o] = " "
            else:
                blockboard[i][o] = pieces[placepiece][rotation][i][o]
    if placedpiece == 1:
        if blockboard[0][0] == blockboard[0][1] == blockboard[0][2] == " ":
            y -= 1
            if blockboard[1][0] == blockboard[1][1] == blockboard[1][2] == " ":
                y -= 1
    for i in range(0, len(pieces[placepiece][rotation])):
        for o in range(0, len(pieces[placepiece][rotation])):
            if blockboard[i][o] == 1:
                board[i+y][o+x]=blockboard[i][o]
                previousplaces.append([i+y,o+x])
    printboard()
    #movement
    move = input("A,S, or D to move, and W to rotate").lower()
    if move == "a":
        checkcollision = []
        checkpiece = 0
        for i in range(0,len(blockboard)):
            for o in range(0,len(blockboard)):
                   if blockboard[o][i] == 1:
                    checkpiece += 1
            if checkpiece != 0:
                if x+i == 0:
                    pass
                else:
                    checkpiece = 0
                    for i in range(0,len(blockboard)):
                        for o in range(0,3):
                            try:
                                if blockboard[o][i] == 1 and blockboard[o][i-1]==" ":
                                    checkcollision.append([o+y,i+x])
                            except:
                                checkcollision.append([o+y,i+x])
                    for i in range(0,len(checkcollision)):
                        if placeboard[checkcollision[i][0]+1][checkcollision[i][1]-1]==1:
                            checkpiece += 1
                            break
                    if checkpiece == 0:
                        x-=1
                break
    elif move == "s":
        checkpiece = 0
        if placepiece != 0:
            if not y == 19:
                checkcollision = []
                for i in range(2,-1,-1):
                    for o in range(0,3):
                        if blockboard[i][o] == 1 and blockboard[i+1][o]==" ":
                            checkcollision.append([i+y,o+x])
                for i in range(0,len(checkcollision)):
                    if placeboard[checkcollision[i][0]+1][checkcollision[i][1]] == 1:
                        placedpiece = 1
                        for i in range(0, len(pieces[placepiece][rotation])):
                            for o in range(0, len(pieces[placepiece][rotation])):
                                if blockboard[i][o] == 1:
                                    placeboard[i+y][o+x]=blockboard[i][o]
                        break
                    else:
                        checkpiece += 1
                if checkpiece == len(checkcollision):
                    y+=1
        elif placepiece == 0:
            if rotation == 1 or rotation == 3:
                if not y == 18:
                    checkcollision = []
                    for i in range(3,-1,-1):
                        for o in range(2,3):
                            if blockboard[i][o] == 1 and blockboard[i+1][o]==" ":
                                checkcollision.append([i+y,o+x])
                    for i in range(0,len(checkcollision)):
                        if placeboard[checkcollision[i][0]+1][checkcollision[i][1]] == 1:
                            placedpiece = 1
                            for i in range(0, len(pieces[placepiece][rotation])):
                                for o in range(0, len(pieces[placepiece][rotation])):
                                    if blockboard[i][o] == 1:
                                        placeboard[i+y][o+x]=blockboard[i][o]
                            break
                        else:
                            checkpiece += 1
                    if checkpiece == len(checkcollision):
                        y+=1
            else:
                if not y == 19:
                    if placeboard[y+4][x] == 0 and placeboard[y+4][x+1] == 0 and placeboard[y+4][x+2] == 0 and placeboard[y+4][x+3] == 0:
                        y += 1
        elif not y == 20:
            y += 1
    elif move == "d":
        checkcollision = []
        checkpiece = 0
        for i in range(0,len(blockboard)):
            for o in range(len(blockboard)-1, -1, -1):
                   if blockboard[o][i] == 1:
                    checkpiece += 1
            if checkpiece != 0:
                if x-i == 8 and placepiece == 1:
                    pass
                elif x-i == 6 and placepiece == 0:
                    pass
                elif not (blockboard[0][2] == 1 or blockboard[1][2] == 1 or blockboard[2][2] == 1) and x == 8:
                        pass
                elif x-1 == 6 and (blockboard[0][2] == 1 or blockboard[1][2] == 1 or blockboard[2][2] == 1):
                    pass
                else:
                    checkpiece = 0
                    for i in range(len(blockboard)-1,-1,-1):
                        for o in range(0,len(blockboard)):
                            try:
                                if blockboard[o][i] == 1 and blockboard[o][i+1]==" ":
                                    checkcollision.append([o+y,i+x])
                            except:
                                checkcollision.append([o+y,i+x])
                    for i in range(0,len(checkcollision)):
                        if placeboard[checkcollision[i][0]+1][checkcollision[i][1]+1]==1:
                            checkpiece += 1
                            break
                    if checkpiece == 0:
                        x+=1
                break
    elif move == "w":
        checkpiece = 0
        if placepiece == 0:
            if rotation == 3:
                for i in range(0, len(blockboard)):
                    for o in range(0, len(blockboard)):
                        if pieces[placepiece][0][i][o] == 1 and placeboard[i+y][o+x] == 1:
                            checkpiece += 1
                            break
                if checkpiece == 0:
                    rotation = 0
            else:
                for i in range(0, len(blockboard)):
                    for o in range(0, len(blockboard)):
                        if pieces[placepiece][rotation][i][o] == 1 and placeboard[i+y][o+x] == 1:
                            checkpiece += 1
                            break
                if checkpiece == 0:
                    rotation += 1
        else:
            if rotation == 3:
                for i in range(0, 3):
                    for o in range(0, 3):
                        if pieces[placepiece][0][i][o] == 1 and placeboard[i+y][o+x] == 1:
                            checkpiece += 1
                            break
                if checkpiece == 0:
                    rotation = 0
            else:
                for i in range(0, 3):
                    for o in range(0, 3):
                        if pieces[placepiece][rotation][i][o] == 1 and placeboard[i+y][o+x] == 1:
                            checkpiece += 1
                            break
                if checkpiece == 0:
                    rotation += 1
    checkpiece = 0
    if placepiece != 0:
        if not y == 19:
            checkcollision = []
            for i in range(2,-1,-1):
                for o in range(0,3):
                    if blockboard[i][o] == 1 and blockboard[i+1][o]==" ":
                        checkcollision.append([i+y,o+x])
            for i in range(0,len(checkcollision)):
                if placeboard[checkcollision[i][0]+1][checkcollision[i][1]] == 1:
                    placedpiece = 1
                    for i in range(0, len(pieces[placepiece][rotation])):
                        for o in range(0, len(pieces[placepiece][rotation])):
                            if blockboard[i][o] == 1:
                                placeboard[i+y][o+x]=blockboard[i][o]
                    break
                else:
                    checkpiece += 1
            if checkpiece == len(checkcollision):
                y+=1
    elif placepiece == 0:
        if rotation == 1 or rotation == 3:
            if not y == 18:
                y += 1
        else:
            if not y == 19:
                y += 1
    elif not y == 20:
        y += 1
    #collision for line piece
    if placepiece == 0:
        if rotation == 1 or rotation == 3:
            if y == 18:
                placedpiece = 1
                for i in range(0, len(pieces[placepiece][rotation])):
                    for o in range(0, len(pieces[placepiece][rotation])):
                        if blockboard[i][o] == 1:
                            placeboard[i+y][o+x]=blockboard[i][o]
            elif placeboard[y+4][x+2] == 1:
                placedpiece = 1
                for i in range(0, len(pieces[placepiece][rotation])):
                    for o in range(0, len(pieces[placepiece][rotation])):
                        if blockboard[i][o] == 1:
                            placeboard[i+y][o+x]=blockboard[i][o]
        elif y == 19:
            newpiece = 1 
        elif placeboard[y+3][x] == 1 or placeboard[y+3][x+1] == 1 or placeboard[y+3][x+2] == 1 or placeboard[y+3][x+3] == 1:
            newpiece = 1 
        else:
            placedpiece = 0
    #bottom block collision
    elif blockboard[2][2] == " " and blockboard[2][1] == " " and blockboard[2][0] == " ":
        if y == 19:
            y+=1
            newpiece = 1
        elif placeboard[y+2][x] == 1 or placeboard[y+2][x+1] == 1 or placeboard[y+2][x+2] == 1:
            newpiece = 1
        else:
            placedpiece = 0
    elif y == 19 or y == 20:
        placedpiece = 1
        for i in range(0, len(pieces[placepiece][rotation])):
            for o in range(0, len(pieces[placepiece][rotation])):
                if blockboard[i][o] == 1:
                    placeboard[i+y][o+x]=blockboard[i][o]
    else:
        try:
            checkcollision = []
            for i in range(2,-1,-1):
                for o in range(0,3):
                    if blockboard[i][o] == 1 and blockboard[i+1][o]==" ":
                        checkcollision.append([i+y,o+x])
            for i in range(0,len(checkcollision)):
                if placeboard[checkcollision[i][0]+1][checkcollision[i][1]] == 1:
                    placedpiece = 1
                    for i in range(0, len(pieces[placepiece][rotation])):
                        for o in range(0, len(pieces[placepiece][rotation])):
                            if blockboard[i][o] == 1:
                                placeboard[i+y][o+x]=blockboard[i][o]
                    break
                else:
                    placedpiece = 0
        except:
            newpiece = 1
    line = clearlines(lines)
    if line == 1:
        score += 40 * (level + 1)
    elif line == 2:
        score += 100 * (level + 1)
    elif line == 3:
        score += 300 * (level + 1)
    elif line == 4:
        score += 1200 * (level + 1)
    lines += line
    level = math.floor(lines/10)
    for i in range(0, len(placeboard)):
        for o in range(0,len(placeboard[i])):
            if placeboard[i][o] == 0:
                board[i-1][o] = " "
            else:
                board[i-1][o] = placeboard[i][o]
    if 1 in placeboard[2]:
        lose = 1