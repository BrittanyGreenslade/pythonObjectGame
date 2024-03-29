class GameBoard:
    def __init__(self):
        self.winningRow = 0
        self.winningColumn = 2
        # this is how the borders print out to the screen - not scary! boundaries of game
        self.board = [
            [" * ", " * ", "   ", " * ", " * ", " * "],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                " * ",
                " * ",
            ],
            [
                " * ",
                "   ",
                " * ",
                " * ",
                "   ",
                " * ",
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [" * ", " * ", " * ", " * ", " * ", " * "],
        ]

    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print(" P ", end="")
                else:
                    print(self.board[i][j], end="")
            print("")
# if find 'finds' nothing, it's = -1: so, if finds *, return false

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    # TODO

    # Return True if the player is in the winning column and row
    # Return False otherwise
    def checkWin(self, playerRow, playerColumn):
        if(playerRow == 0 and playerColumn == 2):
            return True
        else:
            return False
