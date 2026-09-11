class ThreeStudents:

    def __init__(self, name, age, my_class, section, favourite_food, favourite_fruit, favourite_colour):
        self.name = name
        self.age = age
        self.my_class = my_class
        self.section = section
        self.favourite_food = favourite_food
        self.favourite_fruit = favourite_fruit
        self.favourite_colour = favourite_colour

    def student_data(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My my class is {self.my_class}")
        print(f"My section is {self.section}")
        print(f"My favourite food is {self.favourite_food}")
        print(f"My favourite fruit is {self.favourite_fruit}")
        print(f"My favourite colour is {self.favourite_colour}")


stu_1 = ThreeStudents("Shaheer", 10, 4, "Green", "Biryani", "Cherry", "Yellow")
stu_2 = ThreeStudents("Arisha", 13, 7, "Yellow", "Palao", "Guava", "Black")
stu_3 = ThreeStudents("Mustafa", 12, 6, "Blue", "Bhindi", "Mango", "Blue")

stu_1.student_data()
stu_2.student_data()
stu_3.student_data()