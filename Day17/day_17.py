import os
import heapq
import math

def pretty_print(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end='')
        print()

# PART 1

# Helper function to build our matrix
def build_matrix(input):
    output = []
    
    with open(input, 'r') as file:
        for line in file:
            row = []
            output.append([int(char) for char in line.strip()])
    
    return output

def min_heat_loss(city_map):
    matrix = build_matrix(city_map)
    rows, cols = len(matrix), len(matrix[0])
    distance = [[math.inf] * cols for _ in range(rows)]
    distance[0][0] = 0
    pq = [(0, (0, 0, None, 1))]  # Priority queue with initial node and its cost, direction and count

    while pq:
        cost, (r, c, prev_direction, consecutive_count) = heapq.heappop(pq)

        # Explore neighbors (up, down, left, right)
        for dr, dc, direction in [(0, 1, 'right'), (0, -1, 'left'), (1, 0, 'down'), (-1, 0,'up')]:
            nr, nc = r + dr, c + dc

            # Check boundaries
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = cost + matrix[nr][nc]
                new_consecutive_count = consecutive_count + 1 if direction == prev_direction or prev_direction is None else 1
                # Avoid moving back to previous node
                if new_cost < distance[nr][nc] and (nr, nc) != (r, c):
                    # Check if consecutive count is within limit
                    if new_consecutive_count <= 3:
                        distance[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, (nr, nc, direction, new_consecutive_count)))

    # pretty_print(distance)
    return distance[rows-1][cols-1] # Shortest path to bottom-right corner


# PART 2

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'test_puzzleinput.txt')

print(min_heat_loss(puzzle_input))
