############################################################################
# Title: Matrix Physics                                                    #
# Created by: Nathan Nguyen                                                #
# Last Modified: November 9, 2017                                          #              
############################################################################


from tkinter import *
from time import *
from random import *
from math import *

myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background="white")
s.pack()

space=0
space1=0
space2=0

#Background
s.create_rectangle(0,0,805,200,fill="lightskyblue")#Sky
s.create_rectangle(0,200,805,805,fill="gray69",outline="black")#Roof
s.create_rectangle(500,3,700,200,fill="dodgerblue",outline="black")#Building
s.create_rectangle(0,200,805,250,fill="gray53",outline="black")#Ledge

#Windows
for n in range (9):
    s.create_line(520+space,0,520+space,200,fill="gray")
    space=space+20
for q in range (3):
    s.create_line(500,50.2+space1,700,50.2+space1,fill="gray1")
    space1=space1+50.2
for w in range (10): #Tiles
    s.create_line(50+space2,250,0,300+space2,fill="black")
    s.create_line(0,250+space2,805,250+space2,fill="black")
    space2=space2+150

#Left Arm
s.create_polygon(40,320,40,345,15,345,fill="black")
s.create_rectangle(39,345,15,415,fill="black")
s.create_rectangle(39,415,15,440,fill="tan")

#Body
s.create_rectangle(40,320,110,445,fill="gray4")

#Right Arm
rightArm3= s.create_polygon(110,320,135,344,110,344,fill="black")
rightArm1= s.create_rectangle(110,344,134,425,fill="black")
rightArm2= s.create_rectangle(110,415,134,440,fill="tan")

#Legs
s.create_rectangle(42,446,72,540,fill="gray25")
s.create_rectangle(78,446,110,540,fill="gray25")
s.create_rectangle(42,527,72,540,fill="black")
s.create_rectangle(78,527,110,540,fill="black")
s.create_polygon(40,446,62,446,62,530,20,530,fill="gray4")
s.create_polygon(110,446,93,446,93,530,131,530,fill="gray4")

#Head
s.create_rectangle(40,320,110,255,fill="tan")
s.create_polygon(40,270,60,265,75,265,80,270,90,270,85,265,105,265,110,270,110,255,40,255,fill="black")
s.create_rectangle(52,280,68,287,fill="black")
s.create_rectangle(82,280,98,287,fill="black")
s.create_line(40,275,52,283.5,fill="black")
s.create_line(110,275,98,283.5,fill="black")
s.create_line(67,283.5,82,283.5,fill="black")
s.create_line(94,308,59,308,fill="black")

#Gun and Hand
s.create_polygon(585,580,685,635,665,670,565,615,fill="black")
s.create_polygon(665,670,635,730,613,720,625,648,fill="black")
s.create_polygon(625,655,640,663,635,673,620,665,fill="tan",outline="black")
s.create_polygon(620,670,640,680,635,690,615,685,fill="tan",outline="black")
s.create_line(622.5,660,637.5,668,fill="black")
s.create_line(617.5,677,637.5,685,fill="black")
s.create_polygon(665,670,685,680,675,700,652,695,fill="tan",outline="black")
s.create_polygon(660,680,655,659,665,662,667,675,fill="tan",outline="black")
s.create_polygon(685,680,801,715,801,735,675,700,fill="black")

#Parameters
numBullets= 20
colour=["red","orange","yellow"]
x1=[]
y1=[]
x2=[]
y2=[]
bOutside=[]
bInside=[]
bang=[]

#Creating Bullet Coordinates
for i in range (0,numBullets): #top left
    x1.append (randint(200,550))
    x2.append (x1[i] + 20)
    y1.append (randint(400,700))
    y2.append (y1[i] +20)


#Displaying Bullets
s.update()
sleep(2)

