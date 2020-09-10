import random

N_CITIES = 10
cities = []

class City:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.number = num
        
    def display(self):
        fill(0, 255, 255)
        ellipse(self.x, self.y, 10, 10)
        noFill()
        textSize(20)
        text(self.number, self.x - 10, self.y - 10)
        
        
class Route:
    def __init__(self):
        self.distance = 0
        self.cityNums = random.sample(list(range(N_CITIES)), N_CITIES)
        
    def display(self):
        strokeWeight(3)
        stroke(255, 0, 255)
        beginShape()
        for i in self.cityNums:
            vertex(cities[i].x, cities[i].y)
            cities[i].display()
        endShape(CLOSE)
    
    def calcLength(self):
        self.distance = 0
        for i, num in enumerate(self.cityNums):
            self.distance += dist(cities[num].x,
                                  cities[num].y,
                                  cities[self.cityNums[i - 1]].x,
                                  cities[self.cityNums[i - 1]].y)
        return self.distance
    
random_improvements = 0
mutated_improvements = 0
    
def setup():
    global best, record_distance
    size(600, 600)
    for i in range(N_CITIES):
        cities.append(City(random.randint(50, width-50),
                           random.randint(50, height-50), i))
    best = Route()
    record_distance = best.calcLength()
    
def draw():
    global best, record_distance, random_improvements
    background(0)
    best.display()
    println(record_distance)
    println("random: "+str(random_improvements))
    route1 = Route()
    length1 = route1.calcLength()
    if length1 < record_distance:
        record_distance = length1
        best = route1
        random_improvements += 1
