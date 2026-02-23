class Students:

    def __init__(self, name, age, my_class, favourite_color, favourite_food, favourite_fruit):
        self.name = name
        self.age = age
        self.my_class = my_class
        self.favourite_color = favourite_color
        self.favourite_food = favourite_food
        self.favourite_fruit = favourite_fruit

    def my_self(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My class is {self.my_class}")
        print(f"My favourite color is {self.favourite_color}")
        print(f"My favourite food is {self.favourite_food}")
        print(f"My favourite fruit is {self.favourite_fruit}")

    def depend_on_things(self):
        if self.name == "Shaheer":
            if self.age == 9:
                if self.my_class == 3:
                    if self.favourite_color == "Yellow":
                        if "Biryani" in self.favourite_food:
                            if "Cherry" in self.favourite_fruit:
                                return self.name

student1 = Students("Shaheer", 9, 3, "Yellow", ["Daleem", "Biryani"], ["Cherry", "Strawberry"])
student2 = Students("Mustafa", 11,5, "Blue", ["Channa", "Bhindi"], ["Apple", "Banana"])
student3 = Students("Arisha", 12,6, "Red", ["Gobi", "Bhindi"], ["Cherry", "Apple"])
student4 = Students("Shaheer", 18,9, "Black", ["Bhindi", "Aloo_Matar"], ["Amrood", "Banana"])
student5 = Students("Ahmad", 5,1, "Pink", ["Channa", "Gobi"], ["Apple", "Strawberry"])


student1.my_self()
print(student1.depend_on_things())