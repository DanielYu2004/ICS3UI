#################################################################
#                                                               #
#   Joey Maillette                                              #
#   Nasa Rocket Launch                                          #
#   November 1st, 2019                                          #
#                                                               #
#################################################################

from math import*
from random import*
from tkinter import*
from time import*

myinterface=Tk()
screen=Canvas(myinterface, width=800, height=900, background="black")
screen.pack()

sleep(0.25)

#=======================================#
#               INTRO                   #
#=======================================#

###First message
nasa=screen.create_text(400,450, text="Apollo 11 Launch @ Kennedy Space Center – July 16, 1969.",font="system 10", fill="white")

screen.update()
sleep(2)
screen.delete(nasa)

#3,2,1
extent=359
num=4

for a in range(114):
    if extent<1:
        extent=359

    if extent==359:
        num=num-1

    if num<1:
        break
    
    circ=screen.create_arc(200,200,600,600,extent=extent,start=0, fill="grey")
    t=screen.create_text(400,400, text=num,font="arial 100", fill="white")
    screen.update()
    sleep(0.03)
    screen.delete(circ,t)
    extent=extent-10

#=======================================#
#               ARRAY FILLING           #
#=======================================#

colours=["green","green2","green3"]
grass=[]
grassx=[]
grassy=[]
leng=[]
wid=[]
col=[]
hbeam=[]
yvalues=[]


for i in range(3000):
    grassx.append(randint(0,800))
    grassy.append(randint(800,900))
    leng.append(randint(4,8))
    col.append(choice(colours))
    wid.append(randint(1,3))
    grass.append(0)



cloudsx=[]
cloudsy=[]
bubblex=[]
bubbley=[]
cloud=[]

for i in range(30):
    cloudsx.append(randint(1,800))
    cloudsy.append(randint(-900,200))


for i in range(450):
    bubblex.append(randint(-75,75))
    bubbley.append(randint(-50,50))
    cloud.append(0)

ybeam=700
gap=[]

for f in range(6):
    gap.append(f*100)
    hbeam.append(0)

for i in range(6):
    y=ybeam-gap[i%6]
    yvalues.append(y)

l1stagex=[]
l1stagey=[]
l2stagex=[]
l2stagey=[]
l3stagex=[]
l3stagey=[]
ldot1=[]
ldot2=[]
ldot3=[]

for g in range(50):
    l1stagex.append(randint(368,402))
    l2stagex.append(randint(375,395))
    l3stagex.append(randint(382,388))
    l1stagey.append(randint(655,680))
    l2stagey.append(randint(680,710))
    l3stagey.append(randint(710,740))
    ldot1.append(0)
    ldot2.append(0)
    ldot3.append(0)

r1stagex=[]
r1stagey=[]
r2stagex=[]
r2stagey=[]
r3stagex=[]
r3stagey=[]
rdot1=[]
rdot2=[]
rdot3=[]


for g in range(50):
    r1stagex.append(randint(418,452))
    r2stagex.append(randint(425,445))
    r3stagex.append(randint(432,438))
    r1stagey.append(randint(655,680))
    r2stagey.append(randint(680,710))
    r3stagey.append(randint(710,740))
    rdot1.append(0)
    rdot2.append(0)
    rdot3.append(0)

window=[]

for g in range(2):
    window.append(0)

#sky stuff(dark to light)
skycolors=["#000000","#000305","#010509","#01080e","#020b13","#020d17","#03101c","#031321","#031625","#04182a","#041b2f","#051e33","#052038","#06233d",
           "#062641","#072846","#072b4b","#072e4f","#083054","#083359","#09365d","#093962","#0a3b67","#0a3e6b","#0a4170","#0b4375","#0b4679","#0c497e",
           "#0c4b83","#0d4e87","#0d518c","#0d5391","#0e5695","#0e599a","#0f5b9f","#0f5ea3","#1061a8","#1064ad","#1066b1","#1169b6","#116cbb","#126ebf",
           "#1271c4","#1374c9","#1376cd","#1479d2","#147cd7","#147edb","#1581e0","#1584e5","#1687e9","#1a89ea","#1f8bea","#248eeb","#2890eb","#2d93eb",
           "#3295ec","#3697ec","#3b9aed","#409ced","#449fee","#49a1ee","#4ea3ef","#52a6ef","#57a8ef","#5cabf0","#60adf0","#65b0f1","#6ab2f1","#6eb4f2"]

gap=2500/len(skycolors)