for i in range (0,numBullets):
    bOutside.append (0)
    bInside.append (0)
    bang.append (0)
    bOutside[i]= s.create_oval(x1[i],y1[i],x2[i],y2[i],fill="darkgoldenrod1")
    bInside[i]= s.create_oval(x1[i]+5,y1[i]+5,x2[i]-5,y2[i]-5,fill="snow3")
    bang[i]= s.create_polygon(585,580,565,615,550,592,fill=colour[i%3])
    s.update () 
    sleep (0.03)

for i in range (0,numBullets):
    s.delete(bOutside[i],bInside[i],bang[i])
    
#Animation
for i in range (55):    
    for i in range (0,numBullets):

        if x1[i]>400: 
            x1[i]= x1[i]*0.99 
        else:
            x1[i]= 1-(1-(x1[i]*0.99))
            
        if x2[i]<400: 
            x2[i]= 1-(1-(x2[i]*0.99))
        else:
            x2[i]= x2[i]*0.99
            
        if y1[i]<400: 
            y1[i]= 1-(1-(y1[i]*0.99))            
        else:            
            y1[i]= y1[i]*0.99
            
        if y2[i]>400:            
            y2[i]= y2[i]*0.99
        else:
            y2[i]= 1-(1-(y2[i]*0.99))
            

    for i in range (0,numBullets):
        bOutside.append (0)
        bInside.append (0)
        bOutside[i] = s.create_oval(x1[i],y1[i],x2[i],y2[i],fill="darkgoldenrod1")
        bInside[i]  = s.create_oval(x1[i]+5,y1[i]+5,x2[i]-5,y2[i]-5,fill="snow3")

    s.update()
    sleep(0.03)

    for i in range (0,numBullets):
        s.delete (bOutside[i],bInside[i])


#He is the One (Arm raise)
s.delete (rightArm3,rightArm1,rightArm2)
RA1= s.create_polygon(111,320,125,328,111,350,fill="black")
RA2= s.create_polygon(125,328,155,340,150,360,111,350,fill="black")
fin1= s.create_rectangle(150,339,172,360,fill="tan")
fin2= s.create_rectangle(150,339,155.5,320,fill="tan")
fin3= s.create_rectangle(155.5,339,162,317,fill="tan")
fin4= s.create_rectangle(162,339,167.5,320,fill="tan")
fin5= s.create_rectangle(167.5,339,172,325,fill="tan")
fin6= s.create_rectangle(150,360,142,352,fill="tan")
fin7= s.create_rectangle(142,360,147,348,fill="tan")


#Stopping the Bullets
for i in range (0,numBullets):
    bOutside[i]= s.create_oval(x1[i],y1[i],x2[i],y2[i],fill="darkgoldenrod1")
    bInside[i]= s.create_oval(x1[i]+5,y1[i]+5,x2[i]-5,y2[i]-5,fill="snow3")
    bOutside.append (0)
    bInside.append (0)
    
#Lowering Arm
s.update()
sleep (2)

s.delete (RA1,RA2,fin1,fin2,fin3,fin4,fin5,fin6,fin7)
s.create_polygon(110,320,135,344,110,344,fill="black")
s.create_rectangle(110,344,134,425,fill="black")
s.create_rectangle(110,415,134,440,fill="tan")

#Dropping the Bullets
for i in range (0,numBullets):
    s.delete (bOutside[i],bInside[i])

speed = 0

for f in range (100):
    for i in range(0,numBullets):
       if y2[i] <= 650: #What is the purpose of this if-statement?
            y1[i]=y1[i]+speed
            y2[i]=y2[i]+speed
            bOutside[i]= s.create_oval(x1[i],y1[i],x2[i],y2[i],fill="darkgoldenrod1")
            bInside[i]= s.create_oval(x1[i]+5,y1[i]+5,x2[i]-5,y2[i]-5,fill="snow3")
            bOutside.append (0)
            bInside.append (0)

    s.update()
    sleep(0.03)

    speed = speed + 0.65  #Bullets accelerate with gravity as they fall

    for i in range (0,numBullets):
        if y2[i] < 650:  #What is the purpose of this if-statement?
            s.delete(bOutside[i],bInside[i])

