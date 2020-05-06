from tkinter import *
from time import *
from math import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="black")
screen.pack()

xSpeed=50
ySpeed=-50

xP=20
yP=780
xP2=780
yP2=20

for n in range(10):
      Particel1=screen.create_oval(xP,yP,xP+20,yP+20, fill="blue")
      Particel2=screen.create_oval(xP2,yP2,xP2+20,yP2+20, fill="red")
      
      screen.update()
      sleep(0.03)
      screen.delete(Particel1,Particel2)

      xP = xP + xSpeed
      yP = yP + ySpeed
      xP2 = xP2 - xSpeed
      yP2 = yP2 - ySpeed


xp=[]
yp=[]
xspeedp=[]
yspeedp=[]
xspeed2=[]
yspeed2=[]
sizep=[]
par=[]
colourchoice=[]
colorChoices = ["khaki1","gray63","gray77","LightYellow2","dark green","cyan1","light steel blue", "cyan2", "lawn green","ivory4","ivory3","lightSkyBlue1","lightSkyBlue2","LightSkyBlue3"]           

for i in range(50):
      xp.append(400)
      yp.append(400)
      xspeedp.append(randint(-8,8))
      yspeedp.append(randint(-4,4))
      sizep.append(randint(2,10))
      colourchoice.append(choice(colorChoices))
      par.append(0)   

for f in range(160):
    for i in range(50):
        par[i] = screen.create_oval(xp[i], yp[i], xp[i]+sizep[i], yp[i]+sizep[i], fill=colourchoice[i])
        xp[i] = xp[i] + xspeedp[i]
        yp[i] = yp[i] + yspeedp[i]
        if xp[i]>800 or xp[i]<0:
              for i in range(45):
                    xspeed2.append((400-xp[i])/100)
                    yspeed2.append((400-yp[i])/100)
                    xp2=xp[i]
                    yp2=yp[i]
                    xspeed2New=xspeed2[i]
                    yspeed2New=yspeed2[i]
                    xp[i]=xp2 + xspeed2New
                    yp[i]=yp2 + yspeed2New


        if xp[i]==400 and yp[i]==400:
             xspeed2[i]=0
             yspeed2[i]=0
              
    screen.update()  
    sleep(0.05)  
    for i in range(50):
        screen.delete(par[i])

numLines=50
colorChoices = ["khaki1","gray63","gray77","LightYellow2","dark green","cyan1","light steel blue", "cyan2", "lawn green","ivory4","ivory3","lightSkyBlue1","lightSkyBlue2","LightSkyBlue3"]

x = []
y = []
theta = []
width = []
speed = []
colors=[]      
for l in range(0,numLines):
      x.append(400)
      y.append(400)
      theta.append( uniform(0,2*pi) )
      speed.append( uniform(4,8) )
      width.append( randint(1,4))
      colors.append( choice(colorChoices)) 

b=0.05
r=5
a=0
xCenter=400
yCenter=400

c1 = choice(colorChoices)
c2= choice(colorChoices)
c3= choice(colorChoices)
c4= choice(colorChoices)
c5= choice(colorChoices)

for f in range (1000):
      y1=r*a*cos(b*f) + yCenter
      x1=r*a*sin(b*f) + xCenter
      y2=r*a*sin(-b*f) + yCenter
      x2=r*a*cos(b*f) + xCenter
      y3=r*2*a*cos(b*f) + yCenter
      x3=r*-a*sin(b*f) + xCenter
      y4=r*a*2*sin(b*f) +yCenter
      x4=r*-a*cos(b*f) +xCenter
      x5=r*-a*cos(b*f) +xCenter
      y5=r*-a*sin(b*f) +yCenter
      screen.create_oval(x1,y1,x1+5,y1+5, fill=c1)
      screen.create_oval(x2,y2,x2+3,y2+3, fill=c2)
      screen.create_oval(x3,y3,x3+4,y3+4, fill=c3)
      screen.create_oval(x4,y4,x4+5,y4+5, fill=c4)
      screen.create_oval(x5,y5,x5+3,y5+3, fill=c5)
      a=a+1
      screen.update()
      sleep(0.05)
      
      for i in range (0,numLines):
      
        alpha=theta[i] 
        y2 = y[i] + speed[i]*cos(alpha)
        x2 = x[i] - speed[i]*sin(alpha)

        screen.create_line(x[i],y[i],x2,y2,fill=colors[i], width=width[i])
        x[i] = x2
        y[i] = y2
            




      
