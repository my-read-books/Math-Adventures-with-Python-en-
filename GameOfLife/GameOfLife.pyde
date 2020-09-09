from random import choice
GRID_W = 51
GRID_H = 51

SZ = 18

generation = 0

class Cell:
    def __init__(self, c, r, state=0):
        self.c = c
        self.r = r
        self.state = state
        
    def display(self):
        if self.state == 1:
            fill(0)
        else:
            fill(255)
        rect(SZ*self.r,SZ*self.c,SZ,SZ)
        
    def checkNeighbors(self):
        neighbs = 0
        for dr, dc in [[-1,-1],[-1,0],[-1,1],[1,0],[1,-1],[1,1],[0,-1],[0,1]]:
            try:
                if cellList[self.r+dr][self.c+dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if self.state == 1:
            if neighbs in [2, 3]:
                return 1
            return 0
        if neighbs == 3:
            return 1
        return 0    
        

def setup():
    global SZ, cellList
    size(600, 600)
    SZ = width // GRID_W + 1
    cellList = createCellList()
    
def draw():
    global cellList
    frameRate(10)
    cellList = update(cellList)
    for row in cellList:
        for cell in row:
            cell.display()


def update(cellList):
    newList = []
    for r, row in enumerate(cellList):
        newList.append([])
        for c, cell in enumerate(row):
            newList[r].append(Cell(c, r, cell.checkNeighbors()))
    return newList[::]

def createCellList():
    '''Creates a big list of off cells with
    one on Cell in the center'''
    newList=[]#empty list for cells
    #populate the initial cell list
    for j in range(GRID_H):
        newList.append([]) #add empty row
        for i in range(GRID_W):
            newList[j].append(Cell(i,j,choice([0, 1]))) #add off Cells or zeroes
    #center cell is set to on
    newList[GRID_H//2][GRID_W//2].state = 1
    return newList
