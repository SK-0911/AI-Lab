from queue import PriorityQueue

def best_first_search(start, goal, neighbors):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next_node in neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + 1
                frontier.put(next_node, priority)
                came_from[next_node] = current

    return came_from, cost_so_far


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def neighbors(node):
    return graph[node]

start = 'A'
goal = 'F'

came_from, cost_so_far = best_first_search(start, goal, neighbors)

print("Came from: ", came_from)
print("Cost so far: ", cost_so_far)
