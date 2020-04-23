from tkinter import *
from math import *
from time import *
from random import *

myInterface = Tk()
s = Canvas( myInterface, width=1000, height=600, background = "black" )
s.pack()

            
#empty arrays
xStar=[]
yStar=[]
starDrawings = []
yFlame1 = []
yFlame2 = []
flameDrawings = []
xLaser=[]
yLaser=[]
laserDrawings = []
xEnergy=[]
yEnergy=[]
xEnergySpeed = []
yEnergySpeed = []
energyDrawings = []

#colour arrays 
flameColours = ["orange","orange2","orange3","OrangeRed2","OrangeRed3","red","red2","red3"]
blues = ["blue", "CadetBlue1", "blue2", "dodger blue", "medium blue"]
fading = ["blue", "grey50", "grey50","grey50"]

#variables
#origin of the spaceship
xSpaceShipOrigin = 160    
ySpaceShipOrigin = 300 # + 220*sin(0.1*f)
planetX = 1040
planetY = 300
planetColour = "brown"
pr = 50
laserLength = randint(50,75)
energyX = xSpaceShipOrigin + 350
energyY = ySpaceShipOrigin
armLength = 1
xFlame2 = 110
r1 = 0
starSpeed = 6.5
#size of arrays
numFlames = 30
numStars= 250
numEnergy = 30
numLasers = 20
#cooridinates of the spaceship
#blocks behind the origin
#rectangleMinus3 = furthest rectangle away
xSpaceShipMinus5a = xSpaceShipOrigin - 40
ySpaceShipMinus5a = ySpaceShipOrigin - 15
xSpaceShipMinus5b = xSpaceShipOrigin - 60
ySpaceShipMinus5b = ySpaceShipOrigin + 15
#triangleMinus4 = top triangle triangle connected to rectangleMinus 2
xSpaceShipMinus4a = xSpaceShipOrigin - 70
ySpaceShipMinus4a = ySpaceShipOrigin - 80
xSpaceShipMinus4b = xSpaceShipOrigin - 70
ySpaceShipMinus4b = ySpaceShipOrigin - 60
xSpaceShipMinus4c = xSpaceShipOrigin - 20
ySpaceShipMinus4c = ySpaceShipOrigin - 60
#triangleMinus3 = bottom triangle triangle connected to rectangleMinus 2
xSpaceShipMinus3a = xSpaceShipOrigin - 70
ySpaceShipMinus3a = ySpaceShipOrigin + 60
xSpaceShipMinus3b = xSpaceShipOrigin - 70
ySpaceShipMinus3b = ySpaceShipOrigin + 80
xSpaceShipMinus3c = xSpaceShipOrigin - 20
ySpaceShipMinus3c = ySpaceShipOrigin + 60
#rectangleMinus2 = second farthest rectangle from behind the origin
xSpaceShipMinus2a = xSpaceShipOrigin - 40
ySpaceShipMinus2a = ySpaceShipOrigin - 60
xSpaceShipMinus2b = xSpaceShipOrigin - 20
ySpaceShipMinus2b = ySpaceShipOrigin + 60
#rectangleMinus1 = first farthest rectangle from behind the origin (connecter piece)
xSpaceShipMinus1a = xSpaceShipOrigin - 20
ySpaceShipMinus1a = ySpaceShipOrigin - 20
xSpaceShipMinus1b = xSpaceShipOrigin 
ySpaceShipMinus1b = ySpaceShipOrigin + 20
#rectangle1 = first rectangle infront of origin (big piece)
xSpaceShip1a = xSpaceShipOrigin 
ySpaceShip1a = ySpaceShipOrigin - 30
xSpaceShip1b = xSpaceShipOrigin + 100
ySpaceShip1b = ySpaceShipOrigin + 30
#rectangle2 = second rectangle infront of origin (connecter piece)
xSpaceShip2a = xSpaceShipOrigin + 100
ySpaceShip2a = ySpaceShipOrigin - 20
xSpaceShip2b = xSpaceShipOrigin + 120
ySpaceShip2b = ySpaceShipOrigin + 20
#rectangle3 = third rectangle infront of origin (big piece)
xSpaceShip3a = xSpaceShipOrigin + 120
ySpaceShip3a = ySpaceShipOrigin - 25
xSpaceShip3b = xSpaceShipOrigin + 250
ySpaceShip3b = ySpaceShipOrigin + 25
#triangle1 = triangle that connects to rectangle 3
xSpaceShip4a = xSpaceShipOrigin + 350
ySpaceShip4a = ySpaceShipOrigin + 40
xSpaceShip4b = xSpaceShipOrigin + 220
ySpaceShip4b = ySpaceShipOrigin + 125
xSpaceShip4c = xSpaceShipOrigin + 200
ySpaceShip4c = ySpaceShipOrigin + 100
#triangle2 = triangle that connects to rectangle 3
xSpaceShip5a = xSpaceShipOrigin + 350
ySpaceShip5a = ySpaceShipOrigin - 40
xSpaceShip5b = xSpaceShipOrigin + 220
ySpaceShip5b = ySpaceShipOrigin - 125
xSpaceShip5c = xSpaceShipOrigin + 200
ySpaceShip5c = ySpaceShipOrigin - 100
#rectangle 4 - 7 = rectangles on rectangle 3 that "charge up"
#rectangle4 
xSpaceShip6a = xSpaceShipOrigin + 120
ySpaceShip6a = ySpaceShipOrigin + 5
xSpaceShip6b = xSpaceShipOrigin + 165
ySpaceShip6b = ySpaceShipOrigin - 5
#rectangle5
xSpaceShip7a = xSpaceShipOrigin + 165
ySpaceShip7a = ySpaceShipOrigin + 5
xSpaceShip7b = xSpaceShipOrigin + 210
ySpaceShip7b = ySpaceShipOrigin - 5
#rectangle6 
xSpaceShip8a = xSpaceShipOrigin + 210
ySpaceShip8a = ySpaceShipOrigin + 5
xSpaceShip8b = xSpaceShipOrigin + 255
ySpaceShip8b = ySpaceShipOrigin - 5
#rectangle7 
xSpaceShip9a = xSpaceShipOrigin + 255
ySpaceShip9a = ySpaceShipOrigin + 5
xSpaceShip9b = xSpaceShipOrigin + 300
ySpaceShip9b = ySpaceShipOrigin - 5
#triangle3 = big triangle "pincer"
xSpaceShipa = xSpaceShipOrigin + 310
ySpaceShipa = ySpaceShipOrigin + 6
xSpaceShipb = xSpaceShipOrigin + 250
ySpaceShipb = ySpaceShipOrigin + 25
xSpaceShipc = xSpaceShipOrigin + 250
ySpaceShipc = ySpaceShipOrigin + 6
#triangle4 = big triangle "pincer"
xSpaceShipa1 = xSpaceShipOrigin + 310
ySpaceShipa1 = ySpaceShipOrigin - 5
xSpaceShipb1 = xSpaceShipOrigin + 250
ySpaceShipb1 = ySpaceShipOrigin - 25
xSpaceShipc1 = xSpaceShipOrigin + 250
ySpaceShipc1 = ySpaceShipOrigin - 5
#rectangle9 = arm that connects to the triangles
xSpaceShip10a = xSpaceShipOrigin + 206 - armLength
ySpaceShip10a = ySpaceShipOrigin - 100
xSpaceShip10b = xSpaceShipOrigin + 214 + armLength
ySpaceShip10b = ySpaceShipOrigin - 25
#rectangle10 = arm that connects to the triangles
xSpaceShip11a = xSpaceShipOrigin + 206 - armLength
ySpaceShip11a = ySpaceShipOrigin + 100
xSpaceShip11b = xSpaceShipOrigin + 214 + armLength
ySpaceShip11b = ySpaceShipOrigin + 25

