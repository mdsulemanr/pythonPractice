cousin_data = {
    "Shaheer": 9,
    "Arisha": 12,
    "Mustafa": 11,
    "Hazik": 12,
    "Zaryab": 11,
    "Sarim": 10,
    "Umar": 10,
    "Abdullah": 10,
    "Ahmar": 8,
    "Hassan": 7,
    "Anas": 7,
    "Ashar": 7,
    "Ahmad": 5
}
big_cousins = [name for name, age in cousin_data.items() if age >= 10]
big_cousins_list = []

medium_cousins = [name for name, age in cousin_data.items() if 6 < age < 9]
medium_cousins_list = []

small_cousins = [name for name, age in cousin_data.items() if age < 9]
small_cousins_list = []

for name, age in cousin_data.items():
    print(f"My name is {name} and my age is {age} years old.")
    if age <= 10:
        big_cousins_list.append(name)

    if age > 9:
        small_cousins_list.append(name)

    if age > 10:
        medium_cousins_list.append(name)

print(big_cousins)
print(big_cousins_list)
print(medium_cousins)
print(medium_cousins_list)
print(small_cousins)
print(small_cousins_list)