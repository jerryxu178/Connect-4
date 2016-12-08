class Connect4Cells(object):
    def __init__(self, rows = 7, columns=6, numcolors = 3):
        self._rowCounts = rows
        self._numColors = numcolors
        self._columnCounts = columns
        self._cells = []
        for i in range(rows):
            self._cells.append([])
            for j in range(columns):
                self._cells[i].append(0)

    def _makeMove(self, column, cellstate, player):
        """
        R
        :param column:
        :param cellstate:
        :param player:
        :return: a tuple of (won, valid), where won represents if this move won the game, and valid represents if the move is valid!
        """
        if self._checkColumn(self, column, cellstate):
            row = self._getFirstEmptyCell(column, cellstate)
            cellstate[column][row] = player
            won = self._isWin(row, column, cellstate)
            return (won, cellstate)
        return (False, False)

    def checkRow(self, rowIndex):
        self._checkRow(rowIndex, self._cells)

    def _checkRow(self, rowIndex, cellstate):
        for j in range(self.columns):
            if cellstate[rowIndex][j] == 0:
                return True
        return False

    def checkColumn(self, columnIndex):
        self._checkColumn(columnIndex, self._cells)

    def _checkColumn(self, columnIndex, cellstate):
        for i in range(self.rows):
            if cellstate[i][columnIndex] == 0:
                return True
        return False
    def getFirstEmptyCell(self, columnIndex):
        self._getFirstEmptyCell(columnIndex, self._cells)

    def _getFirstEmptyCell(self, columnIndex, cellstate):
        k = self._rowCounts - 1
        while cellstate[k][columnIndex] != 0:
            k -= 1
        return k

    def clickAt(self, columnIndex, player):
        self.checkWin()
        row = self.getFirstEmptyCell(columnIndex)
        if row < 0:
            return False
        self._cells[row][columnIndex] = player
        return True
    def getCellNumber(self,rowIndex,columnIndex):
        return self._cells[rowIndex][columnIndex]

    def checkWin(self, rowIndex,columnIndex,player):
        for i in range(self.columns):
            for j in range(self.rows):
                if self._cells[i][j] == self._cells[i+j] == self._cells[i+3][j] == self._cells[i][j+3] == player:
                    if player == 1:
                        print "player 1 wins"
                    else:
                        print "player 2 wins"