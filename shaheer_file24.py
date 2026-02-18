while True:
    try:
        num = int(input("please enter a integer: "))
        break
    except ValueError:
        print("Invalid Input, enter only whole numbers")

print(num)

num1 = input("please enter a integer: ")
print(type(num1))

print('1 2 3'.split())
