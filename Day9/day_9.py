import os

# PART 1

# def get_next_value(line):
#     # Get a list of integers for the first line
#     differences = list(map(int, line.split()))
#     # Add this to the differences matrix
#     dif_matrix = [differences]
#     # Keep finding next differences until all values are 0
#     while not all(x == 0 for x in differences):
#         new_differences = [differences[i] - differences[i - 1] for i in range(1, len(differences))]
#         dif_matrix.append(new_differences)
#         differences = new_differences
#     # Traverse the matrix backwards starting at the second to last row, 
#     # increment next_value by last value of the current row
#     row = len(dif_matrix) - 2
#     next_value = 0
#     while row >= 0:
#         next_value += dif_matrix[row][-1]
#         row -= 1

#     return next_value

# def sum_next_values(report):
#     output = 0
#     with open(report, 'r') as file:
#         for line in file:
#             line = line.strip()
#             next_value = get_next_value(line)
#             output += next_value

#     return output

# PART 2

def get_first_value(line):
    # Get a list of integers for the first line
    differences = list(map(int, line.split()))
    # Add this to the differences matrix
    dif_matrix = [differences]
    # Keep finding next differences until all values are 0
    while not all(x == 0 for x in differences):
        new_differences = [differences[i] - differences[i - 1] for i in range(1, len(differences))]
        dif_matrix.append(new_differences)
        differences = new_differences
    # Traverse the matrix backwards starting at the second to last row, 
    # reassign first_value to the difference of that row's original first value 
    # and the previous first_value
    row = len(dif_matrix) - 2
    first_value = 0
    while row >= 0:
        first_value = dif_matrix[row][0] - first_value
        row -= 1
    return first_value

def sum_first_values(report):
    output = 0
    with open(report, 'r') as file:
        for line in file:
            line = line.strip()
            next_value = get_first_value(line)
            output += next_value

    return output

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

print(sum_first_values(puzzle_input))
