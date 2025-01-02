import math

# Constants for player symbols
X = 'X'
O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == EMPTY]

def minimax(board, depth, maximizing_player, alpha, beta):
    if is_winner(board, X):
        return 10
    if is_winner(board, O):
        return -10
    if len(get_empty_cells(board)) == 0:
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for (row, col) in get_empty_cells(board):
            board[row][col] = X
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[row][col] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for (row, col) in get_empty_cells(board):
            board[row][col] = O
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[row][col] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for (row, col) in get_empty_cells(board):
        board[row][col] = X
        eval = minimax(board, 0, False, alpha, beta)
        board[row][col] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = (row, col)
    return best_move

def main():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    print("Welcome to Tic-Tac-Toe with AI (Alpha-Beta Pruning)!")
    print_board(board)

    while True:
        row, col = map(int, input("Enter your move (row and column, separated by a space): ").split())
        if board[row][col] == EMPTY:
            board[row][col] = O
            print_board(board)

            if is_winner(board, O):
                print("You win!")
                break
            if len(get_empty_cells(board)) == 0:
                print("It's a draw!")
                break

            ai_move = best_move(board)
            board[ai_move[0]][ai_move[1]] = X
            print("AI's move:")
            print_board(board)

            if is_winner(board, X):
                print("AI wins!")
                break
            if len(get_empty_cells(board)) == 0:
                print("It's a draw!")
                break
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
