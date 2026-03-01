class Marks:
    def __init__(self):
        self.marks = 0

    def take_marks(self):
        while True:
            try:
                value = float(input('Please enter your marks between 0 to 100: '))

                if 0 <= value <= 100:
                    self.marks = value
                    break
                else:
                    print('Enter between 0 to 100 only')

            except ValueError:
                print('Invalid input! only digits are allowed.')

    def marks_checker(self):
        while True:

            self.take_marks()
            if self.marks <= 20:
                print("Oops, You are failed!😢 I will tell your 'Mom and Dad'!")
            elif self.marks <= 40:
                print("Oh, So you passed!🙂 but you need to work hard!")
            elif self.marks <= 60:
                print("Wow! You passed with good marks!😀")
            elif self.marks <= 80:
                print("Very very good!😃 You passed with very good marks!")
            else:
                print("Excellent! You are a Shining Star!🌟 Your passed with first position!")

            again = input('Do you want to continue? press yes: ').lower()
            if again in ['yes', 'y']:
                print('Hurry! lets play it again... 🌟')
                continue
            else:
                print('Good bye!')
                break

marks = Marks()
marks.marks_checker()