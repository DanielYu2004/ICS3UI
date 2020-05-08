def coneVolume(r, h):
    volume = 3.14 * r * r * h / 3
    return volume

myVol = round(coneVolume( 10, 40 ), 2)
yourVol = round(coneVolume( 3.5, 86.01 ), 2)
print( "My volume  is",  myVol,  "cm^3"  )
print( "Your volume is",  yourVol, "cm^3" )



def getSlope(x1, y1, x2, y2):
    if (x2 - x1 != 0):
        slope = (y2 - y1) / (x2 - x1) 
        return slope
    else:
        return "undefined"
    
m1 = getSlope(2, 5, -8, 6)  #Here, the two points are (2,5) and (-8, 6), so the answer should be 1/(-10) = -0.1
m2 = getSlope(1, 5, 1, 6)   #What answer should you get here?
m3 = getSlope(1, 2, 3, 4)   #Enter any values you want and predict the answer

      #Printing the results
print("The slopes are", m1, m2, "and", m3)

def getEOL(m, b):
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
    return("The equation of the line is y = " + mOutput + bOutput )

eol1 = getEOL(3, 5)
eol2 = getEOL(0, 5)
eol3 = getEOL(6, 0)
eol4 = getEOL(1, 1) 
print( eol1 )
print( eol2 )
print( eol3 )
print( eol4 )