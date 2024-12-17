import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    options = ["rock", "paper", "scissors"]
    
    while True:
        # User input
        user_choice = input("Enter your choice (rock, paper, scissors or 'quit' to stop): ").lower()
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        # Computer choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        print()

# Run the game
rock_paper_scissors()