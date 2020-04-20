##########################################################
#                       Daniel Yu                        # 
#                   Reuleaux Triangle                    #
#                        ICS3UI                          #
##########################################################

from tkinter import *
import time
import math
myInterface = Tk()


#Variables
width =800
height = 800
triLen = 300
x1 = width/2
y1 = (height - (triLen/2 * math.sqrt(3)))/2
x2 = (width -triLen)/2
y2 = (height - (triLen/2 * math.sqrt(3)))/2 + (triLen/2 * math.sqrt(3))
x3 = ((width-triLen)/2) + triLen
y3 = (height - (triLen/2 * math.sqrt(3)))/2 + (triLen/2 * math.sqrt(3))


screen = Canvas(myInterface, width=width, height=height, background="sky blue")
screen.pack()


#screen.create_polygon(x1,y1,x2,y2,x3,y3, fill="red")

screen.create_arc(x2-triLen,y2 - triLen, x3 ,y3 + triLen, start=0, extent=60, fill="red", outline="red")
#screen.create_rectangle(x2-triLen,y2 - triLen, x3 ,y3 + triLen, outline="blue")

screen.create_arc(x2,y2 - triLen, x3 + triLen,y3 + triLen, start=120, extent=60, fill="red", outline="red")
#screen.create_rectangle(x2,y2 - triLen, x3 + triLen ,y3 + triLen, outline="green")

screen.create_arc(x1-triLen, y1-triLen, x1 + triLen, y1 + triLen, start=240, extent=60, fill="red", outline="red")
#screen.create_rectangle(x1-triLen, y1-triLen, x1 + triLen, y1 + triLen, outline="red")



screen.mainloop()