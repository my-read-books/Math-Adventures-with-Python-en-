def setup():
    size(600, 600)
    rectMode(CENTER)
    colorMode(HSB)
    
t = 0

def draw():
    background(255)
    global t
    translate(width / 2, height / 2)
    for i in range(90):
        rotate(radians(360/90))
        pushMatrix()
        translate(200, 0)
        rotate(radians(t + 2 * i * 360 / 90))
        stroke(0.3 * (t//360 + 2 * i * 360 / 90), 255, 255)
        tri(100)
        popMatrix()
    t += 0.5
    
def tri(length):
    noFill()
    triangle(0, -length, -length*sqrt(3)/2, length/2,
length*sqrt(3)/2, length/2)
