#Augusto Tavares
#Hyper Cube

from tkinter import *
from time import *
from random import *

root = Tk()
screen = Canvas( root, width=800, height=800, background = "black" )
screen.pack()

n = 90  #number of points
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
starDrawings1 = []#These ended up being useless put was part of the process, so...
starDrawings2 = []#These ended up being useless put was part of the process, so...
starDrawings3 = []#These ended up being useless put was part of the process, so...
starDrawings4 = []#These ended up being useless put was part of the process, so...
testnet1 = []
testnet2 = []
testnet3 = []
testnet4 = []
ySpeed = []
xSpeed = []
col = []
finn = PhotoImage (file = "finn.gif")#change this to where you have the file
screen.create_image(  400, 400, image=finn, anchor=CENTER)

###Directional Guides
##screen.create_line(0,0,300,300, fill=col[i])
##screen.create_line(800,0,500,300, fill=col[i])
##screen.create_line(0,800,300,500, fill=col[i])
##screen.create_line(800,800,500,500, fill=col[i])
###End Guide
##screen.create_line(300,300,500,300, fill=col[i])
##screen.create_line(300,500,500,500, fill=col[i])
##screen.create_line(500,300,500,500, fill=col[i])
##screen.create_line(300,300,300,500, fill=col[i])


for i in range( n ):
    x1.append( randint(300, 500 ))
    y1.append( randint(550, 770 ))
    x2.append( randint(300, 500 ))
    y2.append( randint(0, 300 ))
    x3.append( randint(0, 300 ))
    y3.append( randint(300, 500 ))
    x4.append( randint(500, 800 ))
    y4.append( randint(300, 500 ))
    starDrawings1.append( 0)#These ended up being useless put was part of the process, so...
    starDrawings2.append( 0)#These ended up being useless put was part of the process, so...
    starDrawings3.append( 0)#These ended up being useless put was part of the process, so...
    starDrawings4.append( 0)#These ended up being useless put was part of the process, so...
    testnet1.append( 0)
    testnet2.append( 0)
    testnet3.append( 0)
    testnet4.append( 0)
    ySpeed.append( uniform(2, 5) )
    xSpeed.append( uniform(-2, 2) )
    col.append(choice(["red","blue","white","yellow","green"]))


while True: 
    
    for i in range( n ): #down pannel
        #starDrawings1[i] = screen.create_line( x1[i]-2, y1[i]-2, x1[i]+2, y1[i]+2, fill=col[i]) now useless...
        y1[i] = y1[i] + ySpeed[i]
        x1[i] = x1[i] + xSpeed[i]
        
        if y1[i] > 800: 
            y1[i] = 502
            x1[i] = x1[i]/4+300

        testnet1[i] = screen.create_line(x1[i], y1[i],x1[i-1],y1[i-1], fill=col[i], width = 1) #draws lines from last point to new point
            
        #if x1[i] <

    for i in range( n ): #up pannel
        #starDrawings2[i] = screen.create_line( x2[i]-2, y2[i]-2, x2[i]+2, y2[i]+2, fill=col[i]) now useless...
        y2[i] = y2[i] + ySpeed[i]*-1
        x2[i] = x2[i] + xSpeed[i]
        
        if y2[i] < 0: 
            y2[i] = 298
            x2[i] = x2[i]/4+300

        testnet2[i] = screen.create_line(x2[i], y2[i],x2[i-1],y2[i-1], fill=col[i])#draws lines from last point to new point

    for i in range( n ): #left pannel
        #starDrawings3[i] = screen.create_line( x3[i]-2, y3[i]-2, x3[i]+2, y3[i]+2, fill=col[i]) now useless...
        y3[i] = y3[i] + xSpeed[i]
        x3[i] = x3[i] + ySpeed[i]*-1
        
        if x3[i] < 0: 
            y3[i] = y3[i]/4+300
            x3[i] = 298

        testnet3[i] = screen.create_line(x3[i], y3[i],x3[i-1],y3[i-1], fill=col[i])#draws lines from last point to new point

    for i in range( n ): #right pannel
        #starDrawings4[i] = screen.create_line( x4[i]-2, y4[i]-2, x4[i]+2, y4[i]+2, fill=col[i]) now useless...
        y4[i] = y4[i] + xSpeed[i]
        x4[i] = x4[i] + ySpeed[i]
        
        if x4[i] > 800: 
            y4[i] = y4[i]/4+300
            x4[i] = 502

        testnet4[i] = screen.create_line(x4[i], y4[i],x4[i-1],y4[i-1], fill=col[i])#draws lines from last point to new point

    
    screen.update()
    sleep(0.01)

    for i in range( n ):
        screen.delete( starDrawings1[i], starDrawings2[i], starDrawings3[i], starDrawings4[i], testnet1[i], testnet2[i], testnet3[i], testnet4[i] )
