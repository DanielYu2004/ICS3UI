from tkinter import *
import time
import random
import math
tk = Tk()


width = 800
height = 700

screen = Canvas(tk, width=width, height=height, background="#A8B8E8")
screen.pack()






#Road

screen.create_rectangle(0, 500, 800, 700, fill="grey", outline="black")

lines = random.randint(6, 18)
lineWidth = random.randint(40, 100)
lineHeight = random.randint(10,20)
space = width/(lines-1)

for line in range(lines):
    screen.create_rectangle((space+lineWidth)*line, 600 - lineHeight/2, (space+lineWidth)*line + lineWidth, 600 + lineHeight/2, fill="white")

#Clouds

numClouds = random.randint(4,5)

for cloud in range(numClouds):
    clouds = random.randint(8,15)

    x1 = random.randint(0,width)
    y1 = random.randint(0, 350 - 200)
    #screen.create_rectangle(x1,y1, x1 + 100, y1 + 100, fill="blue")

    for circle in range(clouds):
        cloudSize = random.randint(80,100)
        cloudx1 = random.randint(x1, x1+50) 
        cloudy1 = random.randint(y1, y1+50)
        screen.create_oval(cloudx1, cloudy1, cloudx1+ random.randint(cloudSize-20, cloudSize+20), cloudy1 + random.randint(cloudSize-20, cloudSize+20), fill="white", outline="white")




#Grass

screen.create_rectangle(0, 350, 800, 500, fill="green")


for grass in range(2000):
    grassWidth = random.randint(4,8)
    grassHeight = random.randint(10,15)
    x1 = random.randint(0,800-grassWidth)
    y1 = random.randint(350-grassHeight,500-grassHeight)
    colours = ["green", "#209145", "#5DBF7E"]

    screen.create_rectangle(x1,y1, x1 + grassWidth, y1 + grassHeight, fill=colours[random.randint(0,2)])















"""
#WALL
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

"""





screen.mainloop()