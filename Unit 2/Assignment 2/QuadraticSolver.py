from math import sqrt

#Introduction
print("Welcome to Daniel's wonderful quadratic solver")
print("*********************************************")
print()

#User inputs the degree of the polynomial
power = int(input("Please enter the degree of your polynomial: "))

#Handling different degrees of the polynomial
if power > 2:
    #Program doesn't handle degrees higher than 2
    print("Sorry, this program cannot handle polynomials of degree 3 or higher")
elif power == 1:
    #Handling polynomial of degree 1
    pass
elif power == 2:
    #Handling polynomial of degree 2
    quadratic = input("Please enter your quadratic in the form ax^2+bx+c=0 (eg: -5x^2-4x+3=0): ")

    #Variable to keep track of index of the quadratic 
    index = 0

    #Variable for the coefficient of x^2
    a = ""

    #Loop to parce for coefficient of x^2
    while quadratic[index] != "x":
        a += quadratic[index]
        index += 1

    #Move index to next index after x^2
    index += 3

    #Variable for the coefficient of x
    b = ""

    #Loop to parce for coefficient of x
    while quadratic[index] != "x":
        b += quadratic[index]
        index += 1
    #Move index to next index for x
    index += 1

    #Variable for the constant
    c = ""

    #Loop to parce for constant
    while quadratic[index] != "=" and index < len(quadratic):
        c += quadratic[index]
        index += 1

    a = float(a)
    b = float(b)
    c = float(c)

    if a == 0:
        print("I guess your quadratic was not to degree 2")
    else:
        sol1 = (-b + sqrt((b**2)-(4*a*c)))/2
        sol2 = (-b - sqrt((b**2)-(4*a*c)))/2
        print(sol1)
        print(sol2)
    print(a)
    print(b)
    print(c)

    

    



    #print(quadratic)


