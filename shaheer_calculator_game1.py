print("=== Simple Calculator ===")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Choose 1, 2, 3, or 4: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "1":
    print("Answer =", num1 + num2)

elif choice == "2":
    print("Answer =", num1 - num2)

elif choice == "3":
    print("Answer =", num1 * num2)

elif choice == "4":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print("Answer =", num1 / num2)

else:
    print("Wrong choice! Please choose 1 to 4.")
