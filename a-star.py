# Code for A* Search algorithm in Python

import heapq

def heuristic(a, b):
    # Euclidean distance
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

def a_star(graph, start, goal):
    frontier = [(0, start)]
    heapq.heapify(frontier)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    return came_from, cost_so_far



class Graph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, node):
        return self.edges.get(node, [])

    def cost(self, a, b):
        return 1

graph = Graph()
graph.edges = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 0)],
}

start, goal = (0, 0), (4, 5)
came_from, cost_so_far = a_star(graph, start, goal)

print("Came from:")
for node, parent in came_from.items():
    print(f"{node} -> {parent}")

print("\nCost so far:")
for node, cost in cost_so_far.items():
    print(f"{node}: {cost}")


