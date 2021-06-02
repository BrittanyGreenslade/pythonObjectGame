from player import Player
from gameboard import GameBoard
import gameboard
import player

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
# Create a new Player called player starting at position 3,2
# creating a gameboard by calling GameBoard fn from gameboard.py
board = GameBoard()

# creating a player by calling Player fn from player.py with arguments of
#3 (intitalRow) and 2 (initialColumn)
player = Player(3, 2)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    if(selection == "w"):
        player.moveUp()
    elif(selection == "s"):
        player.moveDown()
    elif(selection == "a"):
        player.moveLeft()
    elif(selection == "d"):
        player.moveRight()
# when we do these todos, we'll figure out which fn is next
# TODO
# Move the player through the board
# Check if the player has won, if so print a message and break the loop!
