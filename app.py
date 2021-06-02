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
# Create a new Player called Player starting at position 3,2

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # when we do these todos, we'll figure out which fn is next
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
