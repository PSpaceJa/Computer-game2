import random

class WordJumbleGame:
    def __init__(self):
        self.words = ["python", "programming", "computer", "jumble", "easy", "difficult"]

    def jumble_word(self, word):
        return "".join(random.sample(word, len(word)))

    def play_game(self):
        while True:
            start_game = input("Press Enter to start the game, or type 'exit' to quit: ")
            if start_game.lower() == 'exit':
                print("Game Over")
                break
            elif start_game.lower() != '':
                print("Invalid input. Press Enter to start the game, or type 'exit' to quit.")
                continue

            attempts_list = []
            while True:
                word = random.choice(self.words)
                jumbled_word = self.jumble_word(word)

                print("\nJumbled word:", jumbled_word)
                guess = input("Guess the original word: ")
                if guess.lower() == word:
                    print("Correct!")
                else:
                    print("Incorrect. The word was:", word)
                attempts_list.append(word)

                play_again = input("Play again? (y/n): ")
                if play_again.lower() != 'y':
                    print("Game Over")
                    break

def main():
    game = WordJumbleGame()
    game.play_game()

if __name__ == "__main__":
    main()

