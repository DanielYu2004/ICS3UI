from tkinter import *
from time import *
tk = Tk()
screen = Canvas(tk, width=1000, height=1000, background="grey10")
screen.pack()

ringColours = ["red", "yellow", "dark orange", "green", "blue", "purple"]

xRightWall = 800      #How far to the right a ring is allowed to expand before it stops and the next ring begins
showWalls = True    #Set this to False after you've seen the animation once and understood what the loops are doing

for i in range(35):
     #Resets the starting position of the next ring to the centre of the screen
    x1 = 500  #upper left corner of the ring
    y1 = 500
    
    x2 = 500  #lower right corner of the ring
    y2 = 500

    if showWalls == True:
        wall1 = screen.create_line( xRightWall, 0, xRightWall, 1000, fill="yellow")
        label1 = screen.create_text( xRightWall, 50, text = "xRightWall = " + str(xRightWall) , font="Arial 20", fill="yellow")

    #Animates the next ring until its right edge (x2) reaches the current limit (xRightWall)
    while x2 < xRightWall:
        
        if showWalls == True:
            wall2 = screen.create_line( x2, 0, x2, 1000, fill="white")
            label2 = screen.create_text( x2, 100, text = "x2", font="Arial 20", fill="yellow")

        ring = screen.create_rectangle(x1, y1, x2, y2, outline = ringColours[i%6], width=3 )

        #Makes the upper-left and lower-right corners of the ring expand outwards by a small amount before the next frame
        x1 = x1 - 5
        y1 = y1 - 5
        
        x2 = x2 + 5
        y2 = y2 + 5
       
        screen.update()
        sleep(0.03)
        screen.delete(wall2, label2)

        #Avoids deleting the very last frame in each ring, so that the picture keeps building on itself
        if x2 < xRightWall:  
            screen.delete(ring)

    #Reduces xRightWall so that the next ring will stop sooner than the current one
    xRightWall = x2 - 10
    screen.delete(wall1,label1)
    


# Just for fun...wipes the slate clean with a black hole
sleep(2)

x1 = 500
y1 = 500

x2 = 500
y2 = 500

while x2 < 2000: 
        x1 = x1 - 4
        y1 = y1 - 4
        x2 = x2 + 4
        y2 = y2 + 4

        disk = screen.create_oval(x1, y1, x2, y2, fill = "black", outline="red", width=4)
        screen.update()
        sleep(0.03)
        screen.delete(disk)