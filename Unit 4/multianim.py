#############################
#TITLE:  Candy Cane Snow Fall
#This program draws a snow fall with candy cane flavours
#Programmer:  Mr. Schattman
#Last modified:  Jan 5, 2018
###############################

from tkinter import *
from time import *
from math import *
from random import *

tk = Tk()
s = Canvas(tk, width=800,height=800,background="sky blue")
s.pack()


#Sets the number of snow flakeDrawings, ground level and wind speed
numflakeDrawings = 500
groundLevel = 500
windSpeed = 2
colors = ["white", "red", "green", "purple", "yellow"]


#Draws the ground
ground = s.create_rectangle(0, groundLevel-5, 800, 800, fill="white", outline="white")


#Sets up the empty arrays 
xSpeeds = []
ySpeeds = []
xPos = []
yPos = []
sizes = []
colorIndex = []
flakeDrawings = []


#Sets random initial values for each snow flake's speed, starting point, and size
for n in range(numflakeDrawings):
    xPos.append( randint(-200*windSpeed, 800))
    yPos.append( randint(-800,0))
     
    xSpeeds.append( windSpeed )
    ySpeeds.append( randint(1,5) )
    
    sizes.append( randint(2,4) )
    
    flakeDrawings.append(0)
    colorIndex.append( 0 )



#For each frame, do all this
for f in range(1000):

    #For each individual flake in the current frame, do all this
    for i in range(numflakeDrawings):

        #Draws the current flake in the current frame using its own position, size, and current color choice
        flakeDrawings[i] = s.create_oval(xPos[i], yPos[i], xPos[i]+sizes[i], yPos[i]+sizes[i], fill = colors[ colorIndex[i] ], outline = colors[ colorIndex[i] ])

        #Updates the flake's position
        xPos[i] = xPos[i] + xSpeeds[i]
        yPos[i] = yPos[i] + ySpeeds[i]

        if yPos[i] >= groundLevel:
            # As soon as a flake hits the ground, resets its yStart to 0, and change its color
            xPos[i] = randint(-200*windSpeed, 800)
            yPos[i] = 0
            colorIndex[i] = (colorIndex[i] + 1) % len(colors)

    s.update()
    sleep(0.03)

    #Deletes all flakeDrawings before going on to the next frame
    for i in range(numflakeDrawings):
            s.delete( flakeDrawings[i] )