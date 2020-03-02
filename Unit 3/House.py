from tkinter import *

myInterface = Tk()
screen = Canvas (myInterface, width=700, height=700, background="lightblue")
screen.pack()

#Field
screen.create_rectangle(0, 400, 700, 700, fill="green")


#House
screen.create_rectangle(200, 300, 500, 500, fill="dark blue")
screen.create_polygon(200, 300, 350, 200, 500, 300, fill="red")
screen.create_polygon(325, 500, 325, 400, 375, 400, 375, 500, fill="purple")

#Path 
screen.create_polygon(300, 700, 325, 500, 375, 500, 400, 700, fill="gray")






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

