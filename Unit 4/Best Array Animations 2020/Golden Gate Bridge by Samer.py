from tkinter import *
from random import *
from time import *
from math import *
myInterface = Tk()
screen = Canvas( myInterface, width=1400, height=1000, background="#21276b" )
screen.pack()

###########################################

bridge = list()
#########################################
#Sky(Gradient maker)
r = 33
g = 39
b = 107
x1 = 0
x2 = 1420
y = 0

for f in range(51):
    hr = hex(r)
    hr = str(hr.lstrip("0x"))
    hg = hex(g)
    hg = str(hg.lstrip("0x"))
    hb = hex(b)
    hb = str(hb.lstrip("0x"))
    
    if len(hr) == 1:
        hr = "0"+hr
    if len(hg) == 1:
        hg = "0"+hg
    if len(hb) == 1:
        hb = "0"+hb
        
    screen.create_line(x1,y,x2,y, fill =("#"+hr+hg+hb),width = 20)
    
    b = b+1
    r = r+3
    g = g+2
    if f  > 35:
        r = r+6
        g = g+4
    y = y + 10
    
    if r>= 244:     #Sets a stop for the colours
        r = 244
    if b >= 244:
        b = 244
    if g >= 244:
        g = 244
########################################################################
#Terrain(Different layers stacked on top of each other)
screen.create_polygon(1000,430,1320,370,1430,400,1430,510,1000,510,fill = "#786202", outline = "#786202")

screen.create_polygon(500,470,760,400,960,415,1140,460,1430,460,1430,510,500,510,
                      fill = "#574701", outline = "#574701")

screen.create_polygon(300,475,440,460,720,480,1020,460,1240,
                      430,1450,450,1400,1000,1430,510,300,510
                      ,fill = "#403400", outline = "#403400")    

screen.create_polygon(0,480,120,470,320,475,420,475,600,470,760,465,880,
                      460,920,455,1080,470,1240,475,1360,480,1430,470,1430,510,0,510,
                      fill="#332901",outline="#332901",smooth = "false")

#######################################################################
#Details in water(The white lines)
for i in range(50):
    x = randint(0,1400)
    y = randint(53,100)
    size = randint(30,100)
    screen.create_line(x,y*10,x+size,y*10, width = 1,fill = "#3340a1")


################################################################
#Left parabolas
parab1L = list()
parabx1L = list()
paraby1L = list()
parab2L = list()
parabx2L = list()
paraby2L = list()

#Nothing is being drawn right now
#Saved for the animation

#Assigning values
#Foreground curve 
for i in range(0,320):
    parab1L.append(i)
    parabx1L.append(i)
    parab1L.append((-5/10368)*(i+400)**2+570)
    paraby1L.append((-5/10368)*(i+400)**2+570)
#Background curve
for i in range(0,190):
    parab2L.append(i)
    parabx2L.append(i)
    parab2L.append((-5/9248)*(i+480)**2+570)
    paraby2L.append((-5/9248)*(i+480)**2+570)

#########################################################    
#Centre Parabolas
#Background curve
parabc1 = list()
parabxc1 = list()
parabyc1= list()
parabc1 = list()

#Assigning values
for i in range(208,881):
    parabc1.append(i)
    parabxc1.append(i)
    parabc1.append((-5/9248)*(i-880)**2+570)
    parabyc1.append((-5/9248)*(i-880)**2+570)
    
#I used two different loops since I'm combining two different curves
for i in range(881,1100):
    parabc1.append(i)
    parabxc1.append(i)
    parabc1.append((-19/4840)*(i-880)**2+570)
    parabyc1.append((-19/4840)*(i-880)**2+570)
   
#Foreground parabola
parabc2 = list()
parabyc2 = list()
parabxc2 = list()
parabyc2 = list()

#Assigning values
for i in range(324,1041):
    parabc2.append(i)
    parabxc2.append(i)
    parabc2.append((-5/10368)*(i-1040)**2+570)
    parabyc2.append((-5/10368)*(i-1040)**2+570)
    
for i in range(1041,1200):
    parabc2.append(i)
    parabxc2.append(i)
    parabc2.append((-19/2560)*(i-1040)**2+570)
    parabyc2.append((-19/2560)*(i-1040)**2+570)

######################################################
    
#Right Parabolas
parabr1 = list()
parabxr1 = list()
parabyr1 = list()
parabr2 = list()
parabxr2 = list()
parabyr2 = list()

#Assigning values

