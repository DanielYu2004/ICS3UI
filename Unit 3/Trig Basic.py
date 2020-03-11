from tkinter import *
import math
import time
myInterface = Tk()
screen = Canvas(myInterface, width=700, height=700, background="black")
screen.pack()


x1 = 350
y1 = 350
A = 300
balls = []
ballss = []
coords = []
# for f in range(5000):
#     x1 = 350 + A*math.sin(0.03*f)
#     y1 = 350 + A*math.cos(0.03*f)
#     ball = screen.create_oval(x1 -10, y1 -10, x1 + 10, y1 + 10, fill="white", outline="white")
#     balls.append(ball)
#     screen.update()
#     time.sleep(0.003)
#     #screen.delete(ball)
#     if f > 50:
#         screen.delete(balls.pop(0))
#     if A > 0:
#         A -= 0.5
#     else:
#         break
#     print(A)

for f in range(5000):
    x1 = 350 + A*math.sin(0.03*(5000-f))
    y1 = 350 + A*math.cos(0.03*(5000-f))
    print(x1, y1)
    ball = screen.create_oval(x1 -10, y1 -10, x1 + 10, y1 + 10, fill="white", outline="white")
    balls.append(ball)
    coords.append([x1 -10, y1 -10, x1 + 10, y1 + 10])
    screen.update()
    time.sleep(0.003)
    #screen.delete(ball)
    if f > 50:
        screen.delete(balls.pop(0))
        ball = screen.create_oval(coords[0 + f-51], fill="grey", outline="grey")
        ballss.append(ball)
    if f > 100:
        screen.delete(ballss.pop(0))
    if abs(A) <= 300:
        A -= 0.5
    else:
        while balls:
            screen.delete(balls.pop(0))
            screen.update()
            time.sleep(0.003)
        break






screen.mainloop()