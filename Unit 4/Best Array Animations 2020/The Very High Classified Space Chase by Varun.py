####################
# Title: The Very High Classified Space Chase
# Programmer:  Varun Kondam
# Last modified:  April 30, 2020
####################


from tkinter import *
from time import *
from math import *
from random import*

tk = Tk()
screen = Canvas(tk, width = 1000, height = 800, background = "Sky Blue")
screen.pack() 

#CLOUDS

for c in range(50):
    cx = randint(0, 1000)
    cy = randint(0,800)
    
    
    size = randint(50, 80)

    screen.create_oval(cx, cy, cx + size, cy + size, fill = "White", outline = "White")
    screen.create_oval(cx, cy, cx + size, cy + size, fill = "White", outline = "White")
    screen.create_oval(cx, cy, cx + size, cy + size, fill = "White", outline = "White")

#STORY PROMPTS
message1 = "ATTENTION! An Unidentified Flying Mass has entered Earth's atmosphere!"
message2 = "Send the closest patrol aircraft in the airspace!"
message3 = "Scanning Target."
message4 = "Cannon will be ineffective."
message5 = "Switching to heavy weapon."
message6 = "Glad we took care of that before things got out of hand."
message7 = "Time to keep this incredibly important information away from the public."
message8 = "The End."
message9 = "By Varun Kondam"

####NOTE: I TRIED TO INTEGREATE THESE WIND LINES BUT THEY VERY SADLY DON'T WORK

#WIND LINES
##numWind = 100
##
##xWind = []
##yWind = []
##xWindSpeed = 25
##windSize = []
##wind = []
##
##for i in range(numWind):
##    xWind.append(randint(0,1000))
##    yWind.append(randint(5,800))
##    windSize.append(randint(10,25))
##    wind.append(0)
##    
##
##for f in range(1000):
##    for i in range(numWind):
##        if xWind[i] >= 1000:
##            xWind[i] = xWind[i] - 1000
##            
##        wind[i] = screen.create_line(xWind[i], yWind[i], xWind[i] + windSize[i], yWind[i], fill = "White")
##
##        xWind[i] = xWind[i] + xWindSpeed
##
##    screen.update()
##    sleep(0.03)
##        
##    
##    for i in range(numWind):
##        screen.delete(wind[i])

    







#UFM - Unidentified Flying Mass (Because it's a large MASS of small balls)    
numUFM = 300

#EMPTY ARRAYS
xUFM = []
yUFM = []
yUFMSpeeds = []
ufmSize = []
ufmColours = ["Red","Maroon","Black"]
ufm = []

#APPENDING VALUES
for i in range(numUFM):
    xUFM.append(randint(100,300))
    yUFM.append(randint(350,500))
    ufmSize.append(randint(10,20))
    ufm.append(0)



for f in range(100):
    
    for i in range(numUFM):

        #THE UFM NEEDS TO START OFFSCREEN, SO WE ADD SOME EXTRA UPWARDS DISPLACEMENT (OF 800)        
        ufm[i] = screen.create_oval(xUFM[i], yUFM[i] - 800, xUFM[i] + ufmSize[i], yUFM[i] + ufmSize[i] - 800, fill = choice(ufmColours))

        yUFM[i] = yUFM[i] + 8#OBVIOUSLY, THE UFM NEEDS TO BE ON THE SCREEN, SO WE SLOWLY MAKE THE -800 BIGGER AND BIGGER UNTIL WE HAVE OUR ORIGINAL COORDINATES

    screen.update()
    sleep(0.03)

    #MAKING SURE THE UFM DOESN'T GET DELETED ON THE LAST FRAME
    if f != 99:
        
        for i in range(numUFM):
            screen.delete(ufm[i])


#BEGINNING OF CYCLING THROUGH STORY PROMPTS
message = screen.create_text(500, 300, text = message1, font = "Times90", fill = "Black")
sleep(3)

screen.update()
screen.delete(message)

message = screen.create_text(500, 300, text = message2, font = "Times90", fill = "Black")
sleep(3)

screen.update()
screen.delete(message)

sleep(3)


#JET 

#THIS "r" VALUE OFFSETS THE JET SO IT DOESN'T APPEAR ON SCREEN, ALLOWING IT TO FLY IN (LIKE THE UFM)
r = 800

