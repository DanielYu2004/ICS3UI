print("Welcome to Daniel's Fraction Reducer")
print("***********************************")

def EuclideanAlgo(bigger, smaller):    
    if bigger % smaller == 0:
        return(smaller)
    elif bigger > 0 and smaller > 0:
        return(EuclideanAlgo(smaller, bigger % smaller))

while True:
    print()
    numerator = int(input("Please enter the numerator of the fraction: "))
    denominator  = int(input("Please enter the denominator  of the fraction: "))

    if denominator == 0:
        print("This fraction is undefined.")
    elif numerator == 0:
        print(str(numerator) + "/" + str(denominator) ,"=","0")
    elif numerator < 0 and denominator < 0:
        print("Sorry, this program only handles non-negative numerators and non-negative denominators.")
    elif numerator < 0:
        print("Sorry, this program only handles non-negative numerators.")
    elif denominator < 0:
        print("Sorry, this program only handles non-negative denominators.")
    else:
        GCD = (EuclideanAlgo(max(numerator, denominator), min(numerator, denominator)))
        if denominator / GCD == 1:
            print("Here is your reduced fraction:")
            print(str(numerator) + "/" + str(denominator) ,"=",str(int(numerator/GCD)))
            print()
        elif GCD == 1:
            print(str(int(numerator/GCD)) +"/" + str(int(denominator/GCD)) , "is already in reduced form")
        else:
            print("Here is your reduced fraction:")
            print(str(numerator) + "/" + str(denominator) ,"=",str(int(numerator/GCD)) +"/" + str(int(denominator/GCD)))