ysky=[]
skyblock=[]

y=-1800

for i in range(len(skycolors)):
    ysky.append(y)
    skyblock.append(0)
    y=y+gap

yground=700

#=======================================#
#   FIRST ANIMATION(sky to space        #
#=======================================#

for abc in range(220):

    ####ground
    if yground<900:
        ground1=screen.create_polygon(0,yground,0,yground+100,800,yground+100,800,yground, fill="grey",outline="grey")
        ground2=screen.create_polygon(0,yground+200,0,yground+100,800,yground+100,800,yground+200,fill="green4", outline="green4")

    for i in range(len(grassx)):
        if grassy[i]<900:
            grass[i]=screen.create_line(grassx[i],grassy[i],grassx[i]+1,grassy[i]+leng[i],width=wid[i], fill=col[i])


    #sky
    for i in range(len(skycolors)):
        if ysky[i]+gap<900+gap:
            skyblock[i]=screen.create_rectangle(0,ysky[i],800,ysky[i]+gap, fill=skycolors[i], outline=skycolors[i])

    #clouds

    for i in range(450):
        if cloudsy[i%10]+bubbley[i]<900:
            cloud[i]=screen.create_oval(cloudsx[i%10]+bubblex[i],cloudsy[i%10]+bubbley[i],cloudsx[i%10]+bubblex[i]+75,50+cloudsy[i%10]+bubbley[i], fill="whitesmoke", outline="whitesmoke")
       
    #####crane
    if ybeam-500<900:
        cranefill=screen.create_rectangle(100,ybeam,250,ybeam-500, fill="saddlebrown")

    #horizontal beam

    for i in range(6):
        if yvalues[i]-10<900:
            hbeam[i]=screen.create_rectangle(100,yvalues[i],250,yvalues[i]-10, fill="beige", outline="beige")
        
    #verticle beams
    if ybeam-500<900:
        beam1=screen.create_rectangle(100,ybeam,115,ybeam-500, fill="beige", outline="beige")
        beam2=screen.create_rectangle(135,ybeam,150,ybeam-500, fill="beige", outline="beige")
        beam3=screen.create_rectangle(250,ybeam,235,ybeam-500, fill="beige", outline="beige")
        beam4=screen.create_rectangle(215,ybeam,200,ybeam-500, fill="beige", outline="beige")

    #center top/bot
    if ybeam-480<900:
        top=screen.create_arc(125,ybeam-540,230,ybeam-480, fill="beige", extent=180, start=0, outline="beige")
    if ybeam+50<900:
        bot=screen.create_arc(260,ybeam-50,560,ybeam+50, fill="grey3", extent=180, start=180, outline="grey2")
    if ybeam+40<900:
        bot2=screen.create_arc(280,ybeam-40,540,ybeam+40, fill="snow", extent=180, start=180, outline="snow")

    ###rocketship
    winy=390

    midrec=screen.create_rectangle(370,600,450,350,fill="grey", width=3)
    tip=screen.create_polygon(358,370,390,265,430,265,462,370, smooth=True, fill="red", outline="black",width=3)
    for g in range(2):
        window[g]=screen.create_oval(390,winy,430,winy+40, fill="powder blue", width=3)
        winy=winy+75
    left=screen.create_polygon(370,515,370,600,320,600, fill="grey", outline="black", width=3)
    right=screen.create_polygon(450,515,450,600,500,600, fill="grey", outline="black", width=3)
    mid=screen.create_oval(400,530,420,610, fill="grey", outline="black", width=3)
    lbooster=screen.create_polygon(395,600,375,600,365,650,405,650, fill="grey", outline="black", width=3)
    rbooster=screen.create_polygon(425,600,445,600,455,650,415,650, fill="grey", outline="black", width=3)

    ####ROCKET BOOST

    #left boost


    for i in range(50):
        ldot1[i]=screen.create_oval(l1stagex[i]-4,l1stagey[i]-4,l1stagex[i]+4,l1stagey[i]+4, fill="red", outline="red")
        ldot2[i]=screen.create_oval(l2stagex[i]-3,l2stagey[i]-3,l2stagex[i]+3,l2stagey[i]+3, fill="orange", outline="orange")
        ldot3[i]=screen.create_oval(l3stagex[i]-2,l3stagey[i]-2,l3stagex[i]+2,l3stagey[i]+2, fill="yellow", outline="yellow")

       #RIGHT BOOST

    for i in range(50):
        rdot1[i]=screen.create_oval(r1stagex[i]-4,r1stagey[i]-4,r1stagex[i]+4,r1stagey[i]+4, fill="red", outline="red")
        rdot2[i]=screen.create_oval(r2stagex[i]-3,r2stagey[i]-3,r2stagex[i]+3,r2stagey[i]+3, fill="orange", outline="orange")
        rdot3[i]=screen.create_oval(r3stagex[i]-2,r3stagey[i]-2,r3stagex[i]+2,r3stagey[i]+2, fill="yellow", outline="yellow")

    screen.update()
    sleep(0.003)
    screen.delete(ground1,ground2,cranefill)
    screen.delete(midrec,tip,left,right,mid,lbooster,rbooster)

    for i in range(50):
        screen.delete(ldot1[i],ldot2[i],ldot3[i],rdot1[i],rdot2[i],rdot3[i])
        
    for i in range(len(grassx)):
        screen.delete(grass[i])

    for i in range(450):
        screen.delete(cloud[i])

    for i in range(6):
        screen.delete(hbeam[i])

    for i in range(2):
        screen.delete(window[i])
        
    screen.delete(beam1,beam2,beam3,beam4,bot,bot2,top,midrec,tip,left,right,mid,lbooster,rbooster)

    for i in range(50):
        screen.delete(ldot1[i],ldot2[i],ldot3[i],rdot1[i],rdot2[i],rdot3[i])
    
    yground=yground+12
    ybeam=ybeam+12

    for i in range(50):
        l1stagey[i]=l1stagey[i]+5
        l2stagey[i]=l2stagey[i]+5
        l3stagey[i]=l3stagey[i]+5
        r1stagey[i]=r1stagey[i]+5
        r2stagey[i]=r2stagey[i]+5
        r3stagey[i]=r3stagey[i]+5

        if l1stagey[i]>680:
            l1stagey[i]=655

        if l2stagey[i]>710:
            l2stagey[i]=680

        if l3stagey[i]>740:
            l3stagey[i]=710

        if r1stagey[i]>680:
            r1stagey[i]=655

        if r2stagey[i]>710:
            r2stagey[i]=680

        if r3stagey[i]>740:
            r3stagey[i]=710
            

    for i in range(len(grassx)):
        grassy[i]=grassy[i]+12

    for i in range(30):
        cloudsy[i]=cloudsy[i]+12

    for i in range(6):
        yvalues[i]=yvalues[i]+12

    for i in range(len(skycolors)):
        screen.delete(skyblock[i])
        ysky[i]=ysky[i]+12

