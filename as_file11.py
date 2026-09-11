stu1 = {
    'name': 'Arisha',
    'age': 13,
    'section': '7Yellow',
    'fav_game': ['Badminton', 'Football']
}

stu2 = {
    'name': 'Shaheer',
    'age': 10,
    'section': '4Green',
    'fav_game': ['Cricket', 'Football']
}

print(stu1)
print(stu1['name'])
print(list(stu1.keys()))
print(type(list(stu1.keys())))
print(stu1.values())
print(stu1.get('name'))
print(type(list(stu1.items())[0]))
print(type(stu1.items()))
print(stu1.update({'naughty': True}))
print(stu1)
copy_of_stu = stu1.copy()
print(f'this is the copy dictionary {copy_of_stu}')
print(stu1)
print(stu1.popitem())
print(stu1)


stu1.clear()
print(stu1)