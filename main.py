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
game_on = True
while game_on:
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

    # Get user and computer choices index in game elements:
    user_index = game_elements.index(user_choice)
    computer_index = game_elements.index(computer_choice)

    # Turn User and computer choices to Symbols:
    user_symbol = symbol[user_index]
    computer_symbol = symbol[computer_index]

    # Game Logic:
    #Draw
    if user_choice == computer_choice:
        print(f"\nYour choose: \n{user_symbol} \nComputer choose: \n{computer_symbol}")
        print(f"It's a Draw")

    # User Win:
    elif ( (user_choice == "rock" and computer_choice == "scissors") or
           (user_choice == "paper" and computer_choice == "rock")    or
           (user_choice == "scissors" and computer_choice == "paper") ):

        print(f"\nYour choose: \n{user_symbol} \nComputer choose: \n{computer_symbol}")
        print(f"You Win, {user_choice} beat {computer_choice}")

    # User Lost:
    else:
        print(f"\nYour choose: \n{user_symbol} \nComputer choose: \n{computer_symbol}")
        print(f"You Lose, {computer_choice} beat {user_choice}")

    if input("Do you want to play again (Y/N): ").lower() != "y":
        print("Bye Bye...")
        game_on = False
    else:
        pass
