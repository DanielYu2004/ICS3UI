#################################################################
#                                                               #
#   Hyunzee Kim                                                 #
#   The Four Seasons                                            #
#   November 9th, 2017                                          #
#                                                               #
#################################################################

from tkinter import *
from random import*
from math import*
from time import*
master = Tk()
s = Canvas( master, width = 600, height = 700)
s.pack()


while True: #Keep the four seasons going on forever

    
    #=======================================#
    #                 SPRING                #
    #=======================================#


    #Draw the sky
    s.create_rectangle(0, 0, 600, 57, fill = "RoyalBlue4", outline = "RoyalBlue4")
    s.create_rectangle(0, 57, 600, 57*2, fill = "RoyalBlue3", outline = "RoyalBlue3")
    s.create_rectangle(0, 57*2, 600, 57*3, fill = "RoyalBlue2", outline = "RoyalBlue2")
    s.create_rectangle(0, 57*3, 600, 57*4, fill = "RoyalBlue1", outline = "RoyalBlue1")
    s.create_rectangle(0, 57*4, 600, 57*5, fill = "DodgerBlue2", outline = "DodgerBlue2")
    s.create_rectangle(0, 57*5, 600, 57*6, fill = "SteelBlue2", outline = "SteelBlue2")
    s.create_rectangle(0, 57*6, 600, 57*7, fill = "SkyBlue2", outline = "SkyBlue2")
    s.create_rectangle(0, 57*7, 600, 57*8, fill = "SkyBlue1", outline = "SkyBlue1")
    s.create_rectangle(0, 57*8, 600, 57*9, fill = "LightBlue2", outline = "LightBlue2")
    s.create_rectangle(0, 57*9, 600, 57*10, fill = "LightBlue1", outline = "LightBlue1")

    #Draw sun
    s.create_oval(200, 25, 400, 225, fill = "yellow", outline = "yellow")

    #Draw two trees
    s.create_oval(-100, 75, 100, 300, fill = "pink", outline = "pink")
    s.create_oval(50, 100, 200, 250, fill = "pink", outline = "pink")
    s.create_oval(0, 220, 200, 350, fill = "pink", outline = "pink")

    s.create_oval(700, 75, 500, 300, fill = "pink", outline = "pink")
    s.create_oval(550, 100, 400, 250, fill = "pink", outline = "pink")
    s.create_oval(600, 220, 400, 350, fill = "pink", outline = "pink")

    s.create_rectangle(0, 700, 75, 250, fill = "sienna4", outline = "sienna4")
    s.create_rectangle(600, 700, 525, 250, fill = "sienna4", outline = "sienna4")

    s.create_polygon(75, 250, 175, 250, 75, 275, fill = "sienna4", outline = "sienna4")
    s.create_polygon(75, 250, 125, 150, 75/2, 250, fill = "sienna4", outline = "sienna4")
    s.create_polygon(0, 250, 75/2, 250, 0, 125, fill = "sienna4", outline = "sienna4")

    s.create_polygon(525, 250, 425, 250, 525, 275, fill = "sienna4", outline = "sienna4")
    s.create_polygon(525, 250, 475, 150, 525+75/2, 250, fill = "sienna4", outline = "sienna4")
    s.create_polygon(600, 250, 525+75/2, 250, 600, 125, fill = "sienna4", outline = "sienna4")

    #Draw hill
    s.create_oval(-50, 450, 650, 1150, fill = "forest green", outline = "forest green")

    #Draw randomized pattern of flowers on the hill
    for n in range(0, 15):
        diameter = randint(10,12)
        circleX = randint(50, 550)
        circleY = randint(550, 650)
        circleX2 = circleX + diameter
        circleY2 = circleY + diameter

        petalX = circleX-10
        petalY = circleY-10
        petalX2 = circleX+5
        petalY2 = circleY+5

        petal1 = s.create_oval(petalX, petalY, petalX2, petalY2, fill = "red", outline = "red")
        petal2 = s.create_oval(petalX2, petalY-2, petalX2+diameter, petalY2-2, fill = "red", outline = "red")
        petal3 = s.create_oval(petalX2+5, petalY2-2, petalX2+diameter+5, petalY2+diameter, fill = "red", outline = "red")
        petal4 = s.create_oval(petalX2-5, petalY2+5, petalX2+10, petalY2+20, fill = "red", outline = "red")
        petal5 = s.create_oval(petalX, petalY+diameter, petalX2, petalY2+diameter, fill = "red", outline = "red")

        center = s.create_oval(circleX, circleY, circleX2, circleY2, fill="yellow", outline = "yellow")

    #SPRING BLOSSOMS FALLING
    #Initial values
    hillRadius = 350
    numBlossoms = 30
    
    xBlossoms = []
    yBlossoms = []
    blossoms = []
    xBlossomsSpeed = []
    yBlossomsSpeed = []

    #Append values to arrays
    for i in range(numBlossoms):
        if i % 2 == 0:#Blossoms falling from the left tree
            xBlossoms.append(randint(50, 200))

        else: #Blossoms falling from the right tree
            xBlossoms.append(randint(400, 550))

        yBlossoms.append(randint(100,300))
        xBlossomsSpeed.append(uniform(-0.7, 0.7))
        yBlossomsSpeed.append(uniform(1.5, 2.5))
        blossoms.append(0)
       
    
    #Draw blossoms
    for f in range(300):
        for i in range(numBlossoms):
            blossoms[i] = s.create_polygon(xBlossoms[i], yBlossoms[i], xBlossoms[i]+10, yBlossoms[i]+30, xBlossoms[i]+30, yBlossoms[i]+20, fill ="pink", outline = "pink", smooth = True)
            distanceToBlossom = sqrt((300 - xBlossoms[i])**2 + (800 - yBlossoms[i])**2)    #Distance from this blossom to the center of the hill (300,800).
            
            #If the distance from the center of the hill to the blossom is smaller than the hill's radius, then (maybe) stop the blossom
            if distanceToBlossom <= hillRadius:
                dieRoll = randint(1, 100)
                
                if dieRoll <= 4:  #4% chance of stopping in this frame
                    xBlossomsSpeed[i] = 0
                    yBlossomsSpeed[i] = 0

                else:  #96% chance of not stopping
                    xBlossoms[i] = xBlossoms[i] + xBlossomsSpeed[i]
                    yBlossoms[i] = yBlossoms[i] + yBlossomsSpeed[i]

            #...but if the distance from the center of the hill to the blossom is larger than the radius, then the blossom continues to fall in this frame
            else:
                xBlossoms[i] = xBlossoms[i] + xBlossomsSpeed[i]
                yBlossoms[i] = yBlossoms[i] + yBlossomsSpeed[i]
                
        s.update()
        sleep(0.03)

        for i in range(numBlossoms):
            s.delete(blossoms[i])

    #Scene changes to summer
    sleep(0.001)
    s.delete


    #=======================================#
    #                 SUMMER                #
    #=======================================#


    #Draw the sky
    s.create_rectangle(0, 0, 600, 57, fill = "gray40", outline = "gray40")
    s.create_rectangle(0, 57, 600, 57*2, fill = "gray42", outline = "gray42")
    s.create_rectangle(0, 57*2, 600, 57*3, fill = "gray44", outline = "gray44")
    s.create_rectangle(0, 57*3, 600, 57*4, fill = "gray46", outline = "gray46")
    s.create_rectangle(0, 57*4, 600, 57*5, fill = "gray48", outline = "gray48")
    s.create_rectangle(0, 57*5, 600, 57*6, fill = "gray50", outline = "gray50")
    s.create_rectangle(0, 57*6, 600, 57*7, fill = "gray52", outline = "gray52")
    s.create_rectangle(0, 57*7, 600, 57*8, fill = "gray54", outline = "gray54")
    s.create_rectangle(0, 57*8, 600, 57*9, fill = "gray56", outline = "gray56")
    s.create_rectangle(0, 57*9, 600, 57*10, fill = "gray58", outline = "gray58")

    #Draw two trees
    s.create_oval(-100, 75, 100, 300, fill = "sea green", outline = "sea green")
    s.create_oval(50, 100, 200, 250, fill = "sea green", outline = "sea green")
    s.create_oval(0, 220, 200, 350, fill = "sea green", outline = "sea green")

    s.create_oval(700, 75, 500, 300, fill = "sea green", outline = "sea green")
    s.create_oval(550, 100, 400, 250, fill = "sea green", outline = "sea green")
    s.create_oval(600, 220, 400, 350, fill = "sea green", outline = "sea green")

    s.create_rectangle(0, 700, 75, 250, fill = "sienna4", outline = "sienna4")
    s.create_rectangle(600, 700, 525, 250, fill = "sienna4", outline = "sienna4")

    s.create_polygon(75, 250, 175, 250, 75, 275, fill = "sienna4", outline = "sienna4")
    s.create_polygon(75, 250, 125, 150, 75/2, 250, fill = "sienna4", outline = "sienna4")
    s.create_polygon(0, 250, 75/2, 250, 0, 125, fill = "sienna4", outline = "sienna4")

    s.create_polygon(525, 250, 425, 250, 525, 275, fill = "sienna4", outline = "sienna4")
    s.create_polygon(525, 250, 475, 150, 525+75/2, 250, fill = "sienna4", outline = "sienna4")
    s.create_polygon(600, 250, 525+75/2, 250, 600, 125, fill = "sienna4", outline = "sienna4")

    #Draw hill
    s.create_oval(-50, 450, 650, 1150, fill = "forest green", outline = "forest green")

    #Draw randomized pattern of grass on the hill
    for n in range(0, 20):
         x = randint(50, 550)
         y = randint(550, 700)
         x2 = x + 5
         y2 = y - 5
         x3 = x2
         y3 = y2
         x4 = x3 + 5
         y4 = y3 + 5
         x5 = x4
         y5 = y4
         x6 = x5 + 5
         y6 = y5 - 5
         x7 = x6
         y7 = y6
         x8 = x7 + 5
         y8 = y7 + 5

         #Draw the grass
         s.create_line(x, y, x2, y2, fill = "black")
         s.create_line(x3, y3, x4, y4, fill = "black")
         s.create_line(x5, y5, x6, y6, fill = "black")
         s.create_line(x7, y7, x8, y8, fill = "black")

    #SUMMER RAIN
    #Initial values
    numRain = 250
    xRain = []
    yRain = []
    ySpeedRain = []
    rain = []

    #Append values to arrays
    for i in range(numRain):
        xRain.append(randint(-100,600))
        yRain.append(randint(-1000,-100))
        ySpeedRain.append(randint(4,10))
        rain.append(0)

    #Draw and animate the summer rain to fall
    for f in range(500):
        for i in range(numRain):
            rain[i] = s.create_line(xRain[i], yRain[i], xRain[i]+20, yRain[i]+100, fill = "blue")
            xRain[i] = xRain[i] + 1
            yRain[i] = yRain[i] + ySpeedRain[i]
            
            #Delete rain when it hits the hill
            if yRain[i] >= 500:
                s.delete(rain[i])
                
        s.update()
        sleep(0.005)
        
        for i in range(numRain):
            s.delete(rain[i])

    #Scene changes to fall
    sleep(0.3)
    s.delete


    #=======================================#
    #                 FALL                  #
    #=======================================#


    #Draw the sunset
    s.create_rectangle(0, 0, 600, 57, fill = "DarkOrchid4", outline = "DarkOrchid4")
    s.create_rectangle(0, 57, 600, 57*2, fill = "MediumOrchid4", outline = "MediumORchid4")
    s.create_rectangle(0, 57*2, 600, 57*3, fill = "orchid4", outline = "orchid4")
    s.create_rectangle(0, 57*3, 600, 57*4, fill = "MediumOrchid3", outline = "MediumORchid3")
    s.create_rectangle(0, 57*4, 600, 57*5, fill = "MediumOrchid2", outline = "MediumORchid2")
    s.create_rectangle(0, 57*5, 600, 57*6, fill = "orchid3", outline = "orchid3")
    s.create_rectangle(0, 57*6, 600, 57*7, fill = "orchid2", outline = "orchid2")
    s.create_rectangle(0, 57*7, 600, 57*8, fill = "LightPink2", outline = "LightPink2")
    s.create_rectangle(0, 57*8, 600, 57*9, fill = "LightPink1", outline = "LightPink1")
    s.create_rectangle(0, 57*9, 600, 57*10, fill = "pink1", outline = "pink1")

    #Draw sun
    s.create_oval(200, 375, 400, 575, fill = "yellow", outline = "yellow")

    #Draw two trees
    treeLeaves1 = s.create_oval(-100, 75, 100, 300, fill = "DarkOrange3", outline = "DarkOrange3")
    treeLeaves2 = s.create_oval(50, 100, 200, 250, fill = "DarkOrange3", outline = "DarkOrange3")
    treeLeaves3 = s.create_oval(0, 220, 200, 350, fill = "DarkOrange3", outline = "DarkOrange3")

    treeLeaves4 = s.create_oval(700, 75, 500, 300, fill = "DarkOrange3", outline = "DarkOrange3")
    treeLeaves5 = s.create_oval(550, 100, 400, 250, fill = "DarkOrange3", outline = "DarkOrange3")
    treeLeaves6 = s.create_oval(600, 220, 400, 350, fill = "DarkOrange3", outline = "DarkOrange3")

    s.create_rectangle(0, 700, 75, 250, fill = "sienna4", outline = "sienna4")
    s.create_rectangle(600, 700, 525, 250, fill = "sienna4", outline = "sienna4")

    s.create_polygon(75, 250, 175, 250, 75, 275, fill = "sienna4", outline = "sienna4")
    s.create_polygon(75, 250, 125, 150, 75/2, 250, fill = "sienna4", outline = "sienna4")
    s.create_polygon(0, 250, 75/2, 250, 0, 125, fill = "sienna4", outline = "sienna4")

    s.create_polygon(525, 250, 425, 250, 525, 275, fill = "sienna4", outline = "sienna4")
    s.create_polygon(525, 250, 475, 150, 525+75/2, 250, fill = "sienna4", outline = "sienna4")
    s.create_polygon(600, 250, 525+75/2, 250, 600, 125, fill = "sienna4", outline = "sienna4")

    #Draw hill
    s.create_oval(-50, 450, 650, 1150, fill = "forest green", outline = "forest green")

    #Draw randomized pattern of leaves on the hill
    colours = []

