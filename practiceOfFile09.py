

def marks_checker(marks):

    if  marks <= 25 :
        return 'OMG! You failed.'
    elif marks <= 50:
        return 'You passed this time , but you need to work hard'
    elif marks <= 70:
        return 'You doing great. Keep it up.'
    elif marks <= 90:
        return 'You are an  very ordinary student'
    else:
        return 'You are a shining star!'

def try_enteringMarks():
    while True:
        try:
            marks = int(input('Please enter your marks!:'))
            if   marks < 0 or marks > 100 :
                print('Please enter marks between 0 and 100 ')
                continue
            return marks
        except ValueError:
            print('Warning!!!\nPLease enter correct marks!: ')


marks = try_enteringMarks()
print(marks)

print(marks_checker(marks))