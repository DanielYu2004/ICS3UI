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
    print("degree1")
    pass
elif power == 2:
    #Handling polynomial of degree 2
    quadratic = input("Please enter your quadratic in the form ax^2+bx+c=0 (eg: -5x^2-4x+3=0): ")

    if "x^2" not in quadratic:
        print("You didn't put a quadratic in degreee 2")
    else:
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
        nextvar = True
        #Loop to parce for coefficient of x
        while quadratic[index] != "x":

            #if this condition is satisfied, that means the coefficient of "x" is 0
            if quadratic[index] == "=":
                c = b
                b = 0
                #print(c)

                nextvar = False
                break
            b += quadratic[index]
            index += 1
        #Move index to next index for x
        index += 1

        #Condition is met when the coefficient of "x" is not 0
        if nextvar == True:
            #print(c)
            #Variable for the constant
            c = ""
        #Loop to parce for constant
            while quadratic[index] != "=" and index < len(quadratic):
                c += quadratic[index]
                index += 1
            if c == "":
                c = 0


        if a == "":
            a = 1
        if b == "":
            b = 1
        if c == "":
            c = 1

        a = float(a)
        b = float(b)
        c = float(c)

        if a == 0:
            print("I guess your quadratic was not to degree 2")
        else:
            discriminant = (b**2) - (4*a*c)
            if discriminant >= 0:
                sol1 = ((-1*b) +  sqrt((b**2) - (4*a*c)))/(2*a)
                sol2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
                print("The solutions to the quadratic are:" , sol1 , "and" , sol2)
            else:
                print("The solutions are complex")

            #print(sol1)
            #print(sol2)
        #print(a)
        #print(b)
        #print(c)

        

        



        #print(quadratic)


