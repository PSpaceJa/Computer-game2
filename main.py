import random
from diegame import DiceRollGame
from Cointossgame import CoinTossGame


class Main:
    show_info = False
    total_score = 0
    amount_of_games = 0

    play_game = True

    def play(self):
        """Main function to initiate and manage the game."""

        specific_number = random.randint(1, 100)  # Generate a random specific number

        while self.play_game:
            if self.show_info:
                if self.amount_of_games > 1:
                    # TODO: Show game stats
                    print()
                    print(f"Total game score is: {self.total_score}")
                    self.play_game = False
                    break
                else:
                    quit()
            else:
                print("\nWelcome to Game Arcade!")
                print()
                print("1. Dice Roll Game")
                print("2. Coin Toss Game")
                print("3. Word Jumble Game")
                print("4. Quit")
                choice = input("Choose a game to play (1-4): ")

                if choice == '1':
                    self.amount_of_games += 1

                    game = DiceRollGame()
                    game.die_game_manager()

                    self.total_score += game.total_score
                    self.show_info = game.show_info
                elif choice == '2':
                    self.amount_of_games += 1

                    game = CoinTossGame()
                    game.coin_toss_manager()

                    # TODO: Do the same like at lines 39 and 40
                elif choice == '3':
                    pass
                elif choice == '4':
                    print(f"Your total score across all games: {self.total_score}")
                    break
                else:
                    print("Invalid choice. Please choose again.")
                    continue


if __name__ == "__main__":
    Main().play()
