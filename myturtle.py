from turtle import *
shape("turtle")
speed(0.5)

def polygon(side_num, side_length=100, degrees=None):
    for _ in range(side_num):
        fd(side_length)
        right(degrees if degrees else 360 / side_num)

l = 5
for _ in range(60):
    polygon(4, l, 144)
    rt(5)
    l += 5
