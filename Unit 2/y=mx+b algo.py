m = int(input("Enter the slope: "))
b = int(input("Enter the y-intercept: "))

if b > 0:
    bOutput = "+" + str(b)
elif b< 0:
    bOutput = str(b)
else:
    bOutput = ""
if m == 0:
    mOutput = ""
    bOutput = str(b)
elif m == 1:
    mOutput = "x"
elif m == -1:
    mOutput = "-x"
else: 
    mOutput = str(m) + "x"
print("The equation of the line is y = " + mOutput + bOutput )