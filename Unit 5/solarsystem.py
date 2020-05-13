from tkinter import *
from random import *
from time import *
from math import *
tk = Tk()
screen = Canvas(tk, width=600, height=600, background="black")
screen.pack()


#SOLAR SYSTEM DATA - TRY CHANGING THESE
planetSizes = [7, 7, 8, 3, 7, 30]
orbitSizes = [200, 120, 180, 185, 250, 375]   #The 180 and the 185 are for the green and blue parts of the earth
angles = [0, 45, 90, 90, 180, 250]
orbitingSpeeds = [4.5, 2.5, 1.5, 1.5, 1.7, 0.6]
colors = ["grey90", "hot pink",    "cyan3","green",    "red", "dark orange"]   #The cyan3 and the green make up the earth
planetDrawings = [0, 0, 0, 0, 0, 0]
numPlanets = 1  #len(orbitSizes)


#DRAWS A CIRCLE WITH A GIVEN CENTRE AND RADIUS
def drawCircle( xC, yC, r, col ):
    x1 = xC - r
    y1 = yC - r
    x2 = xC + r
    y2 = yC + r
    return screen.create_oval( x1, y1, x2, y2, fill= col, outline=col )


#DRAWS A STARRY BACKGROUND, USING THE drawCircle() COMMAND WE JUST TAUGHT PYTHON ABOVE
def drawStars( numStars ):
    for i in range(0,numStars):
        x = randint(0,600)
        y = randint(0,600)
        size = uniform(1,2)
        drawCircle(x, y, size, "white" )
        

#DRAWS THE SUN GIVEN ITS CENTRE AND RADIUS, AGAIN  USING THE drawCircle() COMMAND
def drawSun( xC, yC, sunRadius ):
    drawCircle(xC, yC, sunRadius, "yellow" )


#DRAWS A PLANET GIVEN THE CENTRE OF ITS ORBIT, ITS ANGLE ALONG THAT ORBIT, ITS RADIUS AND COLOUR.
def drawPlanet( xSun, ySun, degAngle, orbitalRadius, planetSize, color, f1, f2, c1, c2 ):
    radianAngle = radians( degAngle )

    xPlanet = xSun + orbitalRadius * f1(c1*radianAngle )
    yPlanet = ySun  -  orbitalRadius * f2(c2*radianAngle )
        
    return drawCircle( xPlanet, yPlanet, planetSize, color )


#RUNS THE ANIMATION USING THE ABOVE PROCEDURES AND FUNCTIONS
def animateSolarSystem(numStars, xSun, ySun, f1, f2, c1, c2, showTrails):
    drawStars( numStars )                  #Procedure-call
    drawSun( xSun, ySun, 35 )           #Procedure-call

    while True:
        
        #Draws all the planets
        for i in range( numPlanets ): 
            planetDrawings[i] = drawPlanet( xSun, ySun, angles[i], orbitSizes[i], planetSizes[i], colors[i], f1, f2, c1, c2)    #Function-call of drawPlanet()
            angles[i] = angles[i] + orbitingSpeeds[i]

        #Updates and sleeps after all planets have been drawn  
        screen.update()  
        sleep(.03)

        #Deletes all planets
        if showTrails == False:
            for i in range( numPlanets ):
                screen.delete( planetDrawings[i] )

        
#The normal animation
#animateSolarSystem(200, 300, 300, cos, sin, 1, 1, False)

#A figure-8 animation.  
#Comment out the previous line to watch this version.
#animateSolarSystem(200, 300, 300, sin, sin, 1, 0.5, True)

#Add your own variations!
animateSolarSystem(200, 300, 300, tan, tan, 0.3, 0.4, True)


screen.mainloop()
