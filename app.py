import gameboard
import player
from input_exception import InputException

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
    try:
        board.printBoard(player.rowPosition, player.columnPosition)
        selection = input("Make a move: ")
        # calling checkWin fn to see if the player has won (break loop) or not (continue loop)
        player_win = board.checkWin(player.rowPosition, player.columnPosition)
        # Check if the player has won, if so print a message and break the loop!
        if(player_win == False):
            if (selection == "w" or selection == "s" or selection == "a" or selection == "d"):
                # checks if there's a wall (calls checkMove fn) for the spot one spot away
                # from user current spot (i.e. the spot they're trying to move to)
                if(selection == "w" and board.checkMove(player.rowPosition - 1, player.columnPosition)):
                    player.moveUp()
                elif(selection == "s" and board.checkMove(player.rowPosition + 1, player.columnPosition)):
                    player.moveDown()
                elif(selection == "a" and board.checkMove(player.rowPosition, player.columnPosition-1)):
                    player.moveLeft()
                elif(selection == "d" and board.checkMove(player.rowPosition, player.columnPosition+1)):
                    player.moveRight()
            else:
                # "raising" custom exception if an invalid input happens
                raise InputException()
        elif(player_win == True):
            print("You did it!")
# break stops the "true" infinite loop from happening if there's no error caught and try completes
            break
# telling user to input another selection. b/c "while True", try will happen again (infinite loop)
    except InputException:
        print("Invalid selection")
