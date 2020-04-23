from tkinter import *
from math import *
from time import *
from random import *
root = Tk()
s = Canvas( root, width=1200, height=800, background = "black" )
s.pack()

#Creating the stars in the background
numstars = 1000
starsx = []
starsy = []
for i in range (numstars):
    starsx.append(randint(0,1200))
    starsy.append(randint(0,800))
    s.create_oval(starsx[i],starsy[i], starsx[i]+2,starsy[i]+2, fill = "white",width=0)

#While loop to keep generating the animation
yes = True 
while yes == True:

#Creating set values and empty arrays
    x = []
    y = []
    debris = []
    debrisE = []
    r = []
    r2 = []
    rSpeeds = []
    rSpeeds2 = []
    angles = []
    angles2 = []
    sizes = []
    EarthColours = []
    xC = randint(100,1100)
    yC = randint(100,700)
    numdebris = 800
    rE = 1
    Ff = 0.5
    earth = []
    ExplodeColours = []
    xl = xC
    yl = 70
    n = int(yC/25)
    
#Filling the arrays with random values, colours and 0's
    for i in range( 0, numdebris ):
        size = randint(1, 15)
        sizes.append( size )
        
        x.append( xC )
        y.append( yC )
        
        r.append( randint(-40,40) )
        angles.append( uniform(0,2*pi) )
        
        r2.append( randint(-50,-20) )
        r2.append( randint(20,50) )
        angles2.append( uniform(0,2*pi) )
        
        speed = uniform(8,10)
        rSpeeds.append( speed )

        speed2 = uniform(5, 8)
        rSpeeds2.append( speed2 )
        
        debris.append(0)
        debrisE.append(0)
        expC = choice(["lightblue","red","tan","orange","gray25"])
        ExplodeColours.append( expC )
        col = choice(["blue","blue","tan","green4"])
        EarthColours.append( col )
        earth.append(0)
        
#Creating the earth using a for loop and trig
    for e in range( 0, numdebris ):
        x[e] = xC + rE * cos( angles[e] )
        y[e] = yC - rE * sin( angles[e] )
        earth[e] = s.create_rectangle(xC,y[e], x[e],yC,fill = EarthColours[e],width = 0)
        rE = rE+Ff
        if rE > 100:
            Ff = -0.15
        s.update()

#Creating the alien and delaying the time to shoot the laser
    s.create_oval(xC,50, xC+40, 90, fill="yellow")
    s.update()
    sleep(3)
    
#Creating the laser right above wherever the earth is
    for l in range(n): #n = int(yC/20) which is the y value of earth divided by the speed of the laser per frame
        laser = s.create_line(xl,yl, xl,yl + 25, fill = "red", width = 5)
        yl = yl+20
        s.update()
        sleep(0.03)
        s.delete(laser)
        
#Deleting the earth after laser finishes its loop
    for e in range( 0, numdebris ):
        s.delete( earth[e] )
        
#Amount of frames the debris animation runs for
    for f in range(0, 200):

#for loop creating the debris using trig and animating it outward by whatever random number was put into the speed array
        for i in range( 0, numdebris ):
            debris[i] = s.create_rectangle( x[i], y[i], x[i] + sizes[i], y[i] + sizes[i], fill = ExplodeColours[i],width=0 )
            x[i] = xC + r[i] * cos( angles[i] )
            y[i] = yC - r[i] * sin( angles[i] )
            r[i] = r[i] + rSpeeds[i]
            debrisE[i] = s.create_rectangle( x[i], y[i], x[i] + sizes[i], y[i] + sizes[i], fill = EarthColours[i],width=0 )
            x[i] = xC + r2[i] * cos( angles[i] )
            y[i] = yC - r2[i] * sin( angles[i] )
            r2[i] = r2[i] + rSpeeds2[i]
        s.update()
        
#deleting the debris after 300 frames
        for i in range(0, numdebris):
            s.delete( debris[i],debrisE[i] )

#starting at the top of the while loop picking a new earth x and y
s.mainloop()
