import random

secret_number = round(random.random() * 11)
players = ["Shaheer", "Mustafa", "Arisha", "Suleman"]
winners = []

print("This is a guess game. In this game there is a random secret number. And you will guess it between 1 to 10.")
print("Ok lets play it!")

for player in players:
    print(f"{player} It Is Your Turn.")
    for tries in range(1, len(players)):
        while True:
            try:
                num = int(input(f"Try {tries}: "))
                if num == secret_number:
                    winners.append(player)
                break
            except ValueError:
                print("Invalid Input! Enter Only Numbers!")

print(f'The secret number was: {secret_number}')
if winners != []:
    print(f'The winner is {winners}')
else:
    print('No one guessed...')