#
#  Owen Bissitt
#  Hour Glass
#  May 1, 2020
#

from tkinter import *
from random import *
from time import *
from math import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=725, background="blanched almond")
screen.pack()



#HOURGLASS

#Pillars of hourglass

#Left pillar
screen.create_oval(180, 60, 230, 357.5, fill = "saddle brown")
screen.create_oval(180, 377.5, 230, 665, fill = "saddle brown")
screen.create_oval(180, 342.5, 230, 392.5, fill = "saddle brown")

#right pillar
screen.create_oval(570, 60, 620, 357.5, fill = "saddle brown")
screen.create_oval(570, 377.5, 620, 665, fill = "saddle brown")
screen.create_oval(570, 342.5, 620, 392.5, fill = "saddle brown")


#bases of hourglass

#top base
screen.create_polygon(150, 0, 650, 0, 650, 40, 615, 75, 185, 75, 150, 40, fill = "saddle brown", outline = "black")
screen.create_oval(150, 5, 220, 75, fill = "saddle brown", outline = "saddle brown")
screen.create_oval(580, 5, 650, 75, fill = "saddle brown", outline = "saddle brown")

#bottom base
screen.create_polygon(150, 725, 150, 685, 185, 650, 615, 650, 650, 685, 650, 725, fill = "saddle brown", outline = "black")
screen.create_oval(150, 650, 220, 720, fill = "saddle brown", outline = "saddle brown")
screen.create_oval(580, 650, 650, 720, fill = "saddle brown", outline = "saddle brown")

#actual glass
screen.create_line(310, 75, 250, 150, width = 1)#first line
screen.create_line(250, 150, 380, 355, width = 1)#second line
screen.create_line(380, 355, 380, 370, width = 1)#third line
screen.create_line(380, 370, 250, 575, width = 1)#fourth line
screen.create_line(250, 575, 310, 650, width = 1)#fifth line
screen.create_line(490, 650, 550, 575, width = 1)#sixth line
screen.create_line(550, 575, 420, 370, width = 1)#seventh line
screen.create_line(420, 370, 420, 355, width = 1)#eighth line
screen.create_line(420, 355, 550, 150, width = 1)#ninth line
screen.create_line(550, 150, 490, 75, width = 1)#tenth line


#ANIMATION

grains = 50
stop = 575


#Variables to use to make top sand decrease
leftCornerX = 316
leftCornerY = 252.5
rightCornerX = 484
rightCornerY = 252.5
x1 = 400
y1 = 365
x2 = 381
y2 = 355
x3 = 419
y3 = 355
j = 1

#Variables to make the bottom increase
x4 = 251
y4 = 575
x42 = 251
y42 = 575
x5 = 400
y5 = 550
x6 = 549
y6 = 575
x62 = 549
y62 = 575

#Array setup

xSpeed = []
ySpeed = []
k = []
size = []
sand = []
x = []
y = []
yTip = []
xTip = []


#filling the arrays

for i in range(0, grains):
    xSpeed.append(randint(-2,2))
    ySpeed.append(randint(10,20))
    size.append(randint(2,4))
    sand.append(0)
    k.append(0)
    x.append(0)
    y.append(0)
    xTip.append(398)
    yTip.append(362)
        

#Making things move
    
for f in range(0, 540):
    for i in range(0, grains):
        y[i] = ySpeed[i]*k[i] + yTip[i]
        x[i] = xSpeed[i]*k[i] + xTip[i]
        
        sand[i] = screen.create_oval(x[i], y[i], x[i] + size[i], y[i] + size[i], fill = "lightgoldenrod3", outline = "lightgoldenrod3")
        
        k[i] = k[i] + 1
        
        #stops the sand from leaving its container
        if y[i] >= stop:
            k[i] = 0



    #making the top sand decrease then vanish
    topSand = screen.create_polygon(x1, y1, x2, y2, leftCornerX, leftCornerY, rightCornerX, rightCornerY, x3, y3, fill = "lightgoldenrod3", outline = "lightgoldenrod3")

    leftCornerX = leftCornerX + 0.125*j
    leftCornerY = leftCornerY + 0.19711538461*j
    rightCornerX = rightCornerX - 0.125*j
    rightCornerY = rightCornerY + 0.19711538461*j

    #Making the bottom sand increase then stop
    bottomSand = screen.create_polygon(311, 649, x42, y42, x4, y4, x5, y5, x6, y6, x62, y62, 489, 649, fill = "lightgoldenrod3", outline = "lightgoldenrod3")

    x4 = x4 + 0.0625*j
    y4 = y4 - 0.09932170542*j
    y5 = y5 - 0.09932170542*j
    x6 = x6 - 0.0625*j
    y6 = y6 - 0.09932170542*j


    
    if leftCornerY >= 360:
        leftCornerX = 800
        leftCornerY = 800
        rightCornerX = 800
        rightCornerY = 800
        x1 = 800
        y1 = 800
        x2 = 800
        y2 = 800
        x3 = 800
        y3 = 800
        j = 0

    if f >=539:
        screen.create_polygon(311, 649, x42, y42, x4, y4, x5, y5, x6, y6, x62, y62, 489, 649, fill = "lightgoldenrod3", outline = "lightgoldenrod3")
        
    
    #updating and removing objects
    screen.update()

    for i in range(0, grains):
        if y[i] <= stop:
            screen.delete(sand[i], topSand, bottomSand)
                
    sleep(0.03)
    
