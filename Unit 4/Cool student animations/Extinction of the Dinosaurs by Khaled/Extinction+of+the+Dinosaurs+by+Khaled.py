#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Title: The Cretaceous Period
# Programmer: Khaled Yaakoub Agha
# Date modified: 11 November 2019
# Purpose: What it feels like to be a dinosaur back in the Cretaceous period
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from tkinter import*
from random import *
from time import *
from math import *

myInterface = Tk()
s = Canvas( myInterface, width=800, height=800, background="black" )
s.pack()


# Variables + Empty Arrays + Filled Arrays
numberOfClouds = 50
numberOfStars = 150
xCentre = 425
yCentre = 375
r = 0
g = 0
gap = -10
xLine = []
yLine = []
xLineIncrease = []
yLineIncrease = []
xStars = []
yStars = []
starSize = []
xSpeed = []
LinesDrawn = []
starsDrawn = []
xPolygon1 = [325, 375, 325, 275, 240, 640, 470, 400, 400, 600, 350, 250]
yPolygon2 = [190, 250, 300, 300, 275, 340, 170, 370, 380, 540, 570, 470]
xPolygon=[]
yPolygon=[]
xIncreaseRate = []
yIncreaseRate = []
aS = 0
col = ["#9bb0ff", "#aabfff", "#cad7ff", "#f8f7ff", "#fff4ea", "#ffd2a1", "#ffcc6f" ]
skyColors = ["#97EBF4", "#7AE5F5", "#65DDEF", "#35D6ED"]
dinosaur = PhotoImage(file = "Dinosaur.gif")
xCloud = []
yCloud = []
cloudRadius = []
cloudsDrawn = []
texts = ["What a beautiful day to be alive", "The sun is really bright today", "Hmmm, why is it so warm??", "What is that thing in the sky?", "Why is it getting bigger and bigger each second?", "Oh my god, it's getting closer", "IT'S REALLY CLOSE NOW!!", "AAAAAAAAAAAAA!!!"]
explosionColors = ["red", "yellow"]
clusterColors = ["#3644E4", "green4", "grey44"]
clusterSpeeds = []
cluster = []
xCluster = []
yCluster = []
clusterSize = []
clustersDrawn = []
angles = []

# Epilepsy Warning
warning = s.create_text(400, 400, text = "WARNING: This video may potentially trigger seizures for people with photosensitive epilepsy. Viewer discretion is advised.", fill = "white",  font = "Arial 10")
s.update()
sleep(5)
s.delete(warning)
    
# Fill empty arrays with values

for i in range(numberOfClouds):
    xCloud.append(randint(200, 700))
    yCloud.append(randint(50, 200))
    cloudRadius.append(randint(30, 70))
    cloudsDrawn.append(0)

for i in range(100):
    line1 = randint(290, 545)
    line2 = randint(220, 520)
    xLine.append(xCentre+(line1/200))
    yLine.append(yCentre-(line2/200))
    xLineIncrease.append((xLine[i]-line1)/200)
    yLineIncrease.append((yLine[i]-line2)/200)
    LinesDrawn.append(0)

# To make the green polygons grow in size at the same rate as the Earth

for i in range(len(xPolygon1)):
    x = xCentre+(xPolygon1[i]/200)
    y = yCentre+(yPolygon2[i]/200)
    xIncrease = (x - xPolygon1[i])/200
    yIncrease = (y-yPolygon2[i])/200
    xPolygon.append(x)
    yPolygon.append(y)
    xIncreaseRate.append(xIncrease)
    yIncreaseRate.append(yIncrease)


for i in range(numberOfStars):
    xStars.append(randint(0, 800))
    yStars.append(randint(0, 800))
    starSize.append(randint(2, 5))
    xSpeed.append(uniform(0.1, 0.2))
    starsDrawn.append(0)
    

    

