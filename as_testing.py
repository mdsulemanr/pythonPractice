import random

def getting_players():
    players = input('PLease enter your names comma seperated: ').strip().split(',')
    return players

players = getting_players()
print(players)
random.shuffle(players)
winners = []
secret_num = round(random.random() * 10)

print('Lets play a game in which you all  will have to guess a number and lets see who among you will win!')

for players in players:
    players = players.capitalize()
print(f'{players}, are you ready!! your turn:')
selected_num = []
for tries in range(1,4):
    while True:
        try:
            num = int(input(f'It is your {tries} turn,please enter your number!: '))
            if -1 > num < 11:
                print('Please enter a number between 0 and 10 ')
                if num != selected_num:
                    selected_num.append(num)
                else:
                    print(f'You already entered this {selected_num} , please enter another num!: ')
                    continue
                break
        except ValueError:
            print('Please enter a number')
    if num == secret_num:
        winners.append(players)
    tries = tries + 1
print(secret_num)
if not winners:
    print('OMG , looks like no one won!')
else:
    print(f'winner are {players}')


