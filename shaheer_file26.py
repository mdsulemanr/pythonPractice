cousins = ["Haider", "Mustafa", "Ahmad", "banana"]
cousins2 = ["Omar", "Hassan", "Ahmad", "Sarim", "Ahmer", "Ashar", "Abdullah", "Anas", "Maaz", "Amna"]
del_list = [0, 1]
print(del_list)

try:
    del del_list
    print(del_list)
except NameError:
    print("The list has been removed.")

temporary_list = [True, False, {"fruit": "apple"}, (4,5)]
print(temporary_list)
temporary_list.clear()
print(temporary_list)

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print(fruits)

scores = [100, 50, 65, 82, 23]
scores.sort()
print(scores)
scores.sort(reverse = True)
print(scores)

if "banana" in cousins:
    cousins.remove("banana")

cousins.insert(0, "Shamsher")
cousins.extend(cousins2)

print(cousins)

fruit_list = ["banana", "Orange", "Kiwi", "cherry"]
fruit_list.reverse()
print(fruit_list)