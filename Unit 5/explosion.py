from tkinter import *
from random import *
from time import *
from math import *
screen = Canvas(Tk(), height = 700, width = 800, background = "skyblue")
screen.pack()


def drawCircle( xC, yC, r, col ):
    x1 = xC - r
    y1 = yC - r
    x2 = xC + r
    y2 = yC + r
    return screen.create_oval( x1, y1, x2, y2, fill= col, outline=col )


def animateExplosion(xC, yC, col):
    numPieces = 90

    #SET UP THE EMPTY ARRAYS
    radii = []
    angles = []

    speeds = []
    sizes = []
    debrisDrawings = []

    #FILL THE ARRAYS WITH RANDOM VALUES
    for i in range( numPieces ):                                            
        radii.append( randint(0, 50) )
        angles.append( radians( randint(0, 360) ) )

        sizes.append( randint(2, 5) )
        speeds.append( uniform(3, 10) )
        debrisDrawings.append(0)

    #MAKE A SHORT FLASH
    flash = screen.create_polygon(xC-30,yC-35, xC-10, yC-35, xC+20,yC-45, xC+30,yC-40, xC+35,yC-15, xC+25,yC, xC+20,yC+40, xC,yC+20,
                                  xC-35,yC+35, xC-35,yC+8, xC-55,yC+10, xC-40,yC-15, fill="white")
    screen.update()
    sleep(0.06)
    screen.delete(flash)

    #ANIMATE THE EXPLOSION
    for f in range( 40 ):                                                 
                
        for i in range( numPieces ):        
            x = xC + radii[i]*cos( angles[i] )
            y = yC  - radii[i]*sin( angles[i] )
            debrisDrawings[i] = drawCircle( x, y, sizes[i], col)  #Looks like a function-call b/c it's on the RHS of an "=" sign.
            radii[i] = radii[i] + speeds[i]
            angles[i] = angles[i] + 0.1
            
        screen.update()
        sleep(0.03)
        
        if f < 39:
            for i in range( numPieces ):
                screen.delete( debrisDrawings[i] )


#Procedure-calls to make 3 different explosions.
#Replace these with a for-loop that makes 10 explosions
x=300
y=600
col = ["#eb4034", "#cf8d88", "#94cf88", "#8c88cf", "#ca88cf", "#88cdcf", "#c4cf88", "#79D2B8", "#AC80A0", "#FF9F7A"]
for i in range(10):
    animateExplosion(x, y, col[i])
    y=y-50


screen.mainloop()