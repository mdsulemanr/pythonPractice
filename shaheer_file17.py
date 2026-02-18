def all(num1, num2, num3, num4, num5, num6):
    result = num1 + num2 - num3 * num4 / num5 % num6
    return result

num1 = 4
num2 = 7
num3 = 1
num4 = 2
num5 = 3
num6 = 8

all_result = all(num1, num2, num3, num4, num5, num6)

print(all(num1, num2, num3, num4, num5, num6))
if type(all_result) == float:
    print("✅ Yes! Yes! Yes! This is a float! ✅")
else:
    print("❌ No! No! No! This is not a float! ❌")