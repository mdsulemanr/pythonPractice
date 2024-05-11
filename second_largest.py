def second_largest(num):
    if len(num) < 2:
        return
    if len(num) == 2:
        if num[0] == num[1]:
            return

    num = list(set(num))
    num.sort()
    return num[-2]


num = []
print(second_largest(num))

num = [10]
print(second_largest(num))

num = [-1, 5]
print(second_largest(num))

num = [1, 4, -3, 0, 100, 15, 2]
print(second_largest(num))

num = [2, 3, 3, 2, 2, 3, 3]
print(second_largest(num))
