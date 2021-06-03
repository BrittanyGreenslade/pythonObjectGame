import gameboard
import player
# from input_exception import InputException

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")
# start with this todo
# TODO
# Create a new GameBoard called board
# creating a gameboard by calling GameBoard fn from gameboard.py
board = gameboard.GameBoard()
# Create a new Player called player starting at position 3,2
# creating a player by calling Player fn from player.py with arguments of
# 3 (intitalRow) and 2 (initialColumn)
player = player.Player(3, 2)

# TODO
# Move the player through the board
while True:
    # try:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # calling checkWin fn to see if the player has won (break loop) or not (continue loop)
    player_win = board.checkWin(player.rowPosition, player.columnPosition)
    no_wall = board.checkMove(player.rowPosition, player.columnPosition)
    # Check if the player has won, if so print a message and break the loop!
    # checks if there's a wall (calls checkMove fn). I can't figure out how to continue the
    # game when no_wall becomes false though.......
    if(player_win == False and no_wall == True):
        if (selection == "w" or selection == "s" or selection == "a" or selection == "d"):
            if(selection == "w"):
                player.moveUp()
            elif(selection == "s"):
                player.moveDown()
            elif(selection == "a"):
                player.moveLeft()
            elif(selection == "d"):
                player.moveRight()
        else:
            print("Please enter a valid selection")
        # elif(selection != "w" or selection != "s" or selection != "a" or selection != "d"):
        #     print("Please enter a valid move")
    elif(player_win == True):
        print("You did it!")
        break
    # except InputException:
    #     print("Stay in the borders")
