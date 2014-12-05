__author__ = 'steve1281'

meal = ""

print("1. Eggs")
print("2. Pancakes")
print("3. Waffles")
print("4. Oatmeal")

mainChoice = int(input("Choose a breakfast item: "))

if (mainChoice == 2) :
    meal = "Pancakes"
elif (mainChoice == 3):
    meal = "Waffles"

if (mainChoice == 1):
    print("1. Wheat Toast")
    print("2. Sour Dough")
    print("3. Rye Toast")
    print("4. Pancakes")
    bread = int(input('Choose a type of bread: '))

    if (bread == 1) :
        print("You chose eggs with wheat toast.")
    elif (bread == 2) :
        print("You chose eggs with sour dough.")
    elif (bread == 3) :
        print("You chose eggs with rye toast.")
    elif (bread == 4) :
        print("You chose eggs with pancakes.")
    else :
        print("We have eggs, but not that kind of bread.")
elif (mainChoice == 2) or (mainChoice == 3):
    print("1. Syrup")
    print("2. Strawberries")
    print("3. Powdered Sugar")
    topping = int(input("Choose a topping: "))

    if (topping == 1):
        print ("You chose "+ meal + " with syrup" )
    elif (topping == 2) :
        print("You chose "+ meal + " with strawberries")
    elif (topping == 3) :
        print("You chose "+ meal + " with powdered sugar")
    else:
        print("We have " + meal + ", but not that topping.")
elif (mainChoice == 4):
    print ("You chose oatmeal.")
else :
    print("We don't serve that breakfast item!")
