ballList = []


class Ball:
    
    def __init__(self, x, y):
        self.xcor = x
        self.ycor = y
        self.xvel = random(-2, 2)
        self.yvel = random(-2, 2)
        self.radius = random(5, 50)
        self.col = color(random(255),
                         random(255),
                         random(255))
    
    def update(self):
        self.xcor += self.xvel
        self.ycor += self.yvel
        if self.xcor + self.radius/2 > width or self.xcor - self.radius/2 < 0:
            self.xvel = -self.xvel
        if self.ycor + self.radius/2 > height or self.ycor - self.radius/2< 0:
            self.yvel = -self.yvel
        fill(self.col)
        ellipse(self.xcor, self.ycor, self.radius, self.radius)
   
        
def setup():
    size(600, 600)
    for i in range(100):
        ballList.append(Ball(random(width), random(height)))
    
def draw():
    background(0)
    for ball in ballList:
        ball.update()
