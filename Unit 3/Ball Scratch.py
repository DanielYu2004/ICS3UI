from tkinter import *
import time
tk = Tk()
screen = Canvas(tk, width=800, height=700, background="light blue")
screen.pack()

x1, y1 = 700, 650
x2 = x1 + 50
y2 = y1 + 50
ySpeed = 12
xSpeed = 5
gravity = 0.24

for f in range(5000):
    y1 -= 0.24 * f**2 + yspeed
    y2 = y1 + 50
    x1 -= f*xSpeed
    x2 = x1 + 50

    ball = screen.create_oval(x1, y1, x2, y2, fill="red")
    screen.update()
    time.sleep(0.03)
    screen.delete(ball)
screen.mainloop()