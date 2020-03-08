from tkinter import *
import time
import random
import math
tk = Tk()


width = 800
height = 700

screen = Canvas(tk, width=width, height=height, background="light grey")
screen.pack()


#DESK
screen.create_rectangle(0 + 50,525, width-50,height-150, fill="#b5651d")
screen.create_polygon(0 + 50, 525, 0 + 50, 550, 0, height-250, 0 , height - 275, fill="#844F15", outline="black")
screen.create_polygon(0 + 50, 525, 0, height - 275, width - 100 - 25, height - 275, width - 50, height-175, fill="#F49F40", outline="black")
screen.create_rectangle(75, 550, 125, 700, fill="dark grey")
#screen.create_re





#Grid lines
spacing = 50

for x in range(0, 1000, spacing): 
    screen.create_line(x, 25, x, 1000, fill="blue")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    screen.create_line(25, y, 1000, y, fill="blue")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)

screen.update()



screen.mainloop()