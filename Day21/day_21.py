import os

def pretty_print(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end='')
        print()

# PART 1

# Helper function to build our matrix
def build_matrix(plot_map):
    output = []
    start = ()
    r = 0
    with open(plot_map, 'r') as file:
        for line in file:
            row = []
            c = 0
            for char in line.strip():
                row.append(char)
                if char == 'S':
                    start = (r, c)
                c += 1
            output.append(row)
            r += 1
                
    return output, start

# NEED TO FIND A WAY TO MEMOIZE
# def map_step_options(matrix, current, prev, n):
#     row = current[0]
#     col = current[1]
#     # Base cases
#     # If out of bounds, return
#     if row < 0 or col < 0 or row > len(matrix) or col > len(matrix[0]):
#         return
#     # If n reaches 0, return
#     if n < 0:
#         return
#     # If space is a rock, return
#     if matrix[row][col] == '#':
#         return
#     # Otherwise mark current plot as able to visit ('O')
#     matrix[row][col] = 'O'
#     # And change previous plot back to unable to visit ('.')
#     matrix[prev[0]][prev[1]] = '.'
#     # Recurse all neighbors
#     for row_dif, col_dif in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         new_row = row + row_dif
#         new_col = col + col_dif
#         map_step_options(matrix, (new_row, new_col), (row, col), n - 1)

def map_step_bfs(plot_matrix, start, steps):
    queue = []
    queue.append(start)
    while steps > 0:
        prev = []
        steps -= 1
        q_length = len(queue)
        # print(q_length)
        for _ in range(q_length):
            current = queue.pop(0)
            row = current[0]
            col = current[1]
            prev.append((row, col))
            for row_dif, col_dif in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row = row + row_dif
                new_col = col + col_dif
                if 0 <= new_row < len(plot_matrix) and 0 <= new_col < len(plot_matrix) and plot_matrix[new_row][new_col] != '#' and (new_row, new_col) not in queue:
                    queue.append((new_row, new_col))
                    plot_matrix[new_row][new_col] = 'O'
        for r, c in prev:
            plot_matrix[r][c] = '.'

def plot_options(plot_map, steps):
    plot_matrix, start = build_matrix(plot_map)
    # pretty_print(plot_matrix)
    # print(start)
    # Recursively map potential destination options on the plot matrix
    map_step_bfs(plot_matrix, start, steps)
    # pretty_print(plot_matrix)
    count = 0
    # Count visited options in the matrix
    for row in plot_matrix:
        for char in row:
            if char == 'O':
                count += 1
    return count

# PART 2

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

print(plot_options(puzzle_input, 64))
