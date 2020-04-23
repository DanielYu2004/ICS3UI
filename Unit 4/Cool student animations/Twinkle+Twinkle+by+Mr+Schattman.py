from tkinter import *
from time import *
from math import *
from random import *
root = Tk()
s = Canvas( root, width=1700, height=1000, background = "black" )
s.pack()

#TRY CHANGING THESE
numStars = 1600
minBrightness = 20                  #0-50
rateOfBrightnessChange = 8  #0-30 (how quickly each star dims or brightens)


#EMPTY ARRAYS FOR THE STARS
x = []                  #(x, y) position and size
y = []
sizes = []
shades=[]          #will contain 99 greyscale colours: grey1, grey2, ..., grey99
indices = []        #will store the number of the greyscale colour that each star is currently using
directions = []  #will store  +1 or -1 for each star.  +1 means it's currently getting brighter. -1 means it's getting dimmer
stars = []            #will store the create_oval objects


#FILLS THE shades ARRAY WITH 99 SHADES OF GREY
for i in range(99):
      shades.append( "grey" + str(i+1) )


#FILLS THE OTHER EMPTY ARRAYS WITH STARTING VALUES
for n in range(numStars):
      indices.append(randint(0,98))     #Each star will begin with a random shade of grey
      x.append(randint(0,1700))
      y.append(randint(0,1000))
##      yMin = int(400+100*sin(0.01*x[n]))    #Try commenting out the above y.append und using these 3 lines
##      yMax = yMin + 300
##      y.append(randint(yMin, yMax))
      sizes.append(randint(1,2))
      directions.append(choice([-1,1]))
      stars.append(0)


#RUNS THE TWINKLING ANIMATION
while True:
      
      for i in range(numStars):
            col = shades[indices[i]]  #Gets star i's current greyscale colour
            stars[i] = s.create_oval(x[i], y[i], x[i]+sizes[i], y[i]+sizes[i], fill=col, outline = col)
            
            indices[i] = indices[i] + directions[i]*rateOfBrightnessChange #Increase or decrease star i's brightness
            
            if indices[i] >= 98:  #If star i has reached (or surpassed) max brightness, then go into dimming mode
                  indices[i] = 98
                  directions[i] = -1
                  
            elif indices[i] <= minBrightness: #if star i has reached min brightness, then go into brightening mode
                  indices[i] = minBrightness
                  directions[i] = 1
            
      s.update()
      sleep(0.03)
      s.delete("all")  #Deletes everything on screen.  This is easier than using a for-loop if there are no background
                                   #graphics that have to stay on screen between frames
