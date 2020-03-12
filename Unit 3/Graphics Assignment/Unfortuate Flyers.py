from tkinter import *
import time
myInterface = Tk()
screen = Canvas(myInterface, width=1100, height=700, background="sky blue")
screen.pack()


x1 = 400
y1 = 200

x2 = x1 - 80
y2 = y1 + 20

screen.create_oval(x2 - 60, y2 -40, x2 + 60, y2 + 40, fill="white")

screen.create_oval(x1-40,y1-40, x1+40, y1+40, fill="white")
screen.create_polygon(x1+35, y1-20, x1+35, y1+20, x1+40+40, y1, fill="orange")




screen.mainloop()