from tkinter import *
from time import*
from math import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="black")
screen.pack()

#PARAMETERS - TRY CHANGING THESE
A = 250                                              #the amplitude of the motion
B_min = 0.02                                    #the frequency of the slowest, top-most brick
B_difference_per_brick = .006    #the difference in frequency between each successive brick
numbricks = 24
colorChoices = ["red", "yellow", "blue"]
r = 60

screen.update()
sleep(1)


#INITIAL CALCULATIONS
deltaY = 800/numbricks   #Thickness of the bricks
numColours = len(colorChoices)


#ASSIGN A COLOUR AND FREQUENCY TO EACH brick
colors = []
B = []   #The frequencies of the brick's motions
brickDrawings = []

#FILLS THE EMPTY ARRAYS WITH INITIAL VALUES
for i in range( numbricks ):
      b = B_min + i * B_difference_per_brick     #Each brick's frequency is a bit higher than the previous, by the amount B_difference_per_brick
      B.append( b )
      c = colorChoices[ i % numColours ]           #Will cycle through the colour choices
      colors.append( c )
      brickDrawings.append( 0 )


#RUNS THE ANIMATION
      
t = 0 #Takes the place of the frame counter, f.  

while True:  #Keeps the animation going forever.  Every repetition of this loop is 1 frame of the animation
      
      #Draws each brick in the current frame in its current position
      for i in range( numbricks ):
            x = A*sin(B[i]*t) + 400  #Every brick has its own private frequency (B[i]), but they all share the same amplitude (A)
            y = deltaY * i
            brickDrawings[i] = screen.create_rectangle( x-r, y, x+r, y+deltaY, fill = colors[i])

      t = t + 1  

      #Updates the screen after all bricks have been drawn, and then pauses 0.03 seconds before deleting all bricks and starting the next frame
      screen.update()
      sleep(0.03)

      #Delete all bricks before next frame
      for i in range( numbricks ):
            screen.delete( brickDrawings[i] )


screen.mainloop() #needed if using repl.it

 
