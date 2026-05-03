tree_structure = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

graph_structure = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['A'],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}


def bounded_dfs(network, active_node, objective, remaining, seen_nodes):

    print("Current Node:", active_node, "| Remaining Depth:", remaining)

    if active_node == objective:
        return True

    if remaining == 0:
        return False

    seen_nodes.add(active_node)

    connections = network.get(active_node, [])

    for successor in connections:
        if successor not in seen_nodes:
            located = bounded_dfs(network, successor, objective, remaining - 1, seen_nodes)
            if located:
                return True

    return False


def iterative_deepening(network, origin, destination, depth_cap):

    current_depth = 0

    while current_depth <= depth_cap:

        print("\nDepth Level:", current_depth)
        traversed = set()

        status = bounded_dfs(network, origin, destination, current_depth, traversed)

        if status:
            print("\nGoal Reached at Depth:", current_depth)
            return

        current_depth += 1

    print("\nGoal not found within given depth.")


print("===== Running IDDFS on Tree =====")
iterative_deepening(tree_structure, 'A', 'I', 5)

print("\n===== Running IDDFS on Graph =====")
iterative_deepening(graph_structure, 'A', 'I', 5)