# SCENE ONE
while r <= 200:
    # Draw stars
    for i in range(numberOfStars):
       starsDrawn[i] = s.create_oval(xStars[i], yStars[i], xStars[i]+starSize[i], yStars[i]+starSize[i], fill = col[i%7])
       
       if 425 < xStars[i] <= 800:
           xStars[i] = xStars[i] + xSpeed[i]
           
       else:
           xStars[i] = xStars[i] - xSpeed[i]
           
    # Draw the Earth
    earth = s.create_oval(xCentre-r, yCentre-r, xCentre+r, yCentre+r, fill = "#3644E4")
    
    # Draw the clouds 
    if r >= 5:     
        for i in range(100):
            LinesDrawn[i] = s.create_line(xLine[i], yLine[i], xLine[i] + 1, yLine[i]+1, fill = "white")
            xLine[i] = xLine[i] - xLineIncrease[i]
            yLine[i] = yLine[i] - yLineIncrease[i]
            
    # Draw the green land      
    polygon1 = s.create_polygon(xPolygon[0], yPolygon[0], xPolygon[1], yPolygon[1], xPolygon[2], yPolygon[2], xPolygon[3], yPolygon[3], xPolygon[4], yPolygon[4], fill = "green4", smooth = True)
    polygon2 = s.create_polygon(xPolygon[5], yPolygon[5], xPolygon[6], yPolygon[6], xPolygon[7], yPolygon[7], fill = "green4", smooth = True)
    polygon3 = s.create_polygon(xPolygon[8], yPolygon[8], xPolygon[9], yPolygon[9], xPolygon[10], yPolygon[10], xPolygon[11], yPolygon[11], fill = "green4", smooth = True)
    
    # Update values for the land
    for i in range(len(xPolygon)):
        xPolygon[i] = xPolygon[i]-xIncreaseRate[i]
        yPolygon[i] = yPolygon[i]-yIncreaseRate[i]

    # Draw the meteor
    arc1 = s.create_arc(700+aS, -50-aS, 850+aS, 100-aS, start = 140, extent = 180, outline = "#cc5200", width = 5)
    arc2 = s.create_arc(700+aS, -50-aS, 850+aS, 100-aS, start = 320, extent = 180, fill = "black", width = 5)

    oval1 = s.create_oval(725+aS, -25-aS, 825+aS, 75-aS, fill = "grey44", outline = "grey44", width = 5)
    oval2 = s.create_oval(755+aS, 0-aS, 780+aS, 25-aS, outline = "grey20", width = 3)
    oval3 = s.create_oval(735+aS, 40-aS, 750+aS, 55-aS, outline = "grey20", width = 3)
    oval4 = s.create_oval(765+aS, 45-aS, 775+aS, 55-aS, outline = "grey20", width = 3)
    oval5 = s.create_oval(790+aS, 15-aS, 820+aS, 45-aS, outline = "grey20", width = 3)

    line1 = s.create_line(890+aS, -90-aS, 875+aS, -75-aS, fill = "#cc0000", width = 2)
    line2 = s.create_line(865+aS, -40-aS, 900+aS, -75-aS, fill = "#cc0000", width = 2)
    line3 = s.create_line(770+aS, -45-aS, 825+aS, -100-aS, fill = "#cc0000", width = 2)
    line4 = s.create_line(830+aS, -60-aS, 860+aS, -90-aS, fill = "#cc0000", width = 2)
    line5 = s.create_line(845+aS, 30-aS, 905+aS, -30-aS, fill = "#cc0000", width = 2)
    line6 = s.create_line(800+aS, -60-aS, 860+aS, -120-aS, fill = "#cc0000", width = 2)
    line7 = s.create_line(825+aS, -25-aS, 880+aS, -80-aS, fill = "#cc0000", width = 2)

    line8 = s.create_line(715+aS, -20-aS, 795+aS, -100-aS, fill = "#cc5200", width = 5)
    line9 = s.create_line(830+aS, 75-aS, 910+aS, -5-aS, fill = "#cc5200", width = 5)
    
    # Update values
    aS = aS - 1
    r = r + 1
    
    s.update()
    sleep(0.03)
    
    # Delete items
    for i in range(100):
        s.delete(earth, polygon1, polygon2, polygon3, LinesDrawn[i], arc1, arc2, oval1, oval2, oval3, oval4, oval5, line1, line2, line3, line4, line5, line6, line7, line8, line9)
        
    for i in range(numberOfStars):
        s.delete(starsDrawn[i])


# SCENE TWO
# Draw the sky
for i in range(len(skyColors)):
    s.create_rectangle(0, 480-g, 800, 640-g, fill = skyColors[i], outline = skyColors[i])
    g = g + 160

# Draw the background scene 
s.create_polygon(0, 640, 250, 350, 500, 640, fill = "#977c53")
s.create_polygon(500, 640, 650, 450, 800, 640, fill = "#796342")
s.create_rectangle(0, 640, 800, 800, fill = "#7cfc00", outline = "#7cfc00")
s.create_oval(550, 650, 800, 800, fill = "#80c5de", outline = "#80c5de")
s.create_oval(-150, -50, 100, 200, fill = "#FDB813", outline = "#FDB813")
s.create_arc(600, 690, 650, 720, start = 90, extent = 330, fill = "green", outline = "green")
s.create_arc(670, 720, 720, 750, start = 180, extent = 330, fill = "green", outline = "green")
s.create_arc(700, 670, 750, 700, start = 10, extent = 330, fill = "green", outline = "green")

# Draw the bushes
for i in range(50):
    s.create_oval(0+gap, 590, 50+gap, 640, fill = "#526b2d", outline = "#526b2d")
    if i % 5 == 0:
        gap = gap + 70
    else:
        gap = gap + 10
        
