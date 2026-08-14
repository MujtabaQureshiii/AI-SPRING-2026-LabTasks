from queue import PriorityQueue

class Cell:
    def __init__(self, pos, parent=None):
        self.pos = pos
        self.parent = parent
        self.h = 0

    def __lt__(self, other):
        return self.h < other.h


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def single_goal_bfs(grid, source, destination):

    rows, cols = len(grid), len(grid[0])
    frontier = PriorityQueue()
    frontier.put(Cell(source))
    visited_nodes = set()

    while not frontier.empty():

        current = frontier.get()

        if current.pos == destination:
            path = []
            while current:
                path.append(current.pos)
                current = current.parent
            return path[::-1]

        visited_nodes.add(current.pos)

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = current.pos[0]+dx, current.pos[1]+dy

            if (0 <= nx < rows and 0 <= ny < cols and
                grid[nx][ny] == 0 and (nx,ny) not in visited_nodes):

                node = Cell((nx,ny), current)
                node.h = manhattan((nx,ny), destination)
                frontier.put(node)

    return None


def multi_goal_maze(grid, start, goals):

    final_route = []
    current = start
    targets = list(goals)

    while targets:

        best_path = None
        chosen_goal = None

        for g in targets:
            path = single_goal_bfs(grid, current, g)
            if path:
                if best_path is None or len(path) < len(best_path):
                    best_path = path
                    chosen_goal = g

        if best_path is None:
            return None

        final_route += best_path[:-1]
        current = chosen_goal
        targets.remove(chosen_goal)

    final_route.append(current)
    return final_route


maze = [
    [0,0,1,0,0],
    [0,0,0,1,0],
    [1,0,1,0,0],
    [0,0,0,0,1],
    [0,1,0,0,0]
]

print("Multi Goal Path:", multi_goal_maze(maze, (0,0), [(4,4),(3,0),(2,3)]))