#=======================================#
#   SECOND ANIMATION(solar system)      #
#=======================================#

#array filling
star=[]
starx=[]
stary=[]
starsize=[]

for i in range(200):
    star.append(0)
    starx.append(randint(0,800))
    stary.append(randint(0,900))
    starsize.append(randint(1,3))

suncolors=["#ffac05","#ffb41f","#ffc71f","#ffd147","#ffda6b","#ffebad","#fff7e0","#ffffff"]

#sun    
planety=-900
sun=[]
sungap=(800/(len(suncolors)+1))/2

for i in range(len(suncolors)):
    sun.append(0)

#mercury
mercuryy=-2200
randmercx=[]
randmercy=[]
randmerc=[]
randsize=[]

for i in range(6):
    randmercx.append(randint(700,840))
    randmercy.append(randint(-2100,-1900))
    randmerc.append(0)
    randsize.append(randint(15,40))
    
#Venus
venusy=-3000

#earth
earthy=-4200

#mars
marsy=-5000

#jupiter
jupitery=-6000

#saturn
saturny=-7200

####EXPLOSION VARIABLES

ExplosionCenterX=400
ExplosionCenterY=200

x=[]
y=[]

TotalSpeed=[]
Speed=[]

Particles=[]
numParticles=200
pColors=[]
difColors=["#b05f03","black","#fca440","#bc8220","grey","red"]

xSize=[]
ySize=[]

degrees=[]


for i in range(numParticles):
    x.append(ExplosionCenterX)
    y.append(ExplosionCenterY)
    TotalSpeed.append(0)
    Speed.append(randint(10,15))
    Particles.append(0)
    pColors.append(choice(difColors)) #ALL COLORS OF SPACESHIP AND SATURN
    xSize.append(randint(10,15))
    ySize.append(randint(10,15))
    degrees.append(uniform(0,2*pi))
                   
                

