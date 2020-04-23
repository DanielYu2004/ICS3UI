# Array Animation Assignment
# Sarah Hardy

from tkinter import *
from math import *
from time import *
from random import *


# Various constants.
screenWidth = 800
screenHeight = 800
rad = 50                # Radius of waves, moon, and sun.
waveNum = 17            # Number of waves.
cirNum = 80             # Number or circles for tornado.
fraNum = 1100           # Number of frames.
dotNum = 6              # Number of dots on moon.
sunNum = 10             # Number or colours in the sun. 
greyNum = 49            # Starting grey value.
greyAdj = -1            # Number used to change greyNum by.
blueNum = 4             # Starting value for bule value.
colD = "grey"           # Colour of dots on moon.
colW = "blue"           # Colour of waves and water.
colM = "white"          # Colour of moon.
colC = ["grey",         # Colour of tornado circles.
        "blue", 
        "white", 
        "cornflowerblue"]


# Create arrays for moon dot.
dot = [0, 0, 0, 0, 0, 0]                # The dots on the moon.
locY = [477, 490, 482, 520, 539, 515]   # y coordinate for each dot.
locX = [-7, -32, 5, 30, -5, 35]         # x coordinate for each dot.
radD = [25, 15, 20, 13, 10, 10]         # The radii for each dot.

               
# Fill arrays for creating wave.
wavX = []       # x coordinate for each wave ball.
wave = []       # Each ball in the wave.

for i in range(waveNum):
    x = 50 * i -25
    wavX.append(x)
    wave.append(0)


# Fill arrays for creating tornado.
radius = []     # Contains the radii for each circle in the tornado.
circle = []     # Contains each circle in the tornado.

for i in range(cirNum):
    r = 150 - 1.6 * i
    radius.append(r)
    circle.append(0)


# Fill arrays for creating sun.
# Colours for each colour ring in the sun.
sunCol = ["yellow1",  "#FFEB00", "gold1", "goldenrod1", "darkgoldenrod1",
          "orange1", "orange", "darkorange", "darkorange1", "darkorange2"]
sun = []        # Contains the colour rings in the sun.
radS = []       # Contains radii for each colour ring in the sun.

for i in range(sunNum):
    srad = (rad/sunNum) * (sunNum - i)
    radS.append(srad)
    sun.append(0)
    
    
# Set up screen.
myInterface = Tk()
screen = Canvas(myInterface, width=screenWidth, height=screenHeight)
screen.pack()


# Create water.
water = screen.create_rectangle(0, 600, screenWidth+10, screenHeight+10, fill = colW)
screen.update()
   
