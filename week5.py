users = []

while True:
    print("\nUser Management System")
    print("1. Show Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if len(users) == 0:
            print("No users found.")
        else:
            print("Users:")
            i = 1
            for user in users:
                print(str(i) + ". " + user)
                i += 1

    elif choice == "2":
        name = input("Enter new user name: ")

        if name == "":
            print("User name cannot be empty.")
        else:
            users.append(name)
            print("User added.")

    elif choice == "3":
        if len(users) == 0:
            print("No users available.")
        else:
            print("Users:")
            i = 1
            for user in users:
                print(str(i) + ". " + user)
                i += 1

            num = int(input("Select user number: "))

            if num >= 1 and num <= len(users):
                new_name = input("Enter new name: ")
                users[num - 1] = new_name
                print("User updated.")
            else:
                print("Invalid user number.")

    elif choice == "4":
        if len(users) == 0:
            print("No users available.")
        else:
            print("Users:")
            i = 1
            for user in users:
                print(str(i) + ". " + user)
                i += 1

            num = int(input("Select user number: "))

            if num >= 1 and num <= len(users):
                users.pop(num - 1)
                print("User deleted.")
            else:
                print("Invalid user number.")

    elif choice == "5":
        break

    else:
        print("Invalid choice")