for abc in range(630):
    for i in range(200):
        star[i]=screen.create_oval(starx[i],stary[i],starx[i]+starsize[i],stary[i]+starsize[i], fill="snow")

    #sun
    if planety<900:
        sun1=screen.create_oval(-400,planety,400,planety+800,fill="#ff9f0f")
        sungap=(800/(len(suncolors)+1))/2

        for i in range(len(suncolors)):
            sun[i]=screen.create_oval(-400+sungap,planety+sungap,400-sungap,planety+800-sungap, fill=suncolors[i],outline=suncolors[i])
            sungap=sungap+(800/(len(suncolors)+1))/2       

    #mercury
    if mercuryy<900:
        mercury=screen.create_oval(600,mercuryy,1000,mercuryy+400, fill="#b0b0b0", outline="#b0b0b0")

        for i in range(6):
            randmerc[i]=screen.create_oval(randmercx[i]-randsize[i],randmercy[i]-randsize[i],randmercx[i]+randsize[i],randmercy[i]+randsize[i], fill="#858585", outline="#5e5e5e", width=4)
    
    #venus
    if venusy<900:
        venus=screen.create_oval(-300,venusy,300,venusy+600,fill="#d15929",outline="#d15929")
        venus1=screen.create_polygon(275,venusy+300,243,venusy+283,226,venusy+223,180,venusy+244,150,venusy+146,134,venusy+123,100,venusy+95,95,venusy+278, smooth=True, fill="#e98935",outline="#be4423", width=2)
        venus2=screen.create_polygon(0,venusy+593,15,venusy+582,23,venusy+569,63,venusy+553,82,venusy+541,106,venusy+513,270,venusy+300,150,venusy+350,0,venusy+425,smooth=True,fill="#a25a20", outline="#6a3b15", width=2)
    
    #earth
    if earthy<900:
        earth=screen.create_oval(500,earthy,1100,earthy+600, fill="#0f64db",outline="#0f64db")
        earth1=screen.create_oval(600,earthy+125,750,earthy+325, fill="#00ad20", outline="#008017")
        earth2=screen.create_polygon(565,earthy+315,640,earthy+520,672,earthy+345,850,earthy+587,850,earthy+200,fill="#00ad20", outline="#00ad20", smooth=True)
    
    #mars
    if marsy<900:
        mars=screen.create_oval(-250,marsy,250,marsy+500, fill="#d82303", outline="#8d1702",width=3)
        mars1=screen.create_oval(-200,marsy+50,200,marsy+450, fill="#e74804",outline="#e74804")
        mars2=screen.create_oval(-150,marsy+150,150,marsy+350, fill="#d82303",outline="#8d1702")
    #jupiter
    if jupitery<900:
        jupiter=screen.create_oval(400,jupitery,1200,jupitery+800, fill="#fca440",outline="#d37203", width=3)
        jupiter1=screen.create_oval(500,jupitery+100,1100,jupitery+700, fill="#a15702", outline="#a15702")
        jupiter2=screen.create_oval(700,jupitery+150,900,jupitery+650, fill="#fdbc72", outline="#fdbc72")

    #saturn

    if saturny<900:
        saturn2=screen.create_oval(0,saturny+200,800,saturny+300, fill="#b05f03", outline="#b05f03")
        saturn1=screen.create_oval(50,saturny+225,750,saturny+275, fill="black")
        saturn=screen.create_oval(150,saturny,650,saturny+500,fill="#fca440")
        saturn3=screen.create_oval(300,saturny+150,500,saturny+350, fill="#bc8220")

    if saturny<0:
        winy=390
        
        midrec=screen.create_rectangle(370,600,450,350,fill="grey", width=3)
        tip=screen.create_polygon(358,370,390,265,430,265,462,370, smooth=True, fill="red", outline="black",width=3)
        for g in range(2):
            window[g]=screen.create_oval(390,winy,430,winy+40, fill="powder blue", width=3)
            winy=winy+75
        left=screen.create_polygon(370,515,370,600,320,600, fill="grey", outline="black", width=3)
        right=screen.create_polygon(450,515,450,600,500,600, fill="grey", outline="black", width=3)
        mid=screen.create_oval(400,530,420,610, fill="grey", outline="black", width=3)
        lbooster=screen.create_polygon(395,600,375,600,365,650,405,650, fill="grey", outline="black", width=3)
        rbooster=screen.create_polygon(425,600,445,600,455,650,415,650, fill="grey", outline="black", width=3)

        ####ROCKET BOOST

        #left boost
        for i in range(50):
            ldot1[i]=screen.create_oval(l1stagex[i]-4,l1stagey[i]-4,l1stagex[i]+4,l1stagey[i]+4, fill="red", outline="red")
            ldot2[i]=screen.create_oval(l2stagex[i]-3,l2stagey[i]-3,l2stagex[i]+3,l2stagey[i]+3, fill="orange", outline="orange")
            ldot3[i]=screen.create_oval(l3stagex[i]-2,l3stagey[i]-2,l3stagex[i]+2,l3stagey[i]+2, fill="yellow", outline="yellow")

           #RIGHT BOOST

        for i in range(50):
            rdot1[i]=screen.create_oval(r1stagex[i]-4,r1stagey[i]-4,r1stagex[i]+4,r1stagey[i]+4, fill="red", outline="red")
            rdot2[i]=screen.create_oval(r2stagex[i]-3,r2stagey[i]-3,r2stagex[i]+3,r2stagey[i]+3, fill="orange", outline="orange")
            rdot3[i]=screen.create_oval(r3stagex[i]-2,r3stagey[i]-2,r3stagex[i]+2,r3stagey[i]+2, fill="yellow", outline="yellow")


    #EXPLOSION
    if saturny>=0:
        for i in range(numParticles):

            if 0<=x[i]<=800 and 0<=y[i]<=900:
                Particles[i]=screen.create_rectangle(x[i],y[i],x[i]+xSize[i],y[i]+ySize[i], fill=pColors[i],outline=pColors[i])

                x[i]=x[i]-TotalSpeed[i]*sin(Particles[i])
                y[i]=y[i]+TotalSpeed[i]*cos(Particles[i])
                TotalSpeed[i]=TotalSpeed[i]+Speed[i]

            
    
    screen.update()
    sleep(0.03)

    screen.delete(midrec,tip,left,right,mid,lbooster,rbooster)

    for i in range(50):
        screen.delete(ldot1[i],ldot2[i],ldot3[i],rdot1[i],rdot2[i],rdot3[i])

    for i in range(50):
        l1stagey[i]=l1stagey[i]+5
        l2stagey[i]=l2stagey[i]+5
        l3stagey[i]=l3stagey[i]+5
        r1stagey[i]=r1stagey[i]+5
        r2stagey[i]=r2stagey[i]+5
        r3stagey[i]=r3stagey[i]+5

        if l1stagey[i]>680:
            l1stagey[i]=655

        if l2stagey[i]>710:
            l2stagey[i]=680

        if l3stagey[i]>740:
            l3stagey[i]=710

        if r1stagey[i]>680:
            r1stagey[i]=655

        if r2stagey[i]>710:
            r2stagey[i]=680

        if r3stagey[i]>740:
            r3stagey[i]=710

    for i in range(2):
        screen.delete(window[i])

    for i in range(200):
        screen.delete(star[i])

    if saturny<0:
        for i in range(200):
            stary[i]=stary[i]+12

            if stary[i]>900:
                stary[i]=0

    for i in range(numParticles):
        screen.delete(Particles[i])

    screen.delete(sun1,mercury,venus,venus1,venus2,earth,earth1,earth2,mars,mars1,mars2,jupiter,jupiter1,jupiter2,saturn,saturn1,saturn2,saturn3)
    
    planety=planety+12
    mercuryy=mercuryy+12
    venusy=venusy+12
    earthy=earthy+12
    marsy=marsy+12
    jupitery=jupitery+12

    if saturny<0:
        saturny=saturny+12
    

    for i in range(len(suncolors)):
        screen.delete(sun[i])
    
    for i in range(6):
        screen.delete(randmerc[i])
        randmercy[i]=randmercy[i]+12


###THEN ALL OF A SUDDEN
screen.update()
words=screen.create_text(400,450,text="THEN ALL OF A SUDDEN", font="system 10", fill="snow")

screen.update()
sleep(3)
screen.delete(words)

blackhole=screen.create_text(400,450,text="A BLACK HOLE APPEARED", font="system 10", fill="snow")

screen.update()
sleep(2)
screen.delete(blackhole)

grey=[]
x=0
y=0


for i in range(100):
    num=i+1
    grey.append("grey"+str(num))


for i in range(100):
    x=x+2
    y=y+2
    screen.create_oval(x,y,800-x,900-y,fill=grey[i], outline=grey[i])


screen.create_oval(202,202,598,698,fill="black")
screen.mainloop()