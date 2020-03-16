##########################################################
#                       Daniel Yu                        # 
#                    Rainbow Target                      #
#                        ICS3UI                          #
##########################################################

from tkinter import *
import time
import random
import math
tk = Tk()


#Variables
width = 800 #Width of screen
height = width #Height of screen
xCenter = width/2 #X coordinate of center of circles
yCenter = height/2 #Y coordinate of center of circles
targetDist = width / 12 #Space between each target

diameter = 30 #Diameter of ball
x1 = 100 #X1 coordinate of ball 
y1 = 100 #Y1 coordinate of ball
x2 = x1 + diameter #X2 coordinate of ball
y2 = y1 + diameter #Y2 coordinate of ball
xBall = (x1 + x2)/2 #X coordinate of center of ball
yBall = (y1 + y2)/2 #Y coordinate of center of ball
xSpeed = 5 #X speed of ball
ySpeed = 5 #Y speed of ball

colours = ["blue", "green", "red", "purple", "orange", "hot pink", "grey"] #Colour choices

#Initialize screen
screen = Canvas(tk, width=width, height=height, background="black")
screen.pack()


#Create Ovals
for f in range(1,7):
    screen.create_oval(xCenter - (f*targetDist), yCenter - (f*targetDist), xCenter + (f*targetDist), yCenter + (f*targetDist), outline="white")

#Animation Loop
while True:

    #To iterate for each target size and determine its colour based on the radius of the circle and the distance between the ball's center to the origin
    for circle in range(1,7):

        radius = circle * targetDist
        xDelta = xBall - width/2
        yDelta = yBall - width/2
        distance = math.sqrt(xDelta**2 + yDelta**2)

        if distance < radius:
            color = colours[circle-1]
            break
        elif circle == 6:
            color = colours[circle]

    ball = screen.create_oval(x1, y1, x2, y2, fill=color)

    screen.update()
    time.sleep(0.03)
    screen.delete(ball)

    #To move the ball
    x1 = x1 + xSpeed  
    y1 = y1 + ySpeed
    x2 = x1 + diameter
    y2 = y1 + diameter

    #Update center of ball values
    xBall = (x1 + x2)/2
    yBall = (y1 + y2)/2
 
    #To detect collision with wall
    if x1 <= 0:
        xSpeed = -1 * xSpeed
    elif x2 >= width:
        xSpeed = -1 * xSpeed
    if y1 <= 0:
        ySpeed *= -1
    elif y2 >= height:
        ySpeed *= -1

screen.mainloop() #For visual studio code 