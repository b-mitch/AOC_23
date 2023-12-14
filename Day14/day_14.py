import os
# import numpy as np

def pretty_print(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end='')
        print()

# PART 1

# Helper function to build our matrix
def build_matrix(rock_layout):
    output = []
    
    with open(rock_layout, 'r') as file:
        for line in file:
            output.append([char for char in line.strip()])
    
    return output

# Helper function to roll rock 'north' (down the matrix)
def roll_rock(matrix, row, col):
    while True:
        if row - 1 >= 0 and matrix[row - 1][col] == '.':
            matrix[row - 1][col] = 'O'
            matrix[row][col] = '.'
            row = row - 1
        else:
            break

# Helper function to check each element of matrix and 'roll' all the 'O's
def tilt_platform(matrix):
    for r in range(1, len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'O':
                roll_rock(matrix, r, c)

def get_load(rock_layout):
    total_load = 0
    # Build a matrix to track rock positions and tilt the platform
    matrix = build_matrix(rock_layout)
    # pretty_print(matrix)
    # print('\n')
    tilt_platform(matrix)
    # pretty_print(matrix)

    # Calculate load of each row and add to output
    for row in range(len(matrix)):
        rocks = 0
        load_multiplier = len(matrix) - row
        for char in matrix[row]:
            if char == 'O':
                rocks += 1
        row_load = rocks * load_multiplier
        total_load += row_load

    return total_load

# PART 2

# Helper function to build our matrix
def build_matrix(rock_layout):
    output = []
    
    with open(rock_layout, 'r') as file:
        for line in file:
            output.append([char for char in line.strip()])
    
    return output

# Helper function to roll rock in the correct direction
def roll_rock(matrix, row, col, direction):
    # If rolling North, move 'O' as far down the matrix as possible
    if direction == 1:
        while True:
            if row - 1 >= 0 and matrix[row - 1][col] == '.':
                matrix[row - 1][col] = 'O'
                matrix[row][col] = '.'
                row = row - 1
            else:
                break
    # If rolling West, move 'O' as far left in the matrix as possible
    if direction == 2:
        while True:
            if col - 1 >= 0 and matrix[row][col - 1] == '.':
                matrix[row][col - 1] = 'O'
                matrix[row][col] = '.'
                col = col - 1
            else:
                break
    # If rolling South, move 'O' as far up the matrix as possible
    if direction == 3:
        while True:
            if row + 1 < len(matrix) and matrix[row + 1][col] == '.':
                matrix[row + 1][col] = 'O'
                matrix[row][col] = '.'
                row = row + 1
            else:
                break
    # If rolling East, move 'O' as far right in the matrix as possible
    if direction == 4:
        while True:
            if col + 1 < len(matrix[0]) and matrix[row][col + 1] == '.':
                matrix[row][col + 1] = 'O'
                matrix[row][col] = '.'
                col = col + 1
            else:
                break

# Helper function to check each element of matrix and 'roll' all the 'O's
def tilt_platform(matrix, x):
    # Traverse the matrix by row or column, depending on current spin direction
    if x == 1:
        for r in range(1, len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 'O':
                    roll_rock(matrix, r, c, x)
    if x == 2:
        for c in range(1, len(matrix[0])):
            for r in range(len(matrix)):
                if matrix[r][c] == 'O':
                    roll_rock(matrix, r, c, x)
    if x == 3:
        for r in range(len(matrix) - 2, -1, -1):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 'O':
                    roll_rock(matrix, r, c, x)
    if x == 4:
        for c in range(len(matrix[0]) - 2, -1, -1):
            for r in range(len(matrix)):
                if matrix[r][c] == 'O':
                    roll_rock(matrix, r, c, x)

def get_load(rock_layout, total_spins):
    # Build a matrix to track rock positions
    matrix = build_matrix(rock_layout)
    # Determine a cycle start and length to spin much fewer times
    cycle_start,  cycle_length = explore_cycles(rock_layout, total_spins) # puzzle input
    # cycle_start = 4 # test input
    # cycle_length = 7 # test input
    # Determine how many spins is needed based on cycle
    ignore_start = total_spins - cycle_start
    spins_needed = ignore_start % cycle_length
    # Spin only as many times as is necessary
    for _ in range(cycle_start + spins_needed):
        for x in range(1,5):
            tilt_platform(matrix, x)
    # Calculate load of each row and add to output
    total_load = 0
    for row in range(len(matrix)):
        rocks = 0
        load_multiplier = len(matrix) - row
        for char in matrix[row]:
            if char == 'O':
                rocks += 1
        row_load = rocks * load_multiplier
        total_load += row_load

    return total_load

# Use to determine if a cycle exists
def explore_cycles(rock_layout, max_spins):
    matrix = build_matrix(rock_layout)
    state_map = dict()
    cycle_start = None
    cycle_length = None

    for spins in range(1, max_spins + 1):
        matrix_key = tuple(map(tuple, matrix))
        if matrix_key in state_map:
            # Detected a potential cycle
            # print(spins)
            cycle_start = state_map[matrix_key]
            cycle_length = spins - cycle_start
            # print(f"Potential cycle detected: start = {cycle_start}, length = {cycle_length}")
            break
        else:
            state_map[matrix_key] = spins
            for x in range(1, 5):
                tilt_platform(matrix, x)

    return cycle_start, cycle_length

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

print(get_load(puzzle_input, 1000000000))
