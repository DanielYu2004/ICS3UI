from tkinter import *
import time
import math
myInterface = Tk()


#Variables
width = 600
height = 600
triLen = 300
x1 = width /2
y1 = (height - (triLen/2 * math.sqrt(3)))/2
x2 = (width -triLen)/2
y2 = (height - (triLen/2 * math.sqrt(3)))/2 + (triLen/2 * math.sqrt(3))
x3 = ((width-triLen)/2) + triLen
y3 = (height - (triLen/2 * math.sqrt(3)))/2 + (triLen/2 * math.sqrt(3))


screen = Canvas(myInterface, width=width, height=height, background="sky blue")
screen.pack()


screen.create_polygon(x1,y1,x2,y2,x3,y3, fill="red")


screen.mainloop()