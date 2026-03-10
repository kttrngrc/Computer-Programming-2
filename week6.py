cart = []

while True:
    print("\nShopping Cart Simulator")
    print("1. View Cart")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            print("Items in Cart:")
            i = 1
            for item in cart:
                print(str(i) + ". " + item)
                i += 1

    elif choice == "2":
        item = input("Enter item name: ")

        if item == "":
            print("Item name cannot be empty.")
        else:
            cart.append(item)
            print("Item added to cart.")

    elif choice == "3":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("Items in Cart:")
            i = 1
            for item in cart:
                print(str(i) + ". " + item)
                i += 1

            num = int(input("Select item number: "))

            if num >= 1 and num <= len(cart):
                removed = cart.pop(num - 1)
                print(removed + " removed from cart.")
            else:
                print("Invalid item number.")

    elif choice == "4":
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            print("Checking out the following items:")
            for item in cart:
                print("- " + item)

            print("Checkout complete.")
            cart.clear()

    elif choice == "5":
        break

    else:
        print("Invalid choice")