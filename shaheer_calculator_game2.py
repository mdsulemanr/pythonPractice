print("=== Simple Calculator === " )
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

while True:
    try:
        choice = int(input("Choose 1, 2, 3, or 4: "))
        if choice in [1, 2, 3, 4]:
            break
        else:
            print("Please enter a number between 1 to 4.")
            continue
    except ValueError:
        print("Invalid Input! Enter an integer only!")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

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
