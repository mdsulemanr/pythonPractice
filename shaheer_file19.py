import random

players = ["Shaheer", "Papa", "Arisha", "Mustafa"]

shaheer_secret_num = int(input(f"{players[0]} Select your number between 0 to 10: "))
papa_secret_num = int(input(f"{players[1]} Select your number between 0 to 10: "))
arisha_secret_num = int(input(f"{players[2]} Select your number between 0 to 10: "))
mustafa_secret_num = int(input(f"{players[3]} Select your number between 0 to 10: "))

for i in range(4):
    result = random.randrange(0, 11)
    print(result)
    if result == shaheer_secret_num:
        print(f"Congratulations! You won {players}!")
        break
    elif result == papa_secret_num:
        print(f"Congratulations! You won {players}!")
        break
    elif result == arisha_secret_num:
        print(f"Congratulations! You won {players}!")
        break
    elif result == mustafa_secret_num:
        print(f"Congratulations! You won {players}!")
        break