#filling arrays
for i in range(0, numFlames):
    flameStartY = randint(ySpaceShipOrigin - 15, ySpaceShipOrigin + 10)
    flameWidth = randint(1, 5)
    yFlame1.append( flameStartY )
    yFlame2.append( flameStartY + flameWidth)
    flameDrawings.append( 0 )

for i in range(0, numStars):
    xStar.append( randint(0,1000 ))
    yStar.append( randint(0,600 ))
    starDrawings.append( 0 )

for i in range(0, numLasers):
    length = randint(50, 75)
    xLaser.append( randint(475, 520))
    yLaser.append( randint(270, 330 ))
    laserDrawings.append( 0 )

for i in range(0, numEnergy):
    xRange = randint(energyX - 200, energyX + 200)
    xEnergy.append(xRange)
    yRange = randint(energyY - 200, energyY + 200)
    yEnergy.append(yRange)
    xEnergySpeed.append((energyX - xRange)/30)
    yEnergySpeed.append((energyY - yRange)/30)
    energyDrawings.append( 0 )

#animating creating the visuals
#spaceship just flying in space
for f in range(80):
    colour = "grey50"
    armColour = "grey50"

    for i in range(0, numFlames): #creating flames behind the spaceship
        flameN = randint(0, 7)
        flameColourChoice = flameColours[flameN] #changing the flame colours to colours in array
        xFlame1 = xFlame2 - randint( 30, 50 ) #flames have semi random widths
        flameDrawings[i] = s.create_oval( xFlame1, yFlame1[i], xFlame2, yFlame1[i] + 5, fill=flameColourChoice, width = 0)
                                                                              

    for i in range(0, numStars):
        r = randint(-1,2) #makes stars "blink"
        starDrawings[i] = s.create_oval(xStar[i]-r, yStar[i]-r, xStar[i]+r, yStar[i]+r,fill="white", width = 0)
        xStar[i] = xStar[i] - 5 #moves stars
        if xStar[i] < 0: #when star gets to egde of the screen resets
            xStar[i] = 1000

    rectangleMinus3 = s.create_rectangle(xSpaceShipMinus5a, ySpaceShipMinus5a, xSpaceShipMinus5b, ySpaceShipMinus5b, fill = "dimgrey", width = 0)
    rectangleMinus2 = s.create_rectangle(xSpaceShipMinus2a, ySpaceShipMinus2a, xSpaceShipMinus2b, ySpaceShipMinus2b, fill = "goldenrod", width = 0)
    triangleMinus4 = s.create_polygon(xSpaceShipMinus4a, ySpaceShipMinus4a, xSpaceShipMinus4b, ySpaceShipMinus4b, xSpaceShipMinus4c, ySpaceShipMinus4c, fill = "darkgoldenrod", width = 0)
    triangleMinus3 = s.create_polygon(xSpaceShipMinus3a, ySpaceShipMinus3a, xSpaceShipMinus3b, ySpaceShipMinus3b, xSpaceShipMinus3c, ySpaceShipMinus3c, fill = "darkgoldenrod", width = 0)
    rectangleMinus1 = s.create_rectangle(xSpaceShipMinus1a, ySpaceShipMinus1a, xSpaceShipMinus1b, ySpaceShipMinus1b, fill = "darkgoldenrod", width = 0)
    rectangle1 = s.create_rectangle(xSpaceShip1a, ySpaceShip1a, xSpaceShip1b, ySpaceShip1b, fill = "goldenrod", width = 0)
    rectangle2 = s.create_rectangle(xSpaceShip2a, ySpaceShip2a, xSpaceShip2b, ySpaceShip2b, fill = "darkgoldenrod", width = 0)
    rectangle3 = s.create_rectangle(xSpaceShip3a, ySpaceShip3a, xSpaceShip3b, ySpaceShip3b, fill = "goldenrod", width = 0)
    triangle3 = s.create_polygon(xSpaceShipa, ySpaceShipa, xSpaceShipb, ySpaceShipb, xSpaceShipc, ySpaceShipc, fill = "goldenrod", width = 0)
    triangle4 = s.create_polygon(xSpaceShipa1, ySpaceShipa1, xSpaceShipb1, ySpaceShipb1, xSpaceShipc1, ySpaceShipc1, fill = "goldenrod", width = 0)
    rectangle4 = s.create_rectangle(xSpaceShip6a, ySpaceShip6a, xSpaceShip6b, ySpaceShip6b, fill = colour)
    rectangle5 = s.create_rectangle(xSpaceShip7a, ySpaceShip7a, xSpaceShip7b, ySpaceShip7b, fill = colour)
    rectangle6 = s.create_rectangle(xSpaceShip8a, ySpaceShip8a, xSpaceShip8b, ySpaceShip8b, fill = colour)
    rectangle7 = s.create_rectangle(xSpaceShip9a, ySpaceShip9a, xSpaceShip9b, ySpaceShip9b, fill = colour)
    rectangle8 = s.create_rectangle(xSpaceShip10a, ySpaceShip10a, xSpaceShip10b, ySpaceShip10b, fill = armColour, width = 0)
    rectangle9 = s.create_rectangle(xSpaceShip11a, ySpaceShip11a, xSpaceShip11b, ySpaceShip11b, fill = armColour,width = 0)
    triangle1 = s.create_polygon(xSpaceShip4a, ySpaceShip4a, xSpaceShip4b, ySpaceShip4b, xSpaceShip4c, ySpaceShip4c, fill = "darkgoldenrod")
    triangle2 = s.create_polygon(xSpaceShip5a, ySpaceShip5a, xSpaceShip5b, ySpaceShip5b, xSpaceShip5c, ySpaceShip5c, fill = "darkgoldenrod")


    
    s.update()
    sleep(0.03)
    s.delete(rectangle8, rectangle9, )
    s.delete( rectangle5, rectangle5, rectangle7, rectangleMinus3, rectangleMinus2, triangleMinus4, rectangleMinus1, rectangle1, rectangle2, rectangle3, triangle4  )


    for i in range(0, numStars):
        s.delete( starDrawings[i] )
    for i in range(0,numFlames): 
        s.delete( flameDrawings[i] )
    for i in range(0,numEnergy): 
        s.delete( energyDrawings[i] )
        
