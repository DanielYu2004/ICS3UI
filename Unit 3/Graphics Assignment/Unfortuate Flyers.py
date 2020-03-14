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


x1 = 400
y1 = 350

x2 = x1 - 80
y2 = y1 + 20


cloudList = []
cloudSpeed = 5
start = time.time()
breakVar = False
for f in range(10000):
    if breakVar == False:   
        if time.time() - start > 10:
            for x in range(10000):


                if 700 <= (5*x):
                    y1 += 40
                    x1 -= 5
                else:
                    y1 = 350 + 200*math.sin(0.04*(f+x))

                if y1 > 5000:
                    breakVar = True
                    break

                for bigC in cloudList:

                    for littleC in range(len(bigC)):
                        appendBool = True
                        newCoords = []
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


                x2 = x1 - 80
                y2 = y1 + 20

                #Pole
                Pole = screen.create_rectangle(x2 + 800 - (5*x), 100, x1 + 800 - (5*x), 700, fill="grey")

                #Tail
                Tail = screen.create_polygon(x1-120, y1+25, x1-175, y1+50, x1-175, y1-25, fill="white", outline="black")

                #Body
                Body = screen.create_oval(x2 - 60, y2 -40, x2 + 60, y2 + 40, fill="white")

                #Head
                Head = screen.create_oval(x1-40,y1-40, x1+40, y1+40, fill="white")

                #Beak
                Beak = screen.create_polygon(x1+35, y1-20, x1+35, y1+20, x1+40+40, y1, fill="orange", outline="black")

                #Wing
                Wing = screen.create_polygon(x1-75, y1, x1-75, y1+25, x1-45, y1+25, x1-90, y1-60, x1-150, y1-75, x1-175, y1-50, fill="white", outline="black", smooth=True)

                #Eye
                Eye = screen.create_oval(x1,y1-15, x1+10, y1, fill="black")

                screen.update()
                screen.delete(Tail, Body, Head, Beak, Wing, Pole, Eye)
                for cloud in renderClouds:
                    screen.delete(cloud)
                time.sleep(0.03)

        else:
            if breakVar == False:
                if f % 40 == 0:
                    Cx1 = random.randint(1200, 1300)
                    Cy1 = random.randint(0, 700)
                    cloud = []
                    for circle in range(random.randint(7, 14)):
                        cloudSize = random.randint(80,150)
                        cloudx1 = random.randint(Cx1, Cx1+120) 
                        cloudy1 = random.randint(Cy1, Cy1+40)
                        #screen.create_oval(cloudx1, cloudy1, cloudx1+ cloudSize, cloudy1 +cloudSize, fill="white", outline="white")
                        cloud.append([int(cloudx1), int(cloudy1), int(cloudx1+ cloudSize), int(cloudy1 + cloudSize)])
                    cloudList.append(cloud)




                y1 = 350 + 200*math.sin(0.04*f)

                x2 = x1 - 80
                y2 = y1 + 20


                renderClouds = []

                for bigC in cloudList:
                    for littleC in range(len(bigC)):
                        newCoords = []
                        appendBool = True
                        for coord in range(len(bigC[littleC])):
                            if bigC[littleC][coord] < -100:
                                appendBool = False
                            #    break
                            #else:
                            if coord % 2 == 0:
                                newCoords.append(bigC[littleC][coord] - cloudSpeed)
                            else:
                                newCoords.append(bigC[littleC][coord])
                        bigC[littleC] = newCoords
                        if appendBool == True:
                            renderClouds.append(screen.create_oval(newCoords, fill="white", outline="white"))






                #Tail
                Tail = screen.create_polygon(x1-120, y1+25, x1-175, y1+50, x1-175, y1-25, fill="white", outline="black")

                #Body
                Body = screen.create_oval(x2 - 60, y2 -40, x2 + 60, y2 + 40, fill="white")

                #Head
                Head = screen.create_oval(x1-40,y1-40, x1+40, y1+40, fill="white")

                #Beak
                Beak = screen.create_polygon(x1+35, y1-20, x1+35, y1+20, x1+40+40, y1, fill="orange", outline="black")

                #Wing
                Wing = screen.create_polygon(x1-75, y1, x1-75, y1+25, x1-45, y1+25, x1-90, y1-60, x1-150, y1-75, x1-175, y1-50, fill="white", outline="black", smooth=True)

                #Eye
                Eye = screen.create_oval(x1,y1-15, x1+10, y1, fill="black")

                screen.update()
                screen.delete(Tail, Body, Head, Beak, Wing, Eye)
                for cloud in renderClouds:
                    screen.delete(cloud)
                time.sleep(0.003)
            else:
                break







screen.mainloop()