print("Select your ride:")
print("1. Bike")
print("2. Car")
choice = int(input("Enter your choice: "))
if(choice == 1):
    print("What type of bike do you want to ride?")
    print("1. Sports Bike")
    print("2. Motocross bike")
    print("3. Trail bike")
    print("4. touring bike")
    choice2=int(input("Enter your choice: "))
    if choice2 == 1:
        print("You have selected Sports Bike")
    elif choice2 == 2:
        print("You have selected Motocross Bike")
    elif choice2 == 3:
        print("You have selected Trail Bike")
    elif choice2 == 4:
        print("You have selected Touring Bike")
elif(choice == 2):
    print("what type of car do you want to ride?")
    print("1. Electric car")
    print("2. sports car")
    print("3. SUV")
    print("4. Hypercar")
    print("5. Pick-up truck")
    choice3=int(input("Enter your choice: "))
    if choice3 == 1:
        print("You have selected Electric Car")
    elif choice3 == 2:
        print("You have selected Sports Car")
    elif choice3 == 3:
        print("You have selected SUV")
    elif choice3 == 4:
        print("You have selected Hypercar")
    elif choice3 == 5:
        print("You have selected Pick-up Truck")
else:
    print("Invalid choice. Please select either 1 for Bike or 2 for Car.")