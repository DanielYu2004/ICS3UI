from tkinter import *
from time import *
from math import *
from random import *
tk = Tk()
screen = Canvas(tk, width=800, height=800, background="sky blue")
screen.pack()

#Cloud 1
numClouds1 = 70
xx = []
yx = []
sizex = 50

for i in range (numClouds1):
    xx.append(randint(50,250))
    yx.append(randint(0,80))

for i in range (numClouds1):
    screen.create_oval(xx[i], yx[i], xx[i] + sizex, yx[i] +sizex, fill = "white", outline = "white")

#Cloud 2
numClouds1 = 100
xy = []
yy = []


for i in range (numClouds1):
    xy.append(randint(500,700))
    yy.append(randint(0,80))

for i in range (numClouds1):
    screen.create_oval(xy[i], yy[i], xy[i] + sizex, yy[i] +sizex, fill = "white", outline = "white") 
        
#Bleachers
screen.create_rectangle(0, 150, 800, 365, fill = "#878787")

#People in the stands
numPeople = 500
xp = []
yp = []
size = []
face = []
shirt = []
head = []
body = []

for i in range(numPeople):
    xp.append(randint(0, 800))
    yp.append(randint(150, 350))
    size.append(randint(10,15))
    face.append(choice ( ["#ffe6a1", "#5c400b", "#e8b556"]))
    shirt.append(choice ( [ "blue", "red", "green" ] ))
    head.append(0)
    body.append(0)

                 
##for i in range (numPeople):
##    head[i] = screen.create_oval(xp[i], yp[i], xp[i] + size[i], yp[i] + size[i], fill = face[i])
##    body[i] = screen.create_rectangle(xp[i], yp[i] + size[i], xp[i] + size[i], yp[i] + size[i] + 20, fill = shirt[i])

#Wall
screen.create_rectangle(0, 360, 800, 400, fill = "white")
#Track
screen.create_rectangle(0, 400, 800, 700, fill = "#2e2e2e")
#Side of the track
screen.create_rectangle(0, 700, 800, 800, fill = "#4f4f4f")
#Dividing line
screen.create_line(0, 700, 800, 700, width = 5, fill="white")
#Fence
a = 0
for n in range (34):
    screen.create_line(a, 200, a, 360, fill = "black", width = 3)
    a = a + 25

b = 200
for n in range (3):
    screen.create_line(0, b, 800, b, fill="black", width =5 )
    b = b + 50

#Number of cars
numCars=4

#Empty arrays
x =[]
y=[]
carSpeeds=[]
carBody =[]
wheelA = []
wheelB=[]
glass=[]
line=[]
colours = []
number = []
text =[]

#Filling arrays
for i in range (numCars):
    x.append(randint(200, 800))

    carBody.append(0)
    wheelA.append(0)
    wheelB.append(0)
    glass.append(0)
    line.append(0)
    text.append(0)

#Filling arrays that will change when the car reaches the left side
for i in range (600):
    colours.append(choice(["#006fde", "orange", "#a62508", "#046e12", "#cfbe04", "#40ff50", "#c20450", "#04c2a2", "#b3b3b3"]))
    number.append(randint(0, 99))
    carSpeeds.append(uniform(10, 20))
    y.append(randint(400, 625))
    
#Creating animation
for f in range (10000):
    
    for i in range (numPeople):
        head[i] = screen.create_oval(xp[i], yp[i], xp[i] + size[i], yp[i] + size[i], fill = face[i])
        body[i] = screen.create_rectangle(xp[i], yp[i] + size[i], xp[i] + size[i], yp[i] + size[i] + 20, fill = shirt[i])
        yp[i] = yp[i] + randint(-1,1)

    for i in range (numCars):
        carBody[i]= screen.create_polygon(x[i], y[i], x[i]+75, y[i], x[i]+125, y[i] -50, x[i]+225, y[i]-50, x[i]+275, y[i], x[i]+290, y[i], x[i]+290, y[i]+50, x[i], y[i] +50, fill = colours[i], outline= "black")
        wheelA[i]= screen.create_oval(x[i] +25, y[i] +25, x[i]+75, y[i]+75, fill="black")
        wheelB[i]=screen.create_oval(x[i]+200, y[i] +25, x[i]+250, y[i]+75, fill="black")
        glass[i]= screen.create_polygon(x[i]+75, y[i], x[i]+125, y[i] -50, x[i]+225, y[i]-50, x[i]+275, y[i], fill = "black")
        line[i]= screen.create_line(x[i] + 175, y[i]-50, x[i]+175, y[i], fill = colours[i], width = 4)
        text[i] = screen.create_text(x[i] +125, y[i]+25, text = str(number[i]), font =  "arial 40", fill = "white")
        x[i]=x[i]-carSpeeds[i]
        #If statement that changes the colour, number, and speed of car when it reaches left side of screen
        if x[i] < -290:
            x[i] = 800
            number[i] = choice(number)
            colours[i] = choice(colours)
            carSpeeds[i]= choice(carSpeeds)
            y[i] = choice(y)
            
    screen.update()
    sleep(0.03)
      
    for i in range( numCars ):
        screen.delete( carBody[i], wheelA[i], wheelB[i], glass[i], line[i], text[i])

    for i in range( numPeople ):
        screen.delete(head[i], body[i])




    
