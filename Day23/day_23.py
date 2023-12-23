import os

def pretty_print(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end='')
        print()

# PART 1

# Helper function to build our matrix
# def build_matrix(trail_map):
#     output = []
    
#     with open(trail_map, 'r') as file:
#         for line in file:
#             output.append([char for char in line.strip()])
    
#     return output

# def get_next_steps(matrix, current):
#     row = current[0][0]
#     col = current[0][1]
#     current_step = matrix[row][col]
#     visited = current[1]
#     next_steps = []
#     for rdif, cdif, dir in [(1,0,'v'), (-1,0,'^'), (0,1,'>'), (0,-1,'<')]:
#         new_row = row + rdif
#         new_col = col + cdif
#         if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
#             next_step = matrix[new_row][new_col]
#             if next_step == '#' or (new_row, new_col) in visited:
#                 continue
#             if current_step == '.' or current_step == dir:
#                 next_steps.append((new_row, new_col))
#     return next_steps 

# def longest_path(matrix):
#     longest = 0
#     start = (0,1)
#     stack = []
#     stack.append([start, []])
#     while len(stack) > 0:
#         current = stack.pop()
#         index = current[0]
#         visited = current[1]
#         path_length = len(visited)
#         if path_length > longest:
#             longest = path_length
#         visited = visited + [index]
#         valid_steps = get_next_steps(matrix, current)
#         for step in valid_steps:
#             stack.append([step, visited])
#         # matrix[index[0]][index[1]] = 'O'
#     return longest

# def get_longest_path(trail_map):
#     trail_matrix = build_matrix(trail_map)
#     # pretty_print(trail_matrix)
#     longest = longest_path(trail_matrix)
#     # pretty_print(trail_matrix)
#     return longest


# PART 2

# Helper function to build our matrix
def build_matrix(trail_map):
    output = []
    
    with open(trail_map, 'r') as file:
        for line in file:
            output.append([char for char in line.strip()])
    
    return output

def get_next_steps(matrix, current):
    row = current[0][0]
    col = current[0][1]
    current_step = matrix[row][col]
    visited = current[1]
    next_steps = []
    for rdif, cdif in [(1,0), (-1,0), (0,1), (0,-1)]:
        new_row = row + rdif
        new_col = col + cdif
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            next_step = matrix[new_row][new_col]
            if next_step != '#' and (new_row, new_col) not in visited:
                next_steps.append((new_row, new_col))
    return next_steps 

def longest_path(matrix):
    longest = 0
    start = (1,1)
    stack = []
    stack.append([start, [start]])
    while len(stack) > 0:
        current = stack.pop()
        index = current[0]
        visited = current[1]
        path_length = len(visited)
        if path_length > longest:
            longest = path_length
        valid_steps = get_next_steps(matrix, current)
        for step in valid_steps:
            stack.append([step, visited + [step]])
        # matrix[index[0]][index[1]] = 'O'
    return longest

def get_longest_path(trail_map):
    trail_matrix = build_matrix(trail_map)
    # pretty_print(trail_matrix)
    longest = longest_path(trail_matrix)
    # pretty_print(trail_matrix)
    return longest


# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'test_puzzleinput.txt')

print(get_longest_path(puzzle_input))

