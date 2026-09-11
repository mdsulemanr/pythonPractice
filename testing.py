import random

def get_players():
    players = input('Please enter players name comma separated: ').strip().split(',')
    return players

players = get_players()
print(players)
random.shuffle(players)
winners = []
secret_number = round(random.random() * 10)

print('Lets play a game, all the players will be provided with three tries to guess the secret number '
      'between 0 to 10 inclusive.\n')

for player in players:
    selected_numbers = []
    player = player.capitalize()
    print(f'{player}, are you ready!! your turn:')
    for i in range(1, 4):
        while True:
            try:
                num = int(input(f'Try {i}, enter the number: '))
                if -1 < num < 11:
                    if num not in selected_numbers:
                        selected_numbers.append(num)
                    else:
                        print(f'You already selected this {num}, please try a different one this time')
                        continue
                else:
                    print('Your selected number is out of range.')
                    continue
                break
            except ValueError:
                print('Please select integer between 0 to 10 inclusive.')
        if num == secret_number:
            winners.append(player)

print(secret_number)
if not winners:
    print('Alas!! No one won..')
else:
    print(f'Winners are {winners}')