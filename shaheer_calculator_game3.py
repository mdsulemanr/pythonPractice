print("=== Simple Calculator === " )
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

while True:

    while True:
        try:
            choice = int(input("Choose 1, 2, 3, or 4: "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid Input! Enter a number between 1 to 4.")
                continue

        except ValueError:
            print("ValueError, Invalid Input! Please enter integers only!")

    while True:
        try:
            num1 = int(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid Input! Please enter integers only!")

    while True:
        try:
            num2 = int(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid Input! Please enter integers only!")

    if choice == 1:
        print(f"Answer = {num1 + num2}")

    elif choice == 2:
        print(f"Answer = {num1 - num2}")

    elif choice == 3:
        print(f"Answer = {num1 * num2}")

    elif choice == 4:
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print(f"Answer = {num1 / num2}")

    while True:
        again = input("do you want to do this again? enter yes or no: ").casefold()
        if again == 'yes':
            print("Hurry! Lets play again.")
            break
        elif again == 'no':
            exit()
        else:
            print("Bany ka puttar bn, smjh aye. Please type either yes or no: ")
            continue
