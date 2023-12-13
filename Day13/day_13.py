import os

# def pretty_print(matrix):
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             print(matrix[row][col], end='')
#         print()

# PART 1

# def get_reflection_count(section):
#     # Check for vertical reflection first
#     row = 0
#     for row in range(1, len(section)):
#         # If potential reflection found, use two pointers to double check
#         if section[row] == section[row - 1]:
#             r1 = row - 1
#             r2 = row
#             while r1 >= 0 and r2 < len(section):
#                 if section[r1] != section[r2]:
#                     break
#                 r1 -= 1
#                 r2 += 1
#             if r1 < 0 or r2 == len(section): 
#                 return 0, row
#     # Check for horizontal reflection
#     for col in range(1, len(section[0])):
#         # If potential reflection found, use two pointers to double check
#         if all(section[r][col] == section[r][col - 1] for r in range(len(section))):
#             c1 = col - 1
#             c2 = col
#             while c1 >= 0 and c2 < len(section[0]):
#                 if not all(section[r][c1] == section[r][c2] for r in range(len(section))):
#                     break
#                 c1 -= 1
#                 c2 += 1
#             if c1 < 0 or c2 == len(section[0]): 
#                 return col, 0

# def find_mirrors(patterns):
#     cols_left = 0
#     rows_above = 0
#     with open(patterns, 'r') as file:
#         current_line = file.readline().strip()
#         section = []
#         while True:
#             # print(current_line)
#             section.append(current_line)
#             next_line = file.readline()
#             if next_line == '':
#                 add_cols, add_rows = get_reflection_count(section)
#                 # print(add_cols, add_rows, 'end')
#                 cols_left += add_cols
#                 rows_above += add_rows
#                 # print(section)
#                 section = []
#                 break
#             next_line = next_line.strip()
#             if len(next_line) <= 0:
#                 add_cols, add_rows = get_reflection_count(section)
#                 # print(add_cols, add_rows)
#                 cols_left += add_cols
#                 rows_above += add_rows
#                 # print(section)
#                 section = []
#                 next_line = file.readline().strip()
#             current_line = next_line
#     return cols_left + (100 * rows_above)


# PART 2

# Helper function to swap values 
def swap(section, row, col):
    if section[row][col] == '.':
        section[row][col] = '#'
    else:
        section[row][col] = '.'

def get_reflection_count(section):
    # Check each index to see if that's where the smudge is
    for y in range(len(section)):
        for x in range(len(section[y])):
            # Swap '#' with '.' and vice versa
            swap(section, y, x)
            # Check for vertical reflection first
            row = 0
            for row in range(1, len(section)):
                # Check that swap is not outside reflection range
                reflection_lower = row - (len(section) - row)
                reflection_upper = row - 1
                if reflection_lower > y or reflection_upper < y:
                    continue 
                # If potential reflection found, use two pointers to double check
                if section[row] == section[row - 1]:
                    r1 = row - 1
                    r2 = row
                    while r1 >= 0 and r2 < len(section):
                        if section[r1] != section[r2]:
                            break
                        r1 -= 1
                        r2 += 1
                    if r1 < 0 or r2 == len(section): 
                        return 0, row
            # Check for horizontal reflection
            for col in range(1, len(section[0])):
                # Check that swap is not outside reflection range
                reflection_lower = col - (len(section[0]) - col)
                reflection_upper = col - 1
                if reflection_lower > x or reflection_upper < x:
                    continue 
                # If potential reflection found, use two pointers to double check
                if all(section[r][col] == section[r][col - 1] for r in range(len(section))):
                    c1 = col - 1
                    c2 = col
                    while c1 >= 0 and c2 < len(section[0]):
                        if not all(section[r][c1] == section[r][c2] for r in range(len(section))):
                            break
                        c1 -= 1
                        c2 += 1
                    if c1 < 0 or c2 == len(section[0]): 
                        return col, 0
            # Swap back if a reflection was not found
            swap(section, y, x)

def find_mirrors(patterns):
    cols_left = 0
    rows_above = 0
    with open(patterns, 'r') as file:
        current_line = file.readline().strip()
        section = []
        while True:
            # print(current_line)
            section.append([char for char in current_line])
            next_line = file.readline()
            if next_line == '':
                add_cols, add_rows = get_reflection_count(section)
                # print(add_cols, add_rows, 'end')
                cols_left += add_cols
                rows_above += add_rows
                # pretty_print(section)
                section = []
                break
            next_line = next_line.strip()
            if len(next_line) <= 0:
                add_cols, add_rows = get_reflection_count(section)
                # print(add_cols, add_rows)
                cols_left += add_cols
                rows_above += add_rows
                # pretty_print(section)
                # print('\n')
                section = []
                next_line = file.readline().strip()
            current_line = next_line
    return cols_left + (100 * rows_above)

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

print(find_mirrors(puzzle_input))
