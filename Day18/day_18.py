import os

def pretty_print(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end='')
        print()

# PART 1
        
def build_matrix(dig_plan):
    max_row = current_row = 1
    max_col = current_col = 1
    with open(dig_plan, 'r') as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            length = line[2:4]
            length = int(length.replace(' ',''))
            if direction == 'R':
                current_col = current_col + length
                if current_col > max_col:
                    max_col = current_col
            if direction == 'L':
                current_col = current_col - length
            if direction == 'D':
                current_row = current_row + length
                if current_row > max_row:
                    max_row = current_row
            if direction == 'U':
                current_row = current_row - length
    return [['.' for _ in range(max_col)] for _ in range(max_row)] 

def dig_outside(matrix, dig_plan):
    matrix[0][0] = '#'
    with open(dig_plan, 'r') as file:
        row = 0
        col = 0
        for line in file:
            line = line.strip()
            direction = line[0]
            length = line[2:4]
            length = int(length.replace(' ',''))
            # pretty_print(matrix)
            # print('\n')
            for _ in range(1, length + 1):
                if direction == 'R':
                    col += 1
                    matrix[row][col] = '#'
                if direction == 'L':
                    col -= 1
                    matrix[row][col] = '#'
                if direction == 'D':
                    row += 1
                    matrix[row][col] = '#'
                if direction == 'U':
                    row -= 1
                    matrix[row][col] = '#'

def dig_inside(matrix):
    count = 0
    for row in range(len(matrix)):
        col = 0
        while col < len(matrix[0]):
            if matrix[row][col] == '#':
                start = col
                while col < len(matrix[0]) and matrix[row][col] == '#':
                    col += 1
                while col < len(matrix[0]) and matrix[row][col] == '.':
                    matrix[row][col] = '#'
                    col += 1
                while col < len(matrix[0]) and matrix[row][col] == '#':
                    col += 1
                count += (col - start)
            col += 1
    pretty_print(matrix)
    return count

        
def get_hole_size(dig_plan):
    matrix = build_matrix(dig_plan)
    dig_outside(matrix, dig_plan)
    pretty_print(matrix)
    print('\n')
    return dig_inside(matrix)

    


# PART 2

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'test_puzzleinput.txt')

print(get_hole_size(puzzle_input))
