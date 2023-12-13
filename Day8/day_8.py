import os
import math
# PART 1

# def process_map(map):
#     directions = []
#     map_dict = dict()
#     # Convert the txt file into a list of directions and an adjacency map
#     with open(map, 'r') as file:
#         line1 = file.readline().strip()
#         for direction in line1:
#             directions.append(direction) 
#         file.readline()
#         for line in file:
#             line = line.strip()
#             node = ''
#             left = ''
#             right = ''
#             for i in range(3):
#                 node += line[i]
#             for i in range(7,10):
#                 left += line[i]
#             for i in range(12,15):
#                 right += line[i]
#             map_dict[node] = (left, right)
#     return directions, map_dict          

# def get_steps(map):
#     directions, map_dict = process_map(map)
#     steps = 0
#     i = 0
#     node = 'AAA'
#     # Iterate the directions, moving through the map each iteration
#     while True:
#         direction = directions[i]
#         index = 0 if direction == 'L' else 1
#         node = map_dict[node][index]
#         steps += 1
#         if node == 'ZZZ':
#             return steps
#         if i == len(directions) - 1:
#             i = 0
#         else:
#             i += 1

# PART 2

def process_map(map):
    directions = []
    map_dict = dict()
    # Convert the txt file into a list of directions and an adjacency map
    with open(map, 'r') as file:
        line1 = file.readline().strip()
        for direction in line1:
            directions.append(direction) 
        file.readline()
        for line in file:
            line = line.strip()
            node = ''
            left = ''
            right = ''
            for i in range(3):
                node += line[i]
            for i in range(7,10):
                left += line[i]
            for i in range(12,15):
                right += line[i]
            map_dict[node] = (left, right)
    return directions, map_dict          

def get_steps(map):
    directions, map_dict = process_map(map)
    nodes = []
    steps_list = []
    # Add all start nodes (nodes ending in 'A')
    for key in map_dict.keys():
        if key[-1] == 'A':
            nodes.append(key)
    # Iterate the directions, moving through the map for each start node 
    # and save the number of steps to reach the end
    for j in range(len(nodes)):
        i = 0
        steps = 0
        while True:
            direction = directions[i]
            index = 0 if direction == 'L' else 1
            next_node = map_dict[nodes[j]][index]
            steps += 1
            if next_node[-1] == 'Z':
                steps_list.append(steps)
                break
            nodes[j] = next_node
            if i == len(directions) - 1:
                i = 0
            else:
                i += 1
    # Return the lowest common multiple of the steps
    return math.lcm(*steps_list)

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

print(get_steps(puzzle_input))
