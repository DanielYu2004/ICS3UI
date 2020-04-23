from tkinter import *
from time import *
from math import *
from random import *


tk = Tk()
screen = Canvas(tk, width=800,height=800,background="light blue")
screen.pack()

#Background

#Grass
screen.create_rectangle (0, 800, 800, 650, fill="green3", outline="green3")


#House
screen.create_rectangle(300, 750, 500, 600, fill="khaki")
screen.create_polygon(300, 600, 500, 600, 400, 500, fill="red4")
screen.create_rectangle(380, 750, 420, 675, fill="brown")
screen.create_rectangle (310, 625, 360, 675, fill = "lightblue", outline = "gray60", width = 5)
screen.create_line(310, 650, 360, 650, fill = "gray70", width = 5)
screen.create_line(335, 625, 335, 675, fill = "gray70", width = 5)
screen.create_rectangle (490, 625, 440, 675, fill = "lightblue", outline = "gray60", width = 5)
screen.create_line(490, 650, 440, 650, fill = "gray70", width = 5)
screen.create_line(465, 625, 465, 675, fill = "gray70", width = 5)

#Balloons
numBalloons = 150
Bx=[]
By=[]
balloonColours = ["red", "dodger blue", "yellow", "green2", "cyan", "magenta", "purple", "orange", "purple4"]
balloons=[]
rope=[]
balloonWidth = []
balloonSpeed = []
#Sky, Stars and Clouds
skycolours = ["lightblue", "light steel blue", "steel blue", "steelblue4", "black"]
Sx = []
Sy = []
stars = []
Cx1 = []
Cy1 = []
Cx2 = []
Cy2 = []
cloud1 = []
cloud2 = []
moon = []

#Filling Arrays
for b in range(numBalloons):
    Bx.append(randint(150, 600))
    By.append(randint(50, 400))
    balloons.append(0)
    rope.append(0)
    Sx.append(randint(0,800))
    Sy.append(randint(-800, 0))
    stars.append(0)
    balloonWidth.append(randint(5, 35))
    balloonSpeed.append(randint(1, 5))
    Cx1.append(randint(100, 250)) 
    Cy1.append(randint(100, 200))
    Cx2.append(randint(600, 750))
    Cy2.append(randint(-300, -150))
    cloud1.append(0)
    cloud2.append(0)
    moon.append(0)

#Starting Animation
for f in range (600):

#Lift off
    if f > 100 and f < 118:
        x1 = 0
        x2 = 800
        y1 = 640
        y2 = 642 + 10*(f-100)
        screen.create_rectangle(x1, y1, x2, y2, fill = "lightblue", outline = "lightblue")
        screen.create_rectangle(300, 750, 500, 600, fill="khaki")
        screen.create_rectangle(380, 750, 420, 675, fill="brown")
        screen.create_rectangle (310, 625, 360, 675, fill = "lightblue", outline = "gray60", width = 5)
        screen.create_line(310, 650, 360, 650, fill = "gray70", width = 5)
        screen.create_line(335, 625, 335, 675, fill = "gray70", width = 5)
        screen.create_rectangle (490, 625, 440, 675, fill = "lightblue", outline = "gray60", width = 5)
        screen.create_line(490, 650, 440, 650, fill = "gray70", width = 5)
        screen.create_line(465, 625, 465, 675, fill = "gray70", width = 5)
        screen.create_polygon(325, 775, 225, 730, 250, 720, 325, 775, fill = "gray50", width = 10, smooth = True)
        screen.create_polygon(325, 775, 250, 730, 275, 700, 325, 775, fill = "gray55", width = 10, smooth = True)
        screen.create_polygon(475, 775, 575, 730, 550, 720, 475, 775, fill = "gray55", width = 10, smooth = True)
        screen.create_polygon(475, 775, 550, 730, 525, 700, 475, 775, fill = "gray50", width = 10, smooth = True)                   

#Clouds
    if f < 325:
        for b in range(numBalloons-110):
            cloud1[b] = screen.create_oval(Cx1[b], Cy1[b], Cx1[b]+50, Cy1[b]+50, fill = "white", outline = "white")
            cloud2[b] = screen.create_oval(Cx2[b], Cy2[b], Cx2[b]+50, Cy2[b]+50, fill = "white", outline = "white")
            if f > 100 and f < 300:
                Cy1[b] = Cy1[b]+ 4
                Cy2[b] = Cy2[b]+ 5
            elif f > 290:
                Cy2[b] = Cy2[b] + 5

            
                
#Stars                    
    if f > 325:
        for b in range(numBalloons-75):
            stars[b] = screen.create_oval(Sx[b], Sy[b], Sx[b]+4, Sy[b]+4, fill = "white", outline = "yellow")
            Sy[b] = Sy[b] + 2

#Changing Sky Colour        
    if f == 120:
        screen.create_rectangle (0,0, 800, 800, fill = skycolours[0])

    if f == 150:
        screen.create_rectangle (0,0, 800, 800, fill = skycolours[1])

    if f == 200:
        screen.create_rectangle (0,0, 800, 800, fill = skycolours[2])
        
    if f == 250:
        screen.create_rectangle (0,0, 800, 800, fill = skycolours[3])
        
    if f == 300:
        screen.create_rectangle (0,0, 800, 800, fill = skycolours[4])

#BALLOONS    
    for b in range(numBalloons):
        c = balloonColours[b%len(balloonColours)]
        x1 = Bx[b] + balloonWidth[b]*sin(0.05*f*balloonSpeed[b])
        x2 = x1+50
        y1 = By[b]
        y2 = y1+50
        balloons[b] = screen.create_oval(x1, y1, x2, y2, fill = c, outline = c)
        rope[b] = screen.create_line(400, 500, x1+25, y1+50, fill = "gray80")

#Moon
    if f > 325:
        for b in range (numBalloons):
            y1 = -300+6*(f-325)
            y2 = y1+300 
            if y1 > 750:
                y1 = 750
                y2 = 1050
            moon[b] = screen.create_oval(250, y1, 550, y2, fill = "gray55", outline = "gray40", width = 10)
            
#Animating the House    
    if f > 100 and f <118 or f == 120 or f == 150 or f == 200 or f == 250 or f == 300:
        screen.create_rectangle(300, 750, 500, 600, fill="khaki")
        screen.create_polygon(300, 600, 500, 600, 400, 500, fill="red4")
        screen.create_rectangle(380, 750, 420, 675, fill="brown")
        screen.create_rectangle (310, 625, 360, 675, fill = "lightblue", outline = "gray60", width = 5)
        screen.create_line(310, 650, 360, 650, fill = "gray70", width = 5)
        screen.create_line(335, 625, 335, 675, fill = "gray70", width = 5)
        screen.create_rectangle (490, 625, 440, 675, fill = "lightblue", outline = "gray60", width = 5)
        screen.create_line(490, 650, 440, 650, fill = "gray70", width = 5)
        screen.create_line(465, 625, 465, 675, fill = "gray70", width = 5)




    screen.update()
    sleep(0.03)
    for b in range (numBalloons):
        screen.delete(balloons[b], rope[b], stars[b], cloud1[b], cloud2[b], moon[b])
