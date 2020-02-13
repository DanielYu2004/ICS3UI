steak = input("do you like steak? ")

if steak == "yes":
    cookness = input("do you like it rare, medium rare, medium, well done? ")
    if cookness == "rare":
        print("you are disgusting")
    elif cookness == "medium rare":
        print("you are a sane human being")
    elif cookness == "medium":
        print("you are not a garbage human being")
    elif cookness == "welldone":
        print("you are a garbage human being")
    else:
        print("you messed up")
else:
    print("you should try a steak.")