for f in range(101):
    
    jAfterburner1 = screen.create_oval(900+r,410,1000+r,440, fill = "Orange", outline = "Orange")
    jAfterburner2 = screen.create_oval(925+r,420,975+r,430, fill = "Yellow", outline = "Yellow")
    jRudder = screen.create_polygon(900+r,410,950+r,410,950+r,360,935+r,360, fill = "Grey70", outline = "Black")
    jBody = screen.create_polygon(650+r,435,750+r,450,925+r,450,950+r,440,950+r,410,725+r,400, fill = "Slate Grey", outline = "Black")
    jBrand = screen.create_text(800+r,415, text = "VK - 17", fill = "White")
    jScanner = screen.create_oval(750+r,420,753+r,421, fill = "Black")
    jCanopy = screen.create_polygon(725+r,400,750+r,402,700+r,411.6, fill = "Gold", outline = "Black")
    jElevators = screen.create_polygon(900+r,425,950+r,425,955+r,430,935+r,430, fill = "Grey70", outline = "Black")
    jMissileWings = screen.create_polygon(900+r,430,900+r,470,875+r,450,fill = "Slate Grey", outline = "Black")
    jMissileBody = screen.create_polygon(800+r,450,810+r,445,900+r,445,900+r,455,810+r,455, fill = "Dark Green", outline = "Black")
    jWing = screen.create_polygon(775+r,425,875+r,425,890+r,460,840+r,460, fill = "Grey70", outline = "Black")

    r = r - 8#SAME FUNCTION AS THE UFM

    screen.update()
    sleep(0.03)

    #MAKING SURE WE DON'T DELETE THE JET AFTER IT REACHES IT'S POSITION
    if f != 100:
        screen.delete(jAfterburner1,jAfterburner2,jRudder,jBody,jBrand,jScanner,jCanopy,jElevators,jMissileWings,jMissileBody,jWing)
 

#wRITING ANOTHER MESSAGE ON THE SCREEN
sleep(1)
message = screen.create_text(500, 300, text = message3, font = "Times90", fill = "Black")
screen.update()
sleep(3)
screen.delete(message)


#THIS IS THE ANIMATION FOR THE SCANNING OF THE UFO
x = []
y = []
firingTimes = []#THIS ARRAY ALLOWS FOR THE LASERS TO BE FIRED AT DIFFERENT TIMES
x2 = 753
y2 = 420
scan = []


for i in range(40):
    x.append(randint(100,300))
    y.append(randint(350,450))

    firingTimes.append(randint(0,60))

    scan.append(0)


for i in range(40):
    if f >= firingTimes[i]:

        if x2 > x[i]:
            scan[i] = screen.create_line(x[i],y[i],x2,y2, fill = "Green")

    else:
        scan[i] = 0    

    screen.update()
    sleep(0.03)
    screen.delete(scan[i])



sleep(1)
#WRITING ANOTHER TWO MESSAGES
message = screen.create_text(500, 300, text = message4, font = "Times90", fill = "Black")
screen.update()
sleep(2)
screen.delete(message)

message = screen.create_text(500, 300, text = message5, font = "Times90", fill = "Black")
screen.update()
sleep(2)
screen.delete(message)

screen.delete(jMissileWings,jMissileBody,jWing)

r = 0#WE USE THE SAME VALUE FOR THE MISSILE AND HET SO WE SET IT TO 0 (IT WAS ORGINALLY 800)


for f in range(95):

    #WE DRAW THE FIRE, THEN THE ACTUAL MISSILE, THEN THE WING, SO THAT NOTHING OVERLAPS IN A WEIRD WAY 
    missileBurner1 = screen.create_oval(875-r,445,925-r,455, fill = "Orange", outline = "Orange")
    missileBurner2 = screen.create_oval(885-r,448,915-r,452, fill = "Yellow", outline = "Yellow")

    jMissileWings = screen.create_polygon(900-r,430,900-r,470,875-r,450,fill = "Slate Grey", outline = "Black")
    jMissileBody = screen.create_polygon(800-r,450,810-r,445,900-r,445,900-r,455,810-r,455, fill = "Dark Green", outline = "Black")
    jWing = screen.create_polygon(775,425,875,425,890,460,840,460, fill = "Grey70", outline = "Black")

    if f == 0:#BECAUSE THE FIRST FRAME IS 0, WE ADD ONE TO GIVE IT A KICKSTART
        r = r + 1

    else:
        r = 1.07*r#AFTER WE ADD ONE FOR THE FIRST ONE, THIS FUNCTION ALLOWS THE MISSILE TO ACCELERATE TOWARDS THE UFM

    screen.update()
    sleep(0.03)
    if f != 94:
        screen.delete(missileBurner1,missileBurner2,jMissileWings,jMissileBody,jWing)
    else:
        screen.delete(missileBurner1,missileBurner2,jMissileWings,jMissileBody)
        #THE REASON WHY THERE ARE TWO DELETE LINES IS BECAUSE THE "jWing" IMAGE IS STILL NEEDED ON THE PLANE (Y'KNOW, SO IT CAN FLY)


