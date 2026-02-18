paragraph = "Apple, Banana, Cherry, Orange, Pineapple"
print(paragraph)
result = paragraph.split(", ")
print(result)
new_paragraph = ", ".join(result)
print(new_paragraph)
print(type(new_paragraph))

txt = "Name is a Good boy! One of the intelligent Student in Class number."

shaheer_txt = txt.replace("Name", "Shaheer").replace("number", "three")
mustafa_txt = txt.replace("Name", "Mustafa").replace("number", "five")
arisha_txt = txt.replace("Name", "Arisha").replace("number", "six").replace("boy", "girl")

print(shaheer_txt)
print(mustafa_txt)
print(arisha_txt)