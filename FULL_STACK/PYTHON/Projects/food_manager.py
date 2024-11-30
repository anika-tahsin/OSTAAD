# initialize empty list for your favourite foods 
favourite_food = [] 

while True:
    print("Favourite food manager")
    print("0. Exit")
    print("1. Add food")
    print("2. Remove food")
    print("3. View Favourite food")

    # Enter choice from the above options 
    choice = input("Enter your choice from the menu list: ")

    if choice == '0':
        print("Thanks for using Favourite Food manager.")
        break

    elif choice == '1':
        food = input("Enter Your favourite food name: ")
        favourite_food.append(food)
        print (f"{food} added successfully")
        print(favourite_food)
        

    elif choice == '2':
        food = input("Enter food name that you want to remove: ")
        if favourite_food:
            favourite_food.remove(food)
            print (f"{food} removed successfully")
            
        else:
            print(f"{food} is not in your list")
            

    elif choice == '3':
        if favourite_food:
            print("Your favourite foods are:")
            for index, food in enumerate(favourite_food, start=1):
                print(f"{index}.{food}")
            
        else:
            print("Your favourite food list is empty or haven't added yet")
            
    
    else: 
        print("Sorry! Invalid choice")
        
