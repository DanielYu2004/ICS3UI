from tkinter import *
from time import *
from random import *
from math import *

window_width = 800
window_height = 800

myInterface = Tk()
screen = Canvas( myInterface, width = window_width, height = window_height, background = "grey10")
screen.pack()

class Point:
    def __init__(self, x, y, vx, vy, after):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.after = after

def clamp(x, vmin, vmax):
    if x > vmax:
        return vmax
    elif x < vmin:
        return vmin
    else:
        return x

sparks = 100
steam = 300

sparks_p = []
steam_p = []

sparks_o = [None] * sparks
steam_o = [None] * steam

lines = [None] * 80

# conveyor
screen.create_rectangle(0, 450, 800, 550, fill = "grey30", width = 0)
screen.create_rectangle(0, 550, 800, 600, fill = "grey40", width = 0)

screen.create_text(650, 575, text = "conveyormatic 2000", font = "Arial 20", fill = "grey30")

# steam pipe
screen.create_rectangle(50, 287, 125, 500, fill = "grey30", width = 0)
screen.create_oval(50, 275, 125, 300, fill = "grey20", width = 0)

# entrance
screen.create_rectangle(0, 400, 100, 450, fill = "grey20", width = 0)

# floor
screen.create_rectangle(0, 600, 800, 800, fill = "bisque4", width = 0)

# Robot arm
screen.create_polygon(550, 175, 675, 250, 675, 225, 560, 160, fill = "cyan")
screen.create_polygon(675, 225, 700, 200, 575, 137, 560, 160, fill = "cyan3")

screen.create_polygon(700, 200, 675, 450, 700, 450, 725, 225, fill = "cyan3")
screen.create_polygon(675, 200, 650, 450, 675, 450, 700, 200, fill = "cyan")

screen.create_line(675, 450, 700, 250, 550, 200, 450, 200, 400, 300, 400, 350, fill = "grey20", width = 8, smooth = True)

# generating the sparks
for i in range(0, sparks):
    x = randint(500, 510)
    y = 475

    # sparks should make less of a square pattern so we use triangle
    vx = triangular(0, -9)
    vy = triangular(-10, -15)
    
    after = randint(250, 275)
    
    sparks_p.append(Point(x, y, vx, vy, after))

# generating the steam
for i in range(0, steam):
    x = randint(50, 100)
    y = randint(0, 280)

    vx = 0
    vy = triangular(-1, -5)

    after = randint(0, 450)

    steam_p.append(Point(x, y, vx, vy, after))

while True:
    for t in range(450):

        # Conveyor belt        
        for i in range(0, 80):
            x1 = ((i+5) * 20 + (2*t)) % 1000
            x2 = (i * 20 + (2*t)) % 1000

            if x2 < x1:
                lines[i] = screen.create_line(x1 - 40, 450, x2 - 40, 550, fill = "white")

        # Box
        box1 = screen.create_rectangle(t*2 - 50, 475, t*2, 525, fill = "snow2", width = 0)
        box2 = screen.create_polygon(t*2 - 50, 475, t*2, 475, t*2 + 25, 450, t*2 - 25, 450, fill = "snow", width = 0)
        box3 = screen.create_polygon(t*2, 475, t*2, 525, t*2 + 25, 500, t*2 + 25, 450, fill = "snow3", width = 0)

        # Weld robot
        weld1 = screen.create_oval(387, 312, 450, 375, fill = "cyan3", width = 0)
        
        arm1 = screen.create_polygon(550, 125, 575, 137, 450, 350, 425, 337, fill = "cyan3")
        arm2 = screen.create_polygon(425, 337, 412, 312, 525, 125, 550, 125, fill = "cyan")
        
        weld2 = screen.create_line(475, 400, 512, 437, 512, 470, fill = "grey50", width = 4, smooth = True)
        weld3 = screen.create_polygon(450, 350, 425, 375, 475, 425, 500, 400, fill = "gray20")

        if 280 > t > 250:
            weld4 = screen.create_polygon(510, 470, 513, 479, 515, 470, fill = ["red", "yellow", "orange"][t % 3])

        # Entrance to conveyor
        entrance1 = screen.create_rectangle(0, 450, 50, 600, fill = "grey40", width = 0)
        entrance2 = screen.create_polygon(0, 450, 50, 450, 100, 400, 0, 400, fill = "grey50", width = 0)

        # Steam
        for i in range(len(steam_p)):
            if t > steam_p[i].after:
                tx = steam_p[i].x
                ty = steam_p[i].y

                tvx = steam_p[i].vx
                tvy = steam_p[i].vy

                steam_o[i] = screen.create_oval(tx, ty, tx + 30, ty + 30, fill = "grey80", outline = "white")

                steam_p[i].x = tx + tvx
                steam_p[i].y = ty + tvy
        
        # Sparks
        for i in range(len(sparks_p)):
            if t > sparks_p[i].after:
                # Apply gravity
                sparks_p[i].vy += 0.3

                sparks_p[i].vx = clamp(sparks_p[i].vx, -20, 20)
                sparks_p[i].vy = clamp(sparks_p[i].vy, -20, 20)
           
                tx = sparks_p[i].x
                ty = sparks_p[i].y
                
                tvx = sparks_p[i].vx
                tvy = sparks_p[i].vy

                sparks_o[i] = screen.create_oval(tx, ty, tx + 3, ty + 3, fill = "yellow", outline = "orange")
            
                sparks_p[i].x = tx + tvx
                sparks_p[i].y = ty + tvy

        screen.update()
        sleep(1 / 60)

        for i in range(len(sparks_o)):
            screen.delete(sparks_o[i])
        for i in range(len(steam_o)):
            screen.delete(steam_o[i])
        for i in range(len(lines)):
            screen.delete(lines[i])

        screen.delete(entrance1, entrance2, box1, box2, box3, arm1, arm2, weld1, weld2, weld3)

        if 280 > t > 250:
            screen.delete(weld4)

    # regenerate the sparks
    for i in range(len(sparks_p)):
        sparks_p[i].x = randint(500, 510)
        sparks_p[i].y = 475
        sparks_p[i].vx = triangular(0, -9)
        sparks_p[i].vy = triangular(-10, -15)
        sparks_p[i].after = randint(250, 275)

    # regenerate the steam
    for i in range(len(steam_p)):
        steam_p[i].x  = randint(50, 100)
        steam_p[i].y = randint(0, 280)
        steam_p[i].vx = 0
        steam_p[i].vy = triangular(-1, -5)
        steam_p[i].after = randint(0, 450)
        
