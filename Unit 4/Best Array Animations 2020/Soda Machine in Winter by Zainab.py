from tkinter import*
from random import*
from time import*
 
root = Tk()
screen = Canvas( root, width=800, height=800, background = "grey79" )
screen.pack()

#Table
screen.create_rectangle(0, 675, 810, 810, fill="sienna", outline="saddle brown")


#Window
screen.create_rectangle(20, 50, 780, 500, fill="#00C9FF", outline="grey", width="10" )
screen.create_line(400, 55, 400, 495, fill="black", width="5" )
screen.create_line(25, 280, 775, 280, fill="black", width="5" )

#soda Machine
screen.create_polygon(675, 510, 750, 525, 775, 765, 675, 765, fill="grey", outline="grey10")
sodaDis = screen.create_polygon(675, 540, 675, 590, 610, 590, 610, 540, fill="grey", outline="grey10")
sodaDis1 = screen.create_rectangle(626, 590, 658, 610, fill="black")

#glass
screen.create_line(620, 765, 610, 600, fill="white")
screen.create_line(673, 600, 663, 765, fill="white")
screen.create_line(620, 765, 663, 765, fill="white")
screen.create_line(673, 600, 610, 600, fill="white")

#Soda Dispenser
x1 = 610
y1 = 540

x2 = 626
y2 = 590
y3 = y2 + 20

ySpeed = 10

#BUBBLES & Snow
b = 100
x = []
y = []
x5 = []
y5 = []
s = []
speeds = []
speeds1 = []
bubblesDrawings = []
snowDrawings = []



#Fills empty arrays 
for i in range(b):
 x.append(randint(620, 660))
 y.append(randint(600, 760))
 s.append(randint(2, 10))
 y5.append(randint(55,495))
 x5.append(randint(25,765))
 speeds.append(uniform(3,6))
 speeds1.append(uniform(1,5))
 bubblesDrawings.append( 0 )
 snowDrawings.append(0)
 
  
#Runs the Animation 
for f in range(120):
   for i in range(b):
       bubblesDrawings[i] = screen.create_oval(x[i], y[i], x[i]+s[i], y[i]+s[i], fill="white")
       snowDrawings[i] = screen.create_oval(x5[i], y5[i], x5[i]+s[i], y5[i]+s[i], fill="white", outline="white")
   #Updates their positions 
       y[i] = y[i] + speeds[i]
       y5[i] = y5[i] + speeds[i]
       x5[i] = x5[i] +speeds1[i]
       
       if y[i] > 760:
           y[i] = 600

       if y5[i] >495:
           y5[i] = 55

       if x5[i] > 765:
           x5[i] = 25
 
   #Update & sleep
   screen.update()
   sleep(0.03)
 
   #Delete the previous bubbles 
   for i in range(b):
    screen.delete(bubblesDrawings[i], snowDrawings[i])


#Dispenser Movement 
for s in range(100):
    screen.delete(sodaDis, sodaDis1)
    
    sodaDis = screen.create_rectangle(x1, y1, x1+65, y1+50, fill="grey", outline="grey10")
    sodaDis1 = screen.create_rectangle(x2, y2, x2+32, y3, fill="black")

    y1 =y1 - ySpeed
    y2 =y2 - ySpeed
    y3 =y3 - ySpeed

    screen.update()
    sleep(0.03)

    if y1 <= 510:
        break


#BUBBLES & Snow 
b = 100
x = []
y = []
x4=[]
y4=[]
s = []
speeds = []
speeds1=[]
bubblesDrawings = []
snowDrawings = []



#Fills empty arrays 
for i in range(b):
 x.append(randint(620, 660))
 y.append(randint(600, 760))
 x4.append(randint(25, 765))
 y4.append(randint(55, 495))
 s.append(randint(2, 10))
 speeds.append(uniform(3,6))
 speeds1.append(uniform(1,5))
 bubblesDrawings.append( 0 )
 snowDrawings.append(0)
    

#Runs the Animation 
for f in range(2000):
   for i in range(b):
       bubblesDrawings[i] = screen.create_oval(x[i], y[i], x[i]+s[i], y[i]+s[i], fill="white")
       snowDrawings[i] = screen.create_oval(x4[i], y4[i], x4[i]+s[i], y4[i]+s[i], fill="white", outline="white")
   #Updates their positions 
       y[i] = y[i] - speeds[i]
       y4[i] = y4[i] + speeds[i]
       x4[i] = x4[i] + speeds1[i]
      
       if y[i] < 600:
           y[i] = 760
                
       if y4[i] > 495:
           y4[i] = 55

       if x4[i] > 765:
           x4[i] = 25
 
   #Update & sleep
   screen.update()
   sleep(0.03)
 
   #Delete the previous bubbles 
   for i in range(b):
    screen.delete(bubblesDrawings[i], snowDrawings[i])


    



screen.mainloop()
