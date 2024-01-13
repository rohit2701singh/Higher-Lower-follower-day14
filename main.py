import random
from game_data import data

print("welcome to higher-lower game\n")


def random_selection():
    return random.choice(data)


choice1 = random_selection()
choice2 = random_selection()

score = 0
game_over = False
while not game_over:
    print(f"compare A : {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
    print("vs")
    print(f"against B : {choice2['name']}, a {choice2['description']}, from {choice2['country']}")

    user_input = input("who has more followers? Type 'A or B': ").upper()

    if (choice1["follower_count"] >= choice2["follower_count"] and user_input == "A") or (choice2["follower_count"] >= choice1["follower_count"] and user_input == "B"):
        score += 1
        print(f"you're right!.your score is {score}\n")
        choice1 = choice2
        choice2 = random_selection()
    else:
        print(f"sorry! wrong choice.your score is {score}\n{choice1['name']}'s follower: {choice1['follower_count']}\n{choice2['name']}'s follower: {choice2['follower_count']}")
        game_over = True
