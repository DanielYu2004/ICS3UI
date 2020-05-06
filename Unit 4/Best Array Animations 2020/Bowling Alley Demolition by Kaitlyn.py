####################
#   BOWLING ALLEY  #
#By Kaitlyn Pereira#
####################

from tkinter import *
from time import *
from math import *
from random import *


tk = Tk()
s = Canvas(tk, width=800,height=600,background="goldenrod")
s.pack()

while True:
##################
#SCENE 1 - BOWLER#
##################

#creating the scene:
    s.create_rectangle(0,0,800,600,fill = "goldenrod") #for the next time it loops through
    lane1 = s.create_arc(200,550,300,650, start=90, extent=90, fill = "gray20", outline = "gray20")
    lane1a = s.create_rectangle(250,550,800,600, fill = "gray20", outline = "gray20")
    lane2 = s.create_arc(255,305,345,395, start=90, extent=90, fill = "gray20", outline = "gray20")
    lane2a = s.create_rectangle(300,305,800,350, fill = "gray20", outline = "gray20")
    lane3 = s.create_arc(315,115,385,185, start=90, extent=90, fill = "gray20", outline = "gray20")
    lane3a = s.create_rectangle(350,115,800,150, fill = "gray20", outline = "gray20")
    lane4 = s.create_arc(375,25,425,75, start=90, extent=90, fill = "gray20", outline = "gray20")
    lane4a = s.create_rectangle(400,25,800,50, fill = "gray20", outline = "gray20")

#creating the bowler animation
    armX = 50
    armY = 450

    s.create_oval(150,250,250,350,fill="peach puff",outline="peach puff")
    s.create_polygon(125,300,200,375,100,475,25,400, fill="red")
    s.create_polygon(25,400,0,450,0,550,40,500,90,550,60,600,110,600,150,550,100,475,fill="blue")

    for i in range(80):
      ball = s.create_oval(armX-25,armY-50,armX+75,armY+50, fill = "black")
      arm = s.create_polygon(170,375,120,375, armX,armY,armX+50,armY, fill = "peach puff",outline="peach puff")
      hand = s.create_oval(armX,armY-25,armX+50,armY+25, fill = "peach puff",outline="peach puff")
      armX = armX+2
      s.update()
      sleep(0.03)
      s.delete(arm,hand,ball)

#ball rolling down the lane:
    ballX = armX-25
    ballY = armY-50
    d = 100
    for i in range(135):
      ball = s.create_oval(ballX,ballY,ballX+d,ballY+d, fill = "black")
      arm = s.create_polygon(170,375,120,375, armX,armY,armX+50,armY, fill = "peach puff", outline="peach puff")
      hand = s.create_oval(armX,armY-25,armX+50,armY+25, fill = "peach puff",outline="peach puff")
      ballX = ballX+5
      s.update()
      sleep(0.03)
      s.delete(ball)

#############################
#SCENE 2 - BALL HITTING PINS#
#############################

#setting up the scene
    s.create_rectangle(0,0,800,600,fill = "goldenrod")
    s.create_rectangle(0,50,800,250, fill = "black")
    s.create_rectangle(0,0,800,50,fill = "blue")
    s.create_text(400,25, font="arial 50", text= "LANE 3")
    s.create_polygon(100,250,200,250,0,600,0,425, fill = "gray20")
    s.create_rectangle(100,0,200,250, fill="gray20")
    s.create_polygon(600,250,700,250,800,425,800,600, fill = "gray20")
    s.create_rectangle(600,0,700,250, fill = "gray20")

