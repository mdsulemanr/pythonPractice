class NameChecker:
    def __init__(self):
        self.name = ""

    def name_checker(self):
        while True:
            try:
                checking = input("What is your name")
            except ValueError:
                print("Enter Only Alphabets Of Your Name.")