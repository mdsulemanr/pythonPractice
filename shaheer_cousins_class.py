

class Cousins:
    def __init__(self, name, age, my_class, favourite_game):
        self.name = name
        self.age = age
        self.my_class = my_class
        self.favourite_game = favourite_game

    names = ["Shaheer", "Mustafa", "Arisha", "Ahmad"]
    ages = [4, 7, 5, 9, 12, 11]
    classes = [4, 7, 5, None]
    favourite_games = ["Cricket", "Foot ball", "Badminton", "Run Catch"]

    def depend_on_your_things(self):
        if self.name in self.names:
            if self.age in self.ages:
                if self.my_class in self.classes:
                    if self.favourite_game in self.favourite_games:
                        print(self.name)

cousin1 = Cousins("Shaheer", 9, 4, "Foot ball")
cousin2 = Cousins("Arisha", 12, 7, "Badminton")
cousin3 = Cousins("Mustafa", 11, 5, "Cricket")
cousin4 = Cousins("Hazik", 14, 8, "Ice Water")
cousin5 = Cousins("Zaryab", 11, 7, "Run Catch")
cousin6 = Cousins("Sarim", 10, 4, "Indoor Games")
cousin7 = Cousins("Ahmer", 8, 2, "Bird Fly")
cousin8 = Cousins("Asher", 6, 1, "Red Hands")
cousin9 = Cousins("Umer", 10, 4, "Outdoor Games")
cousin10 = Cousins("Hassan", 7, 1, "Yasso Pango")
cousin11 = Cousins("Ahmad", 5, None, "Koi Bhi Game! Kuch Bhi! Kuch Bhi!")
cousin12 = Cousins("Abdullah", 10, 4, "Stacho Game")
cousin13 = Cousins("Anas", 6, 1, "Laughing Game")

cousin1.depend_on_your_things()
cousin2.depend_on_your_things()
cousin3.depend_on_your_things()
cousin4.depend_on_your_things()
cousin5.depend_on_your_things()
cousin6.depend_on_your_things()
cousin7.depend_on_your_things()
cousin8.depend_on_your_things()
cousin9.depend_on_your_things()
cousin10.depend_on_your_things()
cousin11.depend_on_your_things()
cousin12.depend_on_your_things()
cousin13.depend_on_your_things()