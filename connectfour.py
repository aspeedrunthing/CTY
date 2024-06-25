def printboard():
    i=6
    o=1
    print("   1  2  3  4  5  6  7")
    while i>0:
        i-=1
        print(o,board[i])
        o+=1  
board = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
o=0      
x = -1
player = 2
changeplayer = 1
printboard()
while x != 8:
    if changeplayer == 1:
        if player == 1:
            player +=1
        else:
            player -= 1
    changeplayer = 1   
    x = int(input("choose your spot 1-7: "))
    o=0
    while o<6:
        if board[o][x-1]>0:
            o+=1
        else:
            board[o][x-1] +=player
            break
        if o>5:
            print("no")
            changeplayer = 0
    printboard()