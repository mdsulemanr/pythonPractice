# Functions


# def my_self(name, age):
#     about_me = f'My name is: {name} and your age is: {age}'
#     return about_me
#
# print(my_self(age = 13, name = 'Arish'))
# print(my_self('Shaheer', 9))

# start =1
# end=101
# nuum=2
#
# def table():
#     for i in range(start,end):
#         tabl=f'{nuum} * {i} = {nuum * i}'
#         print(tabl)
# table()

# def counting(start,end):
#     while start <= end:
#         print(start)
#         start=start + 1
# counting(1,101)

# def char_count(str, char):
#     result = str.count(char)
#     return result
#
# print(char_count('This is a tree', 'b'))
# print(char_count('Thirsty Crow, there was a crow', 'b'))

def friends(names,friend_name):
    if friend_name in names:
        return friend_name
    else:
        return 'Friend not found'


print(friends(names = ['Alpha', 'Beeta', 'Arooj', 'Arisha', 'moti'], friend_name = ''))