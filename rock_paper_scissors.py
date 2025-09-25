import random
from colorama import Fore, Style

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_score = 0
computer_score = 0

while True:
    player_move = input("Choose [r]ock, [p]aper or [s]scissor: ").lower()

    if player_move == ["r", "rock"]:
        player_move = rock

    elif player_move == ["p", "paper"]:
        player_move = paper

    elif player_move == ["s", "scissors"]:
        player_move = scissors

    else:
        print("Invalid Input. Try again...")
        continue

    print(f"The player chose {player_move}.")

    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock

    elif computer_random_number == 2:
        computer_move = paper

    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) \
        or (player_move == paper and computer_move == rock) \
        or (player_move == scissors and computer_move == paper):
        print(Fore.GREEN + "You win!")
        player_score += 1

    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")

    else:
        print(Fore.RED + "You lose!")
        computer_score += 1

    print(Style.RESET_ALL)

    print(f"Current result is player: {player_score}, computer: {computer_score}")

    while True:
        play_again = input(f"Type [y] for 'yes' to Play Again or [n] for 'no' to quit: ").lower()

        if play_again == "y":
            print("Let's pick rock, paper or scissors")
            break

        elif play_again == "n":
            print("Thank you for playing!")
            exit()

        else:
            print("Invalid Input! Please type [y] or [n]... ")
            continue
