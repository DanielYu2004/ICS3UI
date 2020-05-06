#############################
### INFINITE HEXAGON ZOOM ###
#############################

from time import *
from math import *
from tkinter import *
myInterface = Tk()
screen = Canvas(myInterface, width=600, height=600, background="#202020")
screen.pack()

########################################
### DEFINING FUNCTIONS AND VARIABLES ###
########################################

#Given rectangular coordinates, returns polar coordinates
def polar(x,y):
    r = sqrt((c-x)**2+(c-y)**2)     #pythagorean theorum to find radius
    if x == c and c-y > 0:          #accounts for special case of x=0 in order to avoid divide by zero error
        a = 90                      
    elif x == c and c-y <0:         
        a = 270                     
    else:                               
        a = atan(-(y-c)/(x-c))      #inverse tangent to find angle
        a *= 180/pi                 #convert radians to degrees
        if a >= 0 and x-c < 0:      #account for inverse trig function restrictions
            a += 180
        if a < 0 and x-c < 0:
            a += 180
    return [r,a]

#Given polar coordinates, returns rectangular coordinates
def coord(r,a):
    a *= pi/180                     #convert degrees to radians
    x = r*cos(a)+c                  #find x and y using cos and sin
    y = -1*r*sin(a)+c
    return [x,y]

#Create variables for frequently used values
global c
c = 300                 #center point
nFrames = 120           #number of frames per loop
r3 = 50*sqrt(3)         #height of triangle
colour = 'white'        #line colour
size = 2                #line width


#Infinitely loop the animation
while 1:

    #######################
    ### STARTING VALUES ###
    #######################
    
    #Create arrays with starting values for the lines forming the initial mesh of hexagons
    pointsRA      = [[polar(-120,c+(k-3)*r3),polar(720,c+(k-3)*r3)] for k in range(7)]        + \
                    [[polar(c-650+k*100,c-5*r3),polar(c-150+k*100,c+5*r3)] for k in range(9)] + \
                    [[polar(c+650-k*100,c-5*r3),polar(c+150-k*100,c+5*r3)] for k in range(9)]       #array of pairs of (r,a) points forming the lines
    expansionRate = [[k[0],l[0]] for k,l in pointsRA]                                               #array of speeds at which the points expand from the center
    pointsXY      = [[coord(*pointsRA[L][0]),coord(*pointsRA[L][1])] for L in range(len(pointsRA))] #array of pairs of (x,y) points forming the lines



    #Create arrays with starting values for first set of growing lines
    movingXY      = [[c,c-r3/2],[c,c-r3/2]]                                         #array of pairs of (x,y) points forming the lines
    movingRA      = [[polar(*movingXY[0]),polar(*movingXY[1])] for q in range(6)]   #array of pairs of (r,a) points forming the lines
    for q in range(6):              
        movingRA[q][0][1] += 60*q                                                   #duplicates (r,a) every 60 degrees to form full hexagon
        movingRA[q][1][1] += 60*q
    movingXYdrawn = [[coord(*movingRA[L][0]),coord(*movingRA[L][1])]    \
                     for L in range(len(movingRA))]                         #array of pairs of (x,y) points forming the lines
                                                                            #(this array is different from movingXY in that it is calculated
                                                                            # after transformations are applied to movingRA)



    #Create arrays with starting values for second set of growing lines
    #(this part is the same as the previous block of code but with new arrays for new starting points)
    movingXY2      = [[c,c-3*r3/2],[c,c-3*r3/2]]
    movingRA2      = [[polar(*movingXY2[0]),polar(*movingXY2[1])] for q in range(6)]
    for q in range(6):
        movingRA2[q][0][1] += 60*q
        movingRA2[q][1][1] += 60*q
    movingXY2drawn = [[coord(*movingRA2[L][0]),coord(*movingRA2[L][1])] for L in range(len(movingRA))]
    moving2start = nFrames*3/10     #the timing of when this set of lines will start growing


    #################
    ### ANIMATION ###
    #################

    #Loop through all frames
    for i in range(nFrames+1):

        #######################
        ### DRAWING OBJECTS ###
        #######################

        #Create arrays of all drawn line objects
        lines        = [screen.create_line(*pos,fill=colour,width=size) for pos in pointsXY]
        movingLines  = [screen.create_line(*pos,fill=colour,width=size) for pos in movingXYdrawn]
        if i > moving2start:    
            #only draw second set of growing lines once the required time has passed
            movingLines2 = [screen.create_line(*pos,fill=colour,width=size) for pos in movingXY2drawn]
        
        #Update, Sleep, Delete.
        screen.update()
        sleep(3.5/nFrames)
        screen.delete(*lines,*movingLines)
        if i > moving2start:
            screen.delete(*movingLines2) #second set of growing lines only deleted if they were drawn in the first place



        #######################             
        ### UPDATING VALUES ###
        #######################

        #Update points forming inital mesh of hexagons
        for j in range(len(pointsRA)):
            for k in range(2):                                      #For the points in pointsRA:
                pointsRA[j][k][0] += expansionRate[j][k]/nFrames    #push all points further from center based on their expansion speed
                pointsRA[j][k][1] -= 60/nFrames                     #rotate all points about the center
        pointsXY = [[coord(*pointsRA[L][0]),coord(*pointsRA[L][1])] for L in range(len(pointsRA))] #calculate (x,y) for new points to be drawn with


        #Update points in first set of growing lines
        movingXY[0][0] -= 400/nFrames   #move points farther from each other, elongating the line
        movingXY[1][0] += 400/nFrames
        movingRA      = [[polar(*movingXY[0]),polar(*movingXY[1])] for q in range(6)]   #calculating new (r,a) points for the new (x,y) points
        for q in range(6):                                      #For the points in movingRA
            movingRA[q][0][0] += movingRA[q][0][0]*i/nFrames    #Push all points further from center based on
            movingRA[q][1][0] += movingRA[q][1][0]*i/nFrames    #   their distance to the center and frames elapsed
            movingRA[q][0][1] += 60*q - i*60/nFrames            #Rotate all points about the center based on
            movingRA[q][1][1] += 60*q - i*60/nFrames            #   how mant frames have elapsed
        movingXYdrawn = [[coord(*movingRA[L][0]),coord(*movingRA[L][1])] for L in range(len(movingRA))] #calculate final (x,y)
                                                                                                        #now that all transformations are complete

        #Update points in second set of growing lines
        #(this part is the same as the previous block of code, but for the second set of growing lines)
        if i > moving2start:                #will only update if enough time has elapsed
            movingXY2[0][0] -= 240/nFrames  #the only difference from the first set is these lines grow at a slower rate
            movingXY2[1][0] += 240/nFrames
        movingRA2      = [[polar(*movingXY2[0]),polar(*movingXY2[1])] for q in range(6)]
        for q in range(6):
            movingRA2[q][0][0] += movingRA2[q][0][0]*i/nFrames
            movingRA2[q][1][0] += movingRA2[q][1][0]*i/nFrames
            movingRA2[q][0][1] += 60*q - i*60/nFrames
            movingRA2[q][1][1] += 60*q - i*60/nFrames
        movingXY2drawn = [[coord(*movingRA2[L][0]),coord(*movingRA2[L][1])] for L in range(len(movingRA2))]



