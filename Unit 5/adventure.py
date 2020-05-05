from time import *

def noOneShowsUp():
    print("Hmm... It appears that no one has shown up. What do you do again?")

    choice = input("(a) You try to knock again      (b) You leave and decide to go home and play league of legends      (c) You continue to wait")

    if choice == "a":
        print("Mr Schattman did not hear your knock the first time, but hears your second one and lets you in the class to code.")
    if choice == "b":
        print("A phone call gets sent to your house for skipping class and you get suspended. This results in you not being able to get a job and decide to live in the jungle for a living.")
    if choice == "c":
        print("You wait outside the door until the bell rings and class is over. A phone call gets sent to your house for skipping class and you get suspended. This results in you not being able to get a job and decide to live in the jungle for a living.")

def codeOnGround():
    print("You now have discovered a passion for floor programming, a specialized type of programming where the programmer is required to develop from a sitting position on the floor. What do you do?")

    choice = input("(a) You drop out of school to floor program full-time       (b) You fight the urge to floor program and enter the CS classroom forcefully to sit on a chair and program regularly       (c) Try to tell your friend in another class about floor programming")

    if choice == "a":
        print("10 years later, you are now known as a world renowned floor programmer and is leading the industry in floor programming technology. Congrats!")
    if choice == "b":
        print("You become a normal developer sitting on chairs and miss out on becoming the Steve Jobs in floor programming.")
    if choice == "c":
        print("You get in trouble for bother another classroom and get suspended. This results in you not finishing your education and working at Mcdonalds full-time at age 15.")

def lateToCS():
      print("Oh no!  You're late to CS class!  You're standing outside 1706 . What do do you do?")

      choice = input("(a) Knock    (b) Sit outside and write Python code     (c) Play Candy Crush until Mr. S. opens door:  ")
      
      if choice == "a":
            noOneShowsUp()  #Write this procedure. It should give the player a new set of choices.
            playAgain()            

      elif choice == "b":
            codeOnGround()  #Write this procedure. It should give the player a new set of choices
            playAgain()

      else:
            print("A dragon ate you while you were distracted on your phone")
            print("You died.  But at least you made it to Level 12.")
            playAgain()

def startGame():  
    print()
    print("@~" *10 )
    print("Welcome to being late to CS")
    print("@~" *10 )
    print()
    lateToCS()

def playAgain():
    again = input("Would you like to play again? yes/no")
    if again == "yes":
        startGame()  #Or ask user if they want to play again 
    else:
        print("pathetic")



startGame()  #The procedure-call that actually starts the game