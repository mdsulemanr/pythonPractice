"""returns average of input numbers,
display error message if the input is non-integer"""


def get_average():
    total = 0
    count = 0
    while True:
        try:
            inp = input('Enter a number: ')
            if inp in ['Done', 'done', 'DONE', '/n']:
                if total == 0:
                    return
                else:
                    break
            value = float(inp)
            total = total + value
            count = count + 1
            average = total / count
        except ValueError:
            print('Enter only numbers')
            continue
        except ZeroDivisionError:
            return 0
    return '{}: {}'.format('Average', average)


print(get_average())
