######################################
##Underwater Explosion              ##
##By: Evan Wang                     ##
##Assignment: Array Animation       ##
##Teacher: Mr. Schattman            ##
######################################
from tkinter import *
from time import*   
from random import*
from math import*
interface=Tk()
s=Canvas(interface, width=1200, height=800, background="#0600ad")
s.pack()

#Background
wobble=5
volcanox=200
floor=s.create_rectangle(0, 700, 1200, 800, fill="saddle brown", outline="saddle brown")
volcano=s.create_polygon(200+volcanox, 800, 600+volcanox, 800
                         , 500+volcanox, 550, 300+volcanox
                         , 550, fill="orangered4")
#Air bubbles
airx=[]
airy=[]
airspd=2.5
numberOfAirBubbles=100
airBubbles=[]
for i in range (numberOfAirBubbles):
    airx.append(randint(0, 1200))
    airy.append(randint(0, 700))
    airBubbles.append(0)
#Seaweed
numberOfSeaweeds=30
seaweedDelete=[]
wave=[]
waveSpeed=[]
seaWeedxLocation=[]
for i in range (numberOfSeaweeds):
    seaweedDelete.append(0)
    wave1=randint(-20, -10)
    wave2=randint(10, 20)
    wave.append(choice((wave1, wave2)))
    waveSpeed.append(randint(15, 25))
    seaWeedxLocation.append(choice((randint(0, 400), randint(800, 1200))))
#Smoke bubbles
smokex=[]
smokey=[]
smokespd=5
numberOfSmokeBubbles=50
smokeD=30
smokeBubbles=[]
smokecolor="darkgrey"
smokeStop=[]
for i in range (numberOfSmokeBubbles):
    smokex.append(randint(500, 700-smokeD))
    smokey.append(randint(300, 550))
    smokeBubbles.append(0)
    smokeStop.append(randint(100, 400))
#Cracks
numberOfCracks = 6
radians = 2*pi/numberOfCracks
crackx = []
cracky = []
deltaX = []
slope = []
for crackNum in range(numberOfCracks):
      crackx.append(600)
      cracky.append(650)
      theta = numberOfCracks*radians
      deltaX.append(choice([-1, 1]))
      slope.append(tan(theta))
#Fish that alerts his friends that they can come back
afishSpd=10
afishx1=1300
afishy1=randint(200, 500)
afishTailx1=afishx1+20
afishTailx2=afishx1+30
afishTailx3=afishx1+30
afishEyex=afishx1-10
afishEyey=afishy1-3
afishTaily1=afishy1
afishTaily2=afishy1+10
afishTaily3=afishy1-10
#Fishies
fishx1=[]
fishy1=[]
fishDelete=[]
fishSpdx=[]
numberOfFishes=20
fishTailx=[]
fishTaily=[]
fishEyex=[]
fishEyey=[]
fishEyeDelete=[]
fishTailDelete=[]
exclamation=[]
for i in range (numberOfFishes):
    fishx1.append(randint(-100, 1300))
    fishy1.append(randint(50, 650))
    fishSpdx.append(choice((randint(5, 10), randint(-10, -5))))
    fishEyey.append(fishy1[i]-3)
    #Changes values depending on which direction the fish is going
    if fishSpdx[i]>0:
        fishTailx.append(fishx1[i]-20)
        fishTailx.append(fishx1[i]-30)
        fishTailx.append(fishx1[i]-30)
        fishTaily.append(fishy1[i])
        fishTaily.append(fishy1[i]+10)
        fishTaily.append(fishy1[i]-10)
        fishEyex.append(fishx1[i]+10)
    else:
        fishTailx.append(fishx1[i]+20)
        fishTailx.append(fishx1[i]+30)
        fishTailx.append(fishx1[i]+30)
        fishTaily.append(fishy1[i])
        fishTaily.append(fishy1[i]+10)
        fishTaily.append(fishy1[i]-10)
        fishEyex.append(fishx1[i]-10)
    #Deleting arrays
    fishDelete.append(0)
    fishTailDelete.append(0)
    fishTailDelete.append(0)
    fishTailDelete.append(0)
    exclamation.append(0)
    fishEyeDelete.append(0)
