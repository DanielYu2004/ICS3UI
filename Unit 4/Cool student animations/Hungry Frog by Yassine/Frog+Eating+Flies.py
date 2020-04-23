from tkinter import *
from time import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width = 800, height = 800, background = "saddlebrown")
screen.pack()


#Grass
for g in range(3000):
    x = randint(0, 800)
    y = randint(240, 600)
    size = randint(5, 15)
    screen.create_line(x, y, x+size, y+size, fill = "lawn green")


#Background
screen.create_rectangle(0, 0, 800, 250, fill = "skyblue")
screen.create_oval(-150, 500, 900, 1100, fill = "blue")
screen.create_oval(720, -60, 880, 90, fill = "yellow", outline = "yellow")
screen.create_oval(475, 112, 650, 42, fill = "white", outline = "white")
screen.create_oval(235, 65, 400, 135, fill = "white", outline = "white")
screen.create_oval(40, 45, 200, 115, fill = "white", outline = "white")


#Picture of Frog
frogImgFile = PhotoImage(file = "frog.gif")
frogImg = screen.create_image(100, 700, image = frogImgFile)


#Hide Picture
screen.create_polygon(200, 600, 0, 600, 0, 683, 21, 698, 65, 662, 73, 650, 85, 645, 90, 633, 123, 633, 128, 652, 150, 658, 172, 656, 169, 680, 157, 710, 200, 720, fill = "blue")
screen.create_polygon(0, 790, 70, 795, 110, 799, 158, 780, 141, 757, 160, 760, 190, 768, 200, 765, 200, 800, 0, 800, fill = "blue") 

#Drawing Of Lily Pads
numlily = 5
x1 = []
y1 = []

for k in range(0,numlily):
    x1.append(randint(300, 700))
    y1.append(randint(600, 750))
    screen.create_oval(x1[k], y1[k], x1[k]+50, y1[k]+50, fill = "green")
    screen.create_polygon(x1[k]+25, y1[k]+25, x1[k]+50, y1[k], x1[k]+50, y1[k]+50, fill = "blue", outline = "blue")


#Empty arrays for the flies
r = 800
numFlies = 30
x = []
y = []
xSpeeds = []
ySpeeds = []
deadfly = []
body = []
lwing = []
rwing = []
toungeDrawing = 0

lenght = 15
width = 5

#Fill the empy fly-arrays with starting values
for i in range(0, numFlies):
    x.append( randint(100, 700) )
    y.append( randint(100, 550) )
    xSpeeds.append( randint(-8, 8) )
    ySpeeds.append( randint(-8, 8) )
    deadfly.append( False )  #All flies are alive at the start
    body.append(0)
    lwing.append(0)
    rwing.append(0)

numDead = 0

#Animation loop continues for as long as there are still flies
while numDead < numFlies:
    
    for r in range(0, numFlies):
        if deadfly[r] == False:  #We only care about the flies that are still alive

            #Drawing the fly's body and wings
            body[r] = screen.create_oval( x[r], y[r], x[r]+width, y[r]+lenght, fill = "black" )
            lwing[r] = screen.create_oval( x[r]-10, y[r]+5, x[r], y[r]+10, fill = "grey" )
            rwing[r] = screen.create_oval( x[r]+5, y[r]+5, x[r]+15, y[r]+10, fill = "grey" )

            #Checking for bouncing off the edges
            if x[r] < 50 or x[r] > 750: 
                xSpeeds[r] *= -1  #multiplying speed by -1
                
            if y[r] < 50 or y[r] > 700:
                ySpeeds[r] *= -1

            #Checking for getting eaten
            if x[r] > 145 and x[r] < 500 and y[r] > 690:
                screen.delete( toungeDrawing ) #In case the tongue has already been drawn in this frame for some other fly
                toungeDrawing = screen.create_oval(150, 690, 500, 700, fill = "pink") 
                deadfly[r] = True   #Fly gets eaten
                numDead = numDead + 1

            #Updating the fly's position for the next frame
            x[r] = x[r] + xSpeeds[r]
            y[r] = y[r] + ySpeeds[r]
              
    screen.update()
    sleep(0.03)

    #Deleting all flies and the frog's tongue
    for r in range(0, numFlies):
        screen.delete( body[r], lwing[r], rwing[r], toungeDrawing )

      
screen.mainloop() #Needed if being run on repl.it