#Background Curve
for i in range(1100,1160):
    parabr1.append(i)
    parabxr1.append(i)
    parabr1.append((-1/30)*(i-1160)**2+500)
    parabyr1.append((-1/30)*(i-1160)**2+500)

#Foreground Curve
for i in range(1200,1260):
    parabr2.append(i)
    parabxr2.append(i)
    parabr2.append((-1/30)*(i-1260)**2+500)
    parabyr2.append((-1/30)*(i-1260)**2+500)

####################################################

#cars 
#Setting up lists  
colour = list()
xC = list()
speed = list()
cars = list()
size = list()                               #Size is the variable that changes the size
lane = list()                               #of the car depending on its location

#Assigning values
for i in range(13):
    xC.append(randint(0,20)*60)
    speed.append(10)
    colour.append(choice(["blue","orange","green","white","#5a216b","#216b5d","#91bd00"]))
    cars.append(0)
    size.append(0)
    lane.append(randint(1,3))
##################################################################################

#Boats
#Setting up lists
xB = list()
yB = list()
speedxB = list()
speedyB = list()
boats = list()
colourBoat = list()
#assigning values    
for i in range(10):
    xB.append(randint(12,20)*140)
    yB.append(randint(560,1000))
    speedxB.append(randint(-4,-1))
    speedyB.append(randint(-2,2))
    boats.append(0)
    colourBoat.append(choice(["#2e302f","#464f4a","#d4d4d4","#adacac"]))

   
##############################################################            

#random starfall
#setting up lists
starx = list()
stary = list()
starsizey = list()
starsizex = list()
stars = list()
starspeed = list()
#Assigning values
for i in range(5):
    starx.append(randint(600,1400))
    stary.append(randint(-600,-100))
    starsizey.append(randint(10,100))
    starsizex.append(randint(10,50))
    stars.append(0)
    starspeed.append(randint(40,60))
    

#Animation Loop
t = 0                                                   #timer I use for the skyfall animation
fall = True
while True:                                             #Never ending loop
    t += 1
    bridge = list()
    if t % 200>0 and t%200 <50 and fall == True:        #Sky fall animation runs every 200 frames for a maximum of 50 frames
        for i in range(len(stars)):
            if stary[i] < 300:                          #checks if the any of the stars reached the ground
                
                stars[i] = screen.create_line(starx[i],stary[i],starx[i]-30 , stary[i]+100, fill = "white",stipple = "gray25")
            else:
                fall = False                            #Variable that makes sure the animation doesn't continue after the stars hit the ground
                break
            starx[i] -= 5
            stary[i] += starspeed[i]
    if t%200 == 50:                                     #After the fifty frames have passed, fall is set to true again so the loop can happen again in 200 frames
        fall = True
        for i in range(len(stars)):
            starx[i] = randint(700,1400)
            stary[i] = randint(-400,-100)
