import heapq
import random

network = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5},
    'B': {'C': 8, 'D': 10},
    'C': {'G': 3},
    'D': {'G': 6},
    'G': {}
}

h_val = {'S':7,'A':5,'B':6,'C':2,'D':3,'G':0}


def update_random_edge(graph):
    n = random.choice(list(graph.keys()))
    if graph[n]:
        m = random.choice(list(graph[n].keys()))
        graph[n][m] = random.randint(1,12)
        print(f"Edge Updated: {n}->{m} = {graph[n][m]}")


def adaptive_a_star(graph, start, goal):

    open_heap = []
    heapq.heappush(open_heap, (h_val[start], start))

    parent = {start: None}
    g_score = {start: 0}
    closed = set()

    while open_heap:

        f_current, node = heapq.heappop(open_heap)

        if node in closed:
            continue

        print("Expanding:", node)
        closed.add(node)

        if node == goal:
            route = []
            while node:
                route.append(node)
                node = parent[node]
            print("Optimal Route:", route[::-1])
            return route[::-1]

        if random.random() < 0.4:
            update_random_edge(graph)

        for neighbor, cost in graph[node].items():

            tentative_g = g_score[node] + cost

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h_val[neighbor]
                parent[neighbor] = node
                heapq.heappush(open_heap, (f_score, neighbor))

    print("No Path Found")
    return None


adaptive_a_star(network, 'S', 'G')
