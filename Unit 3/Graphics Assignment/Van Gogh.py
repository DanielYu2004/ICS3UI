from tkinter import *
import time
import random
tk = Tk()


length = 100
maxdot = 8
mindot = 4

screen = Canvas(tk, width=length*8, height=length*8, background="white")
screen.pack()

colourBool = True
for column in range(8):
    for row in range(8):
        x1 = length*row
        y1 = length*column
        x2 = length*(row+1)
        y2 = length*(column+1)
        #screen.create_rectangle(x1,y1,x2,y2)

        if colourBool == True:
            colourBool = False
            colour = "#654321"
        else:
            colourBool = True
            colour="#b5651d"

        for dot in range(100):
            size = random.randint(mindot, maxdot)

            dotx1 = random.randint(x1, x2-size) 
            doty1 = random.randint(y1, y2-size)
            screen.create_rectangle(dotx1, doty1, dotx1 + size, doty1 + size, fill=colour)

    if colourBool == True:
        colourBool = False
        colour = "#654321"
    else:
        colourBool = True
        colour="#b5651d"


        

screen.mainloop()

