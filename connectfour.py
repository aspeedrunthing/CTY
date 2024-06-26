import math 
def printboard():
    i=6
    o=1
    print("   1  2  3  4  5  6  7")
    while i>0:
        i-=1
        print(o,board[i])
        o+=1  
board = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]     
x = -1
player = 2
changeplayer = 1
win = 0
printboard()
while win == 0:
    if changeplayer == 1:
        if player == 1:
            player +=1
        else:
            player -= 1
    changeplayer = 1   
    x = (input("choose your spot 1-7: "))
    if not x.isdigit():
        printboard()
        changeplayer = 0
        continue
    if int(math.ceil(float(x)))>8 or int(math.ceil(float(x)))<1:
        print("no")
        changeplayer = 0
        printboard()
        continue
    o=0
    while o<6:
        if board[o][int(math.ceil(float(x)))-1]>0:
            o+=1
        else:
            board[o][int(math.ceil(float(x)))-1] +=player
            break
        if o>5:
            print("no")
            changeplayer = 0
    printboard()
    for i in range(0, 6):
        for t in range(0, 4):
            if board[i][t] == board[i][t+1] == board[i][t+2] == board[i][t+3] !=0:
                win += 1
                print("Player ", board[i][t+3], "has won")
                break
    for i in range(0, 3):
        for t in range(0, 6):
            if board[i][t] == board[i+1][t] == board[i+2][t] == board[i+3][t] !=0:
                win += 1
                print("Player ", board[i][t], "has won")
                break
    for i in range(0, 3):
        for t in range(0, 4):
            if board[i][t] == board[i+1][t+1] == board[i+2][t+2] == board[i+3][t+3] !=0:
                win += 1
                print("Player ", board[i][t], "has won")
                break
    for i in range(0, 3):
        for t in range(0, 4):
            if board[i][t+3] == board[i+1][t+2] == board[i+2][t+1] == board[i+3][t] !=0:
                win += 1
                print("Player ", board[i][t+3], "has won")
                break