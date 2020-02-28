#Daniel Yu
#ICS4UI
#Fraction Reducer


#Introduction   
print("Welcome to Daniel's Fraction Reducer")
print("***********************************")

#Function for Euclidean Algorithm, with parameters for a bigger number and smaller number
def EuclideanAlgo(bigger, smaller): 

    #Base case in recursive function for when we find the GCF 
    if bigger % smaller == 0:
        return(smaller)

    #Rerun recursive function on variable (smaller) and (bigger % smaller) until we get base case
    elif bigger > 0 and smaller > 0:
        return(EuclideanAlgo(smaller, bigger % smaller))

#Loop for multiple inputs
while True:
    print()

    #User inputs
    numerator = int(input("Please enter the numerator of the fraction: "))
    denominator  = int(input("Please enter the denominator of the fraction: "))

    #If the denominator is 0
    if denominator == 0:
        print("This fraction is undefined.")

    #If numberator is 0
    elif numerator == 0:
        print(str(numerator) + "/" + str(denominator) ,"=","0")
    
    #If numerator and denominator is negative
    elif numerator < 0 and denominator < 0:
        print("Sorry, this program only handles non-negative numerators and non-negative denominators.")

    #If only numerator is negative    
    elif numerator < 0:
        print("Sorry, this program only handles non-negative numerators.")
    
    #If only denominator is negative
    elif denominator < 0:
        print("Sorry, this program only handles non-negative denominators.")
    
    #Is not a special case if runs this
    else:

        #EuclideanAlgo function driver with respective parameters
        GCD = (EuclideanAlgo(max(numerator, denominator), min(numerator, denominator)))

        #If the denominator and GCD are equal
        if denominator / GCD == 1:
            print("Here is your reduced fraction:")
            print(str(numerator) + "/" + str(denominator) ,"=",str(int(numerator/GCD)))
            print()
        #If the GCD is 1, which means the fraction is already in reduced form
        elif GCD == 1:
            print(str(int(numerator/GCD)) +"/" + str(int(denominator/GCD)) , "is already in reduced form")
        
        #The fraction is reducable
        else:
            print("Here is your reduced fraction:")
            print(str(numerator) + "/" + str(denominator) ,"=",str(int(numerator/GCD)) +"/" + str(int(denominator/GCD)))