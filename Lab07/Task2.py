# Resources
shirts = [f'S{i}' for i in range(1, 6)]
pants = [f'P{i}' for i in range(1, 4)]
sq = [f'SQ{i}' for i in range(1, 3)]
# Shirt-Pant combinations
sp = [s + '-' + p for s in shirts for p in pants]

# All possible outfits
items = sp + sq

# Days of week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# Assignment and tracking
assignment = {}
used = set()
count = 0
samples = []

# Backtracking function
def backtrack(i=0):
    global count
    
    # All days assigned
    if i == len(days):
        count += 1
        if len(samples) < 20:  # store first 20 solutions
            samples.append(assignment.copy())
        return
    
    d = days[i]
    
    for it in items:
        # Constraint 1: No repetition
        if it in used:
            continue
        
        # Constraint 2: Mon & Thu → Shirt-Pant only
        if d in ('Mon', 'Thu') and '-' not in it:
            continue
        
        # Constraint 3: Fri → Shalwar Qamees only
        if d == 'Fri' and it not in sq:
            continue
        
        # Assign
        assignment[d] = it
        used.add(it)
        
        backtrack(i + 1)
        
        # Backtrack
        used.remove(it)
        del assignment[d]

# Run CSP
backtrack()

# Output
print("Total valid schedules:", count)

print("\nSample solutions:")
for s in samples:
    print(' '.join(d + ':' + s[d] for d in days))
