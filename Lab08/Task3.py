import math

# Minimax function
def minimax(stones, is_max):
    # Terminal state
    if stones == 0:
        return -1 if is_max else 1

    if is_max:
        best = -math.inf
        for move in [1, 2, 3]:
            if stones - move >= 0:
                value = minimax(stones - move, False)
                best = max(best, value)
        return best
    else:
        best = math.inf
        for move in [1, 2, 3]:
            if stones - move >= 0:
                value = minimax(stones - move, True)
                best = min(best, value)
        return best

# Best move for AI
def best_move(stones):
    best_val = -math.inf
    move_choice = 1

    for move in [1, 2, 3]:
        if stones - move >= 0:
            move_val = minimax(stones - move, False)
            if move_val > best_val:
                best_val = move_val
                move_choice = move

    return move_choice

# Game loop
def play():
    # Safe input for total stones
    while True:
        try:
            stones = int(input("Enter total number of stones: "))
            if stones <= 0:
                print("Enter a positive number!")
                continue
            break
        except:
            print("Invalid input! Please enter a number.")

    while stones > 0:
        print("\nStones left:", stones)

        # Player move
        while True:
            try:
                user = int(input("Take 1, 2 or 3 stones: "))
                if user not in [1, 2, 3] or user > stones:
                    print("Invalid move! Try again.")
                    continue
                break
            except:
                print("Invalid input! Enter a number.")

        stones -= user

        if stones == 0:
            print("You win!")
            break

        # AI move
        ai = best_move(stones)
        print("Computer takes:", ai)
        stones -= ai

        if stones == 0:
            print("Computer wins!")
            break


# Run game
play()
