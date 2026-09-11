import random

winners = []
players = ["Shaheer", "Arisha", "Mustafa", "Suleman"]
secret_number = round(random.random() * 11)

print("This is a guess game. In this game there is a random secret number. And you will guess it between 1 to 10.")
print("Ok lets play it.")

for player in players:
    print(f"{player} it is your turn.")
    for tries in range(1, len(players)):
        while True:
            try:
                input_taker = int(input(f"Try {tries}"))
            except ValueError:
                print("Invalid input! Enter only numbers!")