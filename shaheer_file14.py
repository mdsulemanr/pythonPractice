student1 = {
    "name": "Shaheer",
    "age": 9,
    "fruits_i_like": ["Orange", "Cherry"]
}

student2 = {
    "name": "Arisha",
    "age": 12,
    "table": [table for table in range(0, 11) if table %2 != 0]
}

student3 = dict(
    name = "Mustafa",
    age = 11,
    counting = [num for num in range(1, 11)]
)

print(student1)
print(student1["name"])
print(student1["age"])
print(student1["fruits_i_like"])
print(list(student1.keys()))
print(list(student1.values()))
print(list(student1.items()))
print(student2)
print(student2.get("name"))
print(student2.get("age"))
print(student2.get("table"))
print(list(student2.keys()))
print(list(student2.values()))
print(list(student2.items()))
print(student3)
print(student3["name"])
print(student3["age"])
print(student3["counting"])
print(list(student3.keys()))
print(list(student3.values()))
print(list(student3.items()))