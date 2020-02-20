import sys

print("This is a Harvard issued program that can help you determine your admission chances into the coveted Ivy League School...HARVARD")
print("We use a highly accurate algorithm to calculate your probability given many different qualitative and qualitative factors")
print()


score = 0

print("Question 1:")
res1 = input("Is Harvard University the absolutely best university in the whole wide world? Yes or No... ")
if res1 == "no" or res1 == "No":
    print()
    print("Well then why are you on this program then...")
elif res1 == "yes" or res1 == "Yes":
    print()
    print("Very nice answer. Alright there's gonna be a series of questions for the next one...")
    print("Question 2:")
    mathMark  = int(input("Please enter your grade 12 math mark: "))
        if mathMark > 100:
            print("stop lying on these tests")
    engMark = int(input("Please enter your grade 12 english mark: "))
        if mathMark > 100:
            print("stop lying on these tests")
    phyMark = int(input("Please enter your grade 12 physics mark: "))
        if mathMark > 100:
            print("stop lying on these tests")
    chemMark = int(input("Please enter your grade 12 chemistry mark: "))
        if mathMark > 100:
            print("stop lying on these tests")
    bioMark = int(input("Please enter your grade 12 biology mark: "))
        if mathMark > 100:
            print("stop lying on these tests")
    csMark = int(input("Please enter your grade 12 computer science mark: "))
        if mathMark > 100:
            print("stop lying on these tests")
    accountingMark = int(input("Please enter your grade 12 accounting mark: "))
        if mathMark > 100:
            print("stop lying on these tests")
    calcMark = int(input("Please enter your grade 12 calculus mark: "))
        if mathMark > 100:
            print("stop lying on these tests")

    average = round(((mathMark + engMark + phyMark + chemMark + bioMark + csMark + accountingMark + calcMark)/8), 2)
    print("this means your grade 12 average was..." , average)
    if average < 90:
        print()
        print("Sorry, you were almost there buddy. Goodbye.")
    elif average > 100:
        print()
        print("I don't believe you...")
    else:
        if average < 95:
            print()
            print("Hmmm, not bad")
            score +=10
        elif average < 100:
            print()
            print("Hey, thats pretty good")
            score += 20
        elif average == 100:
            print()
            print("Thats very very nice bud.")
            score += 30
        print()
        print("Just a few more questions...")
        print("Question 3:")

        height = int(input("Please enter your height in centimeters: "))

        if height < 160:
            print()
            print("Awwww, just a little taller and you could've made it...")
        elif height > 200:
            print()
            print("You might have some trouble going through doors. Maybe next time...")
        else:
            if height < 170:
                print()
                print("hmm, thats an interesting height for a student")
                score += 10
            elif height < 180:
                print()
                print("you can comfortably walk through doors. Nice.")
                score += 20
            elif height < 190:
                print()
                print("you might hit your head on the door, but you'll be fine.")
                score += 30
            elif height <= 200:
                print()
                print("I would watch your head when you walk through doors. Just don't hit your head too hard.")
                score +=20
            print()
            print("Alright, maybe like 2 more questions... maybe... Question 4:")
            print()
            SteakCook = input("How do you like your steak cooked... Choose from: raw, rare, medium rare, medium, well done, burnt to a crisp...")
            SteakOptions = ['raw', 'rare', 'medium rare', 'medium', 'well done', 'burnt to a crisp']

            if SteakCook not in SteakOptions:
                print("We don't know how to cook steak like that... Sorry, no admission for you.")
            else:
                if SteakCook == SteakOptions[0]:
                    print()
                    print("hmmm, you're quirky, we like that at Harvard")
                if SteakCook == SteakOptions[1]:
                    print("I don't knowwwwww...")
                if SteakCook == SteakOptions[2]:
                    print()
                    print("Excellent choice sir")
                if SteakCook == SteakOptions[3]:
                    print()
                    print("You like it a little overdone I see")

                if SteakCook == SteakOptions[4]:
                    print()
                    print()
                if SteakCook == SteakOptions[5]:
                    print()
else:
    print("I don't understand what that even means")

