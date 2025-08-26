import random
import sys

def get_difficulty():
    """Get difficulty level from user and set the range accordingly."""
    print("\nSelect difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    print("4. Custom range")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                return 1, 50
            elif choice == 2:
                return 1, 100
            elif choice == 3:
                return 1, 200
            elif choice == 4:
                min_num = int(input("Enter minimum number: "))
                max_num = int(input("Enter maximum number: "))
                if min_num >= max_num:
                    print("Maximum must be greater than minimum. Try again.")
                    continue
                return min_num, max_num
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

def get_user_guess(min_num, max_num):
    """Get and validate user's guess."""
    while True:
        try:
            guess = int(input(f"Enter your guess ({min_num}-{max_num}): "))
            if min_num <= guess <= max_num:
                return guess
            else:
                print(f"Please enter a number between {min_num} and {max_num}.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    """Main game function."""
    print("Welcome to the Number Guessing Game!")
    
    while True:
        min_num, max_num = get_difficulty()
        secret_number = random.randint(min_num, max_num)
        attempts = 0
        
        print(f"\nI'm thinking of a number between {min_num} and {max_num}.")
        
        while True:
            attempts += 1
            guess = get_user_guess(min_num, max_num)
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        
        # Ask if the user wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
