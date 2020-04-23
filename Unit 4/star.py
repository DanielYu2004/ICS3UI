from tkinter import *
from time import *
from random import *
root = Tk()
screen = Canvas( root, width=700, height=700, background = "black" )
screen.pack()

num_rain = 200  
x = []
y = []
rain = []
speed = []

for i in range(num_rain):
    x.append(randint(0, 700))
    y.append(randint(0, 700))
    speed.append(randint(6,10))
    rain.append(0)

for f in range(10000000000000):

    for i in range(num_rain):
        rain[i] = screen.create_line(x[i]-2, y[i]-2, x[i], y[i]+2, fill="blue")
        y[i] = y[i] + speed[i]
        if x[i] < 0:
            x[i] = 800

    screen.update()
    sleep(0.03)

    for i in range(num_rain):
        screen.delete(rain[i])