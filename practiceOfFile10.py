import random

fruits = ["apple", "banana", "cherry", 'apricot', 'alobukhara', 'almond']
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
random.shuffle(fruits)

print(random.choice(fruits))
print(random.choice(alpha))

friends = ['Arooj', 'Alpha', 'Beeta', 'Ali']
random.shuffle(friends)
print(friends)

print(round(random.random() * 1000))