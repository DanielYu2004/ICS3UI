from tkinter import *
from time import *
from math import *
from random import *
tk = Tk()
screen = Canvas(tk, width=600, height=600, background="light blue")
screen.pack()

#Background
hill1 = screen.create_rectangle(0,400,700,700,fill="darkgreen",outline="darkgreen")
hill2 = screen.create_oval(0,400,800,700,fill="darkgreen",outline="darkgreen")
sun = screen.create_oval(200,100,400,300,fill="gold",outline="gold")
finishline1 = screen.create_line(150,400,150,600,fill="red",width=4)
finishline2 = screen.create_rectangle(0,400,50,600,fill="red")
finishword = screen.create_text(100,500, text = "FINISH", fill = "white", font = "Times 20 bold")

#Clouds
for cloud in range (150):
    x = randint(0,200)
    y = randint(0,50)
    size = randint (20,40)
    screen.create_oval(x,y,x+size,y+size,fill="white",outline="white")
    
for cloud2 in range (150):
    x = randint(400,600)
    y = randint(100, 150)
    size = randint(20,40)
    screen.create_oval(x,y,x+size,y+size,fill="white",outline="white")
    
#Empy arrays
numSnails = 30
size = 40
snailX = []
snailY = []
snailSpeed = []
bodyDrawings = []
headDrawings = []
eyeDrawings = []
colours = []

#Filling arrays with random values
for i in range(0, numSnails):
    snailX.append( randint(400, 700) )
    snailY.append( randint(400, 600) )
    snailSpeed.append( uniform(-2.0, -0.5) ) #Random decimal between -2.0 and -0.5
    bodyDrawings.append( 0 )
    headDrawings.append( 0 )
    eyeDrawings.append( 0 )
    colours.append(choice(["peach puff","brown4","dark slate gray","saddle brown","light goldenrod", "white", "firebrick"]))

#Animation
for f in range(800):
    for i in range( numSnails ):
        headDrawings[i] = screen.create_oval( snailX[i]+40, snailY[i], snailX[i]+7, snailY[i]-5, fill="sandy brown", outline = "sandy brown")
        bodyDrawings[i] = screen.create_oval( snailX[i]+size, snailY[i], snailX[i]+20, snailY[i]-10, fill = colours[i], outline = colours[i])
        eyeDrawings[i] = screen.create_oval( snailX[i]+5, snailY[i]-3, snailX[i]+3, snailY[i]-5, fill="sandy brown", outline = "sandy brown")
        snailX[i] = snailX[i] + snailSpeed[i] #Updating the position of snail i
             
    screen.update()
    sleep(0.03)

    for i in range( numSnails ):
        screen.delete( bodyDrawings[i], headDrawings[i], eyeDrawings[i] )

screen.mainloop() #needed if being run on repl.it

