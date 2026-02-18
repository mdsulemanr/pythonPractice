stud1 = {"name": "Shaheer", "age": 9, "fruits_i_like": ["Orange", "Cherry"]}
stud2 = {"name": "Arisha", "age": 12, "fruits_she_like": ["Guava", "Apple"]}

def print_dict(stud1):
    return stud1

print(print_dict(stud1))
print(print_dict(stud2))

def print_values(stud1):
    return list(stud1.values())

print(print_values(stud1))
print(print_values(stud2))

def print_keys(stud1):
    return list(stud1.keys())

print(print_keys(stud1))
print(print_keys(stud2))

def print_items(stud1):
    return list(stud1.items())

print(print_items(stud1))
print(print_items(stud2))