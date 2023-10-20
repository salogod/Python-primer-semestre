import random

def initialize_board(rows, columns):
    # Create a list with pairs of token values
    tokens = [str(i) for i in range(1, (rows * columns // 2) + 1)]
    tokens *= 2
    random.shuffle(tokens)

    # Create the initial game board with tokens
    board = [[' ' for _ in range(columns)] for _ in range(rows)]
    for row in range(rows):
        for col in range(columns):
            board[row][col] = tokens.pop()

    return board

def display_board(board):
    rows = len(board)
    columns = len(board[0])

    # Display the board with row and column numbers
    print("   ", end="")
    for col in range(columns):
        print(f" {col}  ", end="")
    print()

    for row in range(rows):
        print(f"{row} ", end="")
        for col in range(columns):
            print(f"[{board[row][col] if board[row][col] != ' ' else '-'}]", end="")
        print()

def is_valid_input(input_str, board):
    try:
        row, col = map(int, input_str.split())
        rows = len(board)
        columns = len(board[0])

        # Check if the input is within the matrix range
        if 0 <= row < rows and 0 <= col < columns:
            # Check if the selected cell is not empty and is free
            return board[row][col] != ' ' and is_free(board, row, col)
    except ValueError:
        pass

    return False

def is_free(board, row, col):
    # A cell is free if it doesn't have tokens to its left or right
    if col > 0 and board[row][col - 1] != ' ':
        return False
    if col < len(board[0]) - 1 and board[row][col + 1] != ' ':
        return False

    return True

def eliminate_tokens(board, row1, col1, row2, col2):
    if board[row1][col1] == board[row2][col2]:
        # Tokens are equal, eliminate them by setting cells to ' '
        board[row1][col1] = ' '
        board[row2][col2] = ' '
        return True
    return False

def play_game():
    rows, columns = 4, 5
    board = initialize_board(rows, columns)
    tokens_left = rows * columns

    while tokens_left > 0:
        display_board(board)
        print(f"Tokens left: {tokens_left}")
        
        while True:
            input_str = input("Enter row and column (e.g., '0 0'): ")
            if is_valid_input(input_str, board):
                break
            print("Invalid input. Try again.")

        row1, col1 = map(int, input_str.split())
        board[row1][col1] = str(board[row1][col1])

        display_board(board)

        while True:
            input_str = input("Enter another row and column: ")
            if is_valid_input(input_str, board):
                break
            print("Invalid input. Try again.")

        row2, col2 = map(int, input_str.split())
        board[row2][col2] = str(board[row2][col2])

        if eliminate_tokens(board, row1, col1, row2, col2):
            tokens_left -= 2

    display_board(board)
    print("You won!")

if __name__ == "__main__":
    print("Welcome to the Memory Game!")
    play_game()
