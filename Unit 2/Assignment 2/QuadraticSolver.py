from math import sqrt

#Introduction
print("Welcome to Daniel's Wonderful Quadratic Solver")
print("*********************************************")
print()

#User inputs the degree of the polynomial
power = int(input("Please enter the degree of your polynomial: "))

#Handling different degrees of the polynomial

#Program doesn't handle degrees higher than 2
if power > 2:
    print("Sorry, this program cannot handle polynomials of degree 3 or higher")

#Handling polynomial of degree 1
elif power == 1:
    print("This program solves quadratics, not linear equations. You should be able to solve that yourself.")
    pass

#Handling negative polynomial degree inputs
elif power < 1:
    print("I don't know what that means")

#Handling polynomial of degree 2
elif power == 2:

    #Quadratic Input
    quadratic = input("Please enter your quadratic in the form ax^2+bx+c=0 (eg: -5x^2-4x+3=0): ")

    #To check if the quadratic input is a quadratic
    if "x^2" not in quadratic:
        print("You didn't put a quadratic with degreee 2")
    #To check if the quadratic is formatted correctly

    elif "=0" not in quadratic:
        print("You didn't include an '=0'")

    else:
        #Variable to keep track of index of the quadratic 
        index = 0

        #Variable for the coefficient of x^2
        a = ""

        #Loop to parce for coefficient of x^2
        while quadratic[index] != "x":
            #Add the looped character to a
            a += quadratic[index]
            index += 1

        #Move index to next index after x^2
        index += 3

        #Variable for the coefficient of x
        b = ""

        #A bool to check if the coefficient of x is not 0
        nextvar = True

        #Loop to parce for coefficient of x
        while quadratic[index] != "x":

            #If this condition is satisfied, that means the coefficient of "x" is 0
            if quadratic[index] == "=":

                #We know that the term we just looped over was not the coefficient of x but actually the constant
                c = b
                b = 0

                #Set this bool to false so that we know not to check for the next constant term since we already found it
                nextvar = False

                #We break the loop forcefully because we will not encounter another "x" since the cofficient of "x" is 0
                break

            #Add the looped character to b
            b += quadratic[index]

            #Go to next index
            index += 1


        #Condition is met when the coefficient of "x" is not 0
        if nextvar == True:

            #Move index to next index for x
            index += 1

            #Variable for the constant
            c = ""
            #Loop to parce for constant
            while quadratic[index] != "=" and index < len(quadratic):

                #Add the looped character to c
                c += quadratic[index]

                #Go to next index
                index += 1

            #To check if any characters were detected after the term with the x. 
            if c == "":
                c = 0

        #To catch any empty strings when parcing the quadratic.
        if a == "":
            a = 0
        if b == "":
            b = 0
        if c == "":
            c = 0

        a = float(a)
        b = float(b)
        c = float(c)

        #To check if the user put "0x^2", which would make the equation not a quadratic
        if a == 0:
            print()
            print("I guess your quadratic was not to degree 2")
        else:
            #Discriminant value
            discriminant = (b**2) - (4*a*c)

            #Check if discriminant would result in complex roots or not
            if discriminant >= 0:
                #Define variables for the two solutions
                sol1 = ((-1*b) +  sqrt((b**2) - (4*a*c)))/(2*a)
                sol2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)

                #To format the solutions if they are integers
                if int(sol1) == sol1:
                    sol1 = int(sol1)
                if int(sol2) == sol2:
                    sol2 = int(sol2)

                #To check if there is only one solution or two
                if sol1 == sol2:
                    print()
                    print("The solution to the quadratic is:" , round(sol1,2))
                else:
                    print()
                    print("The solutions to the quadratic are:" , round(sol1,2) , "and" , round(sol2, 2))

            else:
                print("The solutions are complex")
