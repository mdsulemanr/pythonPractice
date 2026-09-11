# Functions

# def find_friend(my_friends):
#
#     if 'Arisha' in my_friends:
#         print('Yes I found her!')
#     else:
#         print('Oops!')
#
# school_friend = ['Arooj', 'Alpha', 'Beeta', 'Gama']
# college_friends = ['Fatima', 'Zainab']
#
# find_friend(school_friend)
# find_friend(college_friends)

# def analyze_str(str):
#     if str.isupper():
#         return 'Provided string is Upper Case.'
#     elif str.islower():
#         return
#
# print(analyze_str('ABCD'))

# def check_str(str):
#     if str.isupper():
#         return'Yeah, maybe you are true'
#     if str.islower():
#         return 'str is lower'
#
# print(check_str('CHUP HO JA'))


# def age_checker(age):
#     if age < 18:
#         print('Hey, you cant drive a car!')
#     elif age >= 18:
#          print('Hmm , maybe you can drive a car.')
# age= 13
# print(age_checker(age))


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

def take_marks():
    while True:
        try:
            marks = int(input('Please enter your marks here: '))
            if marks < 0 or marks > 100:
                print('Please enter marks between 0 and 100 only')
                continue
            return marks
        except ValueError:
            print('WARNING!!!\nPlease enter only valid integer as your marks: ')

marks = take_marks()
print(marks)

print(marks_checker(marks))