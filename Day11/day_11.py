import os
import math

# PART 1

# def get_sum_paths(image):
#     galaxies = []
#     original_width = 0
#     # Traverse the file, saving galaxy locations
#     with open(image, 'r') as file:
#         row = 0
#         for line in file:
#             original_width = len(line.strip())
#             has_galaxy = False
#             col = 0
#             for char in line.strip():
#                 # If line has a galaxy, note this and add to galaxies
#                 if char == '#':
#                     has_galaxy = True
#                     galaxies.append([row, col])
#                 col += 1
#             # If no galaxy was found, increment row x2
#             if not has_galaxy:
#                 row += 1
#             row += 1
#     # Increment every galaxy's col value by one for each emtpy column before it
#     # print(galaxies)
#     galaxy_cols = [galaxy[1] for galaxy in galaxies]
#     for col in range(original_width):
#         if col not in galaxy_cols:
#             index = 0
#             for galaxy in galaxy_cols:
#                 if col < galaxy:
#                     galaxies[index][1] += 1
#                 index += 1
#     # print(galaxies)
#     # For each galaxy, find the shortest path between it and every other galaxy
#     # and add it to the sum
#     paths_sum = 0
#     for i in range(len(galaxies)):
#         row1 = galaxies[i][0]
#         col1 = galaxies[i][1]
#         # print(galaxies[i])
#         for j in range(i + 1, len(galaxies)):
#             row2 = galaxies[j][0]
#             col2 = galaxies[j][1]
#             row_dif = abs(row1 - row2)
#             col_dif = abs(col1 - col2)
#             paths_sum += (row_dif + col_dif)
#     return paths_sum

# PART 2

def get_sum_paths(image):
    galaxies = []
    original_width = 0
    # Traverse the file, saving galaxy locations
    with open(image, 'r') as file:
        row = 0
        for line in file:
            original_width = len(line.strip())
            has_galaxy = False
            col = 0
            for char in line.strip():
                # If line has a galaxy, note this and add to galaxies
                if char == '#':
                    has_galaxy = True
                    galaxies.append([row, col])
                col += 1
            # If no galaxy was found, increment row x2
            if not has_galaxy:
                row += 999999
            row += 1
    # Increment every galaxy's col value by one for each emtpy column before it
    # print(galaxies)
    galaxy_cols = [galaxy[1] for galaxy in galaxies]
    for col in range(original_width):
        if col not in galaxy_cols:
            index = 0
            for galaxy in galaxy_cols:
                if col < galaxy:
                    galaxies[index][1] += 999999
                index += 1
    # print(galaxies)
    # For each galaxy, find the shortest path between it and every other galaxy
    # and add it to the sum
    paths_sum = 0
    for i in range(len(galaxies)):
        row1 = galaxies[i][0]
        col1 = galaxies[i][1]
        # print(galaxies[i])
        for j in range(i + 1, len(galaxies)):
            row2 = galaxies[j][0]
            col2 = galaxies[j][1]
            row_dif = abs(row1 - row2)
            col_dif = abs(col1 - col2)
            paths_sum += (row_dif + col_dif)
    return paths_sum

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

print(get_sum_paths(puzzle_input))
