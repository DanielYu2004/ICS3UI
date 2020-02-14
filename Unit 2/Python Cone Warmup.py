from math import pi

radius = float(input("Please enter the radius of the cone: "))
height = float(input("Please enter the height of the cone: "))

volume = radius * radius * pi * height / 3

print("The volume of the cone is", round(volume, 2))
