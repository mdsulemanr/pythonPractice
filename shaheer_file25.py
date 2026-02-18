x, y = map(int, input("Enter two integers separated by a space: ").split())

print(f"First number: {x}")
print(f"Second number: {y}")

def square(n):
    return n * n

numbers = [1, 2, 3, 4]
# Apply the 'square' function to each item in 'numbers'
result_map = map(square, numbers)

# Convert the map object to a list for display/use
result_list = list(result_map)

print(result_list)
# Output: [1, 4, 9, 16]

fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = list(map(str.upper, fruits))
print(uppercase_fruits)
# Output: ['APPLE', 'BANANA', 'CHERRY']

str_numbers = ['1', '2', '3', '4']
int_numbers = list(map(int, str_numbers))
print(int_numbers)
# Output: [1, 2, 3, 4]

nums = list(map(int, input("Enter numbers only, separated by comma: ").split(' ')))

def sqaure(n):
    return n*n

square = list(map(sqaure, nums))
print(square)


while True:
    try:
        number = int(input("Enter an integer: "))
        break # Exit loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a whole number only.")

print(f"You entered: {number}")
