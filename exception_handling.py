def counting():
    while True:
        try:
            n = int(input('Enter a number to start counting: '))
            limit = int(input('Please define the limit you want to count: '))
            break
        except:
            print('you must enter an integer')

    if n > limit:
        print('limit must be greater than number')
        counting()
    else:
        for num in range(n, limit+1):
            print(num)
        # while True:
        #     print(n)
        #     n += 1
        #     if n == limit + 1:
        #         break


counting()
