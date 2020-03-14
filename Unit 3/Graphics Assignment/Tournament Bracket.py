##########################################################
#                       Daniel Yu                        # 
#                    Tournament Bracket                  #
#                        ICS3UI                          #
##########################################################

from tkinter import *
import time
import random
tk = Tk()


#Variables
width = 800 #Width of board
height = 700 #Height of board
numRounds = 6 #Number of rounds
rounds = [] #Array for rounds

#Calculate number of people per round
for box in range(numRounds):
    rounds.append(2**box)

rounds = rounds[::-1]

#Setting box dimensions
boxHeight = height / (2*rounds[0])
boxWidth = width / (2 * numRounds)
widthSpace = (width-(boxWidth*numRounds))/(numRounds-1)
lineWidth = 1

#Array to keep track of boxes
boxes = []

#Initialize screen
screen = Canvas(tk, width=width, height=height, background="black")
screen.pack()

#Loop for each round
for round in range(numRounds):

    x1 = round*(widthSpace+boxWidth)

    #For the initial left-most round with maximum people
    if boxes == []:

        #Loop for the number of people in this round
        for box in range(rounds[round]):

            #To calculate the space inbetween
            heightSpace = (height - (boxHeight*rounds[round]))/(rounds[round]-1)

            y1 = box*heightSpace + box*boxHeight

            #Create boxes
            screen.create_rectangle(x1, y1, x1 + boxWidth, y1 + boxHeight, fill="red")
            screen.create_line(x1 + boxWidth, y1 + (boxHeight/2) , x1 + boxWidth + (widthSpace/2) , y1 + (boxHeight/2) , fill="red", width=lineWidth)

            #Add box to list for next round
            boxes.append(y1)

    else:
        #Variable to keep track of people for next round so midpoints can be calculated 
        newBoxes = []

        #To loop over each pair of people in the previous round
        for coord in range(int(len(boxes)/2)):

            y1 = (boxes[2*coord] + boxes[2*coord+1])/2

            #Create box
            screen.create_rectangle(x1, y1, x1 + boxWidth, y1 + boxHeight, fill="red")

            #Add box to list for next round
            newBoxes.append(y1)

            #Create connecting lines
            screen.create_line(x1-(widthSpace/2), boxes[2*coord] + (boxHeight/2), x1-(widthSpace/2), boxes[2*coord+1] + (boxHeight/2), fill="red", width=lineWidth)
            screen.create_line(x1, y1+(boxHeight/2), x1 - (widthSpace/2), y1+(boxHeight/2), fill="red", width=lineWidth)
            screen.create_line(x1+boxWidth, (boxes[2*coord] + boxes[2*coord+1])/2 + (boxHeight/2), x1 + boxWidth + (widthSpace/2), (boxes[2*coord] + boxes[2*coord+1])/2 + (boxHeight/2), fill="red", width=lineWidth)
            

        boxes = newBoxes




screen.mainloop() #For visual studio
