def setup():
    size(600,600)
    fill(150,0,150) #purple
    noStroke()

def draw():
    background(255)
    translate(50,50)
    level = int(map(mouseX,0,width,0,7))
    squareFractal(500,level)
    
def squareFractal(sz,level):
    if level == 0:
        rect(0,0,sz,sz)
    else:
        pushMatrix()
        squareFractal(sz/2.0, level - 1)
        translate(sz/2.0,0)
        squareFractal(sz/2.0, level - 1)
        translate(-sz/2.0,sz/2.0)
        squareFractal(sz/2.0, level - 1)
        popMatrix()
