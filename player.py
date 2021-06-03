class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # TODO
    def moveUp(self):
        self.rowPosition -= 1

    # TODO
    def moveDown(self):
        self.rowPosition += 1
        # move down is add because nums get bigger (think: table rows)
    # TODO

    def moveLeft(self):
        self.columnPosition -= 1

    # TODO
    def moveRight(self):
        self.columnPosition += 1
