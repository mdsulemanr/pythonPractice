class UserInput:
    def __init__(self):
        print("This is a simple 'User Input'.")
        self.num = 12
        self.start = 1
        self.end = 11
        self.decoration = " < ^ ! * ! ^ > "

    def ask_input(self, message):
        while True:
            try:
                integer = int(input(message))
                break
            except ValueError:
                print("Invalid Input! Please enter the Whole numbers only because I am writing a table of your entered number!")
        return integer

    def take_user_input(self):
            self.num = self.ask_input("Enter a number for table: ")
            self.start = self.ask_input("Where to start the table: ")
            self.end = self.ask_input("Where to end the table: ")

            if self.start > self.end:
                print("End was smaller than start, so I swapped them. 🙂")
                self.start, self.end = self.end, self.start
                print(f'Now the updated start number is: {self.start} and the updated end number is: {self.end}')


    def table(self):
        self.decoration = " < ^ ! * ! ^ > " * 5
        print(f"{self.decoration} This is your favourite number table {self.decoration}")
        for abc in range(self.start, self.end+1):
            print(f"{self.num} * {abc} = {self.num * abc}")

user_input = UserInput()
user_input.take_user_input()
user_input.table()