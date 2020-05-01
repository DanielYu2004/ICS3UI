from tkinter import *
import time
import math
import random
myInterface = Tk()




screen = Canvas(myInterface, width=1000, height=700, background="sky blue")
screen.pack()




# Foreground
screen.create_rectangle(0, 700, 1000, 600, fill="green")

# Track
screen.create_rectangle(0, 600, 1000, 300, fill="#141414", outline="#141414")



#Grid lines
spacing = 50

for x in range(0, 1000, spacing): 
    screen.create_line(x, 25, x, 1000, fill="blue")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    screen.create_line(25, y, 1000, y, fill="blue")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)

screen.update()



buildings = []
cloudList = []
roadLines = []

cameraSpeed = 5
lineWidth = 50
lineHeight = 15


def createBuilding(coords, colour):
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    buildingComponents = []
    buildingComponents.append(screen.create_rectangle(x1, y1, x2, y2, fill=colour))
    #buildingComponents.append(screen.create_rectangle(x1+50, y1+50, x2-50, y2-50, fill="red"))
    return buildingComponents

def createLine(coords):
    x1 = coords[0]
    y1 = coords[1]
    x2 = x1 + lineWidth
    y2 = y1 + lineHeight
    lineCoords = []
    lineCoords.append(screen.create_rectangle(x1, y1, x2, y2, fill="white"))
    return lineCoords

def drawRunner(coords, frame):
    # x1 = 500
    # y1 = 350
    skinColour = "#ffd17a"
    components = []
    x1 = coords[0]
    y1 = coords[1]
    
    if frame == 2:
        # x1 = 700
        # y1 = 350
        leg1 = screen.create_polygon(x1, y1 + 10, x1 +10, y1 + 10 + 5, x1 + 15, y1 + 10 + 8, x1 + 20, y1 + 10 + 30, x1 + 15, y1 + 10 + 30, x1 + 15, y1 + 10 + 20, x1, y1 + 15,fill=skinColour)
        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour)
        leg2 = screen.create_polygon(x1, y1 + 10, x1 - 10, y1 + 30, x1 - 20, y1 + 35, x1 - 25, y1 + 35, fill=skinColour)
        components = [leg1, leg2, body, head]
    if frame == 0:
        leg1 = screen.create_polygon(x1, y1 + 10, x1 - 10, y1 + 30, x1 - 20, y1 + 35, x1 - 25, y1 + 35, fill=skinColour)
        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour) 
        leg2 = screen.create_polygon(x1, y1 + 10, x1 +10, y1 + 10 + 5, x1 + 15, y1 + 10 + 8, x1 + 20, y1 + 10 + 30, x1 + 15, y1 + 10 + 30, x1 + 15, y1 + 10 + 20, x1, y1 + 15,fill=skinColour)
        components = [leg1, leg2, body, head]
    if frame == 1:
        # x1 = 600
        # y1 = 350

        leg1 = screen.create_polygon(x1, y1 + 5, x1 - 5, y1 + 15, x1 - 20, y1 + 40, x1 - 10, y1 + 40, fill=skinColour)
        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour)
        leg2 = screen.create_polygon(x1, y1 + 5, x1 + 5, y1 + 10, x1 + 10, y1 + 30, x1 + 10, y1 + 40, x1 + 3, y1 + 40, fill=skinColour)
        components = [leg1, leg2, body, head]
    if frame == 4:
        leg1 = screen.create_polygon(x1, y1 + 10, x1 - 10, y1 + 30, x1 - 20, y1 + 35, x1 - 25, y1 + 35, fill=skinColour)
        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour) 
        leg2 = screen.create_polygon(x1, y1 + 10, x1 +10, y1 + 10 + 5, x1 + 15, y1 + 10 + 8, x1 + 20, y1 + 10 + 30, x1 + 15, y1 + 10 + 30, x1 + 15, y1 + 10 + 20, x1, y1 + 15,fill=skinColour)
        components = [leg1, leg2, body, head]
    if frame == 3:
        # x1 = 600
        # y1 = 350

        leg2 = screen.create_polygon(x1, y1 + 5, x1 + 5, y1 + 10, x1 + 10, y1 + 30, x1 + 10, y1 + 40, x1 + 3, y1 + 40, fill=skinColour)

        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour)
        leg1 = screen.create_polygon(x1, y1 + 5, x1 - 5, y1 + 15, x1 - 20, y1 + 40, x1 - 10, y1 + 40, fill=skinColour)
        components = [leg1, leg2, body, head]


    return components


