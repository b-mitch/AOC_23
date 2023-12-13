# PART 1

# def is_possible(game):
#     cubes = {'red': 12, 'green': 13, 'blue': 14}
#     i = 0
#     while game[i] != ':':
#         i += 1
#     count = ''
#     color = ''
#     while i < len(game):
#         while i < len(game) and game[i].isdigit():
#             count += game[i]
#             i += 1
#         while i < len(game) and game[i].isalpha():
#             color += game[i]
#             i += 1
#         if i >= len(game) or game[i] == ',' or game[i] == ';':
#             if int(count) > cubes[color]:
#                 return False
#             else:
#                 count = ''
#                 color = ''
#         i += 1 
#     return True    

# def get_possibility_sum(games_doc):
#     possibility_sum = 0 
#     count = 1

#     with open(games_doc, 'r') as file:
#         for line in file:
#             if is_possible(line.strip()):
#                 possibility_sum += count
#             count += 1

#     return possibility_sum

# PART 2

def get_min_cubes(game):
    cubes = {'red': 0, 'green': 0, 'blue': 0}
    i = 0
    while game[i] != ':':
        i += 1
    count = ''
    color = ''
    while i < len(game):
        while i < len(game) and game[i].isdigit():
            count += game[i]
            i += 1
        while i < len(game) and game[i].isalpha():
            color += game[i]
            i += 1
        if i >= len(game) or game[i] == ',' or game[i] == ';':
            if int(count) > cubes[color]:
                cubes[color] = int(count)
            count = ''
            color = ''
        i += 1 
    return cubes  

def get_powers_sum(games_doc):
    powers_sum = 0 

    with open(games_doc, 'r') as file:
        for line in file:
            power = 1
            cubes = get_min_cubes(line.strip())
            for value in cubes.values():
                power *= value
            powers_sum += power

    return powers_sum

import os

# Tests

cubes = {'red': 12, 'green': 13, 'blue': 14}
puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

# print(get_min_cubes('Game 6: 3 blue, 10 green, 2 red; 5 green; 6 blue, 3 red'))
print(get_powers_sum(puzzle_input))
