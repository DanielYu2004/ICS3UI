from tkinter import *
from random import *
from math import *
from time import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="white")
screen.pack()

#Essential information
numBirds = 10
numSheep = 15
numPuff = 100
numGrass = 1000

bird = []
birdx = []
birdy = []
angle1 = []
angle2 = []
angle3 = []
angle4 = []
sheep = []
xSheep = []
ySheep = []
sheepChangex = []
sheepChangey = []
puff = []
xPuff = []
yPuff = []
xSize = []
ySize = []
legA = []
legB = []
head = []

#Create background
screen.create_rectangle(0, 400, 800, 800, fill='dark green')
screen.create_rectangle(0, 0, 800, 400, fill='steel blue')
screen.create_oval(650, 50, 750, 150, fill='yellow')

for y in range(0, numGrass):
    xGrassA = randint(0, 800)
    yGrassA = randint(400, 800)
    xGrassB = xGrassA + randint(-5, 5)
    yGrassB = yGrassA + randint(3, 7)
    screen.create_line(xGrassA, yGrassA, xGrassB, yGrassB, fill='forest green', width=2)

screen.create_rectangle(50, 450, 250, 550, fill='dark red', outline='white', width=3)
screen.create_polygon(250, 550, 350, 500, 350, 400, 250, 450, fill='dark red', outline='white', width=3)
screen.create_polygon(50, 450, 200, 350, 250, 450, fill='grey', outline='dark grey', width=3)
screen.create_polygon(250, 450, 200, 350, 350, 400, fill='grey', outline='dark grey', width=3)
screen.create_rectangle(100, 460, 200, 500, fill='white', outline='black')
screen.create_text(150, 470, text='Quality Wool', font='Papyrus 10', anchor=N)

xFence = 0
yFence = 560
for x in range(7):
    screen.create_line(0, yFence, 800 , yFence, fill='black', width=1)
    yFence += 5
for x in range(160):
    screen.create_line(xFence, 560, xFence, 590, fill='black', width=1)
    xFence += 5

#Create animation information
for x in range(0, numBirds):

    bird.append(x)
    birdx.append(randint(0, 800))
    birdy.append(randint(0, 300))
    angle1.append(randint(5, 10))
    angle2.append(randint(5, 10))
    angle3.append(randint(5, 10))
    angle4.append(randint(5, 10))

for x in range(0, numSheep):
    sheep.append(x)
    xSheep.append(randint(0, 760))
    ySheep.append(randint(600, 760))
    sheepChangex.append(randint(-6, 6))
    sheepChangey.append(randint(-6, 6))
    legA.append(x)
    legB.append(x)
    head.append(x)
    
    if sheepChangex[x] >= 0:
        headDir = True

    else:
        headDir = False

    for y in range(0, 100):
        puff.append(y)
        xPuff.append(randint(xSheep[x], xSheep[x]+30))
        yPuff.append(randint(ySheep[x], ySheep[x]+15))
        xSize.append(randint(4, 10))
        ySize.append(randint(2, 8))
        
#Animation
for frameCount in range(0, 1000):

    #Create birds
    for x in range(0, numBirds):        
        bird[x] = screen.create_line(birdx[x], birdy[x], birdx[x]+angle1[x], birdy[x]-10, birdx[x]+angle1[x]+angle2[x], birdy[x]+10, birdx[x]+angle1[x]+angle2[x]+angle3[x], birdy[x]-10, birdx[x]+angle1[x]+angle2[x]+angle3[x]+angle4[x], birdy[x], fill='black', width=2, smooth='true')
        birdx[x] += 10
        birdy[x] = birdy[x] + 10*sin(0.1 * birdx[x])
        
        if birdx[x] > 800:
            birdx[x] = 0
            birdy[x] = randint(0, 300)
    #Create sheep
    for x in range(0, numSheep):
        if xSheep[x] < 0 or xSheep[x] + 40 > 800:
            sheepChangex[x] *= -1
            
        if ySheep[x] < 570 or ySheep[x] + 20 > 800:
            sheepChangey[x] *= -1
            
        xSheep[x] += sheepChangex[x]
        ySheep[x] += sheepChangey[x]
        
        if sheepChangex[x] <= 0:
            headDir = True
            
        else:
            headDir = False
        
        if headDir == True:
            head[x] = screen.create_polygon(xSheep[x]+2, ySheep[x]+10, xSheep[x]+2, ySheep[x]+3, xSheep[x]-5, ySheep[x]+3, xSheep[x]-5, ySheep[x]-4, xSheep[x]+7, ySheep[x]-4, xSheep[x]+7, ySheep[x]+4, fill='white', outline='black', smooth='true')
        
        if headDir == False:
            head[x] = screen.create_polygon(xSheep[x]+38, ySheep[x]+10, xSheep[x]+38, ySheep[x]+3, xSheep[x]+45, ySheep[x]+3, xSheep[x]+45, ySheep[x]-4, xSheep[x]+33, ySheep[x]-4, xSheep[x]+33, ySheep[x]+4, fill='white', outline='black', smooth='true')

        sheep[x] = screen.create_oval(xSheep[x], ySheep[x], xSheep[x]+40, ySheep[x]+20, fill='white')
        legA[x] = screen.create_rectangle(xSheep[x]+5, ySheep[x]+17, xSheep[x]+10, ySheep[x]+27, fill='white')
        legB[x] = screen.create_rectangle(xSheep[x]+30, ySheep[x]+17, xSheep[x]+35, ySheep[x]+27, fill='white')

        for y in range(0, numPuff):
            xPuff[y+(x*100)] += sheepChangex[x]
            yPuff[y+(x*100)] += sheepChangey[x]
            puff[y+(x*100)] = screen.create_oval(xPuff[y+(x*100)], yPuff[y+(x*100)], xPuff[y+(x*100)]+xSize[y+(x*100)], yPuff[y+(x*100)]+ySize[y+(x*100)], fill='white')

    screen.update()
 #   sleep(0.01)
    #Delete animation frame
    for x in range(0, numBirds):
        screen.delete(bird[x])

    for x in range(0, numSheep):

        for y in range(0, numPuff):
            screen.delete(puff[y+(x*100)])
            
        screen.delete(sheep[x],legA[x], legB[x], head[x])

screen.mainloop()




