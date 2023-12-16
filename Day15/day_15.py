import os

# PART 1

# # Helper hash function
# def get_hash_value(string):
#     current_value = 0
#     for char in string:
#         ascii_value = ord(char)
#         current_value += ascii_value
#         current_value *= 17
#         current_value %= 256
#     return current_value

# def sum_hash_values(init_seq):
#     hash_total = 0
#     hash_str = ''
#     with open(init_seq, 'r') as file:
#         for line in file:
#             line = line.strip()
#             i = 0
#             while i < len(line):
#                 # Add characters to hash string until a ',' is reached
#                 while i < len(line) and line[i] != ',':
#                     hash_str += line[i]
#                     i += 1
#                 # Only calculate hash value when a ',' is reached
#                 if i < len(line) and line[i] == ',':
#                     hash_value = get_hash_value(hash_str)
#                     # print(hash_value)
#                     hash_total += hash_value
#                     hash_str = ''
#                 i += 1
#     final_hash_value = get_hash_value(hash_str)
#     hash_total += final_hash_value
#     return hash_total 

# PART 2

# Helper hash function
def get_hash_value(string):
    current_value = 0
    for char in string:
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value %= 256
    return current_value

# Helper function to get total focal power of lenses
def get_fp(boxes, focal_map):
    total = 0
    for number, lenses in boxes.items():
        for i, lense in enumerate(lenses):
            focal_power = (1 + number) * (i + 1) * focal_map[lense]
            # print(focal_power)
            total += focal_power
    return total


def sum_hash_values(init_seq):
    boxes = {x: [] for x in range(256)}
    focal_map = dict()
    label = ''
    symbol = None
    fl = 0
    with open(init_seq, 'r') as file:
        for line in file:
            line = line.strip()
            i = 0
            while i < len(line):
                # Add characters to hash string until a '=' or '-' is reached
                while i < len(line) and line[i] != '=' and line[i] != '-':
                    label += line[i]
                    i += 1
                # print(label)
                # Save symbol unless end of line reached
                if i < len(line):
                    symbol = line[i]
                    i += 1
                    if line[i].isdigit():
                        fl = int(line[i])
                        i += 1
                    # Calculate hash value
                    hash_value = get_hash_value(label)
                    # print(boxes)
                    if symbol == '-':
                        # Run dash instructions removing the label from the box and focal length map
                        if label in boxes[hash_value]:
                            boxes[hash_value].remove(label)
                            del focal_map[label]
                    elif symbol == '=':
                        # Run equal instructions, adding or updating the lense in the right box
                        focal_map[label] = fl
                        if label not in boxes[hash_value]:
                            boxes[hash_value].append(label)
                    label = ''
                i += 1
    total_focal_power = get_fp(boxes, focal_map)
    return total_focal_power 

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

# print(get_hash_value('HASH'))

print(sum_hash_values(puzzle_input))
