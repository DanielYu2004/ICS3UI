from time import *
from random import *

playAgain = "y"

print("Can you solve 10 addition problems in 20 seconds?")

while playAgain == "y":
    q = 0  #number of questions answered correctly

    sleep(2)
    print("Get ready...")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("Go!\n")

    elapsedTime = 0
    startTime = time()

    while q < 10 and elapsedTime < 30.0:
        x = randint(10, 30)
        y = randint(10, 30)
        
        rightAnswer = x * y
        userGuess = int(input(str(x) + " x " + str(y)+ " = "))
        
        while userGuess != rightAnswer and elapsedTime < 30.0:
            print("Nope! Try again.")
            userGuess = int(input(str(x) + " x " + str(y)+ " = "))
            elapsedTime = time() - startTime #Updating the time before giving them another try
            
        if userGuess == rightAnswer:
           q = q + 1
        
        elapsedTime = time() - startTime #Updating the time before telling them how long they have left
        
        if 10 < elapsedTime < 30.0 and q < 10:
            timeLeft = 30 - elapsedTime
            print("\nYou have", round(timeLeft, 1), "seconds left!  Hurry!")


    if q == 10:
        if elapsedTime < 30.0:
            timeLeft = 30 - elapsedTime
            print("You made it, with", round(timeLeft, 1), "seconds to spare!")
            
        else:
            print("Sorry, you're too slow")
            print("You got", q-1, "questions right before the deadline.")

    else:
        print("Sorry, you're too slow")
        print("You got", q, "questions right.")

    playAgain = input("Do you want to try again? (y/n) ")
