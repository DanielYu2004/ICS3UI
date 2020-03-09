from tkinter import *
import time
import random
import math
tk = Tk()


width = 800
height = 700

screen = Canvas(tk, width=width, height=height, background="#A8B8E8")
screen.pack()





#Clouds

numClouds = random.randint(4,5)

for cloud in range(numClouds):
    clouds = random.randint(8,15)

    x1 = random.randint(0,width)
    y1 = random.randint(0, 350 - 200)
    #screen.create_rectangle(x1,y1, x1 + 100, y1 + 100, fill="blue")

    for circle in range(clouds):
        cloudSize = random.randint(80,100)
        cloudx1 = random.randint(x1, x1+80) 
        cloudy1 = random.randint(y1, y1+40)
        screen.create_oval(cloudx1, cloudy1, cloudx1+ random.randint(cloudSize-40, cloudSize+40), cloudy1 + random.randint(cloudSize-40, cloudSize+40), fill="white", outline="white")




#Grass

screen.create_rectangle(0, 350, 800, 500, fill="green", outline="green")


for grass in range(3000):
    grassWidth = random.randint(4,8)
    grassHeight = random.randint(10,15)
    x1 = random.randint(0,800-grassWidth)
    y1 = random.randint(350-grassHeight,500-grassHeight)
    colours = ["green", "#209145", "#5DBF7E"]
    color = colours[random.randint(0,2)]
    screen.create_rectangle(x1,y1, x1 + grassWidth, y1 + grassHeight, fill=color, outline=color)


#Road

screen.create_rectangle(0, 500, 800, 700, fill="grey", outline="black")

lines = random.randint(6, 18)
lineWidth = random.randint(40, 100)
lineHeight = random.randint(10,20)
space = width/(lines-1)

for line in range(lines):
    screen.create_rectangle((space+lineWidth)*line, 600 - lineHeight/2, (space+lineWidth)*line + lineWidth, 600 + lineHeight/2, fill="white")



#Temple

screen.create_polygon(150, 450, 150, 375, 250, 375, 300, 350, 325, 250, 350, 150, 350, 125, 375, 100, 400, 90, 425, 100, 450, 125, 450, 150, 475, 250, 500, 350, 550, 375, 650, 375, 650, 450, fill="#CCAF7E", smooth=True, outline="black")




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