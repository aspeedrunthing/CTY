import math
def printboard(width):
    for i in range(0,width):
        if i > 9:
            print(end="  ")
            break
        else:
            print(end="   ")
            break
    for i in range(1,width):
        if i-((int(i//9.5)*9)) > 9:
            print((i-((int(i//9.5)*9)))-9, end=" ")
        else:
            print(i-((int(i//9.5)*9)), end=" ")
    print(width)
    for i in range(0,width):
        if i > 8:
            print(i+1, end=" ")
        else:
            print(i+1, end="  ")
        for o in range(0,width):
            if o == width-1:
                print(showboard[i][0])
            else:
                print(showboard[i][0], end=" ")
def makeboard(showboard):
    boardlength = "yes"
    while not boardlength.isdigit():
        boardlength = input("how big do you want the board to be? (x by x)")
        if not boardlength.isdigit():
            print("please input a valid number")
    for i in range(1, int(math.ceil(float(boardlength)))):
        showboard.append([0])
    for i in range(1, int(math.ceil(float(boardlength)))):
        for o in range(1, int(math.ceil(float(boardlength)))):
            showboard[i].append([0])
def fillboard(showboard, fillboard):
    print("yes")
showboard = [[0]]     
hideboard = showboard
makeboard(showboard)
printboard(len(showboard))