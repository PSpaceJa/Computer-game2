#User. (2023, January 19). What constitutes the end of a Tic Tac Toe game? [Closed question]. BoardGames Stack Exchange. https://boardgames.stackexchange.com/questions/58437/what-constitutes-the-end-of-a-tic-tac-toe-game

import statistics

# Function to calculate mean, median, and mode of a dataset
def calculate_stats(data):
    mean = sum(data) / len(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    return mean, median, mode

# Function to display the Tic Tac Toe board
def display_board():
    global board
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---------")

# Function to check if a player has won
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Main game loop
def play_game():
    # Ask users to enter their names
    x_name = input("Player X, enter your name: ")
    o_name = input("Player O, enter your name: ")

    # Ask users to enter some random numbers to find the mean, median, and mode
    data = list(map(float, input(f"{x_name} and {o_name}, enter some random numbers separated by space: ").split()))

    # Calculate the mean, median, and mode of the dataset
    mean, median, mode = calculate_stats(data)
    print("Stats:")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

    # Initialize the Tic Tac Toe board and the scores
    global board
    board = [' '] * 9
    x_wins = 0
    o_wins = 0

    # Game loop
    current_player = 'X'
    while True:
        display_board()

        # Player's move
        position = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = current_player
            if check_win(current_player):
                display_board()
                if current_player == 'X':
                    x_wins += 1
                    print(f"{x_name} wins!")
                else:
                    o_wins += 1
                    print(f"{o_name} wins!")
                break
            elif ' ' not in board:
                display_board()
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already taken. Try again.")

    # Display the scores
    print(f"{x_name}'s score: {x_wins}")
    print(f"{o_name}'s score: {o_wins}")

    # Ask if players want to play another round
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()

# Call the main function to start the game
play_game()


