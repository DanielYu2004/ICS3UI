from tkinter import *
from random import *
from time import *
 
myInterface = Tk()
s = Canvas(myInterface, width=1000, height=1000, background="black")
s.pack()
 
# stars
for n in range(2000):
   x3 = randint(1, 1000)
   y3 = randint(1, 1000)
   size = randint(1, 3)
   s.create_oval(x3, y3, x3 + size, y3 + size, fill="white", outline="white")
# sun
r = 10
g = 9
b = 1
 #sun
widths = []
heights = []
 #stars
width = []
height = []
sun = []
moon = []
star = []
Star = []
 #sun
w = 700
h = 700
 #stars
ws = 20
hs = 20
for m in range(0, 30):
   widths.append(w)
   width.append(ws)
   heights.append(h)
   height.append(hs)
   sun.append(0)
   star.append(0)
   w = w - 15
   h = h - 15
   ws = ws - 1
   hs = hs - 1
 
xc = 300
yc = 1100
XC = 1090
YC = 800
# planet
s.create_oval(300, 100, 400, 200, fill="gray55")
s.create_oval(310, 120, 395, 195, fill="gray65")
s.create_oval(315, 130, 390, 187, fill="gray75")
s.create_oval(320, 145, 385, 180, fill="gray85")
s.create_polygon(310, 135, 225, 150, 350, 165, 475, 150, 390, 135, 470, 150, 350, 155, 230, 150, 310, 135,
                fill="gray75", smooth=1)
#moon
a = 600
q = 1000
 
#how many frames
for n in range(100):
   #colours for sun
   r = 10
   g = 10
   b = 1
   #draw sun
   for m in range(0, 30):
       rgb = '#%02x%02x%02x' % (r, g, b)
       sun[m] = s.create_oval(xc - widths[m], yc - heights[m], xc + widths[m], yc + heights[m], fill=rgb, outline=rgb)
       r = r + 6
       g = g + 4
       b = b + 1
   yc = yc - 2
 
   # moon
   moon = []
   moon.append(s.create_oval(a, q, a+2*n + 200, q+2*n + 200, fill="gray55", outline="gray55"))
   moon.append(s.create_oval(a + 80, q + 15, a + 195 + 2 * n, q + 185 + 2 * n, fill="gray50", outline="gray50"))
   moon.append(s.create_oval(a + 100, q + 20, a + 190 + 2 * n, q + 180 + 2 * n, fill="gray45", outline="gray45"))
   moon.append(s.create_oval(a + 120, q + 30, a + 185 + 2 * n, q + 170 + 2 * n, fill="gray40", outline="gray40"))
   moon.append(s.create_oval(a+150,q+50,a+160+2*n,q+150+2*n, fill = "gray35", outline="gray35"))
 
 
   a = a + 4
   q = q + 5
   q = 0.25* (n ** 2)-25*n + 1000
 
   # earth
   s.create_oval(-1800, 550, 1400, 3400, fill="SteelBlue4")
   s.create_polygon(-100, 490, 900, 825, 400, 1100, fill="Steelblue3", smooth=1)
   s.create_polygon(50, 520, 825, 830, 400, 925, fill="SteelBlue2", smooth=1)
   s.create_polygon(325, 650, 317, 670, 300, 675, 275, 675, 250, 700, 275, 690, 300, 705, 300, 725,
                    320, 725, 300, 735, 275, 750, 225, 725, 225, 700, 200, 725, 175, 730,
                    145, 750, 130, 775, 100, 775, 150, 825, 225, 845, 375, 775, 350, 729, fill="sea green")
   s.create_polygon(350, 675, 350, 690, 360, 700, fill="sea green", smooth=1)
   s.create_polygon(400, 710, 350, 750, 374, 750, 390, 780, fill="sea green", smooth=1)
   s.create_polygon(374, 725, 380, 780, fill = "sea green", smooth = 1)
   s.create_polygon(300,875, 325,850,325,825,400,850,325,900,fill="sea green")
 
 
   # shooting star
   for i in range(0, 20):
       greyColour = "gray" + str(i*5)
       star[i] = s.create_oval(XC - width[i], YC - height[i], XC + width[i], YC + height[i], fill=greyColour,
                               outline=greyColour)
 
   YC = YC - 6
   XC = XC - 12
 
 
 
   s.update()
   sleep(0.005)

   if n < 99:
       for m in range(30):
           s.delete(sun[m])
     
       for m in range(20):
           s.delete(star[m])
 
   s.delete(moon[0], moon[1],moon[2],moon[3],moon[4])
 
s.update()
 
