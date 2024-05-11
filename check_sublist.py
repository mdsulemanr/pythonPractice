"""Check whether the list is sublist or not"""


def is_sublist(main_list, sub_list):
    if sub_list == []:
        return True
    if sub_list == main_list:
        return True
    if len(sub_list) > len(main_list):
        return False

    for i in sub_list:
        if i not in main_list:
            return False
    return True


a = [2, 4, 3, 5, 7]
b = [4, -3]
c = [3, 7]
d = []
e = [2, 4, 7, 3, 5]
f = [2, 4, 7, 3, 5, 1]
g = ['apple', 'banana', 'orange']
h = ['apple']

# print(is_sublist(a, b))
# print(is_sublist(a, c))
# print(is_sublist(a, d))
# print(is_sublist(a, e))
# print(is_sublist(a, f))
# print(is_sublist(a, c))
print(is_sublist(g, h))