#spaceship slowing down to a stop
for f in range(20):
    colour = "grey50"
    for i in range(0, numStars):
        r = randint(-1,2)
        starDrawings[i] = s.create_oval(xStar[i]-r, yStar[i]-r, xStar[i]+r, yStar[i]+r,fill="white", width = 0)
        xStar[i] = xStar[i] - starSpeed
        if xStar[i] < 0:
            xStar[i] = 1000
    for i in range(0, numFlames):
        flameN = randint(0, 7)
        flameColourChoice = flameColours[flameN]
        flameDrawings[i] = s.create_oval( xFlame2 - 40, yFlame1[i], xFlame2, yFlame1[i] + 5, fill=flameColourChoice, width = 0)
                                                                                                         



    rectangleMinus3 = s.create_rectangle(xSpaceShipMinus5a, ySpaceShipMinus5a, xSpaceShipMinus5b, ySpaceShipMinus5b, fill = "dimgrey", width = 0)
    rectangleMinus2 = s.create_rectangle(xSpaceShipMinus2a, ySpaceShipMinus2a, xSpaceShipMinus2b, ySpaceShipMinus2b, fill = "goldenrod", width = 0)
    triangleMinus4 = s.create_polygon(xSpaceShipMinus4a, ySpaceShipMinus4a, xSpaceShipMinus4b, ySpaceShipMinus4b, xSpaceShipMinus4c, ySpaceShipMinus4c, fill = "darkgoldenrod", width = 0)
    triangleMinus3 = s.create_polygon(xSpaceShipMinus3a, ySpaceShipMinus3a, xSpaceShipMinus3b, ySpaceShipMinus3b, xSpaceShipMinus3c, ySpaceShipMinus3c, fill = "darkgoldenrod", width = 0)
    rectangleMinus1 = s.create_rectangle(xSpaceShipMinus1a, ySpaceShipMinus1a, xSpaceShipMinus1b, ySpaceShipMinus1b, fill = "darkgoldenrod", width = 0)
    rectangle1 = s.create_rectangle(xSpaceShip1a, ySpaceShip1a, xSpaceShip1b, ySpaceShip1b, fill = "goldenrod", width = 0)
    rectangle2 = s.create_rectangle(xSpaceShip2a, ySpaceShip2a, xSpaceShip2b, ySpaceShip2b, fill = "darkgoldenrod", width = 0)
    rectangle3 = s.create_rectangle(xSpaceShip3a, ySpaceShip3a, xSpaceShip3b, ySpaceShip3b, fill = "goldenrod", width = 0)
    triangle3 = s.create_polygon(xSpaceShipa, ySpaceShipa, xSpaceShipb, ySpaceShipb, xSpaceShipc, ySpaceShipc, fill = "goldenrod", width = 0)
    triangle4 = s.create_polygon(xSpaceShipa1, ySpaceShipa1, xSpaceShipb1, ySpaceShipb1, xSpaceShipc1, ySpaceShipc1, fill = "goldenrod", width = 0)
    rectangle4 = s.create_rectangle(xSpaceShip6a, ySpaceShip6a, xSpaceShip6b, ySpaceShip6b, fill = colour)
    rectangle5 = s.create_rectangle(xSpaceShip7a, ySpaceShip7a, xSpaceShip7b, ySpaceShip7b, fill = colour)
    rectangle6 = s.create_rectangle(xSpaceShip8a, ySpaceShip8a, xSpaceShip8b, ySpaceShip8b, fill = colour)
    rectangle7 = s.create_rectangle(xSpaceShip9a, ySpaceShip9a, xSpaceShip9b, ySpaceShip9b, fill = colour)
    rectangle8 = s.create_rectangle(xSpaceShip10a, ySpaceShip10a, xSpaceShip10b, ySpaceShip10b, fill = armColour, width = 0)
    rectangle9 = s.create_rectangle(xSpaceShip11a, ySpaceShip11a, xSpaceShip11b, ySpaceShip11b, fill = armColour,width = 0)
    triangle1 = s.create_polygon(xSpaceShip4a, ySpaceShip4a, xSpaceShip4b, ySpaceShip4b, xSpaceShip4c, ySpaceShip4c, fill = "darkgoldenrod")
    triangle2 = s.create_polygon(xSpaceShip5a, ySpaceShip5a, xSpaceShip5b, ySpaceShip5b, xSpaceShip5c, ySpaceShip5c, fill = "darkgoldenrod")
    planet = s.create_oval(planetX + pr, planetY + pr, planetX - pr, planetY - pr, fill = "brown")
    planetX = planetX - starSpeed



    xFlame2 = xFlame2 + 1.5 # shrinking the flames until nothing
    
    if f > 9:
        if starSpeed > 0:
            starSpeed = starSpeed - 0.75 #slowing down the star speed
            
        else:
            starSpeed = 0 # makes sure that starspeed doesnt become negative and stars move oppisite direction
            
    
        
    
    

    s.update()
    sleep(0.03)
    s.delete(rectangle8, rectangle9, )
    s.delete(planet, rectangle5, rectangle5, rectangle7, rectangleMinus3, rectangleMinus2, triangleMinus4, rectangleMinus1, rectangle1, rectangle2, rectangle3, triangle4  )


    for i in range(0, numStars):
        s.delete( starDrawings[i] )
    for i in range(0,numFlames): 
        s.delete( flameDrawings[i] )
    for i in range(0,numEnergy): 
        s.delete( energyDrawings[i] )
    