for f in range(10):#THESE TWO ARE TWO LARGE COLOURED RECTANGLES THAT ARE SUPPOSED TO BE AN EXPLOSION
    boom1 = screen.create_rectangle(0,0,1000,800, fill = "Yellow")
    screen.update()
    sleep(0.03)

    boom2 = screen.create_rectangle(0,0,1000,800, fill = "Red")
    screen.update()
    sleep(0.03)

    screen.delete(boom1,boom2)

##THIS SECTION HANDLES THE EXPLOSION OF THE ACTUAL UFM

#CREATING 3 NEW ARRAYS
angle = []
r = []
speed = []

for i in range(numUFM):
    screen.delete(ufm[i])#DELETING THE PAST UFM SO THAT IT DOESN'T STAY VISIBLE AFTER THE NEW ONE WE MAKE BLOWS AWAY

for i in range(numUFM):
    angle.append(uniform(0,pi))#ANGLE AT WHICH THEY FLY AWAY
    r.append(0)
    speed.append(uniform(5,10))#SPEED AT WHICH BALLS FLY AWAY

for f in range(25):
    for i in range(numUFM):
        ufm[i] = screen.create_oval(xUFM[i], yUFM[i] - 800, xUFM[i] + ufmSize[i], yUFM[i] + ufmSize[i] - 800, fill = choice(ufmColours))     
        
        
        xUFM[i] = xUFM[i] - r[i] * sin(angle[i]) + 0.1*f**2 #THESE SIN/COS FUNCTIONS HANDLE THE CURVY DIRECTION OF THE EXPLOSION
        yUFM[i] = yUFM[i] + r[i] * cos(angle[i])
        r[i] = r[i] + speed[i]
        
    screen.update()
    sleep(0.03)
    for i in range(numUFM):
        screen.delete(ufm[i])




#THESE LAST FEW MESSAGES TO END THE STORY
message = screen.create_text(500, 300, text = message6, font = "Times90", fill = "Black")
screen.update()
sleep(3)
screen.delete(message)

message = screen.create_text(500, 300, text = message7, font = "Times90", fill = "Black")
screen.update()
sleep(3)

screen.delete(message)



#DELETING THE ORIGINAL PLANE BECAUSE PIECES WILL STAY BEHIND AFTER WE REMAKE IT AND SEND IT OFF
screen.delete(jAfterburner1,jAfterburner2,jRudder,jBody,jBrand,jScanner,jCanopy,jElevators,jWing)

r = 0

for f in range(101):
    
    jAfterburner1 = screen.create_oval(900+r,410,1000+r,440, fill = "Orange", outline = "Orange")
    jAfterburner2 = screen.create_oval(925+r,420,975+r,430, fill = "Yellow", outline = "Yellow")
    jRudder = screen.create_polygon(900+r,410,950+r,410,950+r,360,935+r,360, fill = "Grey70", outline = "Black")
    jBody = screen.create_polygon(650+r,435,750+r,450,925+r,450,950+r,440,950+r,410,725+r,400, fill = "Slate Grey", outline = "Black")
    jBrand = screen.create_text(800+r,415, text = "VK - 17", fill = "White")
    jScanner = screen.create_oval(750+r,420,753+r,421, fill = "Black")
    jCanopy = screen.create_polygon(725+r,400,750+r,402,700+r,411.6, fill = "Gold", outline = "Black")
    jElevators = screen.create_polygon(900+r,425,950+r,425,955+r,430,935+r,430, fill = "Grey70", outline = "Black")
    jWing = screen.create_polygon(775+r,425,875+r,425,890+r,460,840+r,460, fill = "Grey70", outline = "Black")

    if f == 0:
        r = r - 1#SAME DEAL WITH THE MISSILE FROM BEFORE
                 #THE PLANE GETS A KICKSTART IN MOTION AND ACCERATES AWAY
    else:
        r = 1.09*r

    screen.update()
    sleep(0.03)

    if f != 100:
        screen.delete(jAfterburner1,jAfterburner2,jRudder,jBody,jBrand,jScanner,jCanopy,jElevators,jWing)


#THE END!
#THANK YOU SO MUCH FOR LOOKING AT MY ARRAY ANIMATION ASSIGNMENT
message = screen.create_text(500, 400, text = message8, font = "Times400", fill = "Black")
message = screen.create_text(500, 600, text = message9, font = "Times400", fill = "Black")



##spacing = 50 
##for x in range(0, 1000, spacing): 
##    screen.create_line(x, 25, x, 1000, fill= "red")
##    screen.create_text(x, 5, text=str(x), font="Times 9", fill = "red", anchor = N)
##
##for y in range(0, 1000, spacing):
##    screen.create_line(25, y, 1000, y, fill= "yellow")
##    screen.create_text(5, y, text=str(y), font="Times 9", fill = "yellow", anchor = W)



screen.update()
