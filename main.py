import other
import random
print(other.logo)
print("*** Welcome to Rock, Paper, Scissors game ***")
need_help = input("Press Enter to continue or type (H) for the rules: ").lower()
if need_help == "h":
    print(other.rules)
else:
    pass

game_elements = ["rock", "paper", "scissors"]
symbol = [other.rock, other. paper, other.scissors]

while True:
    user_choice = input("Enter your choice (Rock (R) 🧱, Paper (P) 📄, Scissors (S) ✂): ").lower()
    if user_choice == "r":
        user_choice = "rock"
        break
    elif user_choice == "p":
        user_choice = "paper"
        break
    elif user_choice == "s":
        user_choice = "scissors"
        break
    else:
        print("Invalid input, Try again")
computer_choice = random.choice(game_elements)

user_index = game_elements.index(user_choice)
computer_index = game_elements.index(computer_choice)




