print("=== Simple Calculator === " )
print("1. Add (+)")
print("2. Minus (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

math_operations = ['add', 'minus', 'multiply', 'divide']

def get_number(message):
    while True:
        user_input = input(message)
        try:
            return int(user_input)
        except ValueError:
            print("Oops! Please type a whole number like 5 or 12. 🙂")


while True:
    choice = input('Please select your choice. ').casefold()
    if choice not in math_operations:
        print('Wrong word! Please type: add, minus, multiply, or divide.')
        continue

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")


    if choice == math_operations[0]:
        print(f"Answer = {num1 + num2}")

    elif choice == math_operations[1]:
        print(f"Answer = {num1 - num2}")

    elif choice == math_operations[2]:
        print(f"Answer = {num1 * num2}")

    elif choice == math_operations[3]:
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print(f"Answer = {num1 / num2}")

    while True:
        again = input('Do you want to do again? type yes or no: ').lower()

        if again == 'yes':
            print("Hurry! Lets start it again.")
            break

        elif again == 'no':
            print("Good job! Bye 👋")
            exit()

        else:
            print('Please type either yes or no.')