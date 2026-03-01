class UserInput:
    def __init__(self):
        print("This is a simple 'User Input'.")
        self.num = 0
        self.start = 0
        self.end = 0
        self.decoration = "* < ! > * " * 5

    def take_user_input(self):
        while True:
            try:
                self.num = int(input("I am writing a table of your number. So, Please enter a number: "))
                self.start = int(input("Where to start the table: "))
                self.end = int(input("Where to end the table: "))

                if self.start > self.end:
                    print("Your start number is greater than end number, so I swapped it for you.")
                    self.start, self.end = self.end, self.start
                    print(f'Now the updated start number is: {self.start} and the updated end number is: {self.end}')

                break
            except ValueError:
                print("Invalid Input! Please enter the Whole numbers only because I am writing a table of your entered number!")

    def table(self):
        print(f"{self.decoration} This is your favourite number table {self.decoration}")
        for abc in range(self.start, self.end + 1):
            print(f"{self.num} * {abc} = {self.num * abc}")

user_input = UserInput()
user_input.take_user_input()
user_input.table()