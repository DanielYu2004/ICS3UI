from tkinter import *
from time import *
import random
tk = Tk()
screen = Canvas(tk, width=700, height=700, background="lightblue")
screen.pack()

#Traffic Light container
screen.create_rectangle(250, 150, 450, 550, fill="#ffb845")
screen.create_oval(300, 300, 400, 400, fill="#69682d")
screen.create_oval(300, 425, 400, 525, fill="#314a22")
screen.create_oval(300, 175, 400, 275, fill="#692d2d")

#loop
for i in range(1000000):
    red = screen.create_oval(300, 175, 400, 275, fill="red")
    screen.update()
    sleep(random.randint(2,4))
    screen.delete(red)

    yellow = screen.create_oval(300, 300, 400, 400, fill="yellow")
    screen.update()
    sleep(random.randint(1,2))
    screen.delete(yellow)

    green = screen.create_oval(300, 425, 400, 525, fill="green")
    screen.update()
    sleep(random.randint(2,6))
    screen.delete(green)


screen.mainloop()