# 6x6 Sudoku Grid (0 = empty)
grid = [
    [0, 6, 0, 2, 0, 5],
    [0, 0, 4, 6, 0, 0],
    [0, 1, 2, 0, 0, 0],
    [0, 5, 6, 0, 4, 0],
    [0, 4, 3, 0, 2, 0],
    [3, 0, 5, 0, 0, 6]
]
m = 7
n = 6          # grid size
rb, cb = 2, 3  # subgrid size (2x3)

# Check if placing value v at (r, c) is valid
def valid(r, c, v):
    # Row and column check
    for i in range(n):
        if grid[r][i] == v or grid[i][c] == v:
            return False

    # Subgrid check
    br = (r // rb) * rb
    bc = (c // cb) * cb

    for i in range(br, br + rb):
        for j in range(bc, bc + cb):
            if grid[i][j] == v:
                return False

    return True

# Backtracking solver
def solve():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:  # empty cell
                for v in range(1, n + 1):
                    if valid(i, j, v):
                        grid[i][j] = v
                        
                        if solve():
                            return True
                        
                        grid[i][j] = 0  # backtrack
                
                return False  # no valid number found
    return True  # solved

# Run solver
if solve():
    print("Solved Sudoku:\n")
    for row in grid:
        print(' '.join(str(x) for x in row))
else:
    print("No solution exists")
