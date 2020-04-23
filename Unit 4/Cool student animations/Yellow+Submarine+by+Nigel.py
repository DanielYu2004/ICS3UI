from tkinter import *
from time import*
from random import *
from math import *
myInterface = Tk()
screen = Canvas(myInterface, width = 1000, height = 1000, background = "midnight blue")
screen.pack()

    #NUMBER VALUES
nFishFront = 25
nFishBack = 25

nRockPillar = 50
xRockSpeed = 20

    #FRONT FISHES VALUES
xFishFront = []
yFishFront = []
FrontFishSize = []
xFishFrontSpeed = []
exoticColorFront = []

    #BACK FISHES VALUES
xFishBack = []
yFishBack = []
BackFishSize = []
xFishBackSpeed = []
exoticColorBack = []

    #FISH SHAPES
FrontFish = []
FrontFishTail = []
BackFish = []
BackFishTail = []

    #ROCK PILLAR VALUES
xRockStart = []
yRockTop = []
rockColor = []
xSandPos = []
xRockLength = []
xRockIncline = []

    #ROCK SHAPES
RockShape = []


for i in range(nRockPillar):

    #ROCK START VALUES

    xRockStart.append( randint(-2100, -100) )
    yRockTop.append( randint (300, 800) )
    xSandPos.append( randint(800, 850) )
    xRockLength.append( randint(80, 240) )
    xRockIncline.append( randint(10, 40) )

    RockShape.append("Xenophage")

    rockColor.append( choice(["gray30", "gray28", "gray26", "gray24", "gray22", "gray20", "gray18", "gray16"]) )



# FISHES SWIMMING BEHIND THE SUBMARINE
for i in range(nFishBack):
    
    #BACK FISH START VALUES
    
    xFishBack.append( randint(1100, 5100) )
    
    yFishBack.append( randint(200, 850) )
    
    xFishBackSpeed.append( randint(12, 24) )

    BackFishSize.append( randint(2, 6) )
    
    exoticColorBack.append( choice(["cyan", "magenta", "spring green", "gold", "dark orchid", "firebrick1", "cyan2", "violet red", "SpringGreen2", "gold2", "dark violet", "red"]) )
        
    BackFish.append("Divinity")

    BackFishTail.append("Tarrabah")


for i in range(nFishFront):
    
    #FRONT FISH START VALUES
    
    xFishFront.append( randint(-5100, -100) )
    
    yFishFront.append( randint(150, 800) )
    
    xFishFrontSpeed.append( randint(12, 24) )

    FrontFishSize.append( randint(2, 6) )
    
    exoticColorFront.append( choice(["cyan", "magenta", "spring green", "gold", "dark orchid", "firebrick1", "cyan2", "violet red", "SpringGreen2", "gold2", "dark violet", "red"]) )
     
    FrontFish.append("Eriana")

    FrontFishTail.append("Leviathan")


    #ANIMATION LOOP
    
