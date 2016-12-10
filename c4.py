from connect4cell2 import Connect4Cells
from Tkinter import *
import time

class Connect4Frame(object):

    COLORS = ["White", "Red", "Yellow"]

    def __init__(self,rows = 6, columns = 7):
        self.cells = Connect4Cells(rows, columns, 3)
        self.rows = rows
        self.columns = columns
        self.atRow = 0
        self.atColumn = 0
        self.root = Tk()
        self.root.minsize(500,520)
        self.root.geometry("500x520")
        self.root.title("Connect 4")
        self.root.grid()
        self.player = 1
        self.buttons = []
        for i in range(self.rows):
            self.buttons.append([])
            for j in range(self.columns):
                btn = Button(self.root,command=lambda x=i,y=j: self.clicked(x,y),\
                    borderwidth=2,padx=30,pady=20)
                btn.grid(row=i,column=j)
                self.buttons[i].append(btn)
        self.colorButtons()
        self.AI()
    def makeMove(self, x, y):
        self.buttons[x][y].configure(bg=Connect4Frame.COLORS[1])

    def AI(self):
        #print self.cells._cells
        #self.makeMove(5, 1)
        self.player = 2
        move_col = (self.cells.ai.getMove(self.cells._cells, self.player))
        #self.makeMove(5, move_col)
        self.cells.clickAt(move_col, self.player)
        #print(self.cells._cells)
        #self.cells._cells[5][move_col] = 2
        #print(self.cells._cells)
        self.player = 1
        
    def clicked(self, rowIndex, columnIndex):
        self.atRow = rowIndex
        self.atColumn = columnIndex
        result = self.cells.clickAt(self.atColumn,self.player)
        #set result == False to stop alternating players on click
        #if result:
        #   self.player = 3 - self.player
        #else:
        #    print "invalid move"
        self.player = 1
        self.colorButtons()
        # call AI here
        #self.root.after(0, self.AI())
        self.AI()
        #print(self.cells.ai.getMove(self.cells._cells, self.player))

    def colorButtons(self):
        for i in range(self.rows):
            for j in range(self.columns):
                #print("Updating i=" + str(i) + "and j=" + str(j) + " and c " + Connect4Frame.COLORS[self.cells.getCellNumber(i,j)])
                self.buttons[i][j].configure(bg=Connect4Frame.COLORS[self.cells.getCellNumber(i,j)])
        self.cells.prettyprint()

    def mainloop(self):
        self.root.mainloop()


w = Connect4Frame()
w.mainloop()