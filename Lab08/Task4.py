import math
import copy

# Initial board: [AI side | Player side]
# Each side has 6 pits + 1 store
def create_board():
    return {
        "player": [4, 4, 4, 4, 4, 4],
        "ai": [4, 4, 4, 4, 4, 4],
        "player_store": 0,
        "ai_store": 0
    }

# Print board
def print_board(board):
    print("\nAI side:", list(reversed(board["ai"])))
    print("AI Store:", board["ai_store"])
    print("--------------------------")
    print("Player side:", board["player"])
    print("Player Store:", board["player_store"])
    print()

# Check game end
def is_terminal(board):
    return all(p == 0 for p in board["player"]) or all(p == 0 for p in board["ai"])

# Evaluate board
def evaluate(board):
    return board["ai_store"] - board["player_store"]

# Make move (simplified)
def make_move(board, pit, player):
    new_board = copy.deepcopy(board)
    
    if player == "player":
        stones = new_board["player"][pit]
        new_board["player"][pit] = 0
        idx = pit

        while stones > 0:
            idx += 1
            if idx < 6:
                new_board["player"][idx] += 1
            else:
                new_board["player_store"] += 1
                idx = -1
            stones -= 1

    else:  # AI
        stones = new_board["ai"][pit]
        new_board["ai"][pit] = 0
        idx = pit

        while stones > 0:
            idx += 1
            if idx < 6:
                new_board["ai"][idx] += 1
            else:
                new_board["ai_store"] += 1
                idx = -1
            stones -= 1

    return new_board

# Get valid moves
def get_moves(board, player):
    if player == "player":
        return [i for i in range(6) if board["player"][i] > 0]
    else:
        return [i for i in range(6) if board["ai"][i] > 0]

# Minimax
def minimax(board, depth, is_max):
    if depth == 0 or is_terminal(board):
        return evaluate(board)

    if is_max:
        best = -math.inf
        for move in get_moves(board, "ai"):
            new_board = make_move(board, move, "ai")
            best = max(best, minimax(new_board, depth-1, False))
        return best
    else:
        best = math.inf
        for move in get_moves(board, "player"):
            new_board = make_move(board, move, "player")
            best = min(best, minimax(new_board, depth-1, True))
        return best

# Best move for AI
def best_move(board):
    best_val = -math.inf
    move_choice = 0

    for move in get_moves(board, "ai"):
        new_board = make_move(board, move, "ai")
        move_val = minimax(new_board, 3, False)

        if move_val > best_val:
            best_val = move_val
            move_choice = move

    return move_choice

# Game loop
def play():
    board = create_board()

    while not is_terminal(board):
        print_board(board)

        # Player move
        while True:
            try:
                move = int(input("Choose pit (0-5): "))
                if move not in range(6) or board["player"][move] == 0:
                    print("Invalid move!")
                    continue
                break
            except:
                print("Enter a number!")

        board = make_move(board, move, "player")

        if is_terminal(board):
            break

        # AI move
        ai_move = best_move(board)
        print("Computer chooses pit:", ai_move)
        board = make_move(board, ai_move, "ai")

    print_board(board)

    # Final result
    if board["player_store"] > board["ai_store"]:
        print("You win!")
    elif board["player_store"] < board["ai_store"]:
        print("Computer is the winner!")
    else:
        print("It is a Draw!")

# Run game
play()
