import math

def getCPairs(c):
    cPairs = []
    for i in range(1, int(math.sqrt(c)) + 1):
        if (c % i == 0):
            cPairs.append([int(c/i), i])
        if (c % (-1 * i) == 0):
            cPairs.append([int(c/(-1*i)), (-1*i)])
    return(cPairs)

def getFactoredForm(f1, f2):
    if f1 > 0:
        f1 = " + " + str(f1)
    elif f1 < 0:
        f1 = " - " + str(f1)
    else:
        f1 = ""

    if f2 > 0:
        f2 = " + " + str(f2)
    elif f2 < 0:
        f2 = " - " + str(f2)
    else:
        f2 = ""

    ff = "(x" + f1 + ")(x" + f2 + ")"  
    return ff

myTrinomial = "x**2+5x+6"

#Eventually we'll have Python pull out these numbers for us from the string myTrinomial.
#For today, we the programmer will just type it in
a = 1
b = 5
c = 6

#List of factor pairs of c.
#CHALLENGE 1:  WRITE A FUNCTION NAMED getCPairs(c) THAT GENERATES THIS FOR US USING c
cPairs = getCPairs(c)

pairFound = False
for i in range( len(cPairs) ):
      f1 = cPairs[i][0]
      f2 = cPairs[i][1]

      #CHALLENGE 2:  WRITE A FUNCTION NAMED getFactoredForm(f1, f2) THAT BUILDS THE RIGHT STRING DEPENDING ON WHETHER f1, f2
      #ARE POSITIVE OR NEGATIVE
      if f1 + f2 == b:  
            facForm = getFactoredForm(f1, f2)
            print(myTrinomial, "=", facForm)
            pairFound = True


#CHALLENGE 3:  TELL THE USER IF NO PAIR WAS FOUND.

if pairFound == False:
    print("Cannot factor further")