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
    print("Very nice answer. Alright next question... Question 2:")
    average = float(input("What is your cumulative average out of 100? "))
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
        print("Just a few more questions... Question 3:")
        print()

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
                pass




