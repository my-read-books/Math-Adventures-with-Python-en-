from turtle import *
from random import randint

speed(0)
def wander():
    while True:
        fd(3)
        if xcor() >= 20 or xcor() <= -20 or ycor() <= -20 or ycor() >= 20:
            lt(randint(90, 180))

wander()
