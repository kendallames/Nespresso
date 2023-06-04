# Coffee APP

print("Welcome to Kendall's Coffee App. What would you like to do?")
print("1. Enter a New Drink")
print("2. View Favorites")
print("3. Quit")

operation = input()

if operation == "1":
    # code to enter a new drink
    
    hot_cold = input("Iced or Hot: ")
    new_drink = input("Enter New Drink: ")
    drink_size = input("Enter Size: ")
    capsule = input("Enter Nespresso Capsule: ")
    print("The drink you want is: " + drink_size + " " + hot_cold + " " + new_drink + " " + "using "
          + capsule + " " + "nespresso capsule")
    print("Thank you for ordering!")
elif operation == "2":
    # code to select a favorite drink
    
    favorites = {
        "americano": "Iced Vanilla Americano with Cream",
        "latte": "Iced Caramel Latte with Almond Milk",
        "mocha": "Iced Mocha with Peppermint",
        "cold_brew": "Pumpkin Cream Cold Brew"
    }

    print("Select your favorite:")
    print("1. Iced Vanilla Americano with Cream")
    print("2. Iced Caramel Latte with Almond Milk")
    print("3. Iced Mocha with Peppermint")
    print("4. Pumpkin Cream Cold Brew")

    choice = input("Please select your favorite: ")

    if choice in ["1", "2", "3", "4"]:
        favorite_key = list(favorites.keys())[int(choice) - 1]
        favorite = favorites[favorite_key]
        print("The favorite you selected is: " + favorite)
        print("Thank you for ordering!")
    else:
        print("Invalid choice.")
elif operation == "3":
    # code to quit
    print("Quitting Application. You will be returned to the main menu.")
else:
    print("Invalid Entry. Please Select a Number 1-3.")

