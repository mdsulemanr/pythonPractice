def addition(num1, num2):
    result = num1 + num2
    return result

def subtraction(num1, num2):
    result = num1 - num2
    return result

def multiplication(num1, num2):
    result = num1 * num2
    return result

def division(num1, num2):
    result = num1 / num2
    return result

def remainder(num1, num2):
    result = num1 % num2
    return result

def all(num1, num2, num3, num4, num5):
    result = num1 + num2 - num3 % num4 / num5
    return result


print(addition(7, 9))
print(subtraction(7, 6))
print(multiplication(55, 3))
print(division(6, 7))
print(remainder(4, 10))
print(all(3, 6, 2, 9, 7))