for i in range(4):
    colour = random.choice(["#a8a8a8", "#858585", "#787474"])
    x1 = random.randint(0,1000)
    height = random.randint(200, 400)
    buildings.append([[x1, 300, x1+random.randint(100, 300), 300 - height], colour])

increment = (1000-(8*lineWidth))/7
for i in range(1,9):
    x1 = (increment+lineWidth)*(i-1) 
    y1 = 450-(lineHeight/2)
    roadLines.append([x1,y1])

# drawRunner([250, 400],0)
# drawRunner([350, 400],1)
# drawRunner([450, 400],2)
# drawRunner([550, 400],3)
# drawRunner([650, 400],4)

# drawRunner(1,1)

# drawRunner(1,2)
# drawRunner(1,3)


x = 0

for f in range(1000000):

    # For Clouds
    if f % 40 == 0:
        Cx1 = 1300
        Cy1 = random.randint(0, 200)
        cloud = []
        for circle in range(random.randint(7, 14)):
            cloudSize = random.randint(50,80)
            cloudx1 = random.randint(Cx1, Cx1+80) 
            cloudy1 = random.randint(Cy1, Cy1+40)
            cloud.append([int(cloudx1) + random.randint(-20, 20), int(cloudy1) + random.randint(-20, 20), int(cloudx1+ cloudSize) + random.randint(-20, 20), int(cloudy1 + cloudSize) + random.randint(-20, 20)])
        cloudList.append(cloud)
    renderClouds = []
    for bigC in cloudList:
            for littleC in range(len(bigC)):
                newCoords = []
                appendBool = True
                for coord in range(len(bigC[littleC])):
                    if bigC[littleC][coord] < -100:
                        appendBool = False
                    if coord % 2 == 0:
                        newCoords.append(bigC[littleC][coord] - cameraSpeed)
                    else:
                        newCoords.append(bigC[littleC][coord])
                bigC[littleC] = newCoords
                if appendBool == True:
                    renderClouds.append(screen.create_oval(newCoords, fill="white", outline="white"))
    
        

    # For Buildings
    if f % 60 == 0:
        colour = random.choice(["#a8a8a8", "#858585", "#787474"])
        buildings.append([[1000, 300, 1000 + random.randint(100, 400), 300 - random.randint(100,400)], colour])

    renderBuildings = []
    updatedBuildings = []
    for building in range(len(buildings)):
        if buildings[building][0]:
            x2 = buildings[building][0][2]
            if x2 > 0:
                coords = buildings[building][0]
                colour = buildings[building][1]
                coords[0] -= cameraSpeed
                coords[2] -= cameraSpeed
                renderBuildings.append(createBuilding(coords, colour))
                updatedBuildings.append(buildings[building])
    buildings = updatedBuildings

    # For Lines

    renderLines = []
    updatedLines = []
    for line in roadLines:
        if line:
            if line[0]+lineWidth > 0:
                line[0] = line[0] - cameraSpeed
                renderLines.append(createLine(line))
                updatedLines.append(line)
            else:
                line[0] = 1000
                renderLines.append(createLine(line))
                updatedLines.append(line)
    #print(renderLines)
    roadLines = updatedLines


    
    if f % 20 == 0:
        x += 1
    print(x)
    person = drawRunner([350, 350] , x % 5)

    
    
    
    
    
    
    
    
    screen.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    for cloud in renderClouds:
        screen.delete(cloud)
    
    for building in renderBuildings:
        screen.delete(building)
        
    for line in renderLines:
        screen.delete(line)
    for component in person:
        screen.delete(component)
    
    
    
    
    
    
    
    
    
    
    
    time.sleep(0.003)










screen.mainloop()
