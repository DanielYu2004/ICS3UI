##########################################################
#                       Daniel Yu                        # 
#                      Pole Plunder                      #
#                        ICS3UI                          #
##########################################################

from tkinter import *
import time
import math
import random
myInterface = Tk()
screen = Canvas(myInterface, width=1100, height=700, background="sky blue")
screen.pack()

#Variables
x1 = 400
y1 = 350

x2 = x1 - 80
y2 = y1 + 20

x3 = x1 + 1600

cloudList = []
cloudSpeed = 5
breakVar = False
flying = True

#Loop for animation
for f in range(10000):

    #To detect pole collision
    if (5*f) > 3800:
        flying = False

    #To generate clouds
    if f % 40 == 0:
        Cx1 = random.randint(1200, 1300)
        Cy1 = random.randint(0, 700)
        cloud = []
        for circle in range(random.randint(7, 14)):
            cloudSize = random.randint(80,150)
            cloudx1 = random.randint(Cx1, Cx1+120) 
            cloudy1 = random.randint(Cy1, Cy1+40)
            cloud.append([int(cloudx1) + random.randint(-20, 20), int(cloudy1) + random.randint(-20, 20), int(cloudx1+ cloudSize) + random.randint(-20, 20), int(cloudy1 + cloudSize) + random.randint(-20, 20)])
        cloudList.append(cloud)


    #To detect if moving up or down and move character accordingly
    prevy1 = y1
    if flying == True:
        y1 = 350 + 200*math.sin(0.04*f)
        x1 = 500 + 400*math.sin(0.005*f)
    else:
        y1 += 10
        x1 -= 10

    #To move character
    x2 = x1 - 80
    y2 = y1 + 20


    #Cloud generation and deletion
    renderClouds = []

    for bigC in cloudList:
        for littleC in range(len(bigC)):
            newCoords = []
            appendBool = True
            for coord in range(len(bigC[littleC])):
                if bigC[littleC][coord] < -100:
                    appendBool = False

                if coord % 2 == 0:
                    newCoords.append(bigC[littleC][coord] - cloudSpeed)
                else:
                    newCoords.append(bigC[littleC][coord])
            bigC[littleC] = newCoords
            if appendBool == True:
                renderClouds.append(screen.create_oval(newCoords, fill="white", outline="white"))

    #Pole 
    if flying == True:
        Pole = screen.create_rectangle(x2 + 3800 - (5*f), 100, x1 + 3800 - (5*f), 900, fill="grey")
    else:
        Pole = screen.create_rectangle(x2 , 100, x1, 900, fill="grey")
 

    #Tail
    Tail = screen.create_polygon(x1-120, y1+25, x1-175, y1+50, x1-175, y1-25, fill="white", outline="black")

    #Body
    Body = screen.create_oval(x2 - 60, y2 -40, x2 + 60, y2 + 40, fill="white")

    #Head
    Head = screen.create_oval(x1-40,y1-40, x1+40, y1+40, fill="white")

    #Beak
    Beak = screen.create_polygon(x1+35, y1-20, x1+35, y1+20, x1+40+40, y1, fill="orange", outline="black")

    if prevy1 > y1:
        #Wing down
        Wing  = screen.create_polygon(x1 - 75, y1 , x1 - 45, y1 + 10, x1 - 45, y1 + 20, x1 - 75, y1 + 50, x1 - 150, y1 + 50, x1 - 200, y1 + 25, fill="white", outline="black", smooth=True)
    else:
        #Wing up
        Wing = screen.create_polygon(x1-75, y1, x1-75, y1+25, x1-45, y1+25, x1-90, y1-60, x1-150, y1-75, x1-175, y1-50, fill="white", outline="black", smooth=True)

    if flying == True:
        #Eye open
        Eye = screen.create_oval(x1 + 10,y1-15, x1+ 20, y1, fill="black")
    else:
        #Eye closed
        Eye = screen.create_text(x1 + 15, y1 - 10, text="X", font="20")

    screen.update()

    #Deleting objects
    screen.delete(Tail, Body, Head, Beak, Wing, Eye, Pole)
    for cloud in renderClouds:
        screen.delete(cloud)
    time.sleep(0.003)

screen.mainloop()