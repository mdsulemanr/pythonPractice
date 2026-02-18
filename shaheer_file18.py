import random

print(random.randrange(0, 11))
print(random.choice(["a", "b", "c", "d", "e"]))
print(random.choice(["apple", "cherry", "banana", "mango", "pine apple"]))
print(random.choices(["a", "b", "c", "d", "e"], k=10))
print(random.choices(["Shaheer", "Mustafa", "Arisha", "Papa", "Mama"], k = 10))
print(random.sample(["green", "red", "yellow", "blue", "orange"], k = 5))
print(random.sample(["a", "b", "c", "d", "e"], k=5))
print(random.random())