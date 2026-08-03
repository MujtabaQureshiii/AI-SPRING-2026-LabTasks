import math

# Initialize board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
    print()

# Check winner
def check_winner(b, player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],   # rows
        [0,3,6],[1,4,7],[2,5,8],   # cols
        [0,4,8],[2,4,6]            # diagonals
    ]
    return any(all(b[i] == player for i in state) for state in win_states)

# Check draw
def is_draw(b):
    return ' ' not in b

# Minimax with Alpha-Beta Pruning
def minimax(b, depth, alpha, beta, is_max):
    if check_winner(b, 'O'):
        return 1
    if check_winner(b, 'X'):
        return -1
    if is_draw(b):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                val = minimax(b, depth+1, alpha, beta, False)
                b[i] = ' '
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                val = minimax(b, depth+1, alpha, beta, True)
                b[i] = ' '
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

# Best move for AI
def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Game loop
def play_game():
    print("You are X, Computer is O")
    print_board()

    while True:
        # Player move
        pos = int(input("Enter position (0-8): "))
        if board[pos] != ' ':
            print("Invalid move!")
            continue

        board[pos] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("Draw!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = 'O'
        print("Computer played at:", ai_move)
        print_board()

        if check_winner(board, 'O'):
            print("Computer is the winner!")
            break
        if is_draw(board):
            print("Draw!")
            break


# Run game
play_game()