#empty arrays for the different parts of the pins
    pinA = []
    pinB = []
    pinC = []

    ballx = 400
    bally = 600
    r = 80

    for f in range(55):
        x1a = 255          #values inside the loop so they reset
        x2a = x1a+50
        y1a = 150
        y2a = y1a+50
        x1b = 295
        x2b = x1b+50
        y1b = 165
        y2b = y1b+50
        x1c = 340
        x2c = x1c+50
        y1c = 180
        y2c = y1c+50
        x1 = 375
        x2 = x1+50
        y1 = 195
        y2 = y1+50
        for i in range(10):
            if i<4:            #back 4 pins
                pinA.append(0)
                pinB.append(0)
                pinC.append(0)
                pinA[i] = s.create_oval(x1a,y1a,x2a,y2a, fill = "old lace")
                pinB[i] = s.create_oval(x1a,y2a,x2a,y2a+120, fill = "old lace")
                pinC[i] = s.create_line(x1a,y2a+60,x2a,y2a+60, width = 7, fill = "red")
                x1a = x1a+80
                x2a = x1a+50
            elif i<7:          #third row - 3 pins
                pinA.append(0)
                pinB.append(0)
                pinC.append(0)
                pinA[i] = s.create_oval(x1b,y1b,x2b,y2b, fill = "old lace")
                pinB[i] = s.create_oval(x1b,y2b,x2b,y2b+120, fill = "old lace")
                pinC[i] = s.create_line(x1b,y2b+60,x2b,y2b+60, width = 7, fill = "red")
                x1b = x1b+80
                x2b = x1b+50
            elif i<9:         #second row - 2 pins
                pinA.append(0)
                pinB.append(0)
                pinC.append(0)
                pinA[i] = s.create_oval(x1c,y1c,x2c,y2c, fill = "old lace")
                pinB[i] = s.create_oval(x1c,y2c,x2c,y2c+120, fill = "old lace")
                pinC[i] = s.create_line(x1c,y2c+60,x2c,y2c+60, width = 7, fill = "red")
                x1c = x1c+75
                x2c = x1c+50
            else:             #front pin
                pinA.append(0)
                pinB.append(0)
                pinC.append(0)
                pinA[i] = s.create_oval(x1,y1,x2,y2, fill = "old lace")
                pinB[i] = s.create_oval(x1,y2,x2,y2+120, fill = "old lace")
                pinC[i] = s.create_line(x1,y2+60,x2,y2+60, width = 7, fill = "red")

        ball = s.create_oval(ballx-r,bally-r,ballx+r,bally+r, fill = "black")
        bally = bally-5
        r = r-0.5      #ball gets smaller - adds perspective
        s.update()
        sleep(0.03)
        for i in range(10):
            s.delete(pinA[i], pinB[i],pinC[i])
        s.delete(ball)

#explosion when ball hits the pins
    for f in range(5):
        x1a = 255
        x2a = x1a+50
        y1a = 150
        y2a = y1a+50
        x1b = 295
        x2b = x1b+50
        y1b = 165
        y2b = y1b+50
        x1c = 340
        x2c = x1c+50
        y1c = 180
        y2c = y1c+50
        x1 = 375
        x2 = x1+50
        y1 = 195
        y2 = y1+50
        for i in range(10):
            if i<4:
                pinA.append(0)
                pinB.append(0)
                pinC.append(0)
                pinA[i] = s.create_oval(x1a,y1a,x2a,y2a, fill = "old lace")
                pinB[i] = s.create_oval(x1a,y2a,x2a,y2a+120, fill = "old lace")
                pinC[i] = s.create_line(x1a,y2a+60,x2a,y2a+60, width = 7, fill = "red")
                x1a = x1a+80
                x2a = x1a+50
            elif i<7:
                pinA.append(0)
                pinB.append(0)
                pinC.append(0)
                pinA[i] = s.create_oval(x1b,y1b,x2b,y2b, fill = "old lace")
                pinB[i] = s.create_oval(x1b,y2b,x2b,y2b+120, fill = "old lace")
                pinC[i] = s.create_line(x1b,y2b+60,x2b,y2b+60, width = 7, fill = "red")
                x1b = x1b+80
                x2b = x1b+50
            elif i<9:
                pinA.append(0)
                pinB.append(0)
                pinC.append(0)
                pinA[i] = s.create_oval(x1c,y1c,x2c,y2c, fill = "old lace")
                pinB[i] = s.create_oval(x1c,y2c,x2c,y2c+120, fill = "old lace")
                pinC[i] = s.create_line(x1c,y2c+60,x2c,y2c+60, width = 7, fill = "red")
                x1c = x1c+75
                x2c = x1c+50
            else:
                pinA.append(0)
                pinB.append(0)
                pinC.append(0)
                pinA[i] = s.create_oval(x1,y1,x2,y2, fill = "old lace")
                pinB[i] = s.create_oval(x1,y2,x2,y2+120, fill = "old lace")
                pinC[i] = s.create_line(x1,y2+60,x2,y2+60, width = 7, fill = "red")
        ball = s.create_oval(ballx-r,bally-r,ballx+r,bally+r, fill = "black")
        explosion = s.create_polygon(400,100,435,200,550,150,525,225,550,350,500,300,475,400,425,300,375,350,350,300,300,375,300,300,250,350,300,250,250,150,300,175,350,125,375,175,400,100, fill = "orange")
        s.update()
        sleep(0.03)
        s.delete(explosion)
        
        for i in range(10):
            s.delete(pinA[i], pinB[i],pinC[i])
        s.delete(ball)

