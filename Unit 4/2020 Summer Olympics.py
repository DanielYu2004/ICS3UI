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
screen.create_rectangle(0, 600, 1000, 300, fill="grey", outline="grey")

buildings = []

cloudList = []

def createBuilding(coords):
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    buildingComponents = []
    buildingComponents.append(screen.create_rectangle(x1, y1, x2, y2, fill="red"))
    #buildingComponents.append(screen.create_rectangle(x1+50, y1+50, x2-50, y2-50, fill="red"))
    return buildingComponents


buildings.append([800, 300, 1000, 200])


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
                        newCoords.append(bigC[littleC][coord] - 5)
                    else:
                        newCoords.append(bigC[littleC][coord])
                bigC[littleC] = newCoords
                if appendBool == True:
                    renderClouds.append(screen.create_oval(newCoords, fill="white", outline="white"))
    
        


    if f % 60 == 0:
        
        buildings.append([1000, 300, 1000 + random.randint(100, 300), 300 - random.randint(150,250)])

    renderBuildings = []
    updatedBuildings = []
    for building in range(len(buildings)):
        if buildings[building]:
            print(buildings)
            print(buildings[building])
            x2 = buildings[building][2]
            if x2 > 0:
                coords = buildings[building]
                coords[0] -= 5
                coords[2] -= 5
                renderBuildings.append(createBuilding(coords))
                updatedBuildings.append(buildings[building])
            # else:
            #     updatedBuildings[building] = []
    buildings = updatedBuildings

            
    print(buildings)
    
    
    
    
    
    
    
    
    
    
    
    screen.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    for cloud in renderClouds:
        screen.delete(cloud)
    
    for building in renderBuildings:
        screen.delete(building)
    
    
    
    
    
    
    
    
    
    
    
    
    time.sleep(0.003)










screen.mainloop()
