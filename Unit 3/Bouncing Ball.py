from tkinter import *
from time import *
import random
tk = Tk()
screen = Canvas(tk, width=800, height=700, background="yellow")
screen.pack()

#INITIAL VALUES
diameter = 100

x1 = 100
y1 = 400
x2 = x1 + diameter
y2 = y1 + diameter

xSpeed = 1
ySpeed = 1

#ANIMATION LOOP
while True: 
    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill="red") 

    #Update, sleep, delete
    screen.update()
    sleep(0.009)
    screen.delete( ball )

    #Update positions before the next frame
    x1 = x1 + xSpeed  
    y1 = y1 + ySpeed

    x2 = x1 + diameter
    y2 = y1 + diameter
 
    if x2 >= 800:
        xSpeed = -1 * xSpeed
        xSpeed *= 0.01 * random.randint(100,110)
    if x1 <= 0:
        xSpeed = -1 * xSpeed
        xSpeed *= 0.01 * random.randint(100,110)
    if y1 <= 0:
        ySpeed *= -1
        ySpeed *= 0.01 * random.randint(100,110)

    if y2 >= 700:
        ySpeed *= -1
        ySpeed *= 0.01 * random.randint(100, 110)

screen.mainloop()