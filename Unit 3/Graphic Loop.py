from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=700, height=700, background="sky blue")
screen.pack()


#for line in range(0, 770, 70):
#    screen.create_line(350, 350, 0, line, fill="blue")


#gap = 0

#for square in range(20):
#    screen.create_rectangle(325-gap, 325-gap, 375+gap, 375+gap)
#    gap +=25


#bottom left
for line in range(11):
    screen.create_line(0,350 - (line*35), 35  + (line*35), 0, fill="blue", width="2")

#top left
for line in range(11):
    screen.create_line(0,350 + (line*35), 35  + (line*35), 700, fill="blue", width="2")

#top right
for line in range(11):
    screen.create_line(350 + (line*35),0, 700 , 35 + (line*35), fill="blue", width="2")

#bottom right
for line in range(11):
    screen.create_line(700, 350 + (line*35), 665  - (line*35), 700, fill="blue", width="2")



myInterface.mainloop()
