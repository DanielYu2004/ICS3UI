from tkinter import *
import time
import random
tk = Tk()


#Variables
width = 600
height = 600
numRounds = 4
rounds= []

for box in range(numRounds):
    rounds.append(2**box)
rounds = rounds[::-1]

boxHeight = height / (2*rounds[0])
boxWidth = width / (2 * numRounds)


#Initialize screen
screen = Canvas(tk, width=width, height=height, background="black")
screen.pack()

print(rounds)

for round in range(numRounds):
    #heightSpace = height-rounds[round]
    for box in range(rounds[round]):
        #x1 = box*
        #screen.create_rectangle(x1,y1,x2,y2, fill="red")
        print(box)


 























"""
for round in range(len(rounds)):
    if rounds[::-1][round] != 1 and round == 0:
        heightSpace = (height-(boxHeight*rounds[::-1][round]))/(rounds[::-1][round]-1)
        widthSpace = (width-(boxWidth*numRounds)/(numRounds-1))
        center = False
    elif rounds[::-1][round] != 1:
        heightSpace= boxHeight*2 + heightSpace + heightSpace - boxHeight
        widthSpace = (width-(boxWidth*numRounds))/(numRounds-1)
        center = False
    else:
        print("hi")
        center = True
    for box in range(rounds[::-1][round]):

        if center == False and round == 0:
            #print(heightSpace)
            #print(widthSpace)
            x1 = round*(widthSpace+boxWidth)
            y1 = box*heightSpace + box*boxHeight
            screen.create_rectangle(x1, y1, x1 + boxWidth, y1 + boxHeight, fill="red")
            prevHeightSpace = heightSpace
        elif center == False:
            x1 = round*(widthSpace+boxWidth)
            y1 = round*boxHeight + round*((prevHeightSpace-boxHeight)/2) + box*(heightSpace + boxHeight)
            screen.create_rectangle(x1, y1, x1 + boxWidth, y1 + boxHeight, fill="red")



    
"""




screen.mainloop() #For visual studio