#Explosion/fragments
fragment=[]
fragmentx=[]
fragmenty=[]
fragmentSpdx=[]
fragmentSpdy=[]
numberOfFragments=250
fragmentPointx1=[]
fragmentPointx2=[]
fragmentPointx3=[]
fragmentPointx4=[]
fragmentPointx5=[]
fragmentPointy1=[]
fragmentPointy2=[]
fragmentPointy3=[]
fragmentPointy4=[]
fragmentPointy5=[]
launchTime=[]
fragCol=[]
for i in range (numberOfFragments):
    fragCol.append(choice(("black", "orange", "orange")))
    fragmentx.append(randint(550, 650))
    fragmenty.append(randint(550, 600))
    fragmentSpdx1=randint(3,6)
    fragmentSpdx2=randint(-6, 3)
    fragmentSpdx.append(choice((fragmentSpdx1, fragmentSpdx2)))
    fragmentSpdy.append(randint(5, 10))
    #Uses create polygon with 5 points
    fragmentPointx1.append(fragmentx[i]+randint(0, 0))
    fragmentPointx2.append(fragmentx[i]+randint(10, 15))
    fragmentPointx3.append(fragmentx[i]+randint(5, 10))
    fragmentPointx4.append(fragmentx[i]+randint(-10, 5))
    fragmentPointx5.append(fragmentx[i]+randint(-15, -10))
    fragmentPointy1.append(fragmenty[i]+randint(-15, -10))
    fragmentPointy2.append(fragmenty[i]+randint(-5, 0))
    fragmentPointy3.append(fragmenty[i]+randint(5, 10))
    fragmentPointy4.append(fragmenty[i]+randint(5, 10))
    fragmentPointy5.append(fragmenty[i]+randint(-5, 0))
    fragment.append(0)
    #When the lava/rock erupts
    launchTime.append(randint(280, 500))
