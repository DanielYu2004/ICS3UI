from tkinter import *
import time
import random
import math
tk = Tk()

screen = Canvas(tk, width=1000, height=700, background="blue")
screen.pack()

def drawSandBox(background, grain, bound, x1, y1, x2, y2, num):
    screen.create_rectangle(x1,y1,x2,y2, fill=background, outline=bound)
    for f in range(num):
        xg1 = random.randint(x1,x2)
        yg1 = random.randint(y1,y2) 
        screen.create_oval(xg1 - 1, yg1 - 1, xg1 + 1, yg1 + 1, fill=grain)
    screen.update()

drawSandBox("orange", "grey", "red", 200, 100, 530, 430, 2000)

screen.update()


screen.mainloop()