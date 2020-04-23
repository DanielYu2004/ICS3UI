from tkinter import *
from random import *
from time import *
from math import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="white")
screen.pack()



#background
screen.create_rectangle(0,0,800,550, fill = "PapayaWhip")
screen.create_rectangle(0,550,800,800, fill = "Tan")

#window
screen.create_rectangle(425,275,525,375, fill = "Lightblue")
screen.create_line(425,375,425,275, width = 2)
screen.create_line(425,275,525,275, width = 2)
screen.create_line(525,275,525,375, width = 2)
screen.create_line(425,375,525,375, width = 2)
screen.create_line(475,275,475,375, width = 2)
screen.create_line(425,325,525,325, width = 2)

#door
screen.create_rectangle(625,300,750,550, fill = "Sienna")
screen.create_oval(644,419,656,431, fill = "Gold")
 
#stool
screen.create_rectangle(50,500,100,550, fill = "DarkViolet")

#person + box
screen.create_line(75,425,53,500, width = 2)
screen.create_line(75,425,97,500, width = 2)
screen.create_line(75,362,75,425, width = 2)
screen.create_oval(50,310,100,360, fill = "MistyRose")
screen.create_polygon(49,325,75,304,112,327,50,325, fill = "orangered",smooth = "yes" )

#Poster
poster = PhotoImage (file = "marioposter0.gif")
screen.create_image(250, 275, image = poster)

poster2 = PhotoImage (file = "legomovie.gif")
screen.create_image(350, 100, image = poster2)


#ANIMATION TIME
numbricks = 100
groundLevel = 550
speed = 1
colors = ["red", "blue", "green","white", "yellow"]




#Set up arrays 

ySpeed = []
xPosition = []
yPosition = []
yStart = []
sizes = []
t = []
colorChoice = []
brickDrawings = []



for n in range(0,numbricks):
    xPosition.append(randint(102,145))
    yPosition.append(0)
    ySpeed.append( randint(4,8) )
    yStart.append( randint(380,420))
    sizes.append( randint(2,4) )
    brickDrawings.append(0)
    t.append(0)
    colorChoice.append(0)

    
for f in range(0,400):
    
    for n in range(0, numbricks):
        yPosition[n] = 0.1*t[n]**2 + ySpeed[n]*t[n] + yStart[n]
        brickDrawings[n] = screen.create_rectangle(xPosition[n],yPosition[n],xPosition[n]+sizes[n],yPosition[n]+sizes[n], fill=colors[colorChoice[n]], outline=colors[colorChoice[n]])

        t[n] = t[n] + 1
       
        if yPosition[n] >= groundLevel:
            t[n] = 0
            colorChoice[n] = (colorChoice[n] + 1) % 5

    yBox = 365 + 8*sin( 0.5*f )

    box = screen.create_rectangle(100, yBox, 150, yBox+50, fill = "LightCyan", outline ="black" )
    arm1 = screen.create_line(75, 387, 125, yBox + 30, width = 2)
    arm2 = screen.create_line(75, 387, 125, yBox+40, width = 2)
    label = screen.create_text(125, yBox+25, text="Legos", fill="black")

    screen.update()
    sleep(0.03)
    
    if f < 399:
        screen.delete( box, arm1, arm2, label )
    
    for n in range(0, numbricks):
        if yPosition[n] < groundLevel: 
            screen.delete( brickDrawings[n] )

    groundLevel = groundLevel - 0.2












