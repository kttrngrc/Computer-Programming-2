print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
selected_operator = input("Enter choice(1/2/3/4): ")
if selected_operator in ('1', '2', '3', '4'):
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))

    if selected_operator == '1':
        result = first_num + second_num
        print(first_num, "+", second_num, "=", result)

    elif selected_operator == '2':
        result = first_num - second_num
        print(first_num, "-", second_num, "=", result)
   
    elif selected_operator == '3':
        result = first_num * second_num
        print(first_num, "*", second_num, "=", result)
   
    elif selected_operator == '4':
        if first_num == 0 or second_num == 0:
            print("Division by 0 is not allowed!")
        else:
            result = first_num / second_num
            print(first_num, "/", second_num, "=", result)
    else:
        print("Invalid input. Please select 1, 2, 3, or 4.")
