from tkinter import *
import time
myInterface = Tk()
screen = Canvas(myInterface, width=600, height=600, background="sky blue")
screen.pack()


x1, y1, x2, y2 = 100, 0, 150, 50

for f in range(1000):
    while x2 < 600 and y2 < 600:
            
        rect = screen.create_rectangle(x1,y1,x2,y2, fill="red")
    
        screen.update()

        x1 += 5
        y1 += 5
        x2 = x1 + 50
        y2 = y1 + 50
        
        time.sleep(0.01)
        screen.delete(rect)

    while x2 < 600:
        rect = screen.create_rectangle(x1,y1,x2,y2, fill="red")

        screen.update()

        x1 += 5
        y1 -= 5
        x2 = x1 + 50
        y2 = y1 + 50
        
        time.sleep(0.01)
        screen.delete(rect)

    while x1 > 0 and y1 > 0:
        rect = screen.create_rectangle(x1,y1,x2,y2, fill="red")
        screen.update()

        x1 -= 5
        y1 += 5
        x2 = x1 + 50
        y2 = y1 + 50
        
        time.sleep(0.01)
        screen.delete(rect)

    while x1 > 0:
        rect = screen.create_rectangle(x1,y1,x2,y2, fill="red")
        screen.update()

        x1 -= 5
        y1 -= 5
        x2 = x1 + 50
        y2 = y1 + 50

        time.sleep(0.01)
        screen.delete(rect)

        


myInterface.mainloop()
