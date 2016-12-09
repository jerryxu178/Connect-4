import sys
import numpy as np
import opponent

class Connect4Cells(object):
    def __init__(self, rows = 6, columns=7, numcolors = 3):
        self._rowCounts = rows
        self._numColors = numcolors
        self._columnCounts = columns
        self._connects = 4
        self._cells = np.zeros((rows, columns)).astype(int)
        # for i in range(rows):
        #     self._cells.append([])
        #     for j in range(columns):
        #         self._cells[i].append(0)
        self.ai = opponent.opponent(self)

    def prettyprint(self):
        for i in range(self._rowCounts):
            sys.stdout.write("|")
            for j in range(self._columnCounts):
                sys.stdout.write(" " + str(self._cells[i][j]) + " |")
            sys.stdout.write("\n")
        sys.stdout.flush()

    def _testMove(self, column, cellstate, player):
        """
        R
        :param column:
        :param cellstate:
        :param player:
        :return: a tuple of (won, valid), where won represents if this move won the game, and valid represents if the move is valid!
        """
        if self._checkColumn(column, cellstate):
            row = self._getFirstEmptyCell(column, cellstate)
            cellstate[row][column] = player
            won = self._isWin(row, column, player, cellstate)
            return (won, cellstate, False)
        return (False, cellstate, True)

    def _isWin(self, row, column, player, cellstate):
        # Check horizontal and vertical and diagonal up/down:
        foundLineHorizontal = 0
        foundLineVertical = 0
        foundLineDiagonalDown = 0
        foundLineDiagonalUp = 0
        for i in range(-self._connects/2+1, self._connects/2+1):

            if 0 <= row + i < self._rowCounts and cellstate[row+i][column] == player:
                foundLineHorizontal += 1
            else:
                foundLineHorizontal = 0

            if 0 <= column + i < self._columnCounts and cellstate[row][column + i] == player:
                foundLineVertical += 1
            else:
                foundLineVertical = 0

            if 0 <= column + i < self._columnCounts and 0 <= row + i < self._rowCounts and cellstate[row + i][column + i] == player:
                foundLineDiagonalUp += 1
            else:
                foundLineDiagonalUp = 0

            if 0 <= column + i < self._columnCounts and 0 <= row - i < self._rowCounts and cellstate[row - i][column + i] == player:
                foundLineDiagonalDown += 1
            else:
                foundLineDiagonalDown = 0

            if foundLineHorizontal == self._connects or foundLineVertical == self._connects or foundLineDiagonalDown == self._connects or foundLineDiagonalUp == self._connects:
                return True

        if foundLineHorizontal == self._connects or foundLineVertical == self._connects or foundLineDiagonalDown == self._connects or foundLineDiagonalUp == self._connects:
            return True

        return False

    def _getConsecutiveCounts(self, player, cellstate):
        allcounts = [0] * self._rowCounts

        for i in range(self._rowCounts):
            count = 0
            for j in range(self._columnCounts):
                if cellstate[i][j] == player:
                    count += 1
                elif count != 0:
 #                   print("Found in rows a consecutive of length " + str(count) + " on row " + str(i))
                    allcounts[count] += 1
                    count = 0
            if count != 0:
#                print("Found in rows a consecutive of length " + str(count) + " on row " + str(i))
                allcounts[count] += 1
                count = 0

        for i in range(self._columnCounts):
            count = 0
            for j in range(self._rowCounts):
                if cellstate[j][i] == player:
                    count += 1
                elif count != 0:
                    allcounts[count] += 1
                    count = 0
            if count != 0:
                allcounts[count] += 1
                count = 0

        for i in range(self._rowCounts):
            count = 0
            j = 0
            while i < self._rowCounts and j < self._columnCounts:
                if cellstate[i][j] == player:
                    count += 1
                elif count != 0:
                    allcounts[count] += 1
                    count = 0
                i += 1
                j += 1
            if count != 0:
                allcounts[count] += 1
                count = 0

        for i in range(self._rowCounts):
            count = 0
            j = 0
            while i < self._rowCounts and j < self._columnCounts:
                if cellstate[i][j] == player:
                    count += 1
                elif count != 0:
                    allcounts[count] += 1
                    count = 0
                i -= 1
                j += 1
            if count != 0:
                allcounts[count] += 1
                count = 0

        return allcounts

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
        for i in range(self._rowCounts):
            if cellstate[i][columnIndex] == 0:
                return True
        return False

    def getFirstEmptyCell(self, columnIndex):
        return self._getFirstEmptyCell(columnIndex, self._cells)

    def _getFirstEmptyCell(self, columnIndex, cellstate):
        k = self._rowCounts - 1
        while k >= 0 and cellstate[k][columnIndex] != 0:
            k -= 1
        return k

    def clickAt(self, columnIndex, player):


        row = self.getFirstEmptyCell(columnIndex)

        if row < 0:
           return False

        #print("Clicked column c" + str(columnIndex) + " and adding to row " + str(row) + " for player " + str(player))
        self._cells[row][columnIndex] = player
        self.checkWin(player)  # CURRENTLY CHECK FOR WINS HERE
        return True

    def getCellNumber(self,rowIndex,columnIndex):
        return self._cells[rowIndex][columnIndex]

    def checkWin(self, player):
        counts = self._getConsecutiveCounts(player, self._cells)
        #print(counts)
        if counts[4] > 0:
            print("Player WON!")
            return True