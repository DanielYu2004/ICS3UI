for i in range(1,4):
    print("Moving to place #" + str(i))
    print("Setting the plate")
    print("Setting the fork and knife")
    print("Filling the glass")
    print()

born = 2004
for i in range(2020,2101):
    print("In" , str(i) , "I turn" , str(i-born))

for i in range(4,21):
    print(5*i)

sum = 0

for i in range(1,21):
    sum +=1

print(i)



numInputs = int(input("Enter the number of inputs: "))
mark = 0
for i in range(numInputs):
    mark += int(input("Enter a mark: "))

print("Average: " + str(round(mark/numInputs,2)))