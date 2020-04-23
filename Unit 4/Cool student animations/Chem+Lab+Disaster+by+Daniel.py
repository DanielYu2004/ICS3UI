from tkinter import *
from math import *
from random import *
from time import *

tk = Tk()
s = Canvas(tk, width = 1000, height = 950, background = "Gray80")
s.pack ()

#Smoke Detector & sprinkler 
s.create_rectangle(600, 0, 650, 13, fill="Gray50")
s.create_oval(610, 4, 615, 9, fill="Red")
s.create_oval(620, 4, 625, 9, fill="green")
s.create_line(350, 1, 600, 1, fill="black", width=3)
s.create_rectangle(345, 0, 350, 10, fill="Gray30")
s.create_rectangle(340, 10, 355, 15, fill="Gray30")

#Chalkboard
s.create_rectangle(50, 100, 950, 500, fill="dark green", outline="Gray50", width=5)
s.create_text(500, 300, text="Chemistry Lab", fill="white", font="Comic 48")

#Desk
s.create_rectangle(0, 650, 1000, 675, fill="Gray35")
s.create_rectangle(0, 674, 1000, 950, fill="sandy brown")
s.create_line(0, 750, 1000, 750, fill="black", width=2)

x1=0
x2=75
x3=750
for a in range (4):
    s.create_line(x1, 675, x1, 750, fill="black", width=2)
    x1=x1+250
for a in range (3):
    x1=x1-300
    s.create_line(x1, 750, x1, 950, fill="black", width=2)
for a in range (4):
    s.create_line(x2, 712, x2+100, 712, fill="Gray80", width=5)
    x2=x2+250
for a in range (3):
    s.create_line(x3, 800, x3, 900, fill="Gray80", width=5)
    x3=x3-300


#Person
s.create_oval(770, 270, 880, 380, fill="blanched almond")
s.create_rectangle(770, 310, 880, 320, fill="gray70", outline="gray70")
s.create_oval(790, 300, 820, 330, fill="lightblue1", outline="Gray70", width=3)
s.create_oval(830, 300, 860, 330, fill="lightblue1", outline="Gray70", width=3)
mouth=s.create_line(805, 345, 845, 345, fill="red", width=2)
s.create_polygon(750, 380, 825, 380, 650, 500, 625, 460, fill="white", outline="black")

s.create_rectangle(750, 380, 900, 650, fill="White")
s.create_line(825, 380, 825, 650, fill="black", width=3)


s.create_rectangle(900, 381, 935, 550, fill="white")
s.create_oval(900, 550, 935, 585, fill="Blanched almond", outline="blanched almond")
s.create_oval(600, 470, 640, 510, fill="blanched almond", outline="blanched almond")

#Beaker
x1beaker=590
x2beaker=x1beaker+20
x3beaker=x1beaker+40
x4beaker=x1beaker+60
y1beaker=460
y2beaker=y1beaker+50
y3beaker=y1beaker+80
beaker=s.create_polygon(x1beaker, y3beaker, x2beaker, y2beaker, x2beaker, y1beaker, x3beaker, y1beaker, x3beaker, y2beaker, x4beaker, y3beaker, fill="lightblue1")
acid=s.create_polygon(x1beaker+5, y3beaker-5, x2beaker+3, y2beaker, x3beaker-3, y2beaker, x4beaker-5, y3beaker-5, fill="yellow") 

#Fingers
f1=s.create_oval(605, 475, 630, 482, fill="Blanched almond", outline="Blanched almond")
f2=s.create_oval(602, 482, 632, 489, fill="Blanched almond", outline="Blanched almond")
f3=s.create_oval(602, 489, 632, 496, fill="Blanched almond", outline="Blanched almond")
f4=s.create_oval(605, 496, 630, 503, fill="Blanched almond", outline="Blanched almond")
thumb=s.create_oval(620, 480, 638, 487, fill="Blanched almond", outline="Blanched almond")

s.update()

#Distraction
xbody=-60
ybody=200
for f in range (110):
    body=s.create_polygon(xbody, ybody, xbody, ybody+20, xbody+60, ybody+10, fill="White", outline="Black")
    line=s.create_line(xbody, ybody+10, xbody+60, ybody+10, fill="Black")
    xbody=xbody+10

    s.update()
    sleep(0.03)
    s.delete(body, line)

