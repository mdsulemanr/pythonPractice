students = {
    "Shaheer": {
        "age": 9,
        "Gender": "boy",
        "Class": 3,
        "Section": "Green",
        "favourite": ["Cherry", "Straberry", "Pineapple"],
        "angry": False,
        "favourite_subject": "Math"
    },
    "Arisha": {
        "age": 12,
        "Gender": "girl",
        "Class": 6,
        "Section": "Red",
        "favourite": ["Apple", "Banana"],
        "angry": True,
        "favourite_subject": "Computer"
    },
    "Mustafa": {
        "age": 11,
        "Gender": "boy",
        "Class": 5,
        "Section": None,
        "favourite": ["Guava", "Pineapple"],
        "angry": True,
        "favourite_subject": "Urdu"
    },
    "Hazik": {
        "age": 13,
        "Gender": "boy",
        "Class": 7,
        "Section": None,
        "favourite": ["Apple", "Guava"],
        "angry": False,
        "favourite_subject": "English"
    },
    "Zaryab": {
        "age": 12,
        "Gender": "boy",
        "Class": 6,
        "Section": None,
        "favourite": ["Apple", "Pineapple"],
        "angry": True,
        "favourite_subject": "Science"
    },
    "Ahmad": {
        "age": 5,
        "Gender": "boy",
        "Class": None,
        "Section": None,
        "favourite": ["Apple", "Orange"],
        "angry": True,
        "favourite_subject": None
    },
    "Haris": {
        "age": 9,
        "Gender": "boy",
        "Class": 3,
        "Section": "Orange",
        "favourite": ["Apple", "Banana", "Pineapple"],
        "angry": False,
        "favourite_subject": "Computer"
    }
}

# print(students["Shaheer"]["age"])
# print(students["Shaheer"]["Gender"])
# print(students["Shaheer"]["Class"])
#
papa_copy = students.copy()
# print(students)
# print(papa_copy)

x = ('apple', 'banana', 'orange', 'cherry', 'pumpkin')
y = 100
fruit_data = dict.fromkeys(x, y)
print(fruit_data)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

fruits = {
    "apple": 100,
}
fruits.update({"banana": 150})
fruits["cherry"] = 200
print(fruits)
fruits.update({"banana": 300})
print(fruits)


item2 = car2.popitem()
print(item2)
print(car2)

item = car.pop("model")
print(item)
print(car)

print(students)
students.clear()
print(students)