import os
# PART 1

# def is_symbol(char):
#     if char.isdigit() or char.isalpha() or char == '.':
#         return False
#     return True

# def is_symbol_adjacent(prev_line, next_line, current_line, start, end):
#     # Check same line to each side of number
#     if start > 0 and is_symbol(current_line[start - 1]):
#         return True
#     if end < len(current_line) - 1 and is_symbol(current_line[end + 1]):
#         return True
#     # Check above & below line, including diagonals
#     if prev_line is not None:
#         index = start - 1 if start > 0 else 0
#         while index < end + 2 and index < len(prev_line):
#             if index >=0 and is_symbol(prev_line[index]):
#                 return True
#             index += 1
#     if next_line is not None:
#         index = start - 1 if start > 0 else 0
#         while index < end + 2 and index < len(next_line):
#             if index >=0 and is_symbol(next_line[index]):
#                 return True
#             index += 1

# def sum_part_numbers(schematic):
#     part_numbers_sum = 0
#     prev_line = None
#     next_line = None
#     # Open the file and manually iterate each line
#     with open(schematic, 'r') as file:
#         current_line = file.readline().strip()
#         while current_line:
#             # Store next line without whitespace or set to None if end of file reached
#             next_line = file.readline()
#             if next_line == '':
#                 next_line = None
#             else:
#                 next_line = next_line.strip()
#             if next_line is not None:
#                 next_line = next_line.strip()
#             # Manually iterate through characters in each line
#             i = 0
#             while i < len(current_line):
#                 start = 0
#                 end = 0
#                 part_number = ''
#                 # If a part number is found, save the number and its start & end indices
#                 if current_line[i].isdigit():
#                     start = i
#                 while i < len(current_line) and current_line[i].isdigit():
#                     part_number += current_line[i]
#                     i += 1
#                 end = i - 1
#                 # If a symbol is adjacent to the part number, add the part number to the sum
#                 if part_number != '' and is_symbol_adjacent(prev_line, next_line, current_line, start, end):
#                     part_numbers_sum += int(part_number)
#                 i += 1
#             prev_line = current_line
#             current_line = next_line

#     return part_numbers_sum

# PART 2

def get_numbers(line, index, output):
    i = index
    # Iterate the line within the bounds of adjacency to the gear (index to index + 2)
    while i > 0 and i < len(line) and i <= index + 2:
        # If a digit is found, use two pointers to mark the start and end of the number and add it to output
        if line[i].isdigit():
            start = end = i
            while start >= 0 and end < len(line) and (line[start].isdigit() or line[end].isdigit()):
                if line[start].isdigit():
                    start -= 1
                if line[end].isdigit():
                    end += 1
            output.append(line[start + 1:end])
            i = end - 1
        i += 1

def get_gear_products(prev_line, next_line, current_line, index):
    output = []
    # Check same line to each side of number
    if index > 0 and current_line[index - 1].isdigit():
        i = end = index - 1
        while i > 0 and current_line[i].isdigit():
            i -= 1
        start = i + 1
        output.append(current_line[start:end + 1])
    if index < len(current_line) and current_line[index + 1].isdigit():
        i = start = index + 1
        while i < len(current_line) and current_line[i].isdigit():
            i += 1
        end = i
        output.append(current_line[start:end])
    # Check above & below line, including diagonals
    if prev_line is not None:
        get_numbers(prev_line, index - 1, output)
    if next_line is not None:
        get_numbers(next_line, index - 1, output)

    return output

def sum_gear_ratios(schematic):
    gear_ratios_sum = 0
    prev_line = None
    next_line = None
    # Open the file and manually iterate each line
    with open(schematic, 'r') as file:
        current_line = file.readline().strip()
        while current_line:
            # Store next line without whitespace or set to None if end of file reached
            next_line = file.readline()
            if next_line == '':
                next_line = None
            else:
                next_line = next_line.strip()
            if next_line is not None:
                next_line = next_line.strip()
            # Manually iterate through characters in each line
            i = 0
            while i < len(current_line):
                # If a gear, save the number and its start & end indices
                if current_line[i] == '*':
                    # If a symbol is adjacent to the part number, add the part number to the sum
                    gear_products = get_gear_products(prev_line, next_line, current_line, i)
                    if len(gear_products) == 2:
                        gear_ratio = int(gear_products[0]) * int(gear_products[1])
                        gear_ratios_sum += gear_ratio
                i += 1
            prev_line = current_line
            current_line = next_line

    return gear_ratios_sum

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

print(sum_gear_ratios(puzzle_input))
