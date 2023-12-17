import os

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
            output.append([char for char in line.strip()])
    
    return output

def get_next_tile(matrix, row, col, direction):
    next_tiles = []
    current_tile = matrix[row][col]
    if direction == 'r':
        if current_tile in '.-':
            next_tiles.append((row, col + 1, 'r'))
        elif current_tile == '|':
            next_tiles.extend([(row + 1, col, 'd'),(row - 1, col, 'u')])
        elif current_tile == '\\':
            next_tiles.append((row + 1, col, 'd'))
        elif current_tile == '/':
            next_tiles.append((row - 1, col, 'u'))
    elif direction == 'l':
        if current_tile in '.-':
            next_tiles.append((row, col - 1, 'l'))
        elif current_tile == '|':
            next_tiles.extend([(row + 1, col, 'd'),(row - 1, col, 'u')])
        elif current_tile == '\\':
            next_tiles.append((row - 1, col, 'u'))
        elif current_tile == '/':
            next_tiles.append((row + 1, col, 'd'))
    elif direction == 'u':
        if current_tile in '.|':
            next_tiles.append((row - 1, col, 'u'))
        elif current_tile == '-':
            next_tiles.extend([(row, col + 1, 'r'),(row, col - 1, 'l')])
        elif current_tile == '\\':
            next_tiles.append((row, col - 1, 'l'))
        elif current_tile == '/':
            next_tiles.append((row, col + 1, 'r'))
    elif direction == 'd':
        if current_tile in '.|':
            next_tiles.append((row + 1, col, 'd'))
        elif current_tile == '-':
            next_tiles.extend([(row, col + 1, 'r'),(row, col - 1, 'l')])
        elif current_tile == '\\':
            next_tiles.append((row, col + 1, 'r'))
        elif current_tile == '/':
            next_tiles.append((row, col - 1, 'l'))
    return next_tiles          


def total_helper(matrix, visited, row, col, direction):
    stack = [(row, col, direction)]
    
    while stack:
        row, col, direction = stack.pop()
        print(row, col)
        # Base case to end beam if out of bounds
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[row]):
            continue
        
        # Add current space to visited
        if (row, col) not in visited:
            visited.append((row, col))
        
        # Get next tiles
        next_tiles = get_next_tile(matrix, row, col, direction)
        
        for next_row, next_col, next_direction in next_tiles:
            stack.append((next_row, next_col, next_direction))
    
    return

def total_energized(grid):
    matrix = build_matrix(grid)
    # pretty_print(matrix)
    tiles_energized = []
    
    tiles_energized = total_helper(matrix, tiles_energized, 0, 0, 'r')

    print(tiles_energized)
    return len(tiles_energized)

# PART 2

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'test_puzzleinput.txt')

print(total_energized(puzzle_input))