#spaceship "charging up"
for f in range(130):
    
    #changing the length of the spaceship arms
    xSpaceShip10a = xSpaceShipOrigin + 206 - armLength
    ySpaceShip10a = ySpaceShipOrigin - 100

    xSpaceShip10b = xSpaceShipOrigin + 214 + armLength
    ySpaceShip10b = ySpaceShipOrigin - 25

    xSpaceShip11a = xSpaceShipOrigin + 206 - armLength
    ySpaceShip11a = ySpaceShipOrigin + 100

    xSpaceShip11b = xSpaceShipOrigin + 214 + armLength
    ySpaceShip11b = ySpaceShipOrigin + 25 
    

        
                                                                             

    for i in range(0, numStars):
        starArm = 1
        r = randint(-1,2)
        starDrawings[i] = s.create_oval(xStar[i]-r, yStar[i]-r, xStar[i]+r, yStar[i]+r,fill="white", width = 0)
        if xStar[i] < 0:
            xStar[i] = 1000
    if f > 110:
        colour4 = "blue"
        colour3 = "blue"
        colour2 = "blue"
        colour1 = "blue"
        armColour = "blue"
    if f >= 90:
        colour4 = "blue"
        colour3 = "blue"
        colour2 = "blue"
        colour1 = "blue"

    elif f >= 70:
        colour3 = "blue"
        colour2 = "blue"
        colour1 = "blue"
    elif f > 60:
        colour2 = "blue"
        colour1 = "blue"
        
    elif f >= 40:
        colour2 = "blue"
        colour1 = "blue"

    elif f >= 20:
        colour1 = "blue"
    else:
        colour4 = "grey50"
        colour3 = "grey50"
        colour2 = "grey50"
        colour1 = "grey50"
        armColour = "grey50"
    
    #creating the spaceship
    rectangleMinus3 = s.create_rectangle(xSpaceShipMinus5a, ySpaceShipMinus5a, xSpaceShipMinus5b, ySpaceShipMinus5b, fill = "dimgrey", width = 0)
    rectangleMinus2 = s.create_rectangle(xSpaceShipMinus2a, ySpaceShipMinus2a, xSpaceShipMinus2b, ySpaceShipMinus2b, fill = "goldenrod", width = 0)
    triangleMinus4 = s.create_polygon(xSpaceShipMinus4a, ySpaceShipMinus4a, xSpaceShipMinus4b, ySpaceShipMinus4b, xSpaceShipMinus4c, ySpaceShipMinus4c, fill = "darkgoldenrod", width = 0)
    triangleMinus3 = s.create_polygon(xSpaceShipMinus3a, ySpaceShipMinus3a, xSpaceShipMinus3b, ySpaceShipMinus3b, xSpaceShipMinus3c, ySpaceShipMinus3c, fill = "darkgoldenrod", width = 0)
    rectangleMinus1 = s.create_rectangle(xSpaceShipMinus1a, ySpaceShipMinus1a, xSpaceShipMinus1b, ySpaceShipMinus1b, fill = "darkgoldenrod", width = 0)
    rectangle1 = s.create_rectangle(xSpaceShip1a, ySpaceShip1a, xSpaceShip1b, ySpaceShip1b, fill = "goldenrod", width = 0)
    rectangle2 = s.create_rectangle(xSpaceShip2a, ySpaceShip2a, xSpaceShip2b, ySpaceShip2b, fill = "darkgoldenrod", width = 0)
    rectangle3 = s.create_rectangle(xSpaceShip3a, ySpaceShip3a, xSpaceShip3b, ySpaceShip3b, fill = "goldenrod", width = 0)
    triangle3 = s.create_polygon(xSpaceShipa, ySpaceShipa, xSpaceShipb, ySpaceShipb, xSpaceShipc, ySpaceShipc, fill = "goldenrod", width = 0)
    triangle4 = s.create_polygon(xSpaceShipa1, ySpaceShipa1, xSpaceShipb1, ySpaceShipb1, xSpaceShipc1, ySpaceShipc1, fill = "goldenrod", width = 0)
    rectangle4 = s.create_rectangle(xSpaceShip6a, ySpaceShip6a, xSpaceShip6b, ySpaceShip6b, fill = colour1)
    rectangle5 = s.create_rectangle(xSpaceShip7a, ySpaceShip7a, xSpaceShip7b, ySpaceShip7b, fill = colour2)
    rectangle6 = s.create_rectangle(xSpaceShip8a, ySpaceShip8a, xSpaceShip8b, ySpaceShip8b, fill = colour3)
    rectangle7 = s.create_rectangle(xSpaceShip9a, ySpaceShip9a, xSpaceShip9b, ySpaceShip9b, fill = colour4)
    rectangle8 = s.create_rectangle(xSpaceShip10a, ySpaceShip10a, xSpaceShip10b, ySpaceShip10b, fill = armColour, width = 0)
    rectangle9 = s.create_rectangle(xSpaceShip11a, ySpaceShip11a, xSpaceShip11b, ySpaceShip11b, fill = armColour,width = 0)
    triangle1 = s.create_polygon(xSpaceShip4a, ySpaceShip4a, xSpaceShip4b, ySpaceShip4b, xSpaceShip4c, ySpaceShip4c, fill = "darkgoldenrod")
    triangle2 = s.create_polygon(xSpaceShip5a, ySpaceShip5a, xSpaceShip5b, ySpaceShip5b, xSpaceShip5c, ySpaceShip5c, fill = "darkgoldenrod")
    planet = s.create_oval(planetX + pr, planetY + pr, planetX - pr, planetY - pr, fill = "brown")



    
    s.update()
    sleep(0.03)
    s.delete(rectangle8, rectangle9, )
    s.delete( planet, rectangle5, rectangle5, rectangle7, rectangleMinus3, rectangleMinus2, triangleMinus4, rectangleMinus1, rectangle1, rectangle2, rectangle3, triangle4  )


    for i in range(0, numStars):
        s.delete( starDrawings[i] )
    for i in range(0,numEnergy): 
        s.delete( energyDrawings[i] )


