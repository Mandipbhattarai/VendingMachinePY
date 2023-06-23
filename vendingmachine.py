# Variable initialization
total = 0
purchased_items = []

# Function to display the menu
def menu():
    print("Here, We have got these options:")
    print("1. Hard Drinks")
    print("2. Soft Drinks")
    print("3. Snacks")
    print("4. Kids Section")
    print("5. Exit")


def promocode(total):
    print("Do you have any Promo Code?")
    print("1. Yes")
    print("2. No")
    code = int(input("Enter your choice: "))

    if code == 1:
        promo_code = int(input("Please enter your promo code: "))
        if promo_code == 2325 or promo_code == 6396:
            print("\nCongratulations! You have got 10% discount")
            total -= total * 0.10
        else:
            print("Invalid promo code")
    elif code == 2:
        print("No promo code applied")
    else:
        print("Invalid choice")

    return total

# Function to handle hard drinks section
def harddrink(total):
    print("\nYou have chosen Hard Drinks")
    age = int(input("Enter your age: "))
    if age >= 18:
        hard_drink_menu()
        drinks = int(input("Enter the number of Hard Drinks you want to purchase: "))

        for _ in range(drinks):
            choice = int(input("Enter your choice of Hard Drink: "))
            if choice == 1:
                total += 150
                purchased_items.append("Whiskey - Rs.150")
            elif choice == 2:
                total += 350
                purchased_items.append("Vodka - Rs.350")
            elif choice == 3:
                total += 355
                purchased_items.append("Beer - Rs.355")
            elif choice == 4:
                total += 250
                purchased_items.append("Rum - Rs.250")
            elif choice == 5:
                total += 300
                purchased_items.append("Tequila - Rs.300")
            else:
                print("Invalid choice!")
    else:
        print("Sorry! You're not eligible for the purchase of this item!")
    return total

# Function to display the hard drinks menu
def hard_drink_menu():
    print("\nHard Drinks:")
    print("1. Whiskey - Rs.150")
    print("2. Vodka - Rs.350")
    print("3. Beer - Rs.355")
    print("4. Rum - Rs.250")
    print("5. Tequila - Rs.300")

def softdrink(total):
    # This is the softdrink function
    print("\nYou have chosen Soft Drinks")
    soft_drink_menu()
    soft_drinks = int(input("Enter the number of Soft Drinks you want to purchase: "))

    for i in range(soft_drinks):
        choice = int(input("Enter your choice of Soft Drink: "))
        if choice == 1:
            total += 40
            purchased_items.append("Coke - Rs.40")
        elif choice == 2:
            total += 35
            purchased_items.append("Pepsi - Rs.35")
        elif choice == 3:
            total += 45
            purchased_items.append("Sprite - Rs.45")
        elif choice == 4:
            total += 50
            purchased_items.append("Fanta - Rs.50")
        elif choice == 5:
            total += 60
            purchased_items.append("Mirinda - Rs.60")
        else:
            print("Invalid choice!")

    print("Your total for Soft Drinks is Rs.", total)
    return total

def soft_drink_menu():
    print("\nSoft Drinks:")
    print("1. Coke - Rs.40")
    print("2. Pepsi - Rs.35")
    print("3. Sprite - Rs.45")
    print("4. Fanta - Rs.50")
    print("5. Mirinda - Rs.60")

def snacks(total):
    # This is the snacks function
    print("\nYou have chosen Snacks")
    snacks_menu()
    snacks = int(input("Enter the number of Snacks you want to purchase: "))

    for i in range(snacks):
        choice = int(input("Enter your choice of Snack: "))
        if choice == 1:
            total += 50
            purchased_items.append("Chips - Rs.50")
        elif choice == 2:
            total += 30
            purchased_items.append("Pretzels - Rs.30")
        elif choice == 3:
            total += 25
            purchased_items.append("Popcorn - Rs.25")
        elif choice == 4:
            total += 45
            purchased_items.append("Nuts - Rs.45")
        elif choice == 5:
            total += 40
            purchased_items.append("Biscuits - Rs.40")
        else:
            print("Invalid choice!")

    print("Your total for Snacks is Rs.", total)
    return total

def snacks_menu():
    print("\nSnacks:")
    print("1. Chips - Rs.50")
    print("2. Pretzels - Rs.30")
    print("3. Popcorn - Rs.25")
    print("4. Nuts - Rs.45")
    print("5. Biscuits - Rs.40")

def child(total):
    # This is the child function
    print("\nYou have chosen Kids Section")
    kids_menu()
    kids = int(input("Enter the number of items you want to purchase from Kids Section: "))

    for i in range(kids):
        choice = int(input("Enter your choice from Kids Section: "))
        if choice == 1:
            total += 100
            purchased_items.append("Toy - Rs.100")
        elif choice == 2:
            total += 200
            purchased_items.append("Candy - Rs.200")
        elif choice == 3:
            total += 150
            purchased_items.append("Balloon - Rs.150")
        elif choice == 4:
            total += 80
            purchased_items.append("Sticker - Rs.80")
        elif choice == 5:
            total += 120
            purchased_items.append("Coloring Book - Rs.120")
        else:
            print("Invalid choice!")

    print("Your total for Kids Section is Rs.", total)
    return total

def kids_menu():
    print("\nKids Section:")
    print("1. Toy - Rs.100")
    print("2. Candy - Rs.200")
    print("3. Balloon - Rs.150")
    print("4. Sticker - Rs.80")
    print("5. Coloring Book - Rs.120")


# Main program
print("Hello! Welcome to Our Vending Machine.")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
phone = input("Enter your phone number: ")

while True:
    menu()  # Displaying the menu
    n = int(input("\nEnter your choice: "))

    if n == 1:
        total = harddrink(total)  # Function call
    elif n == 2:
        total = softdrink(total)  # Function call
    elif n == 3:
        total = snacks(total)  # Function call
    elif n == 4:
        total = child(total)  # Function call
    elif n == 5:
        print("You've entered exit")
        break
    else:
        print("Please enter a valid choice!")

print("Here's your bill: Rs.", total)
code = int(input("Do you have any Promo Code?\n1. Yes\n2. No\n"))
code_store = promocode(total)
print("\n\n")
print("*******************************************************")
print("Name:", first_name, last_name)
print("-------------------------------------------------------")
print("Your purchased items:")
for item in purchased_items:
    print(item)
print("-------------------------------------------------------")
print("Your final bill is: Rs.", code_store)
print("*******************************************************")