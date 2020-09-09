from random import choice
WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)
colorList = [WHITE,RED,YELLOW,PURPLE]

class Sheep:
    def __init__(self, x, y, col):
        self.x = x
        self.y = y
        self.sz = 10
        self.energy = 20
        self.col = col
        
    def update(self):
        move = 5
        if self.col == PURPLE:
            move = 7
        self.energy -= 1
        if self.energy <= 0:
            sheepList.remove(self)
        if self.energy >= 50:
            self.energy -= 30
            sheepList.append(Sheep(self.x, self.y, self.col))
        self.x += random(-move, move)
        self.y += random(-move, move)
        #"wrap" the world Asteroidsstyle
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        #find the patch of grass you're on in the grassList:
        xscl = int(self.x / patchSize)
        yscl = int(self.y / patchSize)
        grass = grassList[xscl * rows_of_grass + yscl]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
        fill(self.col)
        ellipse(self.x, self.y, self.sz, self.sz)

class Grass:
    def __init__(self, x, y, sz):
        self.x = x
        self.y = y
        self.energy = 3
        self.eaten = False
        self.sz = sz
        
    def update(self):
        if self.eaten:
            if random(100) < 5:
                self.eaten = False
            fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x, self.y, self.sz, self.sz)        
        
sheepList = []
grassList = []
patchSize = 10

def setup():
    global patchSize, rows_of_grass
    rows_of_grass = height / patchSize
    size(600, 600)
    noStroke()
    for i in range(20):
        sheepList.append(Sheep(random(width),
                               random(height),
                               choice(colorList)))
    for x in range(0, width, patchSize):
        for y in range(0, height, patchSize):
            grassList.append(Grass(x, y, patchSize))
    
def draw():
    background(255)
    for grass in grassList:
        grass.update()
    for sheep in sheepList:
        sheep.update()
