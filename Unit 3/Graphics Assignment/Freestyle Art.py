##########################################################
#                       Daniel Yu                        # 
#                    Cowboy Memorial                     #
#                        ICS3UI                          #
##########################################################

from tkinter import *
import time
import random
import math
tk = Tk()


#Screen dimensions
width = 800
height = 700



#Sun and Sky
sunX = random.randint(0,800)
sunY = random.randint(0,350)
sunSize = random.randint(100, 150)
if sunY > 300:
    sunColour ="#F5822D"
    skyColour ="#F3B26D"
elif sunY > 250:
    sunColour ="#F0B133"
    skyColour="#A8B8E8"

elif sunY > 150:
    sunColour = "#F0DE33"
    skyColour="#A8B8E8"

else:
    sunColour = "#FFEB30"
    skyColour="#A8B8E8"

#Initialize screen
screen = Canvas(tk, width=width, height=height, background=skyColour)
screen.pack()

#Create sun
screen.create_oval(sunX - (sunSize/2), sunY - (sunSize/2), sunX + (sunSize/2), sunY + (sunSize/2), fill=sunColour)





#Clouds

numClouds = random.randint(2,5) #Number of clouds

for cloud in range(numClouds):

    clouds = random.randint(8,15) #Number of circles within cloud

    x1 = random.randint(0,width)
    y1 = random.randint(0, 150)

    for circle in range(clouds):
        cloudSize = random.randint(80,100)
        cloudx1 = random.randint(x1, x1+80) 
        cloudy1 = random.randint(y1, y1+40)
        screen.create_oval(cloudx1, cloudy1, cloudx1+ random.randint(cloudSize-60, cloudSize+60), cloudy1 + random.randint(cloudSize-60, cloudSize+60), fill="white", outline="white")




#Grass

screen.create_rectangle(0, 350, 800, 500, fill="green", outline="green")


for grass in range(3000):
    grassWidth = random.randint(4,8)
    grassHeight = random.randint(10,15)
    x1 = random.randint(0,800-grassWidth)
    y1 = random.randint(350-grassHeight,500-grassHeight)
    colours = ["green", "#209145", "#5DBF7E"]
    color = colours[random.randint(0,2)]
    screen.create_rectangle(x1,y1, x1 + grassWidth, y1 + grassHeight, fill=color, outline=color)


#Road

screen.create_rectangle(0, 500, 800, 700, fill="grey", outline="black")

lines = random.randint(6, 18)
lineWidth = random.randint(40, 100)
lineHeight = random.randint(10,20)
space = width/(lines-1)

for line in range(lines):
    screen.create_rectangle((space+lineWidth)*line, 600 - lineHeight/2, (space+lineWidth)*line + lineWidth, 600 + lineHeight/2, fill="white")



#Hat

screen.create_polygon(150, 450, 150, 350, 250, 375, 300, 350, 325, 250, 350, 150, 350, 125, 375, 70, 400, 125, 425, 70, 450, 125, 450, 150, 475, 250, 500, 350, 550, 375, 650, 350, 650, 450, fill="#CCAF7E", smooth=True, outline="black", width="3")
screen.create_polygon(300, 325, 300, 350, 400, 360, 500, 350, 500, 325, fill="#826334", smooth=True, outline='black', width="3")
screen.create_polygon(300, 340, 305, 325, 495,325, 500, 340, fill="#826334")
screen.create_line( 305, 325, 495,325, width="3" )



screen.mainloop()