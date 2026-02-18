player1 = "Shaheer"
player2 = "Arisha"
player3 = "Mustafa"
player4 = "Papa"

answers = dict(
A1 = 42,
A2 = 48,
A3 = 0,
A4 = 18,
A5 = 81,
A6 = 70,
A7 = 108,
A8 = 110,
A9 = 20,
A10 = 64
)

questions = dict(
Q1 = f"6 * 7 = ",
Q2 = f"8 * 6 = ",
Q3 = f"2 * 0 = ",
Q4 = f"9 * 2 = ",
Q5 = f"9 * 9 = ",
Q6 = f"14 * 5 = ",
Q7 = f"12 * 9 = ",
Q8 = f"11 * 10 = ",
Q9 = f"5 * 4 = ",
Q10 = f"8 * 8 = "
)

import random

players = [player1, player2, player3, player4]
scorecard = {name: 0 for name in players}

# We can use a loop to go through Q1 to Q10
for i in range(1, 11):
    q_key = f"Q{i}"
    a_key = f"A{i}"

    # Pick a random player for this turn
    current_player = random.choice(players)

    print(f"\n--- Question {i} ---")
    user_answer = int(input(f"{current_player}, what is {questions[q_key]}"))

    if user_answer == answers[a_key]:
        print("✅ Correct! Well done.")
        scorecard[current_player] += 1
    else:
        print(f"❌ Ouch! The correct answer was {answers[a_key]}.")

# Final Results
print("\n" + "=" * 20)
print("FINAL SCORES")
for player, score in scorecard.items():
    print(f"{player}: {score} points")
# for key, value in questions.items():
#     answer1 = int(input(f"What is the answer of {questions}"))
#     if answer1 == value:
#         print("Congratulations!")

# player1_game = int(input(f"This is a game {player1} ok.So,The game contains only Multiply. You will answer the questions: {Q1}, {Q2}, {Q3}, {Q4}, {Q5}, {Q6}, {Q7}, {Q8}, {Q9}, {Q10}: "))
# player2_game = int(input(f"This is a game {player2} ok.So,The game contains only Multiply. You will answer the questions: {Q1}, {Q2}, {Q3}, {Q4}, {Q5}, {Q6}, {Q7}, {Q8}, {Q9}, {Q10}."))
# player3_game = int(input(f"This is a game {player3} ok.So,The game contains only Multiply. You will answer the questions: {Q1}, {Q2}, {Q3}, {Q4}, {Q5}, {Q6}, {Q7}, {Q8}, {Q9}, {Q10}."))
# player4_game = int(input(f"This is a game {player4} ok.So,The game contains only Multiply. You will answer the questions: {Q1}, {Q2}, {Q3}, {Q4}, {Q5}, {Q6}, {Q7}, {Q8}, {Q9}, {Q10}."))

# print(player1_game)
# print(player2_game)
# print(player3_game)
# print(player4_game)

print()