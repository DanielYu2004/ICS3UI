from tkinter import *
from time import *
from random import *
from math import *
master=Tk()
screen=Canvas(master,width=1200,height=700,background="sky blue")
screen.pack()

#Grass
screen.create_rectangle(0,600,1200,700,fill="green")
#Head
Head=screen.create_oval(900,300,950,350,fill="tan")
#Cape
Cape=screen.create_polygon(895,290,895,340,750,340,760,330,750,340,760,320,750,310,760,300,750,290,fill="red",smooth="true")
#Torso
Torso=screen.create_polygon(900,300,900,350,900,350,790,340,790,330,800,325,850,340,smooth="true",fill="blue")
#Hips
Hips=screen.create_polygon(830,350,800,350,790,340,790,330,800,325,825,330,smooth="true",fill="red",outline="black")
#Upper Leg
UpperLeg=screen.create_polygon(810,325,810,350,725,350,725,335,760,340,smooth="true",fill="blue")
#Lower Leg
LowerLeg=screen.create_polygon(725,338,725,350,660,350,660,345,700,342,710,338,smooth="true",fill="red")
#Kneecap
Kneecap=screen.create_oval(720,339,730,349,fill="blue")
#Feet
Feet=screen.create_polygon(660,355,640,380,660,330,675,330,fill="red",smooth="true")
#Arm
Arm=screen.create_polygon(890,310,920,370,910,380,870,330,fill="blue",smooth="true",outline="black")
#Upper Arm
UpperArm=screen.create_polygon(910,365,980,365,980,380,910,380,fill="blue",smooth="true")
#Hand
Hand=screen.create_oval(975,365,990,380,fill="tan")

x1m=-500

screen.update()

NumTrees=80
Tree=[]
Stump=[]
x1=[]
y1=[]
for TreeNum in range(1,NumTrees+1):
    Tree.append(0)
    x1.append(0)
    y1.append(0)
    Stump.append(0)

for i in range(0,NumTrees):
        x1[i]=randint(0,4800)
        y1[i]=randint(-40,40)


#FLIGHT ANIMATION
for FrameNum in range(1,700):
    #Body
    Body=screen.create_polygon(x1m,355,x1m-25.1,362.4,x1m-25,362.5,x1m-312.6,362.4,x1m-312.5,362.5,x1m-312.6,344.9,x1m-312.5,345,x1m-25.1,344.9,x1m-25,345,smooth="true",fill="white",outline="black")
    #Back Fins
    BackFin1=screen.create_polygon(x1m-312.5,345,x1m-312.5,325,x1m-287.5,325,x1m-212.5,345,fill="grey")
    BackFin2=screen.create_polygon(x1m-312.5,362.5,x1m-312.5,382.5,x1m-287.5,382.5,x1m-212.5,362.5,fill="grey")
    #Front Fins
    FrontFin1=screen.create_polygon(x1m-162.5,345,x1m-162.5,315,x1m-137.5,315,x1m-62.5,345,fill="grey")
    FrontFin2=screen.create_polygon(x1m-162.5,362.5,x1m-162.5,392.5,x1m-137.5,392.5,x1m-62.5,362.5,fill="grey")
    #Exhaust
    Exhaust=screen.create_polygon(x1m-312.5,362.5,x1m-312.6,362.4,x1m-312.6,344.9,x1m-312.5,345,x1m-415.5,353.75,smooth="true",fill=choice(["red","orange","yellow"]))
    #Decals
    Line=screen.create_line(x1m-35,362,x1m-35,345)
    Text=screen.create_text(x1m-175,353.75,text="USAF Kryptonite AIM-7",font="Arial 12")

    x1m=x1m+2
    
    yBackground = 500+30*sin(FrameNum/80)
    Grass = screen.create_rectangle(0,yBackground-50,1200,700,fill="green")

    for z in range(0,NumTrees):
        x1[z]=x1[z]-1
        yTree = y1[z]+yBackground
        Tree[z]=screen.create_rectangle(x1[z], yTree, x1[z]+50, yTree + 100, fill="dark green")
        Stump[z]=screen.create_rectangle(x1[z]+20, yTree + 100, x1[z]+30, yTree+ 150, fill="brown")



    screen.update()
    sleep(0.01)

    if FrameNum < 698:
        for s in range(0,NumTrees):
            screen.delete(Tree[s])
            screen.delete(Stump[s])
            
        for CheckTrees in range(0,NumTrees):
            if x1[CheckTrees]<-50:
                x1[CheckTrees]=randint(1200,1300)
                y1[CheckTrees]=randint(550,600)

    screen.delete(Grass, Line, Text, Exhaust, FrontFin1, FrontFin2, BackFin1, BackFin2, Body)


#ARRAYS FOR EXPLOSION ANIMATION
xC = 800
yC = 300
numDebris = 1000

x = []
y = []
debris = []
r = []
rSpeeds = []
angles = []
sizes = []
debrisColours = []

screen.delete(Cape, UpperLeg, Torso, Hips, LowerLeg, Kneecap, Feet, Hand, Arm, UpperArm, Head)

for i in range( 0, numDebris ):                                       #FILL ARRAYS WITH RANDOMLY CHOSEN VALUES WITHIN CERTAIN RANGES
    size = randint(1, 15)
    sizes.append( size )

    x.append( xC )
    y.append( yC )
    
    r.append( randint(-50,50) )
    angles.append( uniform(0,2*pi) )

    speed = uniform(-15, 20)
    rSpeeds.append( speed )

    debris.append(0)

    col = choice(["blue","red","white","grey"])
    debrisColours.append( col )


#EXPLOSION ANIMATION
for f in range(0, 250):                                                 
            
    for i in range( 0, numDebris ):
        debris[i] = screen.create_oval( x[i], y[i], x[i] + sizes[i], y[i] + sizes[i], fill = debrisColours[i] )

        x[i] = xC + r[i] * cos( angles[i] )
        y[i] = yC - r[i] * sin( angles[i] ) + .08*f**2
        r[i] = r[i] + rSpeeds[i]

    headX = 900 
    headY = 260 - 24*f + .12*f**2
    head = screen.create_oval(headX, headY, headX + 50,headY+50, fill="tan")
    
    screen.update()
    sleep(0.03)
    
    for i in range(0, numDebris):
        screen.delete( debris[i] )
        
    screen.delete( head )
    





