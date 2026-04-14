file_name = "message.txt"

def main():
    try:
        with open(file_name, "x") as file:
            file.write("Messages Log Here:")
    except FileExistsError:
        print("File Created Successfully!")

    while True:
        print("Wellcome to messaging app")
        print("1. Send Message")
        print("2. View message")
        print("3. Exit")

        choice = input("Enter Choice: ")

        match choice:
            case '1':
                message = input("Enter your message: ")
                with open(file_name, "a") as file:
                    file.write(message + "\n")
                print("Message saved!\n")
            case '2':
                try:
                    with open(file_name, "r") as file:
                        print(file.read())
                except FileExistsError:
                    print("No messages found yet.")
            case '3':

                break
main()