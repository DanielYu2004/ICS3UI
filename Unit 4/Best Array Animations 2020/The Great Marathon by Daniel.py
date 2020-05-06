# Daniel Yu
# Array Animation Assignment
# 5/1/2020


from tkinter import *
import time
import math
import random
myInterface = Tk()
screen = Canvas(myInterface, width=1000, height=700, background="sky blue")
screen.pack()


# Foreground
screen.create_rectangle(0, 700, 1000, 600, fill="green")

# Road
screen.create_rectangle(0, 600, 1000, 300, fill="#141414", outline="#141414")

# Arrays of all objects
buildings = []
buildingWindows = []

cloudList = []

roadLines = []
lineWidth = 50
lineHeight = 15

runners = []
runnerSpeeds1 = []
runnerSpeeds2 = []
numRunners = 20

x = 0 # to delay animation time
finishLinex = 1000

cameraSpeed = 5


def createBuilding(coords, colour, windows):
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    windowHeight = windows[1]
    windowWidth = windows[0]


    width = abs(x1-x2)
    height = abs(y1-y2)
    row = (width) // windowWidth
    column = (height) // windowHeight
    widthSpace = (width - (row*windowWidth))/(row+1)
    heightSpace = (width - (column*windowHeight))/(column+1)


    buildingComponents = []
    buildingComponents.append(screen.create_rectangle(x1, y1, x2, y2, fill=colour))

    for x in range(row):
        for y in range(column):
            buildingComponents.append(screen.create_rectangle(x1 + ((x+1) * (widthSpace)) + (x * windowWidth) + 5, y2 + ((y+1) * (heightSpace)) + (y * windowHeight) + 10, x1 + ((x+1) * (widthSpace)) + (x * windowWidth) + windowWidth - 5, y2 + ((y+1) * (heightSpace)) + (y * windowHeight) + windowHeight - 10, fill="white"))

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
    
    if frame == 3:
        # x1 = 700
        # y1 = 350
        leg1 = screen.create_polygon(x1, y1 + 10, x1 +10, y1 + 10 + 5, x1 + 15, y1 + 10 + 8, x1 + 20, y1 + 10 + 30, x1 + 15, y1 + 10 + 30, x1 + 15, y1 + 10 + 20, x1, y1 + 15,fill=skinColour, outline="black")
        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour)
        leg2 = screen.create_polygon(x1, y1 + 10, x1 - 10, y1 + 30, x1 - 20, y1 + 35, x1 - 25, y1 + 35, fill=skinColour, outline="black")
        components = [leg1, leg2, body, head]
    if frame == 0:
        leg1 = screen.create_polygon(x1, y1 + 10, x1 - 10, y1 + 30, x1 - 20, y1 + 35, x1 - 25, y1 + 35, fill=skinColour, outline="black")
        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour) 
        leg2 = screen.create_polygon(x1, y1 + 10, x1 +10, y1 + 10 + 5, x1 + 15, y1 + 10 + 8, x1 + 20, y1 + 10 + 30, x1 + 15, y1 + 10 + 30, x1 + 15, y1 + 10 + 20, x1, y1 + 15,fill=skinColour, outline="black")
        components = [leg1, leg2, body, head]
    if frame == 1:
        # x1 = 600
        # y1 = 350

        leg1 = screen.create_polygon(x1, y1 + 5, x1 - 5, y1 + 15, x1 - 20, y1 + 40, x1 - 10, y1 + 40, fill=skinColour, outline="black")
        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour)
        leg2 = screen.create_polygon(x1, y1 + 5, x1 + 5, y1 + 10, x1 + 10, y1 + 30, x1 + 10, y1 + 40, x1 + 3, y1 + 40, fill=skinColour, outline="black")
        components = [leg1, leg2, body, head]
    if frame == 2:
        # x1 = 600
        # y1 = 350

        leg2 = screen.create_polygon(x1, y1 + 5, x1 + 5, y1 + 10, x1 + 10, y1 + 30, x1 + 10, y1 + 40, x1 + 3, y1 + 40, fill=skinColour, outline="black")
        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour)
        leg1 = screen.create_polygon(x1, y1 + 15, x1 - 5, y1 + 10, x1 - 5, y1 + 15, x1 - 15, y1 + 40, x1 - 5, y1 + 40, fill=skinColour, outline="black")
       
        components = [leg1, leg2, body, head]

    # if frame == 6:
    #     leg1 = screen.create_polygon(x1, y1 + 10, x1 - 10, y1 + 30, x1 - 20, y1 + 35, x1 - 25, y1 + 35, fill=skinColour)
    #     body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
    #     head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour) 
    #     leg2 = screen.create_polygon(x1, y1 + 10, x1 +10, y1 + 10 + 5, x1 + 15, y1 + 10 + 8, x1 + 20, y1 + 10 + 30, x1 + 15, y1 + 10 + 30, x1 + 15, y1 + 10 + 20, x1, y1 + 15,fill=skinColour)
    #     components = [leg1, leg2, body, head]
    if frame == 4:
        # x1 = 600
        # y1 = 350

        leg2 = screen.create_polygon(x1, y1 + 5, x1 + 5, y1 + 10, x1 + 10, y1 + 30, x1 + 10, y1 + 40, x1 + 3, y1 + 40, fill=skinColour, outline="black")

        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour)
        leg1 = screen.create_polygon(x1, y1 + 15, x1 - 5, y1 + 10, x1 - 5, y1 + 15, x1 - 20, y1 + 40, x1 - 10, y1 + 40, fill=skinColour, outline="black")
        components = [leg1, leg2, body, head]
    if frame == 5:
        leg1 = screen.create_polygon(x1, y1 + 5, x1 - 5, y1 + 15, x1 - 20, y1 + 40, x1 - 10, y1 + 40, fill=skinColour, outline="black")
        body = screen.create_rectangle(x1-8, y1-10, x1+8, y1+20, fill="red")
        head = screen.create_oval(x1 - 8, y1-10, x1 + 8, y1 - 10 - 16, fill=skinColour)
        leg2 = screen.create_polygon(x1, y1 + 5, x1 + 5, y1 + 10, x1 + 10, y1 + 30, x1 + 10, y1 + 40, x1 + 3, y1 + 40, fill=skinColour, outline="black")
        components = [leg1, leg2, body, head]

    return components