#########################################################################            
    #Boat animation
    for i in range(len(boats)):
        x = xB[i]
        y = yB[i]
        #checks the direction to choose the correct shape
        if speedyB[i]> 0:
            cx0 = x +44.851319010308316         #The reason the numbers are so weird is because I wrote some code to rotate shapes and print coordinates in relation
            cy0 = y +-8.343211793760815         #to a main point (x,y)
            cx1 = x +37.161042425638925
            cy1 = y +-11.929246658522231
            cx2 = x +31.522886700923436
            cy2 = y +-9.877125798568215
            cx3 = x +28.895548089166596
            cy3 = y +-10.517119407264317
            cx4 = x +19.733545036504097
            cy4 = y +-7.182423009839056
            cx5 = x +19.54180578590319
            cy5 = y +-5.516368971165946
            cx6 = x +16.72272792354545
            cy6 = y +-4.490308541188938
            cx7 = x +7.851964180386631
            cy7 = y +-13.07398785795391
            cx8 = x +9.850193698762723
            cy8 = y +-16.35531057781708
            cx9 = x +-5.654734544204757
            cy9 = y +-10.711978212943563
            cx10 =x +-6.038213045406565
            cy10 =y +-7.3798701355973435
            cx11 = x +-15.90498556365867
            cy11 = y +-3.788658630677787
            cx12 = x +-21.23325250331777
            cy12 = y +6.132005229152128
            cx13 = x +-41.479827754810344
            cy13 = y +11.904889307812311
            cx14 = x +-42.42712182848368
            cy14 = y +15.442209471153888
            cx15 = x +-34.73684524381417
            cy15 = y +19.02824433591536
            cx16 = x +-25.304336584246926
            cy16 = y +20.38389192551631
            cx17 = x +-19.99887400325042
            cy17 = y +20.049128125734228
            cx18 = x +43.571331792916226
            cy18 = y +-3.088534570247191
        elif speedyB[i]<0:
            cx0 = x +39.72101686042333
            cy0 = y +22.438601105549424
            cx1 = x +36.134981995661974
            cy1 = y +14.748324520879919
            cx2 = x +30.496826270946485
            cy2 = y +12.696203660925903
            cx3 = x +28.895548089166596
            cy3 = y +10.517119407264317
            cx4 = x +19.733545036504097
            cy4 = y +7.182423009839056
            cx5 = x +18.51574535592613
            cy5 = y +8.335446833523633
            cx6 = x +15.696667493568384
            cy6 = y +7.309386403546625
            cx7 = x +14.418750932239504
            cy7 = y +-4.968110461135552
            cx8 = x +18.058677138578787
            cy8 = y +-6.197312321044706
            cx9 = x +2.5537488956113066
            cy9 = y +-11.840644685918221
            cx10 = x +0.11814953445548326
            cy10 = y +-9.534597038549009
            cx11 = x +-9.748622983796622
            cy11 = y +-13.125808543468565
            cx12 = x +-20.207192073340707
            cy12 = y +-8.951083091509815
            cx13 = x +-39.42770689485633
            cy13 = y +-17.543045032527743
            cx14 = x +-42.42712182848368
            cy14 = y +-15.442209471153888
            cx15 = x +-38.841086963722205
            cy15 = y +-7.75193288648444
            cx16 = x +-32.48675959408604
            cy16 = y +-0.6503468890122122
            cx17 = x +-28.207357443066485
            cy17 = y +2.5034947731275565
            cx18 = x +35.36284835310016
            cy18 = y +25.641157469108975
        else:
            cx0 = x +45.0
            cy0 = y +7.5
            cx1 = x +39.0
            cy1 = y +1.5
            cx2 = x +33.0
            cy2 = y +1.5
            cx3 = x +30.75
            cy3 = y +0.0
            cx4 = x +21.0
            cy4 = y +0.0
            cx5 = x +20.25
            cy5 = y +1.5
            cx6 = x +17.25
            cy6 = y +1.5
            cx7 = x +11.850000000000023
            cy7 = y +-9.600000000000023
            cx8 = x +14.850000000000023
            cy8 = y +-12.0
            cx9 = x +-1.6499999999999773
            cy9 = y +-12.0
            cx10 =x +-3.1499999999999773
            cy10 = y +-9.0
            cx11 = x +-13.649999999999977
            cy11 = y +-9.0
            cx12 = x +-22.049999999999955
            cy12 = y +-1.5
            cx13 = x +-43.049999999999955
            cy13 = y +-3.0
            cx14 = x +-45.149999999999864
            cy14 = y +0.0
            cx15 = x +-39.149999999999864
            cy15 = y +6.0
            cx16 = x +-30.749999999999773
            cy16 = y +10.5
            cx17 = x +-25.649999999999864
            cy17 = y +12.0
            cx18 = x +42.0
            cy18 = y +12.0
        boats[i] = screen.create_polygon(cx0,cy0,cx1,cy1,cx2,cy2,cx3,cy3,cx4,cy4,cx5,cy5,
                                              cx6,cy6,cx7,cy7,cx8,cy8,cx9,cy9,cx10,cy10
                                              ,cx11,cy11,cx12,cy12,cx13,cy13,cx14,cy14,cx15,
                                              cy15,cx16,cy16,cx17,cy17,cx18,cy18,fill = colourBoat[i])
        xB[i] += speedxB[i]
        yB[i] += speedyB[i]
        #Boundary detection
        if xB[i] < 0:
            xB[i] = 1450
            colourBoat[i] = choice(["#2e302f","#464f4a","#d4d4d4","#b3a2a2"])
        if yB[i] > 975:
            yB[i] = 974
            speedyB[i]  = speedyB[i]*-1
        if yB[i] < 540:
            yB[i] = 539
            speedyB[i]  = speedyB[i]*-1
  

