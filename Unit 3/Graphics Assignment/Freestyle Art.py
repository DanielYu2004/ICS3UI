from tkinter import *
import time
import random
import math
tk = Tk()


width = 800
height = 700

screen = Canvas(tk, width=width, height=height, background="#A8B8E8")
screen.pack()


#WALl
screen.create_rectangle(0,0,600, 700, fill="#D3DEFF")


#WINDOW
screen.create_rectangle(100,50, 400, 300, fill="light blue")
screen.create_rectangle(100,165, 400, 185, fill="white")
screen.create_rectangle(240,50, 260, 300, fill="white")


#LEGS
screen.create_rectangle(35, 550, 75, 700, fill="dark grey")
screen.create_rectangle(25, 550, 35, 700, fill="#2D3030")

screen.create_rectangle(75, 550, 125, 700, fill="dark grey")
screen.create_rectangle(65, 550, 75, 700, fill="#2D3030")

screen.create_rectangle(75 + 600, 550, 125 + 600, 700, fill="dark grey")
screen.create_rectangle(65 + 600, 550, 75 + 600, 700, fill="#2D3030")

screen.create_rectangle(75 + 525, 550, 115 + 525, 700, fill="dark grey")
screen.create_rectangle(65 + 525, 550, 75 + 525, 700, fill="#2D3030")



#DESK
screen.create_rectangle(0 + 50,575, width-50,height-150 + 25+ 25, fill="#b5651d")
screen.create_polygon(0 + 50, 525+ 25+ 25, 0 + 50, 550+ 25+ 25, 0, height-250+ 25+ 25, 0 , height - 275+ 25+ 25, fill="#844F15", outline="black")
screen.create_polygon(0 + 50, 525+ 25+ 25, 0, height - 275+ 25+ 25, width - 100 - 25, height - 275+ 25+ 25, width - 50, height-175+ 25+ 25, fill="#F49F40", outline="black")







screen.mainloop()