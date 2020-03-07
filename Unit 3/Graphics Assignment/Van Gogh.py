from tkinter import *
import time
import random
tk = Tk()


length = 60 #length and width of each square
maxdot = 8 #max dot size
mindot = 4 #min dot size
colourBool = True #Boolean to alternate colours
excessSpace = 100 #Excess space around the checkerboard

#Initialize screen
screen = Canvas(tk, width=(length*8) + excessSpace, height=(length*8) + excessSpace, background="black")
screen.pack()

#Loop for each square on checkerboard
for row in range(8): #Loop for each row
    for column in range(8): #Loop for each 8 squares in every row

        x1 = length*column + excessSpace/2 #Define top left x coordinate of square
        y1 = length*row + excessSpace/2 #Define top left y coordinate of square
        x2 = length*(column+1) + excessSpace/2 #Define bottom right x coordinate of square
        y2 = length*(row+1) + excessSpace/2 #Define bottom right y coordinate of square


        #To alternate colours every time a square is created
        if colourBool == True:
            colourBool = False
            colour = "#654321"
        else:
            colourBool = True
            colour="#b5651d"

        #Random dot generator
        for dot in range(100):

            size = random.randint(mindot, maxdot) #Choose random dot size

            dotx1 = random.randint(x1, x2-size) #Define top left x coordinate of dot
            doty1 = random.randint(y1, y2-size) #Define top left y coordinate of dot

            screen.create_rectangle(dotx1, doty1, dotx1 + size, doty1 + size, fill=colour)

    #To alternate the starting colour at the start of each row
    if colourBool == True:
        colourBool = False
        colour = "#654321"
    else:
        colourBool = True
        colour="#b5651d"


        

screen.mainloop() #For visual studio