########################################################################
    #Background pillars
    bridge.append(screen.create_line(200,1000,200,325,fill = "red", width = 30))
    bridge.append(screen.create_line(1100,585,1100,380,fill = "red", width = 10))
    #Road + Edge
    bridge.append(screen.create_polygon(0,840,1160,500,1260,500,0,960,fill = "grey"))
    bridge.append(screen.create_line(0,840,1165,500,fill = "red",width = 5))
    bridge.append(screen.create_line(0,960,1260,500,fill = "red",width = 10))

    #Left Background Curve
    bridge.append(screen.create_line(parab2L,fill ="red",width = 5))
    
    #Ropes left of pillar, Background
    for i in range(ceil(len(paraby2L)/20)):
        x = parabx2L[i*20]
        y2 = paraby2L[i*20]
        y  = -17/58*(x)+840
        bridge.append(screen.create_line(x,y,x,y2, fill = "red"))

######################################################################
    #Background curve centre
    bridge.append(screen.create_line(parabc1,fill ="red",width = 5))
    #Vertical ropes, Background
    for i in range(ceil(len(parabyc1)/20)):
        x = parabxc1[i*20]                          #draws a line every 20 units
        y2 = parabyc1[i*20]
        y  = -17/58*(x)+840
        bridge.append(screen.create_line(x,y,x,y2, fill = "red"))

#####################################################################
    #Right Parabolas
    # Background Curve
    bridge.append(screen.create_line(parabr1,width= 5,fill = "red"))

    #Ropes right of pillar, Background
    for i in range(ceil(len(parabyr1)/20)):
        x = parabxr1[i*20]
        y2 = parabyr1[i*20]
        y  = -17/58*(x)+840
        bridge.append(screen.create_line(x,y,x,y2, fill = "red"))
#####################################################################    
    for i in range(len(cars)):
        #Each lane has a different slope
        if lane[i] == 3:
            y = (-7/20)*xC[i]+927
        elif lane[i] == 2:
            y = (-131/400)*xC[i]+900
        elif lane[i] == 1:
            y = (-61/200)*xC[i]+873
        size[i] = ((sqrt((xC[i]-1200)**2+(y - 507)**2))/2000)       #Formula that determines the size of the car in relation 
        x1 = xC[i]-(10*size[i])                                     #to its distance from the far end of the bridge.
        y1 = y-(10*size[i])
        x2 = xC[i]+(10*size[i])
        y2 = y +(10*size[i])
        x4 = xC[i]+(50*size[i])
        y4 = y - (35*size[i])
        x3= xC[i]+(75*size[i])
        y3 = y - (15*size[i])        
        car = screen.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,fill = colour[i],outline = colour[i])
        cars[i] = car
        xC[i] += speed[i]
        if xC[i] >= 1200:
            xC[i] = -10
            colour[i] = (choice(["blue","orange","green","white","#5a216b","#216b5d","#91bd00"]))
####################################################################
    #Foreground pillars
    bridge.append(screen.create_line(320,1000,320,320,fill = "red", width = 30))
    bridge.append(screen.create_line(1200,585,1200,380,fill = "red", width = 10))
    
    #Left Foreground Curve
    bridge.append(screen.create_line(parab1L,fill = "red",width = 5))
    
    #Ropes left of pillar, Foreground
    for i in range(ceil(len(paraby1L)/20)):
        x = parabx1L[i*20]
        y2 = paraby1L[i*20]
        y  = -23/63*(x)+960
        bridge.append(screen.create_line(x,y,x,y2, fill = "red"))

    #Foreground parabola
    bridge.append(screen.create_line(parabc2,fill ="red",width = 5))
    #Vertical ropes, Foreground
    for i in range(ceil(len(parabyc2)/20)):
        x = parabxc2[i*20]
        y2 = parabyc2[i*20]
        y  = -23/63*(x)+960
        bridge.append(screen.create_line(x,y,x,y2, fill = "red"))

    #Foreground curve
    bridge.append(screen.create_line(parabr2,width= 5,fill = "red"))
    #Ropes right of pillar, Foreground
    for i in range(ceil(len(parabyr2)/20)):
        x = parabxr2[i*20]
        y2 = parabyr2[i*20]
        y  = -23/63*(x)+960
        bridge.append(screen.create_line(x,y,x,y2, fill = "red"))


###################################################################
    screen.update()
    sleep(0.03)

    
    #loops that delete all previous frames
    for q in range(len(cars)):
        screen.delete(cars[q])
    for q in range(len(boats)):
        screen.delete(boats[q])
    for q in range(len(bridge)):
        screen.delete(bridge[q])
    for q in range(len(stars)):
        screen.delete(stars[q])

    
        
  
    