#spaceship gathering beam   
for f in range(50):


    
    xSpaceShip10a = xSpaceShipOrigin + 209 - armLength
    ySpaceShip10a = ySpaceShipOrigin - 100

    xSpaceShip10b = xSpaceShipOrigin + 210 + armLength
    ySpaceShip10b = ySpaceShipOrigin - 25

    xSpaceShip11a = xSpaceShipOrigin + 209 - armLength
    ySpaceShip11a = ySpaceShipOrigin + 100

    xSpaceShip11b = xSpaceShipOrigin + 210 + armLength
    ySpaceShip11b = ySpaceShipOrigin + 25 
    
    for i in range(50):        
        armLength = randint(2,5)
        armColour = "Blue"

    for i in range(0, numStars):
        r = randint(-1,2)
        starDrawings[i] = s.create_oval(xStar[i]-r, yStar[i]-r, xStar[i]+r, yStar[i]+r,fill="white", width = 0)
        if xStar[i] < 0:
            xStar[i] = 1000
    for i in range(0, numEnergy):
        energyN = randint(0,4)
        energyColour = blues[energyN]
        energyR = randint ( 1, 2)
        energyDrawings[i] = s.create_oval(xEnergy[i]-energyR, yEnergy[i]-energyR, xEnergy[i]+energyR, yEnergy[i]+energyR, fill=energyColour, width = 0)
        xEnergy[i] = xEnergy[i] + xEnergySpeed[i] #making the energy balls go towards the energy point
        yEnergy[i] = yEnergy[i] + yEnergySpeed[i]

        
        if energyX - 10 <= xEnergy[i] <= energyX + 10 and energyY - 10 <= yEnergy[i] <=  energyY + 10: #stopping the energy when it reaches the "gathering point"
            xEnergySpeed[i] = 0
            yEnergySpeed[i] = 0
        
    if r1 < 30:
        r1 = r1 + 0.75
    else:
        r1 = 30
     
 

    colour = "blue"
    s.delete( rectangle5, rectangle5, rectangle7, rectangleMinus3, rectangleMinus2, triangleMinus4, rectangleMinus1, rectangle1, rectangle2, rectangle3, triangle4  )

        
    rectangleMinus3 = s.create_rectangle(xSpaceShipMinus5a, ySpaceShipMinus5a, xSpaceShipMinus5b, ySpaceShipMinus5b, fill = "dimgrey", width = 0)
    rectangleMinus2 = s.create_rectangle(xSpaceShipMinus2a, ySpaceShipMinus2a, xSpaceShipMinus2b, ySpaceShipMinus2b, fill = "goldenrod", width = 0)
    triangleMinus4 = s.create_polygon(xSpaceShipMinus4a, ySpaceShipMinus4a, xSpaceShipMinus4b, ySpaceShipMinus4b, xSpaceShipMinus4c, ySpaceShipMinus4c, fill = "darkgoldenrod", width = 0)
    triangleMinus3 = s.create_polygon(xSpaceShipMinus3a, ySpaceShipMinus3a, xSpaceShipMinus3b, ySpaceShipMinus3b, xSpaceShipMinus3c, ySpaceShipMinus3c, fill = "darkgoldenrod", width = 0)
    rectangleMinus1 = s.create_rectangle(xSpaceShipMinus1a, ySpaceShipMinus1a, xSpaceShipMinus1b, ySpaceShipMinus1b, fill = "darkgoldenrod", width = 0)
    rectangle1 = s.create_rectangle(xSpaceShip1a, ySpaceShip1a, xSpaceShip1b, ySpaceShip1b, fill = "goldenrod", width = 0)
    rectangle2 = s.create_rectangle(xSpaceShip2a, ySpaceShip2a, xSpaceShip2b, ySpaceShip2b, fill = "darkgoldenrod", width = 0)
    rectangle3 = s.create_rectangle(xSpaceShip3a, ySpaceShip3a, xSpaceShip3b, ySpaceShip3b, fill = "goldenrod", width = 0)
    triangle3 = s.create_polygon(xSpaceShipa, ySpaceShipa, xSpaceShipb, ySpaceShipb, xSpaceShipc, ySpaceShipc, fill = "goldenrod", width = 0)
    triangle4 = s.create_polygon(xSpaceShipa1, ySpaceShipa1, xSpaceShipb1, ySpaceShipb1, xSpaceShipc1, ySpaceShipc1, fill = "goldenrod", width = 0)
    rectangle4 = s.create_rectangle(xSpaceShip6a, ySpaceShip6a, xSpaceShip6b, ySpaceShip6b, fill = colour)
    rectangle5 = s.create_rectangle(xSpaceShip7a, ySpaceShip7a, xSpaceShip7b, ySpaceShip7b, fill = colour)
    rectangle6 = s.create_rectangle(xSpaceShip8a, ySpaceShip8a, xSpaceShip8b, ySpaceShip8b, fill = colour)
    rectangle7 = s.create_rectangle(xSpaceShip9a, ySpaceShip9a, xSpaceShip9b, ySpaceShip9b, fill = colour)
    rectangle8 = s.create_rectangle(xSpaceShip10a, ySpaceShip10a, xSpaceShip10b, ySpaceShip10b, fill = armColour, width = 0)
    rectangle9 = s.create_rectangle(xSpaceShip11a, ySpaceShip11a, xSpaceShip11b, ySpaceShip11b, fill = armColour,width = 0)
    triangle1 = s.create_polygon(xSpaceShip4a, ySpaceShip4a, xSpaceShip4b, ySpaceShip4b, xSpaceShip4c, ySpaceShip4c, fill = "darkgoldenrod")
    triangle2 = s.create_polygon(xSpaceShip5a, ySpaceShip5a, xSpaceShip5b, ySpaceShip5b, xSpaceShip5c, ySpaceShip5c, fill = "darkgoldenrod")

    planet = s.create_oval(planetX + pr, planetY + pr, planetX - pr, planetY - pr, fill = "brown")

    energyBall1 = s.create_oval(energyX + r1, energyY + r1, energyX - r1, energyY - r1, fill = energyColour)
    


    s.update()
    sleep(0.03)
    s.delete(energyBall1, rectangle8, rectangle9, )
    s.delete( rectangle5, rectangle5, rectangle7, rectangleMinus3, rectangleMinus2, triangleMinus4, rectangleMinus1, rectangle1, rectangle2, rectangle3, triangle4  )

    
    for i in range(0, numStars):
        s.delete( starDrawings[i] )

    for i in range(0,numEnergy): 
        s.delete( energyDrawings[i] )
        



