from tkinter import *
from time import *
from math import *
from random import *

tk = Tk()
s = Canvas(tk, width=800, height=800, background="light blue")
s.pack()

#Used later
count = 0

#Function that original dot lies on
def f1(x):
    return (1/100)*((x - 100)**2) + 100


#Function calculating position of dot (width) away from x position on y = f1(x)
#Take derivitive of f1(x) ==>
#   For each t value repeat: find line passing through (t, f1(t)) tangent to y=f1(x) ==> find perpendicular line passing through (t, f1(t))
#   ==> use pythagorean theorem to calculate [x, y] of new dot (width) units away
#Graph for all general porablas : https://www.desmos.com/calculator/eoojum8plk
def f2(x, width):
    a = 1/100
    b = -2
    #Filter out p = 0
    try:
        p = (width**2 / (1 + 1/((2*a*x + b)**2)))**(1/2)
        q = p*(-1)/(2*a*x + b)

    #when p = 0 (maxima of porabola)
    except:
        return [x, f1(x)+width]

    #Different calculations for different sides of the porabola
    if(x > 100):
        return [-1*p, -1*q]
    else:
        return [p, q]

#Function calculating position of dot (length) away from position on y = f1(x)
#Works the same way as f2() using the pythagorean theorem but with the line directly tangent to y=f1(x)
def f3(x, length):
    a = 1 / 100
    b = -2

    w = (length**2 / (1 + (2*a*x + b)**2))**(1/2)
    r = w*(2*a*x + b)

    return [w, r]


#Function that combines f2 and f3 to determine the relative position of of a dot (xIn, yIn) away from the base point (reference point)
def getCords(origin, xIn, yIn):
    x = abs(xIn)
    y = abs(yIn)
    temp1 = f1(origin)
    temp2 = f2(origin, y)
    temp3 = f3(origin, x)
    if(xIn <= 0):
        if(yIn >= 0):
            return([origin + temp2[0] - temp3[0], temp1 + temp2[1] - temp3[1]])
        elif(yIn < 0):
            return([origin - temp2[0] - temp3[0], temp1 - temp2[1] - temp3[1]])
    else:
        if(yIn >= 0):
            return ([origin + temp2[0] + temp3[0], temp1 + temp2[1] + temp3[1]])
        elif(yIn < 0):
            return ([origin - temp2[0] + temp3[0], temp1 - temp2[1] + temp3[1]])


#Linear function for the railgun
def g(x):
    return (3/4)*(x-675) + 750


#Flame trailing after rocket
flameXdist = [randint(-180, -150) for j in range(10)]
flamesYdist = [randint(-15, 65) for j in range(10)]
flameXspeed = [randint(0, 30) for j in range(10)]
flameYspeed = [randint(-10, 20) for j in range(10)]
flamesYdist.sort()





#base of railgun
s.create_rectangle(600, 750, 800, 800, fill="black")
s.create_polygon(650-100, 675, 700-125, 650, 700, 750, 650, 750, fill="black")
bar = []

for i in range(290):
    #Exclude maxima of porabola
    if(i == 100):
        continue
    flameCords = []
    #Points for the body of the rocket
    bp1 = [i, f1(i)]
    bp2 = getCords(i, 0, 50)
    bp3 = getCords(i, -100, 50)
    bp4 = getCords(i, -100, 0)
    body = s.create_polygon(bp1[0], bp1[1], bp2[0], bp2[1], bp3[0], bp3[1], bp4[0], bp4[1], fill="red", outline="red")

    #points for the tail of the rocket
    tailTemp1 = getCords(i, -125, 75)
    tailTemp2 = getCords(i, -125, -25)
    tail = s.create_polygon(bp3[0], bp3[1], bp4[0], bp4[1], tailTemp2[0], tailTemp2[1], tailTemp1[0], tailTemp1[1], fill="black")

    #points for the head of the rocket
    headTemp = getCords(i, 25, 25)
    head = s.create_polygon(bp1[0], bp1[1], bp2[0], bp2[1], headTemp[0], headTemp[1])


    #Update position of flame
    for j in range(10):
        t = getCords(i, flameXdist[j], flamesYdist[j])
        flameCords.append(t[0]+flameXspeed[j])
        flameCords.append(t[1]+flameYspeed[j])

    tEnd1 = getCords(i, -125, 50)
    tEnd2 = getCords(i, -125, 0)
    flameCords = [tEnd2[0], tEnd2[1]] + flameCords + [tEnd1[0], tEnd1[1]]
    #Plot flame
    flame = s.create_polygon(*flameCords, fill="orange")

    #Animation for charging the Railgun
    if(i < 250):
        bar2 = s.create_line(675, 750, 675 - i * (110/250), g(675 - i * (110/250)), width=10, fill="blue")
    s.create_rectangle(600, 750, 800, 800, fill="black")

    #Animation for firing the Railgun
    if(i > 250):
        speed = 5
        count += 1
        #Light produced during the shot
        bar.append(s.create_line(675-i*(110/250) - count*speed, g(675-i*(110/250) - count*speed), 675 - i + 10 - count*speed, g(675 - i + 10 - count*speed), width=10, fill="orange"))
        #Metal being launched (linear)
        metal = s.create_line(675 - i * (110 / 250) - count * speed, g(675 - i * (110 / 250) - count * speed), 675 - i - 5 - count * speed, g(675 - i - 5 - count * speed), fill="grey", width=25)

    s.update()
    sleep(0.01)
    if(i > 250 and i < 289):
        s.delete(metal)
    if(i < 289):
        s.delete(head, body, tail, flame)
    if(i == 289):
        s.delete(bar)


#Delete
s.delete(head, body, tail, flame, metal)
s.delete(*bar)


#Generate debris from the explosion
debris = []
cols = ["red", "black", "grey"]
speeds = []


x_arr = []
y_arr = []
col_arr = []
size_arr = []
for k in range(500):
    tx = randint(100, 400)
    ty = randint(200, 600)
    size = randint(-5, 10)
    colour = cols[randint(0, 100) % 3]

    x_arr.append(tx)
    y_arr.append(ty)
    col_arr.append(colour)
    size_arr.append(size)

    if tx > 250:
        if ty > 400:
            speeds.append([randint(-10, 0), randint(-10, 0)])
        else:
            speeds.append([randint(-10, 0), randint(0, 10)])
    else:
        if ty > 400:
            speeds.append([randint(0, 10), randint(-10, 0)])
        else:
            speeds.append([randint(0, 10), randint(0, 10)])
    debris.append(
        s.create_oval(tx, ty, tx + size, ty + size, fill=colour, outline=colour)
    )

#Animate debries to collapse
for i in range(50):
    for dot in debris:
        coords = s.coords(dot)  #Get coordinates of each dot
        #Get distance from dot to (400, 400)
        xDist = coords[0] - s.winfo_width()//2
        yDist = coords[1] - s.winfo_height()//2

        #Get speeds of each dot
        xSpeed = xDist/(50 - i)
        ySpeed = yDist/(50 - i)

        #Set new position of dot
        s.coords(dot, coords[0] - xSpeed, coords[1] - ySpeed, coords[2] - xSpeed, coords[3] - ySpeed)

    s.update()
    sleep(0.002)

s.mainloop()