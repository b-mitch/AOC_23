import os
import math

def pretty_print(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end='')
        print()

# PART 1

# Helper function to get pipes after start only
def get_start_pipes(matrix, start):
    next_pipes = []
    row, col = start

    if row > 0 and (matrix[row - 1][col] in ['|', '7', 'F']):
            next_pipes.append((row - 1, col))
    if row < len(matrix) - 1 and (matrix[row + 1][col] in ['|', 'L', 'J']):
        next_pipes.append((row + 1, col))
    if col > 0 and (matrix[row][col - 1] in ['-', 'L', 'F']):
        next_pipes.append((row, col - 1))
    if col < len(matrix[row]) - 1 and (matrix[row][col + 1] in ['-', '7', 'J']):
        next_pipes.append((row, col + 1))

    return next_pipes

def get_next_pipe(matrix, current):
    # print(current)
    row, col = current
    next_pipe = None
    current_pipe = matrix[row][col]
    # If current is a vertical pipe, check above and below it
    if current_pipe == '|':
        if row > 0 and (matrix[row - 1][col] in ['|', 'L', 'J', '7', 'F']):
            next_pipe = (row - 1, col)
        if row < len(matrix) - 1 and (matrix[row + 1][col] in ['|', 'L', 'J', '7', 'F']):
            next_pipe = (row + 1, col)
    # If current is a horizontal pipe, check right and left of it
    if current_pipe == '-':
        if col > 0 and (matrix[row][col - 1] in ['-', '7', 'J', 'L', 'F']):
            next_pipe = (row, col - 1)
        if col < len(matrix[row]) - 1 and (matrix[row][col + 1] in ['-', '7', 'J', 'L', 'F']):
            next_pipe = (row, col + 1)
    # If current is a top left corner, check right and below
    if current_pipe == 'F':
        if col < len(matrix[row]) - 1 and (matrix[row][col + 1] in ['-', '7', 'J']):
            next_pipe = (row, col + 1)
        if row < len(matrix) - 1 and (matrix[row + 1][col] in ['|', 'L', 'J']):
            next_pipe = (row + 1, col)
    # If current is top right corner, check left and below
    if current_pipe == '7':
        if col > 0 and (matrix[row][col - 1] in ['-', 'L', 'F']):
            next_pipe = (row, col - 1)
        if row < len(matrix) - 1 and (matrix[row + 1][col] in ['|', 'L', 'J']):
            next_pipe = (row + 1, col)
    # If current is bottom right, check left and above
    if current_pipe == 'J':
        if col > 0 and (matrix[row][col - 1] in ['-', 'L', 'F']):
            next_pipe = (row, col - 1)
        if row > 0 and (matrix[row - 1][col] in ['|', '7', 'F']):
            next_pipe = (row - 1, col)
    # If current is bottom left, check right and above
    if current_pipe == 'L':
        if col < len(matrix[row]) - 1 and (matrix[row][col + 1] in ['-', '7', 'J']):
            next_pipe = (row, col + 1)
        if row > 0 and (matrix[row - 1][col] in ['|', '7', 'F']):
            next_pipe = (row - 1, col)
    matrix[row][col] = 'S'    
    # print(next_pipe)
    return next_pipe

def get_total_steps(matrix, current):
    steps = 1
    # Increment step and move to the next tile until there is no next (start reached)
    while current is not None:
        current = get_next_pipe(matrix, current)
        steps += 1
    return steps

def get_steps(pipe_map):
    matrix = []
    start = None
    row = 0
    # Build matrix to represent the pip map
    with open(pipe_map, 'r') as file:
        for line in file:
            arr = []
            col = 0
            for char in line.strip():
                arr.append(char)
                if char == 'S':
                    start = (row,col)
                col += 1
            matrix.append(arr)
            row += 1
    # print(start)
    # pretty_print(matrix)
    # Get the indices for the next pipes after start
    next_pipes = get_start_pipes(matrix, start)
    # print(next_pipes)
    # Traverse the pipe loop and count steps till start reached
    # and return the ceiling of total divided by two
    return math.ceil(get_total_steps(matrix, next_pipes[0]) / 2)

# PART 2

# Helper function to get pipes after start only
def get_start_pipes(matrix, start):
    next_pipes = []
    row, col = start

    if row > 0 and (matrix[row - 1][col] in ['|', '7', 'F']):
            next_pipes.append((row - 1, col))
    if row < len(matrix) - 1 and (matrix[row + 1][col] in ['|', 'L', 'J']):
        next_pipes.append((row + 1, col))
    if col > 0 and (matrix[row][col - 1] in ['-', 'L', 'F']):
        next_pipes.append((row, col - 1))
    if col < len(matrix[row]) - 1 and (matrix[row][col + 1] in ['-', '7', 'J']):
        next_pipes.append((row, col + 1))

    return next_pipes

