print("Choose your game")
print("1: Connect Four")
print("2: Make Your Own Choose Your Own Adventure Game")
print("3: Minesweeper")
print("4: Tic Tac Toe")
game = 0
while game != 1 and game != 2 and game != 3 and game != 4:
    game = (input(""))
    if game.isdigit():
        game = int(game)
    if game != 1 and game != 2 and game != 3 and game != 4:
        print("Choose a valid option")
if game == 1:
    import connectfour
if game == 2:
    import makeyourownadventure
if game == 3:
    import minesweeper
if game == 4:
    import tictactoe
