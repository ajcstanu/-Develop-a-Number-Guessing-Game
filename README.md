
# Number Guessing Game

A command-based number guessing game where the player tries to guess a randomly generated number within a specified range.

## Features
- Random number generation within a customizable range
- User input validation
- Attempt tracking
- Difficulty levels (Easy, Medium, Hard)
- Helpful hints after each guess
- Play again functionality

## Requirements
- Python 3.x
- No external dependencies required

## Installation & Running
1. Save the code to a file named `number_guessing_game.py`
2. Open a terminal/command prompt
3. Navigate to the directory containing the file
4. Run the script:
   ```bash
   python number_guessing_game.py
   ```

## How to Play
1. Select a difficulty level or customize the range
2. The game will generate a random number within the selected range
3. Enter your guess when prompted
4. Receive feedback if your guess is too high or too low
5. Continue guessing until you find the correct number
6. The game will display the number of attempts it took you to guess correctly
7. Choose to play again or exit

## Example Gameplay
```
Welcome to the Number Guessing Game!
Select difficulty:
1. Easy (1-50)
2. Medium (1-100)
3. Hard (1-200)
4. Custom range
Enter your choice (1-4): 2

I'm thinking of a number between 1 and 100.
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Too high! Try again.
Enter your guess: 31
Congratulations! You guessed the number in 4 attempts!

Would you like to play again? (yes/no): no
Thanks for playing!
```

## Key Features Explained
1. **Difficulty Levels**:
   - Easy: Numbers between 1-50
   - Medium: Numbers between 1-100
   - Hard: Numbers between 1-200
   - Custom: User-defined range

2. **Input Validation**:
   - Ensures the user enters valid numbers
   - Checks that guesses are within the specified range
   - Validates difficulty selection

3. **Game Mechanics**:
   - Generates a random number within the selected range
   - Provides feedback after each guess (too high/too low)
   - Tracks the number of attempts
   - Allows multiple rounds of play

4. **User Experience**:
   - Clear instructions and prompts
   - Helpful error messages
   - Option to play again or exit

## Future Enhancements
- Add a timer to track how long it takes to guess
- Implement a scoring system based on difficulty and attempts
- Add a "hint" feature that reveals a digit of the number
- Create a high score leaderboard
- Add a graphical user interface (GUI)
- Implement multiplayer mode

