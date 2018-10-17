def counting():
    while True:
        try:
            n = int(input('Enter a number: '))
            limit = int(input('Please define max number to print: '))
            break
        except:
            print('you must enter an integer')


    if n > limit:
        print('limit must be greater than number')
        counting()
    else:
        while True:
            print(n)
            n += 1
            if n == limit + 1:
                break
counting()