#exploding bits - start by setting up empty arrays     
    bits1 = []
    bits2 = []
    bits3 = []
    bits4 = []
    ballbits = []
    Bits1x = []
    Bits1y = []
    Bits2x = []
    Bits2y = []
    Bits3x = []
    Bits3y = []
    Bits4x = []
    Bits4y = []
    size = []
    size2 = []
    size3 = []
    size4 = []
    speedx = []
    speedx2 = []
    speedx3 = []
    speedx4 = []
    speedy = []
    speedy2 = []
    speedy3 = []
    speedy4 = []
    ballBitx = []
    ballBity = []
    ballspeedx = []
    ballspeedy = []
    ballsize = []

#filling arrays with random values for random bits
    for b in range(100):
      bits1.append(0)
      Bits1x.append(randint(375,425))
      Bits1y.append(randint(297,353))
      size.append(randint(1,5))
      speedx.append(randint(-5,5))
      speedy.append(randint(-5,5))
    for b in range(200):
      bits2.append(0)
      Bits2x.append(randint(295,505))
      Bits2y.append(randint(257,313))
      size2.append(randint(1,5))
      speedx2.append(randint(-5,5))
      speedy2.append(randint(-5,5))
    for b in range(300):
      bits3.append(0)
      Bits3x.append(randint(215,585))
      Bits3y.append(randint(217,273))
      size3.append(randint(1,5))
      speedx3.append(randint(-5,5))
      speedy3.append(randint(-5,5))
    for b in range(400):
      bits4.append(0)
      Bits4x.append(randint(135,665))
      Bits4y.append(randint(177,233))
      size4.append(randint(1,5))
      speedx4.append(randint(-5,5))
      speedy4.append(randint(-5,5))
    for b in range(100):
        ballbits.append(0)
        ballBitx.append(randint(375,425))
        ballBity.append(randint(300,350))
        ballspeedx.append(randint(-5,5))
        ballspeedy.append(randint(-5,5))
        ballsize.append(randint(1,5))

#creating the bits and moving them
    for c in range(40):
        for f in range(100):
            bits1[f] = s.create_rectangle(Bits1x[f]-size[f],Bits1y[f]-size[f],Bits1x[f]+size[f],Bits1y[f]+size[f], fill = "old lace", outline = "old lace")
            Bits1x[f] = Bits1x[f] + speedx[f]
            Bits1y[f] = Bits1y[f] + speedy[f]

        for f in range(200):
            bits2[f] = s.create_rectangle(Bits2x[f]-size2[f],Bits2y[f]-size2[f],Bits2x[f]+size2[f],Bits2y[f]+size2[f], fill = "old lace", outline = "old lace")
            Bits2x[f] = Bits2x[f] + speedx2[f]
            Bits2y[f] = Bits2y[f] + speedy2[f]

        for f in range(300):
            bits3[f] = s.create_rectangle(Bits3x[f]-size3[f],Bits3y[f]-size3[f],Bits3x[f]+size3[f],Bits3y[f]+size3[f], fill = "old lace", outline = "old lace")
            Bits3x[f] = Bits3x[f] + speedx3[f]
            Bits3y[f] = Bits3y[f] + speedy3[f]

        for f in range(400):
            bits4[f] = s.create_rectangle(Bits4x[f]-size4[f],Bits4y[f]-size4[f],Bits4x[f]+size4[f],Bits4y[f]+size4[f], fill = "old lace", outline = "old lace")
            Bits4x[f] = Bits4x[f] + speedx4[f]
            Bits4y[f] = Bits4y[f] + speedy4[f]

        for f in range(100):
            ballbits[f] = s.create_rectangle(ballBitx[f]-ballsize[f],ballBity[f]-ballsize[f],ballBitx[f]+ballsize[f],ballBity[f]+ballsize[f], fill="black")
            ballBitx[f] = ballBitx[f] + ballspeedx[f]
            ballBity[f] = ballBity[f] + ballspeedy[f]
             
        s.update()
        sleep(0.03)
