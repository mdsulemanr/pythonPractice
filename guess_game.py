import random

secret_num = round(random.random() * 10, 0)

players = ['Arisha', 'Mustafa', 'Shaheer', 'Suleman']
random.shuffle(players)
winners = []

for player in players:
    print(f'{player}! its your turn.')

    for attempt in range(1, 4):
        try:
            num = int(input(f'Attempt: {attempt}, guess the number: '))
            if num == secret_num:
                winners.append(player)
            if attempt == 3:
                print('Your turn is over.')
        except ValueError:
            print('Please enter only integer.')

print(f'The secret number was {secret_num}')

if winners == []:
    print('Oops, looks like no one win.')
else:
    print(f'winners are {winners}')
