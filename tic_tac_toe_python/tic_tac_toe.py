def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_valid_input(num):
    return num in ['1', '2', '3']

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    print_board(board)

    while True:
        row = input("Enter the row number (1, 2, or 3): ")
        col = input("Enter the column number (1, 2, or 3): ")

        if not (is_valid_input(row) and is_valid_input(col)):
            print("Invalid input. Please enter 1, 2, or 3.")
            continue

        row = int(row)
        col = int(col)

        if board[row - 1][col - 1] == ' ':
            board[row - 1][col - 1] = player
        else:
            print("This cell is already occupied. Please try again.")
            continue

        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

if __name__ == "__main__":
    main()