# Animate waves, tornado, moon, and sun. 
k = 10          # Allows us to manipulate the wavelength of the waves to speed up or down.
m = 25          # Initial height of the waves.
for f in range (fraNum):
   
    ## SKY
    
    # Change colour of background.
    #
    # Approach: Start with light grey and make darker until tornado comes on screen.
    #           Hold dark grey for a bit and then make lighter as sun comes on screen.
    #           Transition from grey to lighter shades of blue.
    if (f < 350):
        
        # Make the background darker every 10 frames.
        if (f % 10) == 0:
            colWord = str(greyNum)
            colB = "grey" + colWord
            screen.configure(background = colB)
            greyNum = greyNum + greyAdj
            
    elif (f < 700):
        
        # Keep the background the same colour.
        if (f < 500):
            greyAdj = 0
        
        # Make the background lighter every 5 frames.
        else:
            greyAdj = 1
        
        if (f % 5) == 0:    
            colWord = str(greyNum)
            colB = "grey" + colWord
            screen.configure(background = colB)
            greyNum = greyNum + greyAdj
   
    elif (f < 900):
       
        # Change the background every 50 frames.
        if (f % 50) == 0:
            colWord = str(blueNum)
            colB = "lightblue" + colWord
            screen.configure(background = colB)
            blueNum = blueNum - 1
    
    ## WAVES
    
    # Draw a series of balls to mimic a wave. Adjust the variable k as needed based on 
    # where we are in the animation in order to speed up or slow down the wave.
    
    if (f <= 200):
        k = k
    elif (f > 200) and (f <= 520):
        if (k <= 4):
            k = k
        else:
            k = k - 0.0188
    elif (f > 520) and (f <= fraNum):
        if (k >= 10):
            k = k
        else:
            k = k + 0.015
    
    for i in range(waveNum):
        x1 = wavX[i % waveNum] - rad
        x2 = wavX[i % waveNum] + rad    
        y1 = m * sin((f + 5 * i) / k) + 600 - rad
        y2 = y1 + 2 * rad
        wave[i] = screen.create_oval(x1, y1, x2, y2, outline = colW, fill = colW)
    
    # After frame 800, start reducing the height of the waves, decreasing a bit
    # every 10 frames.
    if ((f >= 800) and (m > 0)):
        if ((f % 10) == 0):
            m = m - 1            
    
    ## TORNADO
    
    # Draw a series of ovals to simulate a tornado.
    x = 925 - 5 * (f - 300)        
    for i in range(cirNum):
    
        # For the smaller circles, move them less side to side, but a bit more up and down.
        if (radius[i] < 50):
            tweakX = randint(-20, 20)
            tweakY = randint(-30, 10)

        # For the larger circles, move them more side to side, but a bit less up and down.
        else:
            tweakX = randint(-40, 40)
            tweakY = randint(-10, 5)

        x1 = x + radius[i] + tweakX 
        x2 = x-radius[i] + tweakX
        y1 = 150 + 5 * i + tweakY
        y2 = y1 + 15
        
        # Only draw the tornado when on screen (i.e. between frame 250 and 530).
        if ((f > 250) and (f < 530)):
            circle[i] = screen.create_oval(x1, y1, x2, y2, outline = choice(colC), width = 5)
       
    
    ## MOON
    
    # Draw the moon. Only draw it during the first 500 frames of the animation.
    if (f <= 500):

        # Draw the empty moon.
        x = 1.7 * f
        y = 0.003 * f**2 - 2.3 * f + 500
        moon = screen.create_oval(x-rad, y-rad, x+rad, y+rad, outline = colM, fill = colM)

        # Create the dots on the moon.
        for i in range(dotNum):
            x = 1.7 * f + locX[i]
            y = 0.003 * f**2 - 2.3 * f + locY[i]
            dot[i] = screen.create_oval(x-radD[i], y-radD[i], x+radD[i], y+radD[i], outline = colD, fill = colD)        
        
        
    ## SUN
    
    # Draw the sun. Only draw it after frame 520.
    if (f > 520):
        
        # Calculate the starting x and y values for the sun and then draw all
        # of the colour rings.
        y = 0.004 * (f - 521)**2 - 2.3 * (f - 521) + 450
        x = 1.5 * (f-521) - 50
        for i in range(sunNum):
            x1 = x - radS[i]
            y1 = y - radS[i]
            x2 = x + radS[i]
            y2 = y + radS[i]
            sun[i] = screen.create_oval(x1, y1, x2, y2, outline = sunCol[i], fill = sunCol[i])
           
        # Once we hit frame 900 we stop the sun from moving.
        if (f > 900):
            for i in range(sunNum):
                screen.delete(sun[i])
        
                
    screen.update()
    sleep(0.03)

    # Delete all of our waves, the tornado, the moon, and the sun.
    if (f < (fraNum - 1)):
        for i in range(waveNum):
            screen.delete(wave[i])
    for i in range(cirNum):
        screen.delete(circle[i])
    for i in range(dotNum):
        screen.delete(moon, dot[i])
    if (f < 900):
        for i in range(sunNum):
            screen.delete(sun[i])  
            
screen.update()
