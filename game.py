from pickle import NONE
import random
while True:
    pick = ["rock", "scissors", "paper"]
    computer = random.choice(pick)
    player = None
    while player not in pick:
        player = input("rock, paper, or scissors: ").lower()
        if player not in pick:
            print("invalid selection pick again")
    if player == computer:
        print("computer: ", computer)
        print("player:", player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("You lose try again")
        if computer == "scissors":
            print("computer:", computer)
            print("player:", player)
            print("You Win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("You lose try again")
        if computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer:", computer)
            print("player:", player)
            print("You lose try again")
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("You win!")
    Try_again = input("Try again (yes or no): ").lower()
    if Try_again != "yes":
        break
print("ok bye!")
