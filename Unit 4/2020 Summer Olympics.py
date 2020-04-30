from tkinter import *
import time
import math
myInterface = Tk()

screen = Canvas(myInterface, width=1000, height=700, background="sky blue")
screen.pack()

# Foreground
screen.create_rectangle(0, 700, 1000, 600, fill="green")



# Track
screen.create_rectangle(0, 600, 1000, 300, fill="black")


screen.mainloop()