#deleting the bits
        for f in range(100):
            s.delete(ballbits[f])
        for f in range(100):
            s.delete(bits1[f])
        for f in range(200):
            s.delete(bits2[f])
        for f in range(300):
            s.delete(bits3[f])
        for f in range(400):
            s.delete(bits4[f])

#######################
#SCENE 3 - CELEBRATION#
#######################

    s.create_rectangle(0,0,800,600,fill = "goldenrod")
    s.create_rectangle(0,0,800,250, fill = "ivory3")

#empty arrays      
    Head = []
    Body = []
    Legs = []
    Arm1 = []
    Arm2 = []
    spectatorX = []
    spectatorY = []
    spectatorSpeed = []
    shirtColours = ["red", "orange", "green", "turquoise1", "purple", "pink"]
    bowlerX = 400
    bowlerY = 300
    speed = 2
    bannerY1 = 0-100
    bannerY2 = bannerY1+100
    
#filling the arrays    
    for i in range(50):
        Head.append(0)
        Body.append(0)
        Legs.append(0)
        Arm1.append(0)
        Arm2.append(0)
        spectatorX.append(randint(75,725))
        spectatorY.append(randint(175,375))
        spectatorSpeed.append(randint(1,3))

#creating the spectators and making them jump up and down, lowering banner
    for f in range(500):
        for i in range(50):
            Head[i] = s.create_oval(spectatorX[i]-25,spectatorY[i]-25,spectatorX[i]+25,spectatorY[i]+25, fill = "peach puff")
            Body[i] = s.create_rectangle(spectatorX[i]-25,spectatorY[i]+25,spectatorX[i]+25,spectatorY[i]+100, fill = shirtColours[i%6])
            Legs[i] = s.create_rectangle(spectatorX[i]-25,spectatorY[i]+100,spectatorX[i]+25,spectatorY[i]+150, fill = "blue")
            Arm1[i] = s.create_polygon(spectatorX[i]-25,spectatorY[i]+25,spectatorX[i]-25,spectatorY[i]+50,spectatorX[i]-63,spectatorY[i]-25,spectatorX[i]-50,spectatorY[i]-25, fill = "peach puff")
            Arm2[i] = s.create_polygon(spectatorX[i]+25,spectatorY[i]+25,spectatorX[i]+25,spectatorY[i]+50,spectatorX[i]+63,spectatorY[i]-25,spectatorX[i]+50,spectatorY[i]-25, fill = "peach puff")
            spectatorY[i] = spectatorY[i]-spectatorSpeed[i]
        bHead = s.create_oval(bowlerX-50,bowlerY-50,bowlerX+50,bowlerY+50, fill = "peach puff")
        bBody = s.create_rectangle(bowlerX-50,bowlerY+50,bowlerX+50,bowlerY+200, fill = "red")
        bLegs = s.create_rectangle(bowlerX-50,bowlerY+200,bowlerX+50,bowlerY+300, fill = "blue")
        lArm = s.create_polygon(bowlerX-50,bowlerY+50,bowlerX-50,bowlerY+100,bowlerX-125,bowlerY-50,bowlerX-100,bowlerY-50, fill = "peach puff")
        rArm = s.create_polygon(bowlerX+50,bowlerY+50,bowlerX+50,bowlerY+100,bowlerX+125,bowlerY-50,bowlerX+100,bowlerY-50, fill = "peach puff")
        bowlerY = bowlerY-speed
        if f%50 == 0:
            speed = speed*(-1)
            for i in range(50):
                spectatorSpeed[i] = spectatorSpeed[i]*(-1)

        banner = s.create_rectangle(200,bannerY1,600,bannerY2, fill = "blue")
        strings = s.create_rectangle(200,0,600,bannerY2, outline = "black")
        text = s.create_text(400,bannerY1+50, font="arial 50", text= "STRIKE!!!")

        if bannerY2<150:
            bannerY1 = bannerY1+2
            bannerY2 = bannerY1+100

        s.update()
        sleep(0.03)
        s.delete(bHead,bBody,bLegs,lArm,rArm,banner,strings,text)
        for i in range(50):
            s.delete(Head[i],Body[i],Legs[i],Arm1[i],Arm2[i])


        
