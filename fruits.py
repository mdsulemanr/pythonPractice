import re

class Fruits:

    def __int__(self, fruits):
        self.fruits = self._normalize(fruits)


    def __init__(self, fruits):
        self.fruits = self._normalize(fruits)

    def _normalize(self, fruits):
        if isinstance(fruits, list):
            return fruits
        if isinstance(fruits, str):
            parts = re.split(r"[,|;]+", fruits)
            return [item.strip() for item in parts if item.strip()]

        return []


    def all_fruits(self):
        return self.fruits

    def all_lower(self):
        return [fruit for fruit in self.fruits if isinstance(fruit, str) and fruit.islower()]

    def all_upper(self):
        return [fruit for fruit in self.fruits if isinstance(fruit, str) and fruit.isupper()]


fruit_list = ["dates", "Apple", "mango", (1, 2), "BANANA", 3, "Orange", "CHERRY"]
fruit_string = "Apple, mango, BANANA, Orange; date | GRAPES"

list_of_fruits = Fruits(fruit_list)
print(list_of_fruits.all_fruits())
print(list_of_fruits.all_lower())
print(list_of_fruits.all_upper())

string_of_fruits = Fruits(fruit_string)
print(string_of_fruits.all_fruits())
print(string_of_fruits.all_lower())
print(string_of_fruits.all_upper())

