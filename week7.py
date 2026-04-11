# Simple Money Withdrawal System

balance = 1000

while True:
    print("\n=== Money Withdrawal System ===")
    print("1. Withdraw Money")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            try:
                print()
                amount = float(input("Enter amount to withdraw: ₱"))

                if amount <= 0:
                    print("\nInvalid amount. Please enter a positive value.\n")
                    continue

                elif amount > balance:
                    print("\nError: Insufficient funds.\n")

                    print("What would you like to do?")
                    print("1. Re-enter amount")
                    print("2. Check balance")
                    print("3. Exit")

                    option = input("Enter option: ")

                    if option == "1":
                        continue
                    elif option == "2":
                        print(f"\nCurrent balance: ₱{balance}\n")
                        continue
                    elif option == "3":
                        print("\nExiting program...\n")
                        exit()
                    else:
                        print("\nInvalid option.\n")
                        continue

                else:
                    balance -= amount
                    print("\nWithdrawal successful!")
                    print(f"Remaining balance: ₱{balance}\n")
                    break

            except ValueError:
                print("\nInvalid input! Please enter a number.\n")

            finally:
                print("Transaction attempt complete.\n")

    elif choice == "2":
        print(f"\nCurrent balance: ₱{balance}\n")

    elif choice == "3":
        print("\nThank you for using the system!\n")
        break

    else:
        print("\nInvalid choice. Please select 1, 2, or 3.\n")
