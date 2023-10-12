import random

while True:
    user_choice = input("Press 0 for Rock, 1 for Paper, or 2 for Scissors: ")
    
    if user_choice not in ["0", "1", "2"]:
        print("Invalid choice. Please choose 0, 1, or 2.")
        continue

    user_choice = int(user_choice)
    computer_choice = random.randint(0, 2)
    
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
        print("Computer wins!")
    else:
        print("You win!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        break