from tkinter import *
myInterface = Tk()
screen = Canvas(myInterface, width=600, height=600, background="sky blue")
screen.pack()


x1 = 250
y1 = 500
x2 = 350
y2 = 600
decrease = 0
diameter = 100
decrease = 2.5
for i in range(100):
    screen.create_oval(x1,y1 , x2,y2, fill="red")
    diameter = diameter - (2*decrease)

    x1 += decrease
    x2 -= decrease
    y2 -= diameter 
    y1 = y2 + diameter


screen.update()





myInterface.mainloop()
