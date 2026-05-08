# Colors and Nodes
colors = ['R', 'G', 'B']
nodes = ['A', 'B', 'C', 'D', 'E']

# Edges (constraints: adjacent nodes must have different colors)
edges = {('A','B'), ('A','E'), ('B','C'), ('B','D'), ('C','D'), ('D','E')}

# Store assignments and solutions
assignment = {}
solutions = []

# Check if assigning color 'c' to node 'n' is valid
def valid(n, c):
    for a, b in edges:
        if n == a and b in assignment and assignment[b] == c:
            return False
        if n == b and a in assignment and assignment[a] == c:
            return False
    return True

# Backtracking function
def backtrack(i=0):
    if i == len(nodes):
        solutions.append(assignment.copy())
        return
    
    n = nodes[i]
    
    for c in colors:
        if valid(n, c):
            assignment[n] = c
            backtrack(i + 1)
            del assignment[n]  # Backtrack

# Run the algorithm
backtrack()

# Print results
print("Total solutions:", len(solutions))

for s in solutions:
    result = []
    for node in sorted(s.keys()):
        result.append(node + ":" + s[node])
    print(" ".join(result))