# Draw the dinosaur
s.create_image(300, 640, image = dinosaur)


frame = 0
a = 0
aS = 0
textPause = 20

while True:
    # Draw the big cloud
    for i in range(numberOfClouds):
        cloudsDrawn[i] = s.create_oval(xCloud[i] - cloudRadius[i], yCloud[i] - cloudRadius[i], xCloud[i] + cloudRadius[i], yCloud[i] + cloudRadius[i], fill = "white", outline = "white")
        xCloud[i] = xCloud[i] - 1
        
        if xCloud[i] == -75:
            xCloud[i] = 875
            
    # To make a text appear, wait for a bit, delete it, and move on to the next text in the array
    if frame == textPause:
        if a < 8:
            text = s.create_text(550, 450, text = texts[a], fill = "black")
            textPause = textPause + 60
            
    if frame == textPause - 30:
        if texts[a] != texts[7]:
            s.delete(text)
        a = a + 1
        
    # Wait until the last text appears and then draw the meteor       
    if frame > 480:
        
        distanceFromGround = sqrt(((725+aS)-375)**2+((-25-aS)-725)**2)
        
        oval1 = s.create_oval(725+aS, -25-aS, 825+aS, 75-aS, fill = "grey44", outline = "grey44", width = 5)
        oval2 = s.create_oval(755+aS, 0-aS, 780+aS, 25-aS, outline = "grey20", width = 3)
        oval3 = s.create_oval(735+aS, 40-aS, 750+aS, 55-aS, outline = "grey20", width = 3)
        oval4 = s.create_oval(765+aS, 45-aS, 775+aS, 55-aS, outline = "grey20", width = 3)
        oval5 = s.create_oval(790+aS, 15-aS, 820+aS, 45-aS, outline = "grey20", width = 3)

        line1 = s.create_line(890+aS, -90-aS, 875+aS, -75-aS, fill = "#cc0000", width = 2)
        line2 = s.create_line(865+aS, -40-aS, 900+aS, -75-aS, fill = "#cc0000", width = 2)
        line3 = s.create_line(770+aS, -45-aS, 825+aS, -100-aS, fill = "#cc0000", width = 2)
        line4 = s.create_line(830+aS, -60-aS, 860+aS, -90-aS, fill = "#cc0000", width = 2)
        line5 = s.create_line(845+aS, 30-aS, 905+aS, -30-aS, fill = "#cc0000", width = 2)
        line6 = s.create_line(800+aS, -60-aS, 860+aS, -120-aS, fill = "#cc0000", width = 2)
        line7 = s.create_line(825+aS, -25-aS, 880+aS, -80-aS, fill = "#cc0000", width = 2)
        
        aS = aS - 10
        r = r + 0.5
        
        # A second before the meteor hits the ground
        if distanceFromGround <= 285:
            break
        
    
    s.update()
    sleep(0.03)
    
    frame = frame + 1

    # Delete items
    for i in range(numberOfClouds):
        s.delete(cloudsDrawn[i])
        
    # Delete items when meteor shows up
    if frame > 480:
         for i in range(100):
            s.delete(oval1, oval2, oval3, oval4, oval5, line1, line2, line3, line4, line5, line6, line7)
            
# Draw the explosion effect
for i in range(50):
    s.create_rectangle(0, 0, 800, 800, fill = explosionColors[i%2])
    s.update()
    sleep(0.03)
s.create_rectangle(0, 0, 800, 800, fill = "black")

# SCENE THREE
# Fill arrays for the explosion
for i in range(150):
    angles.append(uniform(0, 2*pi))
    clusterSpeeds.append(uniform(1, 10))
    xCluster.append(xCentre)
    yCluster.append(yCentre)
    clusterSize.append(randint(4, 8))
    clustersDrawn.append(0)
    cluster.append(0)

# Draw stars
for i in range(numberOfStars):
    s.create_oval(xStars[i], yStars[i], xStars[i]+starSize[i], yStars[i]+starSize[i], fill = col[i%7])

# A never-ending loop
while True:
    # Draw the explosion
    for i in range(150):
        clustersDrawn[i] = s.create_oval(xCluster[i]-clusterSize[i], yCluster[i] - clusterSize[i], xCluster[i] + clusterSize[i], yCluster[i] + clusterSize[i], fill = clusterColors[i%3])
        xCluster[i] = xCentre + cluster[i]* cos(angles[i])
        yCluster[i] = yCentre - cluster[i] * sin(angles[i])
        cluster[i] = cluster[i] + clusterSpeeds[i]
        angles[i] = angles[i] + 0.01
        
        
    s.update()
    sleep(0.03)
    
    # Delete items
    for i in range(150):
        s.delete(clustersDrawn[i])

# END OF ANIMATION








