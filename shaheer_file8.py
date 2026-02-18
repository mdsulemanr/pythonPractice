me_my_sister_my_cousons = ["Shaheer", "Mustafa", "Arisha", "Hazik", "Zaryab", "Sarim", "Umer", "Abdullah", "Ahmar",
"Hassan", "Anas", "Asher", "Ahmad", "4", " "]

def count_name(str):
    result = me_my_sister_my_cousons.count("Shaheer")
    return result

print(count_name(me_my_sister_my_cousons))

text = "Hello! how are you?"

def is_lower(text):
    result = []
    for element in text:
        result.append(element.islower())
    return result

print(is_lower(text))

print(count_name(me_my_sister_my_cousons))

for element in me_my_sister_my_cousons:
    if element == "Shaheer":
        print(f"{element} is a Good boy.")
    elif element == "Arisha":
        print(f"{element} is my sister")
    elif element == "4" or element == " ":
        print("this is not my cousin, ignore it")
    else: print(f"{element} is my cousin")