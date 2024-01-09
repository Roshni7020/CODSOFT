import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return f"You win! {user_choice} beats {computer_choice}."
    else:
        return f"You lose! {computer_choice} beats {user_choice}."

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing. Exiting the game.")
        break