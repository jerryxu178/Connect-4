from connect4cell2 import Connect4Cells
from Tkinter import *
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
                btn = Button(self.root,command=lambda x=i,y=j:self.clicked(x,y),\
                    borderwidth=2,padx=30,pady=20)
                btn.grid(row=i,column=j)
                self.buttons[i].append(btn)
        self.colorButtons()
    def clicked(self, rowIndex, columnIndex):
        self.atRow = rowIndex
        self.atColumn = columnIndex
        result = self.cells.clickAt(self.atColumn,self.player)
        if result:
            self.player = 3 - self.player
        self.colorButtons()
    def colorButtons(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.buttons[i][j].configure(bg=Connect4Frame.COLORS[self.cells.getCellNumber(i,j)])
    def mainloop(self):
        self.root.mainloop()
w = Connect4Frame()
w.mainloop()