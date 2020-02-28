from turtle import *

turtle = Pen()

turtle.speed(20)
turtle.shape("turtle")
turtle.color("blue")
turtle.width("3")

dist = 1
for i in range(1000):
    turtle.forward(dist)
    turtle.right(40)
    if i % 10 == 0:
        dist+=5
