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
    def checkRow(self, rowIndex):
        for j in range(self.columns):
            if self._cells[rowIndex][j] == 0:
                return True
        return False
    def checkColumn(self, columnIndex):
        for i in range(self.rows):
            if self._cells[i][columnIndex] == 0:
                return True
        return False
    def getFirstEmptyCell(self, columnIndex):
        k = self._rowCounts - 1
        while self._cells[k][columnIndex] != 0:
            k -= 1
        return k
    def clickAt(self, columnIndex, player):
        self.checkWin() # CURRENTLY CHECK FOR WINS HERE 
        row = self.getFirstEmptyCell(columnIndex)
        if self.checkWin():
            return 123
        if row < 0:
            return False
        self._cells[row][columnIndex] = player
        return True
    def getCellNumber(self,rowIndex,columnIndex):
        return self._cells[rowIndex][columnIndex]

    def checkWin(self):
        #print self._cells
        if self._cells[5][1] != 0:
            print "winner"
            return True




    def checkWin_OLD(self, rowIndex,columnIndex,player):
        for i in range(self.columns):
            for j in range(self.rows):
                if self._cells[i][j] == self._cells[i+j] == self._cells[i+3][j] == self._cells[i][j+3] == player:
                    if player == 1:
                        print "player 1 wins"
                    else:
                        print "player 2 wins"