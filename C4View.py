from C4Model import C4Model
from Tkinter import *

class C4View(object):

    COLORS = ["White", "Red", "Yellow"]

    def __init__(self,rows = 6, columns = 7):
        self.cells = C4Model(rows, columns, 3)
        self.rows = rows
        self.columns = columns
        self.atRow = 0
        self.atColumn = 0
        self.root = Tk()
        #self.root.minsize(500,520)
        #self.root.geometry("500x500")
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

    def makeMove(self, x, y):
        self.buttons[x][y].configure(bg=C4View.COLORS[1])

    def clicked(self, rowIndex, columnIndex):
        self.atRow = rowIndex
        self.atColumn = columnIndex
        (valid, gameOverState) = self.cells.clickAt(self.atColumn,self.player)

        if valid == False:
            print("Invalid move!")

        if gameOverState != None:
            print("GAME OVER - PLAYER 1 WON IS " + str(gameOverState))

        self.colorButtons()

    def colorButtons(self):
        for i in range(self.rows):
            for j in range(self.columns):
                #print("Updating i=" + str(i) + "and j=" + str(j) + " and c " + Connect4Frame.COLORS[self.cells.getCellNumber(i,j)])
                self.buttons[i][j].configure(bg=C4View.COLORS[self.cells.getCellNumber(i, j)])
        self.cells.prettyprint()

    def mainloop(self):
        self.root.mainloop()

w = C4View()
w.mainloop()