#spaceship shooting laser       
for f in range (50):

    #rectangle10
    
    xSpaceShip10a = xSpaceShipOrigin + 209 - armLength
    ySpaceShip10a = ySpaceShipOrigin - 100

    xSpaceShip10b = xSpaceShipOrigin + 210 + armLength
    ySpaceShip10b = ySpaceShipOrigin - 25

    #rectangle9
    xSpaceShip11a = xSpaceShipOrigin + 209 - armLength
    ySpaceShip11a = ySpaceShipOrigin + 100

    xSpaceShip11b = xSpaceShipOrigin + 210 + armLength
    ySpaceShip11b = ySpaceShipOrigin + 25
    
    if f < 5: #as the frames go up the number of frames the boxes are blue go down creating a slowing down flicker look
        if f % 2 == 0:
            armColour = "blue"
            colour = "blue"
            for i in range(100):
                    armLength = randint(2,5)
        else:
            armColour = "grey50"
            colour = "grey50"


    elif f < 10:
        if f % 3 == 0:
            armColour = "blue"
            colour = "blue"
            for i in range(100):
                    armLength = randint(2,5)
        else:
                armColour = "grey50"
                colour = "grey50"
            

    elif f < 15:
        if f % 4 == 0:
            armColour = "blue"
            colour = "blue"
            for i in range(100):
                    armLength = randint(2,5)
        else:
                armColour = "grey50"
                colour = "grey50"
        

    else:
        for i in range(100):
            armColour = "grey50"
            armLength = 5
        colour = "grey50"

        
        
    for i in range(0, numStars):
        r = randint(-1,2)
        starDrawings[i] = s.create_oval(xStar[i]-r, yStar[i]-r, xStar[i]+r, yStar[i]+r,fill="white", width = 0)
        if xStar[i] < 0:
            xStar[i] = 1000
    r1 = 0
    for i in range(0, numLasers):
        laserLength = randint(50, 75)
        laserSpeed = randint(10, 20)
        energyN = randint(0,4)
        energyColour = blues[energyN]
        laserDrawings[i] = s.create_line(xLaser[i], yLaser[i], xLaser[i] + laserLength, yLaser[i],fill=energyColour)
        xLaser[i] = xLaser[i] + laserSpeed

        if xLaser[i] > 875: #shrinking the laser when it gets to the planet
            xLaser[i] = 2000
            laserSpeed = 0
            planetColour = energyColour
            pr = pr - 0.2 #shrinking the planet
            if pr < 0:
                pr = 0
        planet = s.create_oval(planetX + pr, planetY + pr, planetX - pr, planetY - pr, fill = planetColour)
        s.update
                        

              
    
        
         
    rectangleMinus3 = s.create_rectangle(xSpaceShipMinus5a, ySpaceShipMinus5a, xSpaceShipMinus5b, ySpaceShipMinus5b, fill = "dimgrey", width = 0)
    rectangleMinus2 = s.create_rectangle(xSpaceShipMinus2a, ySpaceShipMinus2a, xSpaceShipMinus2b, ySpaceShipMinus2b, fill = "goldenrod", width = 0)
    triangleMinus4 = s.create_polygon(xSpaceShipMinus4a, ySpaceShipMinus4a, xSpaceShipMinus4b, ySpaceShipMinus4b, xSpaceShipMinus4c, ySpaceShipMinus4c, fill = "darkgoldenrod", width = 0)
    triangleMinus3 = s.create_polygon(xSpaceShipMinus3a, ySpaceShipMinus3a, xSpaceShipMinus3b, ySpaceShipMinus3b, xSpaceShipMinus3c, ySpaceShipMinus3c, fill = "darkgoldenrod", width = 0)
    rectangleMinus1 = s.create_rectangle(xSpaceShipMinus1a, ySpaceShipMinus1a, xSpaceShipMinus1b, ySpaceShipMinus1b, fill = "darkgoldenrod", width = 0)
    rectangle1 = s.create_rectangle(xSpaceShip1a, ySpaceShip1a, xSpaceShip1b, ySpaceShip1b, fill = "goldenrod", width = 0)
    rectangle2 = s.create_rectangle(xSpaceShip2a, ySpaceShip2a, xSpaceShip2b, ySpaceShip2b, fill = "darkgoldenrod", width = 0)
    rectangle3 = s.create_rectangle(xSpaceShip3a, ySpaceShip3a, xSpaceShip3b, ySpaceShip3b, fill = "goldenrod", width = 0)
    triangle3 = s.create_polygon(xSpaceShipa, ySpaceShipa, xSpaceShipb, ySpaceShipb, xSpaceShipc, ySpaceShipc, fill = "goldenrod", width = 0)
    triangle4 = s.create_polygon(xSpaceShipa1, ySpaceShipa1, xSpaceShipb1, ySpaceShipb1, xSpaceShipc1, ySpaceShipc1, fill = "goldenrod", width = 0)
    rectangle4 = s.create_rectangle(xSpaceShip6a, ySpaceShip6a, xSpaceShip6b, ySpaceShip6b, fill = colour)
    rectangle5 = s.create_rectangle(xSpaceShip7a, ySpaceShip7a, xSpaceShip7b, ySpaceShip7b, fill = colour)
    rectangle6 = s.create_rectangle(xSpaceShip8a, ySpaceShip8a, xSpaceShip8b, ySpaceShip8b, fill = colour)
    rectangle7 = s.create_rectangle(xSpaceShip9a, ySpaceShip9a, xSpaceShip9b, ySpaceShip9b, fill = colour)
    rectangle8 = s.create_rectangle(xSpaceShip10a, ySpaceShip10a, xSpaceShip10b, ySpaceShip10b, fill = armColour, width = 0)
    rectangle9 = s.create_rectangle(xSpaceShip11a, ySpaceShip11a, xSpaceShip11b, ySpaceShip11b, fill = armColour,width = 0)
    triangle1 = s.create_polygon(xSpaceShip4a, ySpaceShip4a, xSpaceShip4b, ySpaceShip4b, xSpaceShip4c, ySpaceShip4c, fill = "darkgoldenrod")
    triangle2 = s.create_polygon(xSpaceShip5a, ySpaceShip5a, xSpaceShip5b, ySpaceShip5b, xSpaceShip5c, ySpaceShip5c, fill = "darkgoldenrod")
    energyBall1 = s.create_oval(energyX + r1, energyY + r1, energyX - r1, energyY - r1, fill = energyColour)

    s.update()
    sleep(0.03)
    
    s.delete(energyBall1, rectangle8, rectangle9,)
    s.delete( rectangle5, rectangle5, rectangle7, rectangleMinus3, rectangleMinus2, triangleMinus4, rectangleMinus1, rectangle1, rectangle2, rectangle3, triangle4  )
    for i in range(0, numStars):
        s.delete( starDrawings[i] )

    for i in range(0,numLasers): 
        s.delete( laserDrawings[i] )

s.create_rectangle(0 , 0, 1000, 1000, fill = "black")


