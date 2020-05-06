from tkinter import *
from time import *
from math import *
from random import *
tk = Tk()
screen = Canvas(tk, width=800, height=800, background="grey20")
screen.pack()

numbat = 20
numrain = 200
numghost = 5

bat = []
xbat = []
ybat = []
xbatspeed = []
ybatspeed = []
ghostbody = []
ghosthead = []
ghosttail = []
ghosteye1 = []
ghosteye2 = []
ghostmouth = []
xghost = []
yghost = []
xghostspeed = []
yghostspeed = []
raindrop = []
xrain = []
yrain = []
rainspeed = []
rainsize = []

screen.create_polygon(-100, 400, 100, 200, 400, 400, 620, 300, 900, 400, 1000, 1000, -200, 1000, smooth = "true", fill = "black")
screen.create_polygon(570, 350, 570, 275, 560, 275, 570, 250, 605, 250, 605, 230, 595, 230, 605, 205, 645, 205, 655, 230, 645, 230, 645, 250, 680, 250, 690, 275, 680, 275, 680, 350, fill = "black")
screen.create_oval(725, 75, 650, 150, fill = "lightyellow2", outline = "grey20")
screen.create_oval(725, 75, 665, 150, fill = "grey20", outline = "grey20")
screen.create_rectangle(0, 450, 800, 800, fill = "olivedrab")
screen.create_polygon(300, 800, 375, 700, 350, 600, 425, 500, 440, 435, 450, 500, 470, 550, 460, 600, 500, 650, 500, 700, 550, 800, 450, 1000, smooth = "true", fill = "darkgoldenrod") 
screen.create_oval(550, 550, 650, 650, fill = "darkseagreen4", outline = "darkseagreen4")
screen.create_rectangle(550, 600, 650, 700, fill = "darkseagreen4", outline = "darkseagreen4")
screen.create_oval(100, 500, 200, 600, fill = "dimgrey", outline = "dimgrey")
screen.create_rectangle(100, 550, 200, 650, fill = "dimgrey", outline = "dimgrey")
screen.create_text(600, 650, text = "RIP", font = "Papyrus 40")
screen.create_line(150, 550, 150, 625, width = "20", fill = "ivory4")
screen.create_line(125, 575, 175, 575, width = "20", fill = "ivory4")

for k in range(150):
    xcloud1 = randint(50, 250)
    ycloud = randint(50, 100)
    size = randint(20, 50)
    xcloud2 = randint(350, 615)
    screen.create_oval(xcloud1, ycloud, xcloud1 + size, ycloud + size, fill = "grey10", outline = "grey10")
    screen.create_oval(xcloud2, ycloud, xcloud2 + size, ycloud + size, fill = "grey10", outline = "grey10")

for i in range(numbat):
    xbat.append(randint(0,800))
    ybat.append(randint(0,200))
    xbatspeed.append(randint(5,15))
    ybatspeed.append(randint(5,15))
    bat.append(i)

for i in range(numghost):
    xghost.append(randint(0,700))
    yghost.append(randint(400,600))
    xghostspeed.append(randint(5,10))
    yghostspeed.append(randint(5,10))
    ghostbody.append(i)
    ghosthead.append(i)
    ghosteye1.append(i)
    ghosteye2.append(i)
    ghostmouth.append(i)
    for w in range(4):
         ghosttail.append(w)

for i in range(numrain):
    xrain.append(randint(0,800))
    yrain.append(randint(0,800))
    rainspeed.append(randint(10,20))
    rainsize.append(randint(50,100))
    raindrop.append(i)

for f in range(1000):
    
    for i in range(numbat):
        bat[i] = screen.create_polygon(xbat[i], ybat[i], xbat[i]+1, ybat[i]-3, xbat[i]+6, ybat[i]-3, xbat[i]+10, ybat[i]-6, xbat[i]+12, ybat[i]-11, xbat[i]+4, ybat[i]-9, xbat[i]+3, ybat[i]-12, xbat[i]+2, ybat[i]-10, xbat[i]-2, ybat[i]-10, xbat[i]-3, ybat[i]-12, xbat[i]-4, ybat[i]-9, xbat[i]-12, ybat[i]-11, xbat[i]-10, ybat[i]-6, xbat[i]-6, ybat[i]-3, xbat[i]-1, ybat[i]-3)
        xbat[i] = xbat[i] + xbatspeed[i]
        ybat[i] = ybat[i] + ybatspeed[i]*sin(0.1 * xbat[i])
        if xbat[i]-12 > 800:
            xbat[i] = 0

    for i in range(numghost):
        ghosthead[i] = screen.create_oval(xghost[i], yghost[i], xghost[i]+100, yghost[i]+100, fill = "white", outline = "white")
        ghostbody[i] = screen.create_rectangle(xghost[i], yghost[i]+50, xghost[i]+100, yghost[i]+150, fill = "white", outline = "white")
        ghosteye1[i] = screen.create_oval(xghost[i]+25, yghost[i]+25, xghost[i]+35, yghost[i]+35, fill = "black")
        ghosteye2[i] = screen.create_oval(xghost[i]+65, yghost[i]+25, xghost[i]+75, yghost[i]+35, fill = "black")
        ghostmouth[i] = screen.create_oval(xghost[i]+40, yghost[i]+50, xghost[i]+60, yghost[i]+70, fill = "black")
        xtail = xghost[i]
        for w in range(4):
            ghosttail[w+(i*4)] = screen.create_oval(xtail, yghost[i]+137, xtail+25, yghost[i]+162, fill = "white", outline = "white")
            xtail = xtail + 25
        xghost[i] = xghost[i] + xghostspeed[i]
        yghost[i] = yghost[i] + yghostspeed[i]
        if xghost[i] < 0 or xghost[i] +100 > 800:
            xghostspeed[i] = xghostspeed[i]*-1
        if yghost[i] < 400 or yghost[i] +163 > 800:
            yghostspeed[i] = yghostspeed[i]*-1
        
    for i in range(numrain):
        raindrop[i] = screen.create_line(xrain[i], yrain[i], xrain[i], yrain[i] + rainsize[i], fill = "blue")
        yrain[i] = yrain[i] + rainspeed[i]
        if yrain[i] > 800:
            yrain[i] = -(rainsize[i])
    screen.update()
    sleep(0.03)

    for i in range(numbat):
        screen.delete(bat[i])

    for i in range(numghost):
        screen.delete(ghosthead[i], ghostbody[i], ghosteye1[i], ghosteye2[i], ghostmouth[i])
        for w in range(4):
            screen.delete(ghosttail[w+(i*4)])

    for i in range(numrain):
        screen.delete(raindrop[i])