s.delete(f1, f2, f3, f4, thumb, mouth)

f1=s.create_oval(580, 475, 605, 482, fill="Blanched almond", outline="Blanched almond")
f2=s.create_oval(577, 482, 602, 489, fill="Blanched almond", outline="Blanched almond")
f3=s.create_oval(577, 489, 602, 496, fill="Blanched almond", outline="Blanched almond")
f4=s.create_oval(580, 496, 605, 503, fill="Blanched almond", outline="Blanched almond")
thumb=s.create_oval(638, 480, 656, 487, fill="Blanched almond", outline="Blanched almond")
mouth=s.create_oval(820, 340, 830, 350, fill="red", outline="red")

#Drop the beaker
s.delete(beaker, acid)
while y3beaker < 670:
    beaker=s.create_polygon(x1beaker, y3beaker, x2beaker, y2beaker, x2beaker, y1beaker, x3beaker, y1beaker, x3beaker, y2beaker, x4beaker, y3beaker, fill="lightblue1")
    acid=s.create_polygon(x1beaker+5, y3beaker-5, x2beaker+3, y2beaker, x3beaker-3, y2beaker, x4beaker-5, y3beaker-5, fill="yellow") 

    y1beaker=y1beaker+10

    y1beaker=y1beaker+0.5
    y2beaker=y1beaker+50
    y3beaker=y1beaker+80

    s.update()
    sleep(0.03)
    s.delete(beaker, acid)

s.create_oval(600, 650, 660, 675, fill="yellow")

#Empty Arrays
x=[]
y=[]
size1=[]
size2=[]
yspeed=[]
numglass=100
shards=[]

#Fill Arrays
for i in range (numglass):
    x.append(uniform(600, 680))
    y.append(uniform(600, 650))
    size1.append(randint(-10, 10))
    size2.append(randint(-10, 10))
    yspeed.append(uniform(5, 10))

    shards.append(0)

#Falling glass
for f in range (88):

    for i in range (numglass):

        shards[i]=s.create_polygon(x[i], y[i], x[i]+size1[i], y[i]+size1[i], x[i]-size2[i], y[i]+size2[i], fill="lightblue1", outline="lightblue1")

        y[i]= y[i] + yspeed[i]
        
    s.update()
    sleep(0.03)

    for i in range (numglass):
        s.delete(shards[i])

#Empty Arrays
xsmoke=[]
ysmoke=[]
size=[]
Xspeed=[]
Yspeed=[]

numsmoke=175
smoke=[]


#Fill Arrays
for i in range (numsmoke):
    xsmoke.append(uniform(600, 650))
    ysmoke.append(uniform(650, 663))
    size.append(uniform(10, 20))
    Xspeed.append(uniform(-0.5, 0.5))
    Yspeed.append(uniform(-7, -12))

    smoke.append(0)

#Smoke
for f in range (125):
    
    for i in range (numsmoke):
        
        smoke[i]=s.create_oval(xsmoke[i], ysmoke[i], xsmoke[i]+size[i], ysmoke[i]+size[i], fill="gray30", outline="gray50")

        xsmoke[i]=xsmoke[i]+Xspeed[i]
        ysmoke[i]=ysmoke[i]+Yspeed[i]

    s.update()
    sleep(0.03)

    for i in range (numsmoke):
        s.delete(smoke[i])

s.delete(mouth)
s.update()

s.create_line(805, 355, 825, 345, 845, 355, fill="red", width=2, smooth="true")


#Empty array
xc=347
yc=13

xwater=[]
ywater=[]
r=[]
rspeed=[]
angle=[]

water=[]

numwater=500

#Fill Arrays
for i in range (numwater):
    xwater.append(xc)
    ywater.append(yc)

    r.append(0)
    rspeed.append(uniform(5,25))
    angle.append(uniform(5*pi/4, 7*pi/4))

    water.append(0)


#Sprinkler
for f in range (200):
    for i in range (numwater):
        water[i]=s.create_oval(xwater[i], ywater[i], xwater[i]+5, ywater[i]+5, fill="blue", outline="blue")
        
        xwater[i]=xc+r[i]*cos(angle[i])
        ywater[i]=yc-r[i]*sin(angle[i])

        r[i]=r[i]+ rspeed[i]
        

    s.update()
    sleep(0.03)
    
    for i in range(numwater):
        s.delete( water[i] )

s.mainloop()


    

