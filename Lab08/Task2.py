import numpy as np
import math

ROW_COUNT = 6
COL_COUNT = 7

# Create board
def create_board():
    return np.zeros((ROW_COUNT, COL_COUNT))

# Drop piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Check valid location
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

# Get next open row
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# Print board
def print_board(board):
    print(np.flip(board, 0))

# Check winning move
def winning_move(board, piece):
    # Horizontal
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    # Vertical
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # Positive diagonal
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Negative diagonal
    for c in range(COL_COUNT-3):
        for r in range(3, ROW_COUNT):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

# Get valid locations
def get_valid_locations(board):
    return [c for c in range(COL_COUNT) if is_valid_location(board, c)]

# Simple evaluation function
def evaluate_window(window, piece):
    score = 0
    opp = 1 if piece == 2 else 2

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp) == 3 and window.count(0) == 1:
        score -= 4

    return score

# Score position
def score_position(board, piece):
    score = 0

    # Center column preference
    center_array = list(board[:, COL_COUNT//2])
    score += center_array.count(piece) * 3

    # Horizontal
    for r in range(ROW_COUNT):
        row_array = list(board[r,:])
        for c in range(COL_COUNT-3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Vertical
    for c in range(COL_COUNT):
        col_array = list(board[:,c])
        for r in range(ROW_COUNT-3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    return score

# Check terminal node
def is_terminal(board):
    return winning_move(board, 1) or winning_move(board, 2) or len(get_valid_locations(board)) == 0

# Minimax with Alpha-Beta
def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    terminal = is_terminal(board)

    if depth == 0 or terminal:
        if terminal:
            if winning_move(board, 2):
                return (None, 1000000000)
            elif winning_move(board, 1):
                return (None, -1000000000)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, 2))

    if maximizingPlayer:
        value = -math.inf
        best_col = valid_locations[0]
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp = board.copy()
            drop_piece(temp, row, col, 2)
            new_score = minimax(temp, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value

    else:
        value = math.inf
        best_col = valid_locations[0]
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp = board.copy()
            drop_piece(temp, row, col, 1)
            new_score = minimax(temp, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value


# Game loop
def play():
    board = create_board()
    print_board(board)

    while True:
        # Player move
        col = int(input("Enter column (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print_board(board)
                print("You win!")
                break

        print_board(board)

        # AI move
        col, _ = minimax(board, 4, -math.inf, math.inf, True)
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, 2)

        if winning_move(board, 2):
            print_board(board)
            print("Computer is the winner!")
            break

        print_board(board)


play()
