from tkinter import *
import random
myInterface = Tk()
screen = Canvas (myInterface, width=700, height=800, background="lightblue")
screen.pack()



screen.create_oval(100, 100, 600, 650, fill="#ffe49c")


screen.create_polygon(200, 250, 200, 310, 300, 310, 300, 250, fill="#fff9eb", smooth=True, outline="black")
screen.create_oval(225, 255, 275, 305, fill="black")


screen.create_polygon(200 + 200, 250, 200 + 200, 310, 300 + 200, 310, 300 + 200, 250, fill="#fff9eb", smooth=True, outline="black")
screen.create_oval(225+ 200, 255, 275+ 200, 305, fill="black")

screen.create_polygon(150, 450, 550, 450, 475, 550, 350, 575, 250, 550, smooth=True, fill="red")

#Grid lines
spacing = 50

for x in range(0, 1000, spacing): 
    screen.create_line(x, 25, x, 1000, fill="blue")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    screen.create_line(25, y, 1000, y, fill="blue")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)

screen.update()



myInterface.mainloop()