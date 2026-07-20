import itertools

# Distance (Cost) Matrix
travel_cost = {
    (1, 2): 10, (2, 1): 10,
    (1, 3): 15, (3, 1): 15,
    (1, 4): 20, (4, 1): 20,
    (2, 3): 35, (3, 2): 35,
    (2, 4): 25, (4, 2): 25,
    (3, 4): 30, (4, 3): 30
}

locations = [1, 2, 3, 4]
home_base = 1

best_cost = float('inf')
best_route = []

unvisited = locations[1:]

for permutation in itertools.permutations(unvisited):

    full_trip = [home_base] + list(permutation) + [home_base]

    trip_distance = 0

    for idx in range(len(full_trip) - 1):
        src = full_trip[idx]
        dst = full_trip[idx + 1]
        trip_distance += travel_cost[(src, dst)]

    if trip_distance < best_cost:
        best_cost = trip_distance
        best_route = full_trip

print("Shortest Route:", best_route)
print("Minimum Distance:", best_cost)
