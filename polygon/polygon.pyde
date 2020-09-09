def setup():
    size(600,600)

def draw():
    translate(width/2,height/2)
    polygon(360,100) #3 sides, vertices 100 units from the center

def polygon(sides,sz):
    beginShape()
    step = radians(360/sides)
    for i in range(sides):
        vertex(sz*cos(i * step), sz*sin(i * step))
    endShape(CLOSE)
