import random


class DiceRollGame:
    """Class for the Dice Roll Game."""
    total_score = 0
    show_info = False

    def __init__(self, threshold=24, max_attempts=3):
        """Initialize the dice roll game with a threshold and maximum attempts."""
        self.threshold = threshold
        self.max_attempts = max_attempts
        self.total_score = 0

    def play_game(self):
        """Start the dice roll game."""
        print(f"Objective: Roll a pair of dice and achieve a total score of {self.threshold} or higher.")
        print(f"Rules: You have {self.max_attempts} attempts to reach a total score of {self.threshold} or higher.\n")

        for attempt in range(1, self.max_attempts + 1):
            total_score = 0  # Initialize total score for each attempt
            input("Press Enter to roll the dice...")
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total_score = dice1 + dice2
            print(f"\nAttempt {attempt}: You rolled {dice1} and {dice2}. Total score: {total_score}")
            self.total_score += total_score

            if self.total_score >= self.threshold:
                print("Congratulations! You win!")
                print()
                return True
            else:
                print("Try again...")

        print(
            f"\nSorry, you couldn't achieve a total score of {self.threshold} or higher in {self.max_attempts} attempts. You lose.")
        print()
        return False

    def die_game_manager(self):
        """Main function to initiate and manage the game."""

        print("Welcome to the Dice Roll Game!")

        while True:
            game = DiceRollGame(threshold=24, max_attempts=3)
            game.total_score = self.total_score

            if not game.play_game():
                print(f"Total score across all attempts: {game.total_score}")
                print()

                play_again = input("Do you want to play again? (yes/no): ").lower()

                # Play another dice roll game
                if play_again == 'no':
                    print()  # Add a space
                    # self.total_score = 0  # Reset total_score for new game
                    # print()

                    play_another_game = input("Do you want to play another game? (yes/no): ").lower()

                    # Play another game type in the program
                    if play_another_game == 'yes':
                        self.show_info = False
                        self.total_score = 0
                        continue
                    else:
                        print("Thanks for playing!")
                        self.show_info = True
                        break
                else:
                    self.total_score = 0

                print()
            else:
                print(f"Total score across all attempts: {game.total_score}")
                self.total_score += game.total_score

                play_another_game = input("Do you want to play another game? (yes/no): ").lower()

                if play_another_game == 'yes':
                    print()  # Add a space
                    self.total_score = 0  # Reset total_score for new game
                    continue
                else:
                    print("Thank you for playing!")
                    self.show_info = True
                    break
