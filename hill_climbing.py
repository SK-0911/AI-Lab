import numpy as np

def find_neighbours(state, landscape):
    neighbours = []
    dim = landscape.shape
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in directions:
        x, y = state
        x, y = x + dx, y + dy
        if 0 <= x < dim[0] and 0 <= y < dim[1]:
            neighbours.append((x, y))
    return neighbours

def hill_climb(start, landscape):
    curr = start
    while True:
        neighbours = find_neighbours(curr, landscape)
        best = max(neighbours, key=lambda n: landscape[n[0], n[1]])
        if landscape[best[0], best[1]] <= landscape[curr[0], curr[1]]:
            return curr
        curr = best

if __name__ == '__main__':
    landscape = np.random.randint(1, high=50, size=(10, 10))
    print(landscape)
    start = (3, 6)
    result = hill_climb(start, landscape)
    print(f"Optimal state: {result}, value: {landscape[result[0], result[1]]}")