def get_next_pipe(matrix, current):
    # print(current)
    row, col = current
    next_pipe = None
    current_pipe = matrix[row][col]
    # If current is a vertical pipe, check above and below it
    if current_pipe == '|':
        if row > 0 and (matrix[row - 1][col] in ['|', 'L', 'J', '7', 'F']):
            next_pipe = (row - 1, col)
        if row < len(matrix) - 1 and (matrix[row + 1][col] in ['|', 'L', 'J', '7', 'F']):
            next_pipe = (row + 1, col)
    # If current is a horizontal pipe, check right and left of it
    if current_pipe == '-':
        if col > 0 and (matrix[row][col - 1] in ['-', '7', 'J', 'L', 'F']):
            next_pipe = (row, col - 1)
        if col < len(matrix[row]) - 1 and (matrix[row][col + 1] in ['-', '7', 'J', 'L', 'F']):
            next_pipe = (row, col + 1)
    # If current is a top left corner, check right and below
    if current_pipe == 'F':
        if col < len(matrix[row]) - 1 and (matrix[row][col + 1] in ['-', '7', 'J']):
            next_pipe = (row, col + 1)
        if row < len(matrix) - 1 and (matrix[row + 1][col] in ['|', 'L', 'J']):
            next_pipe = (row + 1, col)
    # If current is top right corner, check left and below
    if current_pipe == '7':
        if col > 0 and (matrix[row][col - 1] in ['-', 'L', 'F']):
            next_pipe = (row, col - 1)
        if row < len(matrix) - 1 and (matrix[row + 1][col] in ['|', 'L', 'J']):
            next_pipe = (row + 1, col)
    # If current is bottom right, check left and above
    if current_pipe == 'J':
        if col > 0 and (matrix[row][col - 1] in ['-', 'L', 'F']):
            next_pipe = (row, col - 1)
        if row > 0 and (matrix[row - 1][col] in ['|', '7', 'F']):
            next_pipe = (row - 1, col)
    # If current is bottom left, check right and above
    if current_pipe == 'L':
        if col < len(matrix[row]) - 1 and (matrix[row][col + 1] in ['-', '7', 'J']):
            next_pipe = (row, col + 1)
        if row > 0 and (matrix[row - 1][col] in ['|', '7', 'F']):
            next_pipe = (row - 1, col)
    matrix[row][col] = 'S'    
    # print(next_pipe)
    return next_pipe

def get_nest_indices(matrix, current, trajectory):
    nest_indices = []
    pipe_indices = []
    # Increment step and move to the next tile until there is no next (start reached)
    while current is not None:
        # Add current to pipe indices
        pipe_indices.append(current)
        # print(trajectory)
        # Remove current index from nest indices if present
        if current in nest_indices:
            nest_indices.remove(current)
        row, col = current
        current_pipe = matrix[row][col]
        # print(current_pipe)
        # Change trajectory if current pipe is a corner
        if current_pipe == '7':
            trajectory = 'd'
        elif current_pipe == 'J':
            trajectory = 'l'
        elif current_pipe == 'L':
            trajectory = 'u'
        elif current_pipe == 'F':
            trajectory = 'r'
        # Add adjacent inner indices based on trajectory if they are not pipes
        if trajectory == 'r':
            nest_index = (row + 1, col)
            if nest_index not in pipe_indices and nest_index not in nest_indices:
                nest_indices.append(nest_index)
        elif trajectory == 'd':
            nest_index = (row, col - 1)
            if nest_index not in pipe_indices and nest_index not in nest_indices:
                nest_indices.append(nest_index)
        elif trajectory == 'l':
            nest_index = (row - 1, col)
            if nest_index not in pipe_indices and nest_index not in nest_indices:
                nest_indices.append(nest_index)
        else:
            nest_index = (row, col + 1)
            if nest_index not in pipe_indices and nest_index not in nest_indices:
                nest_indices.append(nest_index)
        # Get the next pipe
        next_pipe = get_next_pipe(matrix, current)
        # Set current to next pipe
        current = next_pipe
    return nest_indices

def get_start_trajectory(start_pipe, next_pipes):
    start_row = start_pipe[0]
    start_col = start_pipe[1]
    trajectories = []
    for pipe in next_pipes:
        row = pipe[0]
        col = pipe[1]
        row_dif = row - start_row
        col_dif = col - start_col
        if row_dif < 0:
            trajectories.append('u')
        elif row_dif> 0:
            trajectories.append('d')
        elif col_dif < 0:
            trajectories.append('l')
        else:
            trajectories.append('r')
    if 'r' in trajectories and 'd' in trajectories:
        return 'r'
    if 'r' in trajectories and 'u' in trajectories:
        return 'u'
    if 'l' in trajectories and 'd' in trajectories:
        return 'd'
    if 'l' in trajectories and 'u' in trajectories:
        return 'l'

def get_steps(pipe_map):
    matrix = []
    start = None
    row = 0
    # Build matrix to represent the pip map
    with open(pipe_map, 'r') as file:
        for line in file:
            arr = []
            col = 0
            for char in line.strip():
                arr.append(char)
                if char == 'S':
                    start = (row,col)
                col += 1
            matrix.append(arr)
            row += 1
    # print(start)
    # pretty_print(matrix)
    # Get the indices for the next pipes after start
    start_pipes = get_start_pipes(matrix, start)
    # Determine what trajectory we are moving at from the start
    start_trajectory = get_start_trajectory(start, start_pipes)
    first_pipe = None
    # print(start)
    # print(start_trajectory)
    # Determine first pipe based on start trajectory to ensure clockwise movement
    if start_trajectory == 'r':
        first_pipe = (start[0],start[1] + 1)
    elif start_trajectory == 'l':
        first_pipe = (start[0],start[1] - 1)
    elif start_trajectory == 'd':
        first_pipe = (start[0] + 1,start[1])
    else:
        first_pipe = (start[0] - 1,start[1])
    # print(first_pipe)
    # Get all valid indices that are adjacent and in the correct direction
    nest_indices = get_nest_indices(matrix, first_pipe, start_trajectory)
    pretty_print(matrix)
    print(nest_indices)
    return len(nest_indices)

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'test_puzzleinput.txt')

print(get_steps(puzzle_input))
