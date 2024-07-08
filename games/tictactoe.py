import math
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
def printboard(board):
    for i in range(0, 3):
        for o in range(0, 3):
            if o == 2:
                print(board[i][o])
            else:
                print(board[i][o], end =" ")
printboard(board)
win=0
player="x"
changeplayer = 1
turns = 0
while win == 0: 
    if changeplayer == 1:
        if player == "x":
            player = "o"
        else:
            player = "x"
    changeplayer = 1
    location1 = input("put the row you want to go")
    if not location1.isdigit():
        print("choose a valid spot")
        changeplayer = 0
        continue
    location2 = input("put the column you want to go")
    if not location2.isdigit():
        print("choose a valid spot")
        changeplayer = 0
        continue
    board[int(math.ceil(float(location1)))-1][int(math.ceil(float(location2)))-1] = player
    printboard(board)
    turns += 1
    for i in range(0, 2):
            if board[i][0] == board[i][1] == board[i][2] !="_":
                win += 1
                print("Player", board[i][1], "has won")
                break
    for t in range(0, 2):
        if board[0][t] == board[1][t] == board[2][t] !="_":
            win += 1
            print("Player", board[1][t], "has won")
            break
    if board[0][0] == board[1][1] == board[2][2] !="_":
            win += 1
            print("Player", board[1][1], "has won")
            break
    if turns == 9 and win == 0:
        print("The game has ended in a tie. No one wins")
        break
    if board[2][0] == board[1][1] == board[0][2] !="_":
        win += 1
        print("Player", board[1][1], "has won")
        break