################
################
###Animations###
################
################
for f in range (999999):
    #The volcano shaking
    if 500>f>250:
        volcano=s.create_polygon(200+volcanox, 800, 600+volcanox, 800
                         , 500+volcanox, 550, 300+volcanox
                         , 550, fill="orangered4")
        volcanox+=wobble
        wobble=-wobble
        s.tag_lower(volcano)
        s.tag_lower(floor)
    #Air bubble animation
    for i in range (numberOfAirBubbles):
        airBubbles[i]=s.create_oval(airx[i], airy[i], airx[i]+5, airy[i]+5, outline="white")
        if airy[i]<0:
            airy[i]=700
        airy[i]-=airspd
    #Seaweed
    for i in range (numberOfSeaweeds):
        seaWeedx1=sin(f/waveSpeed[i])*wave[i]
        seaWeedx2=sin(f/waveSpeed[i])*wave[i]
        seaWeedx3=sin(f/waveSpeed[i])*wave[i]
        seaweedDelete[i]=s.create_polygon(seaWeedxLocation[i], 700, seaWeedx2+seaWeedxLocation[i], 675,
                                          seaWeedx3+seaWeedxLocation[i], 650, seaWeedx3+10+seaWeedxLocation[i], 650,
                                          seaWeedx2+10+seaWeedxLocation[i],675 ,10+seaWeedxLocation[i], 700,
                                      fill="#00730e", smooth=True)
    #Smoke bubbles
    if f<300:
        for i in range (numberOfSmokeBubbles):
            smokeBubbles[i]=s.create_oval(smokex[i], smokey[i],
                                         smokex[i]+smokeD, smokey[i]+smokeD, fill=smokecolor)
            if smokey[i]<smokeStop[i] and f<275:
                smokey[i]=550
            elif smokey[i]<smokeStop[i]:
                smokey[i]=-100
            smokey[i]-=smokespd
            #Puts the volcano on top
            s.tag_lower(smokeBubbles[i])
    #Fish animation stops the animation at frame 400 because the fish leave the screen by then
    if f<400 or f>800:
        for i in range (numberOfFishes):
            fishDelete[i]=s.create_oval(fishx1[i]-20, fishy1[i]-10, fishx1[i]+20,
                                        fishy1[i]+10, fill="orange")
            fishTailDelete[i]=s.create_polygon(fishTailx[i*3], fishTaily[i*3],
                                               fishTailx[i*3+1], fishTaily[i*3+1],
                                               fishTailx[i*3+2], fishTaily[i*3+2], fill="orange")
            fishEyeDelete[i]=s.create_oval(fishEyex[i], fishEyey[i], fishEyex[i],
                                           fishEyey[i], width="2")
            #Teleports the fish backwards and to random y
            if f<240 or f>800:
                if fishx1[i]-20<-200:
                    fishx1[i]+=1500
                    fishTailx[i*3]+=1500
                    fishTailx[i*3+1]+=1500
                    fishTailx[i*3+2]+=1500
                    fishEyex[i]+=1500
                    fishy1[i]=randint(50, 650)
                    fishEyey[i]=fishy1[i]-3
                    fishTaily[i*3]=fishy1[i]
                    fishTaily[i*3+1]=fishy1[i]+10
                    fishTaily[i*3+2]=fishy1[i]-10
                if fishx1[i]+20>1400:
                    fishx1[i]-=1500
                    fishTailx[i*3]-=1500
                    fishTailx[i*3+1]-=1500
                    fishTailx[i*3+2]-=1500
                    fishEyex[i]-=1500
                    fishy1[i]=randint(50, 650)
                    fishEyey[i]=fishy1[i]-3
                    fishTaily[i*3]=fishy1[i]
                    fishTaily[i*3+1]=fishy1[i]+10
                    fishTaily[i*3+2]=fishy1[i]-10
            #Updates fish values
            fishx1[i]+=fishSpdx[i]
            fishTailx[i*3]+=fishSpdx[i]
            fishTailx[i*3+1]+=fishSpdx[i]
            fishTailx[i*3+2]+=fishSpdx[i]
            fishEyex[i]+=fishSpdx[i]
    #Cracks in the volcano
    if 300>f>250 and f%10==0:
        for i in range(numberOfCracks):
            crackx2=(crackx[i]+deltaX[i]*10+uniform(-0.2, 0.2)*10)
            cracky2=(cracky[i]+slope[i]*10+randint(-1, 1)*10)
            s.create_line(crackx[i] ,cracky[i], crackx2 ,cracky2, fill="black", width=2)
            crackx[i]=crackx2
            cracky[i]=cracky2
    #The volcano begins exploding
    if 240>f>200:
        #Changes color to black & speeds smoke up
        smokecolor="black"
        if smokespd<15:
            smokespd*=1.05
        #Stops the fishes from moving
        for i in range (numberOfFishes):
            fishSpdx[i]=0
    #Creates exclamation marks
    if 300>f>220: 
        for i in range (numberOfFishes):
            exclamation[i]=s.create_text(fishx1[i], fishy1[i]-30, text="!", font="arial 30", fill="white")
    #Makes the fishes run in the opposite direction of the volcano
    if f==240:
        for i in range (numberOfFishes):
            if fishx1[i]>=600:
                fishSpdx[i]=13
            else:
                fishSpdx[i]=-13
        #Flips their tails and eyes in the direction they're running
        for i in range (numberOfFishes):
            if fishx1[i]>=600:
                if fishTailx[i*3]>fishx1[i]:
                    fishTailx[i*3]-=40
                    fishTailx[i*3+1]-=60
                    fishTailx[i*3+2]-=60
                    fishEyex[i]+=20
            else:
                if fishTailx[i*3]<fishx1[i]:
                    fishTailx[i*3]+=40
                    fishTailx[i*3+1]+=60
                    fishTailx[i*3+2]+=60
                    fishEyex[i]-=20
    #Volcano fragments
    if f>275:
        for i in range (numberOfFragments):
            if launchTime[i]<f:
                fragment[i]=s.create_polygon(fragmentPointx1[i], fragmentPointy1[i], fragmentPointx2[i], fragmentPointy2[i]
                                 , fragmentPointx3[i], fragmentPointy3[i], fragmentPointx4[i], fragmentPointy4[i],
                                 fragmentPointx5[i], fragmentPointy5[i], fill=fragCol[i])
                f-=launchTime[i]
                s.tag_lower(fragment[i])
                fragmentPointx1[i]+=fragmentSpdx[i]
                fragmentPointx2[i]+=fragmentSpdx[i]
                fragmentPointx3[i]+=fragmentSpdx[i]
                fragmentPointx4[i]+=fragmentSpdx[i]
                fragmentPointx5[i]+=fragmentSpdx[i]
                fragmentPointy1[i]+=-fragmentSpdy[i]+0.0009*f**2
                fragmentPointy2[i]+=-fragmentSpdy[i]+0.0009*f**2
                fragmentPointy3[i]+=-fragmentSpdy[i]+0.0009*f**2
                fragmentPointy4[i]+=-fragmentSpdy[i]+0.0009*f**2
                fragmentPointy5[i]+=-fragmentSpdy[i]+0.0009*f**2
                f+=launchTime[i]
    #Recreates the volcano
    if f==500:
        volcano=s.create_polygon(200+volcanox, 800, 600+volcanox, 800
                         , 500+volcanox, 550, 300+volcanox
                         , 550, fill="orangered4")
        s.tag_lower(volcano)
        s.tag_lower(floor)
    #The fish that comes back
    if 800>f>675:
            afishDelete=s.create_oval(afishx1-20, afishy1-10, afishx1+20,
                                        afishy1+10, fill="orange")
            afishTailDelete=s.create_polygon(afishTailx1, afishTaily1,
                                               afishTailx2, afishTaily2,
                                               afishTailx3, afishTaily3, fill="orange")
            afishEyeDelete=s.create_oval(afishEyex, afishEyey, afishEyex,
                                           afishEyey, width="2")
            afishx1-=afishSpd
            afishTailx1-=afishSpd
            afishTailx2-=afishSpd
            afishTailx3-=afishSpd
            afishEyex-=afishSpd
            if f==710:
                afishSpd=0
            if f==750:
                    afishTailx1-=40
                    afishTailx2-=60
                    afishTailx3-=60
                    afishEyex+=20
                    afishSpd=-10
    #All the fish return!
    if f==780:
        fishx1=[]
        fishy1=[]
        fishSpdx=[]
        numberOfFishes=20
        fishTailx=[]
        fishTaily=[]
        fishEyex=[]
        fishEyey=[]
        for i in range (numberOfFishes):
            fishx1.append(choice((randint(-100, 0), randint(1200, 1300))))
            fishy1.append(randint(50, 650))
            fishSpdx.append(choice((randint(5, 10), randint(-10, -5))))
            fishEyey.append(fishy1[i]-3)
            #Changes values depending on which direction the fish is going
            if fishSpdx[i]>0:
                fishTailx.append(fishx1[i]-20)
                fishTailx.append(fishx1[i]-30)
                fishTailx.append(fishx1[i]-30)
                fishTaily.append(fishy1[i])
                fishTaily.append(fishy1[i]+10)
                fishTaily.append(fishy1[i]-10)
                fishEyex.append(fishx1[i]+10)
            else:
                fishTailx.append(fishx1[i]+20)
                fishTailx.append(fishx1[i]+30)
                fishTailx.append(fishx1[i]+30)
                fishTaily.append(fishy1[i])
                fishTaily.append(fishy1[i]+10)
                fishTaily.append(fishy1[i]-10)
                fishEyex.append(fishx1[i]-10)
    #Update sleep delete
    s.update()
    sleep(0.03)
    if f>275:
        for i in range (numberOfFragments):
            s.delete(fragment[i])
    if 500>f>=250:
        s.delete(volcano)
    for i in range (numberOfAirBubbles):
        s.delete(airBubbles[i])
    for i in range (numberOfSmokeBubbles):
        s.delete(smokeBubbles[i])
    for i in range (numberOfFishes):
        s.delete(fishTailDelete[i])
        s.delete(fishEyeDelete[i])
        s.delete(fishDelete[i])
    for i in range (numberOfSeaweeds):
        s.delete(seaweedDelete[i])
    #For images that are created after 220 frames
    if f>220:
        for i in range (numberOfFishes):
            s.delete(exclamation[i])
    if 800>f>675:
        s.delete(afishDelete, afishTailDelete, afishEyeDelete)
    
##    print (f)







