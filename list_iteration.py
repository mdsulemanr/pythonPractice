def juice_names(fruits):
    [print(f"{fruit} juice") for fruit in fruits]


juice_names(["apple", "mango", "banana"])


def count_down(num):
    [print(i) for i in range(num + 1)]


count_down(5)


def fruit_names(fruits):
    for i in range(len(fruits)):
        print("The list at index", i, "contains a", fruits[i])

fruit_names(["pineapple", "straberry"])

def counting(num):
    [print(i) for i in range(num+1)]

counting(7)

def table(num):
    [print(f"2 * {i} = {2*i}") for i in range(1, num+1)]

table(10)