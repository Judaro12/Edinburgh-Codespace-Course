# import ramdon library
import random

#variables for player and computer
choices = ['r', 'p', 's']
score_player = 0
score_computer = 0

#funtion to get the input choice
def get_choice():
    choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ").lower()
    while choice not in choices: # checking if the inout is correct
        print("Invalid choice. Please try again.")
        choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ").lower()
    return choice
#function to get the winner
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == 'r' and computer_choice == 's') or
        (player_choice == 'p' and computer_choice == 'r') or
        (player_choice == 's' and computer_choice == 'p')
    ):
        return "player"
    else:
        return "computer"

def print_result(player_choice, computer_choice, winner):
    choices_names = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    print(f"You chose {choices_names[player_choice]}, the computer chose {choices_names[computer_choice]}.")
    if winner == "player":
        print(f"{choices_names[player_choice]} beats {choices_names[computer_choice]}! You win.")
    elif winner == "computer":
        print(f"{choices_names[computer_choice]} beats {choices_names[player_choice]}! You lose.")
    else:
        print("Both players selected", choices_names[player_choice] + ". It's a tie!")

def play_again():
    return input("Play again? (y/n): ").lower() == 'y'

# Main rock paper scissor loop
while True:
    player_choice = get_choice()
    computer_choice = random.choice(choices)

    winner = get_winner(player_choice, computer_choice)
    print_result(player_choice, computer_choice, winner)

    if winner == "player":
        score_player += 1
    elif winner == "computer":
        score_computer += 1

    if not play_again():
        break

# Print final scores
print("Final Scores:")
print("Computer:", score_computer)
print("Player:", score_player)


