board = [[" "," ","#","#","#","#","#"," "],["#","#","#"," "," "," ","#"," "],["#","&"," "," "," "," ","#"," "],["#","#","#"," "," "," ","#"," "],["#"," ","#","#"," "," ","#"," "],["#"," ","#"," "," "," ","#","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#","#","#","#","#","#","#","#"]]
coinboard = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,"*",0,0,0,0,0,0], [0,0,0,0,0,"*",0,0], [0,"*",0,0,0,0,0,0], [0,0,0,0,"*",0,0,0], [0,0,0,"*",0,0,"*",0], [0,0,0,0,"*",0,0,0], [0,0,0,0,0,0,0,0]]
boxboard = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,"b",0,0,0], [0,0,0,0,"b",0,0,0], [0,0,0,0,"b",0,0,0], [0,0,0,0,0,0,0,0], [0,"b",0,"b",0,"b",0,0], [0,0,0,0,"b",0,0,0], [0,0,0,0,0,0,0,0]]
def printboard():
    touchingbomb = 0
    for i in range(9):
        for o in range(8):
            if (boxboard[i][o] == "b" or boxboard[i][o] == "B") and coinboard[i][o] == "*":
                touchingbomb += 1
                boxboard[i][o] = "B"
            if boxboard[i][o] == "b":
                print("b", end=" ")
            elif boxboard[i][o] == "B":
                print("B", end=" ")
            elif coinboard[i][o] == "*" and (not playerlocation[0] == i or not playerlocation[1] == o):
                print("*", end=" ")
            elif o == 7:
                print(board[i][o])
            else:
                print(board[i][o], end=" ")
    return touchingbomb
def movebox(movey, movex):
    if not movex == 0:
        if boxboard[playerlocation[0]][playerlocation[1] + movex] != 0:
            if board[playerlocation[0]][playerlocation[1]+ (movex * 2)] == "#":
                return False
            elif boxboard[playerlocation[0]][playerlocation[1]+ (movex * 2)] == "b" or boxboard[playerlocation[0]][playerlocation[1]+ (movex * 2)] == "B":
                return False
            else:
                boxboard[playerlocation[0]][playerlocation[1] + movex] = 0
                boxboard[playerlocation[0]][playerlocation[1] + (movex * 2)] = "b"
                return True
        else:
            return True
    if not movey == 0:
        if boxboard[playerlocation[0]+movey][playerlocation[1]] != 0:
            if board[playerlocation[0]+ (movey * 2)][playerlocation[1]] == "#":
                return False
            elif boxboard[playerlocation[0]+ (movey * 2)][playerlocation[1]] == "b" or boxboard[playerlocation[0]+ (movey * 2)][playerlocation[1]] == "B":
                return False
            else:
                boxboard[playerlocation[0] + movey][playerlocation[1]] = 0
                boxboard[playerlocation[0] + (movey * 2)][playerlocation[1]] = "b"
                return True
        else:
            return True
playerlocation = [2,1]
touchingbomb = printboard()
win = 0
touchingbomb = 0
while win == 0:
    playinput = input("Press w, a, s, or d")
    if playinput == "w":
        if not board[playerlocation[0]-1][playerlocation[1]] == "#":
            if movebox(-1 , 0):
                board[playerlocation[0]-1][playerlocation[1]] = "&"
                board[playerlocation[0]][playerlocation[1]] = " "
                playerlocation[0] -= 1
    elif playinput == "a":
        if not board[playerlocation[0]][playerlocation[1]-1] == "#":
            if movebox(0, -1):
                board[playerlocation[0]][playerlocation[1]-1] = "&"
                board[playerlocation[0]][playerlocation[1]] = " "
                playerlocation[1] -= 1
    elif playinput == "s":
        if not board[playerlocation[0]+1][playerlocation[1]] == "#":
            if movebox(1, 0):
                board[playerlocation[0]+1][playerlocation[1]] = "&"
                board[playerlocation[0]][playerlocation[1]] = " "
                playerlocation[0] += 1
    elif playinput == "d":
        if not board[playerlocation[0]][playerlocation[1]+1] == "#":
            if movebox(0, 1):
                board[playerlocation[0]][playerlocation[1]+1] = "&"
                board[playerlocation[0]][playerlocation[1]] = " "
                playerlocation[1] += 1
    touchingbomb = printboard()
    if touchingbomb == 7:
        win = 1
print("You Win!")