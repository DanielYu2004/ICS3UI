from tkinter import *
import time
import random
tk = Tk()


#Variables
width = 800
height = 700
numRounds = 2
rounds= []


for box in range(numRounds):
    rounds.append(2**box)
rounds = rounds[::-1]

boxHeight = height / (2*rounds[0])
boxWidth = width / (2 * numRounds)
widthSpace = (width-(boxWidth*numRounds))/(numRounds-1)
lineWidth = 1
boxes = []

#Initialize screen
screen = Canvas(tk, width=width, height=height, background="black")
screen.pack()

print(rounds)

for round in range(numRounds):
    x1 = round*(widthSpace+boxWidth)
    print(x1)
    print(widthSpace)
    print(boxWidth)
    if boxes == []:

        for box in range(rounds[round]):

            heightSpace = (height - (boxHeight*rounds[round]))/(rounds[round]-1)
            y1 = box*heightSpace + box*boxHeight

            screen.create_rectangle(x1, y1, x1 + boxWidth, y1 + boxHeight, fill="red")
            screen.create_line(x1 + boxWidth, y1 + (boxHeight/2) , x1 + boxWidth + (widthSpace/2) , y1 + (boxHeight/2) , fill="red", width=lineWidth)
            boxes.append(y1)
    else:
        newBoxes = []
        for coord in range(int(len(boxes)/2)):
            y1 = (boxes[2*coord] + boxes[2*coord+1])/2
            screen.create_rectangle(x1, y1, x1 + boxWidth, y1 + boxHeight, fill="red")
            newBoxes.append(y1)

            screen.create_line(x1-(widthSpace/2), boxes[2*coord] + (boxHeight/2), x1-(widthSpace/2), boxes[2*coord+1] + (boxHeight/2), fill="red", width=lineWidth)
            screen.create_line(x1, y1+(boxHeight/2), x1 - (widthSpace/2), y1+(boxHeight/2), fill="red", width=lineWidth)

            screen.create_line(x1+boxWidth, (boxes[2*coord] + boxes[2*coord+1])/2 + (boxHeight/2), x1 + boxWidth + (widthSpace/2), (boxes[2*coord] + boxes[2*coord+1])/2 + (boxHeight/2), fill="red", width=lineWidth)
            



            #screen.create_line((boxes[2*coord] + boxes[2*coord+1])/2 + (boxHeight/2), x1 + boxWidth + (widthSpace/2), (boxes[2*coord] + boxes[2*coord+1])/2 + (boxHeight/2), fill="red", width=5)




        boxes = list(newBoxes)





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
