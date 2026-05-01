import heapq

class TargetDrivenDLSAgent:
    def __init__(self, map_graph, target_node, search_depth):
        self.map_graph = map_graph
        self.target_node = target_node
        self.search_depth = search_depth

    def run_depth_limited(self, node, level, visited_path):
        print(f"Perceiving Node: {node}, Depth: {level}")

        if node == self.target_node:
            return visited_path

        if level == self.search_depth:
            return None

        for adjacent in self.map_graph.get(node, []):
            outcome = self.run_depth_limited(
                adjacent,
                level + 1,
                visited_path + [adjacent]
            )
            if outcome is not None:
                return outcome

        return None

    def execute(self, initial_node):
        print("\n===== Goal-Based Agent (DLS) =====")
        found_path = self.run_depth_limited(initial_node, 0, [initial_node])

        if found_path:
            print("Goal Reached!")
            print("Path:", " -> ".join(found_path))
        else:
            print("Goal Not Found Within Depth Limit.")


class CostMinimizingUCSAgent:
    def __init__(self, map_graph, target_node):
        self.map_graph = map_graph
        self.target_node = target_node

    def run_uniform_cost(self, initial_node):
        min_heap = []
        heapq.heappush(min_heap, (0, initial_node, [initial_node]))

        recorded_costs = {}

        while min_heap:
            accumulated, node, trail = heapq.heappop(min_heap)

            print(f"Evaluating Node: {node}, Accumulated Cost: {accumulated}")

            if node == self.target_node:
                return accumulated, trail

            if node not in recorded_costs or accumulated < recorded_costs[node]:
                recorded_costs[node] = accumulated

                for connected, edge_cost in self.map_graph.get(node, []):
                    heapq.heappush(
                        min_heap,
                        (accumulated + edge_cost, connected, trail + [connected])
                    )

        return None, None

    def execute(self, initial_node):
        print("\n===== Utility-Based Agent (UCS) =====")
        final_cost, final_trail = self.run_uniform_cost(initial_node)

        if final_trail:
            print("Goal Reached!")
            print("Minimum Cost:", final_cost)
            print("Path:", " -> ".join(final_trail))
        else:
            print("Goal Not Found.")


dls_map = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

ucs_map = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

if __name__ == "__main__":

    dls_agent = TargetDrivenDLSAgent(dls_map, target_node='G', search_depth=3)
    dls_agent.execute(initial_node='A')

    ucs_agent = CostMinimizingUCSAgent(ucs_map, target_node='G')
    ucs_agent.execute(initial_node='A')