for f in range(12730):

        #ROCKS ANIMATION
    for i in range(nRockPillar):
        
            #ANIMATING PILLAR MOVEMENTS
        RockShape[i] = screen.create_polygon(xRockStart[i], xSandPos[i], xRockStart[i] + xRockIncline[i], yRockTop[i], xRockStart[i] + (xRockLength[i] / 2), yRockTop[i] - 100, xRockStart[i] + xRockLength[i] - xRockIncline[i], yRockTop[i], xRockStart[i] + xRockLength[i], xSandPos[i], fill = str(rockColor[i]), outline = str(rockColor[i]) )
                                              # BL                              TL                        TM                                            TR                              BL
        
            #UPDATING PILLAR NEXT FISH MOVEMENTS
        xRockStart[i] = xRockStart[i] + 10

            #RESET PILLAR XVALUES OFF SCREEN
        if xRockStart[i] > 1100:
            xRockStart[i] = randint(-1100, -300)

    sandGround = screen.create_rectangle(0, 800, 1000, 1000, fill = "blanched almond", outline = "blanched almond")




        #BACK FISH ANIMATION
    for i in range(nFishBack):

            #ANIMATING FISH MOVEMENTS
        BackFish[i] = screen.create_oval(xFishBack[i], yFishBack[i], xFishBack[i] - (5*BackFishSize[i]), yFishBack[i] + (2*BackFishSize[i]), fill = str(exoticColorBack[i]), outline = str(exoticColorBack[i]) )
        BackFishTail[i] = screen.create_polygon(xFishBack[i], yFishBack[i] + BackFishSize[i], xFishBack[i] + (2*BackFishSize[i]), yFishBack[i] + (2*BackFishSize[i]), xFishBack[i] + (2*BackFishSize[i]), yFishBack[i], fill = str(exoticColorBack[i]), outline = str(exoticColorBack[i]) )
                                                                    #ML                                                              TR                                              BR
        xFishBack[i] = xFishBack[i] - xFishBackSpeed[i]
        
            #RESET FISH XVALUES OFF SCREEN
        if xFishBack[i] < -500:
            xFishBack[i] = xFishBack[i] + randint(1100, 5100)
            yFishBack.append( randint(450, 750) )
            xFishBackSpeed[i] = randint(15, 18)


        #SUBMARINE ANIMATION
    headShip = screen.create_arc(220, 500, 300, 580, start = 90, extent = 180, fill = "skyblue", outline = "skyblue")

        #BODY
    bodyShip = screen.create_rectangle(260, 500, 740, 580, fill = "gold", outline = "gold")
    tailShip = screen.create_rectangle(700, 500, 740, 580, fill = "white", outline = "white")

        #FINS
    botFinsBLCornerShip = screen.create_polygon(260, 580, 300, 580, 300, 660, fill = "gold", outline = "gold")
    botFinsBRCornerShip = screen.create_polygon(620, 580, 700, 580, 620, 660, fill = "gold", outline = "gold")

    topFinsTLCornerShip = screen.create_polygon(260, 500, 420, 420, 420, 500, fill = "gold", outline = "gold")
    topFinsTRCornerShip = screen.create_polygon(460, 420, 540, 500, 460, 500, fill = "gold", outline = "gold")

    botFinsMainShip = screen.create_rectangle(300, 580, 620, 660, fill = "gold", outline = "gold")
    botFinsMainShipLine = screen.create_line(300, 660, 621, 660, fill = "gold")

        #HATCH
    hatchShip = screen.create_oval(420, 390, 460, 370, fill = "gold", outline = "gold")
    hatchConnectShip = screen.create_rectangle(420, 500, 460, 380, fill = "gold", outline = "gold")
    hatchConnectLine1 = screen.create_line(420, 380, 420, 421, fill = "gold")
    hatchConnectLine2 = screen.create_line(460, 380, 460, 421, fill = "gold")
    hatchConnectLine3 = screen.create_line(420, 420, 460, 420, fill = "gold")
    

              


        #FRONT FISH ANIMATIOn
    for i in range(nFishFront):

            #ANIMATING FISH MOVEMENTS
        FrontFish[i] = screen.create_oval(xFishFront[i], yFishFront[i], xFishFront[i] + (5*FrontFishSize[i]), yFishFront[i] - (2*FrontFishSize[i]), fill = str(exoticColorFront[i]), outline = str(exoticColorFront[i]) )
        FrontFishTail[i] = screen.create_polygon(xFishFront[i], yFishFront[i] - FrontFishSize[i], xFishFront[i] - (2*FrontFishSize[i]), yFishFront[i] - (2*FrontFishSize[i]), xFishFront[i] - (2*FrontFishSize[i]), yFishFront[i], fill = str(exoticColorFront[i]), outline = str(exoticColorFront[i]) )
                                                                    #ML                                                               TR                                                          BR
            #UPDATING FISH NEXT FISH MOVEMENTS
        xFishFront[i] = xFishFront[i] + xFishFrontSpeed[i]

            #RESET FISH XVALUES OFF SCREEN
        if xFishFront[i] > 1500:
            xFishFront[i] = xFishFront[i] - randint(1100, 5100)
            yFishFront.append( randint(250, 550) )
            xFishFrontSpeed[i] = randint(15, 18)

    screen.update()
    sleep(0.03)
    screen.delete(sandGround, headShip, bodyShip, tailShip, botFinsMainShip, botFinsBLCornerShip, botFinsBRCornerShip, topFinsTLCornerShip, topFinsTRCornerShip, hatchShip, hatchConnectShip, botFinsMainShipLine, hatchConnectLine1, hatchConnectLine2, hatchConnectLine3)


        #DELETE SHAPES PER FRAME
    for i in range(nRockPillar):
         screen.delete(RockShape[i])

    for i in range(nFishBack):
        screen.delete(BackFish[i], BackFishTail[i])

    for i in range(nFishFront):
        screen.delete(FrontFish[i], FrontFishTail[i])