##    for i in range(100):
##         size = randint(5, 10)
##         x = randint(50, 550)
##         y = randint(550, 700)
##         x2 = x + size
##         y2 = y - size
##         x3 = x + size
##         y3 = y
##         colours.append(choice(["red", "orange", "yellow"]))                  
##
##         s.create_polygon(x, y, x2, y2, x3, y3, fill = colours[i], outline = colours[i])

    #FALL LEAVES FALLING
    #Initial values
    #radius = 350
    numLeaves = 200
    
    xLeaves = []
    yLeaves = []
    leaves = []
    xLeavesSpeed = []
    yLeavesSpeed = []
    coloursLeaves = []

    #Append values to arrays
    for i in range(numLeaves):
        if i % 2 == 0: #Leaves falling from the left tree
            xLeaves.append(randint(50, 200))

        else: #Leaves falling from the right tree
            xLeaves.append(randint(400, 550))

        yLeaves.append(randint(100,300))
        xLeavesSpeed.append(randint(-1, 3))
        yLeavesSpeed.append(randint(5, 10))
        coloursLeaves.append(choice(["red", "orange", "yellow"]))
        leaves.append(0)

    #Draw the leaves
    for f in range(150):
        for i in range(numLeaves):
            leaves[i] = s.create_polygon(xLeaves[i], yLeaves[i], xLeaves[i], yLeaves[i]+10, xLeaves[i]+10, yLeaves[i], fill = coloursLeaves[i], outline = coloursLeaves[i])
            distanceToLeaf = sqrt((300 - xLeaves[i])**2 + (800 - yLeaves[i])**2) #distance from the leaf to center of the hill
            
            #When the distance from the center of the hill and the leaf is smaller than the radius, stop the leaves
            if distanceToLeaf <= hillRadius:
                dieRoll = randint(1,100)
                
                if dieRoll <= 3:
                    xLeavesSpeed[i] = 0
                    yLeavesSpeed[i] = 0
                    
                else:
                    xLeaves[i] = xLeaves[i] + xLeavesSpeed[i]
                    yLeaves[i] = yLeaves[i] + yLeavesSpeed[i]

            #While the distance from the center of the hill and the leaf is greater than the radius, leaves fall
            else:
                xLeaves[i] = xLeaves[i] + xLeavesSpeed[i]
                yLeaves[i] = yLeaves[i] + yLeavesSpeed[i]
                
        s.update()
        sleep(0.03)

        for i in range(numLeaves):
            s.delete(leaves[i])
            
    #Scene changes to winter
    sleep(0.001)
    s.delete


    #=======================================#
    #                 WINTER                #
    #=======================================#


    #Draw the sky
    s.create_rectangle(0, 0, 600, 700, fill = "black", outline = "black")

    #Draw randomized pattern of stars in the sky
    for n in range(200):
         size = randint(1, 3)
         x = randint(0, 600)
         y = randint(0, 700)
         x2 = x + size
         y2 = y + size

         s.create_oval(x, y, x2, y2, fill = "yellow", outline = "yellow")

    #Draw two trees without leaves
    s.create_rectangle(0, 700, 75, 250, fill = "sienna4", outline = "sienna4")
    s.create_rectangle(600, 700, 525, 250, fill = "sienna4", outline = "sienna4")

    s.create_polygon(75, 250, 175, 250, 75, 275, fill = "sienna4", outline = "sienna4")
    s.create_polygon(75, 250, 125, 150, 75/2, 250, fill = "sienna4", outline = "sienna4")
    s.create_polygon(0, 250, 75/2, 250, 0, 125, fill = "sienna4", outline = "sienna4")

    s.create_polygon(525, 250, 425, 250, 525, 275, fill = "sienna4", outline = "sienna4")
    s.create_polygon(525, 250, 475, 150, 525+75/2, 250, fill = "sienna4", outline = "sienna4")
    s.create_polygon(600, 250, 525+75/2, 250, 600, 125, fill = "sienna4", outline = "sienna4")

    #Create snow piles on the tree branches
    s.create_polygon(80, 225, 175, 225, 175, 250, 80, 250, fill = "white", outline = "white", smooth = True)
    s.create_polygon(520, 225, 425, 225, 425, 250, 520, 250, fill = "white", outline = "white", smooth = True)

    #Draw hill
    s.create_oval(-50, 450, 650, 1150, fill = "white", outline = "white")

    #HAIL
    #Initial values
    numHail = 800
    xHail = []
    yHail = []
    hail = []
    xHailSpeed = []
    yHailSpeed = []
    coloursHail = []

    #Append values to the arrays
    for i in range(numHail):
        xHailSpeed.append(randint(-5, 5))
        yHailSpeed.append(randint(6, 10))
        xHail.append(randint(0,600))
        yHail.append(randint(-500,100))
        coloursHail.append(choice(["light cyan", "azure", "mint cream"]))
        hail.append(0)

    #Draw and animate the ice pieces to fall
    for f in range(350):
        for i in range(numHail):
            hail[i] = s.create_polygon(xHail[i], yHail[i], xHail[i]-3, yHail[i]+8, xHail[i], yHail[i]+16,xHail[i]+3, yHail[i]+8, fill = coloursHail[i], outline = coloursHail[i])
            xHail[i] = xHail[i] + xHailSpeed[i]
            yHail[i] = yHail[i] + yHailSpeed[i]

        #Delete hail when it hits the hill
            if yHail[i] >= 550:
                s.delete(hail[i])
                
        s.update()
        sleep(0.01)
        
        for i in range(numHail):
            s.delete(hail[i])

    #Scene changes to spring
    sleep(0.01)
    s.delete