# To have clouds and buildings on initial screen by adding the function params to the lists
for i in range(4):
     # Buildings
    colour = random.choice(["#a8a8a8", "#858585", "#787474"])
    window = [random.randint(30, 50), random.randint(30, 50)]
    Bx = random.randint(0, 1000)
    buildings.append([[Bx, 300, Bx + random.randint(100, 400), 300 - random.randint(100, 250)], colour, window])


# To calculate the spacing between road lines for the initial screen
increment = (1000-(8*lineWidth))/7
for i in range(1,9):
    x1 = (increment+lineWidth)*(i-1) 
    y1 = 450-(lineHeight/2)
    roadLines.append([x1,y1])


# Create Runner arrays
for x in range(numRunners):
    runners.append([[random.randint(0, 400), random.randint(300, 550)], random.randint(0,6)])
runners[numRunners-1] = [[0, 400], 0] # The winning runner
runners = sorted(runners, key=lambda x: x[0][1]) # To make sure overlaps of runners are accurate

for i in range(numRunners):
    runnerSpeeds1.append(random.randint(-500, 500) * 0.001)  
runnerSpeeds1[numRunners-1] = 0.5 # The winning runner

for i in range(numRunners):
    runnerSpeeds2.append(random.randint(-1000, 2000) * 0.001)
runnerSpeeds2[numRunners-1] = 4 # The winning runner

# The individual frames 
# drawRunner([250, 400],0)
# drawRunner([350, 400],1)
# drawRunner([450, 400],2)
# drawRunner([550, 400],3)
# drawRunner([650, 400],4)
# drawRunner([750, 400],5)
# drawRunner([850, 400],6)


for f in range(1000000):

    # For rendering clouds
    # Add new cloud to list every 20 frames
    if f % 20 == 0:
        Cx1 = 1300
        Cy1 = random.randint(0, 200)
        

    # For rendering buildings
    if f % 40 == 0: # new building get added every 60 frames to the list
        colour = random.choice(["#a8a8a8", "#858585", "#787474"])
        window = [random.randint(30, 50), random.randint(30, 50)]
        buildings.append([[1000, 300, 1000 + random.randint(100, 400), 300 - random.randint(100, 250)], colour, window])

    renderBuildings = []
    updatedBuildings = []

    # Adds building params to the building list whist deleting building that have gone off screen
    for building in range(len(buildings)):
        if buildings[building][0]:
            x2 = buildings[building][0][2]
            if x2 > 0:
                coords = buildings[building][0]
                colour = buildings[building][1]
                window = buildings[building][2]
                coords[0] -= cameraSpeed
                coords[2] -= cameraSpeed
                renderBuildings.append(createBuilding(coords, colour, window))
                updatedBuildings.append(buildings[building])
    buildings = updatedBuildings


    # Rerender the road ontop of everything else
    screen.create_rectangle(0, 600, 1000, 300, fill="#141414", outline="#141414")

    # For road lines
    renderLines = []
    updatedLines = []

    # Add to line list for rendering:
    # Since I struggled with finding a way to space the lines evenly during this for loop, 
    # I simply append the line back to the list when its about to go off screen and put 
    # it at the start again.
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
    roadLines = updatedLines


    # To delay the frequency of the running frames
    # 2 can be changed to increase or decrease animation speed
    if f % 2 == 0:
        x += 1

    # For rendering the runners
    renderRunners = []
    if f < 150:
        # Move the runners
        for runner in range(len(runners)):
            runners[runner][0][0] += runnerSpeeds1[runner]
            renderRunners.append(drawRunner(runners[runner][0], (runners[runner][1] + x) % 6))
    elif f > 149:
        # To display the finish line
        if runners[numRunners-1][0][0] > 600:
            finishLinex -= cameraSpeed
            screen.create_rectangle(finishLinex, 600, finishLinex + 50, 300, fill="white")

        # Move the runners
        for runner in range(len(runners)):
            runners[runner][0][0] += runnerSpeeds2[runner]
            renderRunners.append(drawRunner(runners[runner][0], (runners[runner][1] + x) % 6))
    if runners[numRunners-1][0][0] > finishLinex:
        # Runner has crossed the finish line
        break

        
    screen.update()
    time.sleep(0.03)
    
    # Rendering all objects
    for buildingObject in renderBuildings:
        for component in buildingObject:
            screen.delete(component)
    for line in renderLines:
        screen.delete(line)
    for runnerObject in renderRunners:
        for component in runnerObject:
            screen.delete(component)

# Winner Screen
screen.create_text(500, 300, text="WINNER", font="Arial 100", fill="blue")

# For vs code
screen.mainloop()
