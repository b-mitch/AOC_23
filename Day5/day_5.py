import os
# PART 1

# # Helper function to iterate first line and return a list of the seeds
# def get_seeds(file):
#     seeds = []
#     seed_line = file.readline().strip()
#     i = 0
#     while i < len(seed_line):
#         if seed_line[i].isdigit():
#             number = ''
#             while i < len(seed_line) and seed_line[i].isdigit():
#                 number += seed_line[i]
#                 i += 1
#             seeds.append(int(number))
#         else:
#             i += 1

#     return seeds

# # Helper function to process each value through each map
# def process_value(values, map):
#     ranges = []
#     # Iterate each map entry and determine the source range plus the conversion factor between source and destination for that range
#     for item in map:
#         destination, source, r = item[0], item[1], item[2]
#         range_conversion = (source, source + r, destination - source)
#         ranges.append(range_conversion)
#     # Check each range to see if value falls within it, if so, update the value
#     for i in range(len(values)):
#         for r in ranges:
#             if values[i] >= r[0] and values[i] <= r[1]:
#                 values[i] += r[2]
#                 break

#     return values
        

# def get_locations(values, file):
#     # Track current map
#     current_map = []
#     for line in file:
#         line = line.strip()
#         # If line is blank and there is a map, push the seed through that map and reset map
#         if len(line) <= 0 and len(current_map) > 0:
#             values = process_value(values, current_map)
#             current_map = []
#             continue
#         # If line has digits, it's a map
#         if len(line) > 0 and line[0].isdigit():
#             i = 0
#             line_map = []
#             while i < len(line):
#                 number = ''
#                 while i < len(line) and line[i].isdigit():
#                     number += line[i]
#                     i += 1
#                 line_map.append(int(number))
#                 i += 1
#             current_map.append(line_map)
#     # Process final map
#     values = process_value(values, current_map)

#     return values


# def get_min_location(almanac):
#     # Get seeds
#     with open(almanac, 'r') as file:
#         seeds = get_seeds(file)
#         # Iterate seeds and get final location for each
#         locations = get_locations(seeds, file)
#     return min(locations)

# PART 2

def get_seeds(file):
    seed_ranges = []
    seed_line = file.readline().strip()
    i = 0
    current_range = []
    # Iterate first line and get a list of seed ranges
    while i < len(seed_line):
        if seed_line[i].isdigit():
            number = ''
            while i < len(seed_line) and seed_line[i].isdigit():
                number += seed_line[i]
                i += 1
            if len(current_range) == 0:
                current_range.append(int(number))
            elif len(current_range) == 1:
                current_range.append(current_range[0] + int(number) - 1)
                seed_ranges.append(current_range)
                current_range = []              
        else:
            i += 1
    # print(seed_ranges)
    return seed_ranges

# Helper function to process each value through each map
def process_value(value_ranges, map):
    # Iterate each map entry and determine the source range plus the conversion factor between source and destination for that range
    map_ranges = [(item[1], item[1] + item[2] - 1, item[0] - item[1]) for item in map]
    map_ranges = sorted(map_ranges, key=lambda x: x[0])
    # Iterate each range of seeds and check if it fits within a map range, if so update seed range
    # If the range does not fit within any map range, split the range and adjust each side by the applicable map range
    # print(value_ranges)
    # print(map_ranges)
    updated_ranges = []
    for vr in value_ranges:
        updated_range = vr
        for mr in map_ranges:
            if vr[0] >= mr[0] and vr[1] <= mr[1]:
                updated_range = [vr[0] + mr[2], vr[1] + mr[2]]
                break
            if vr[0] < mr[0] and vr[1] >= mr[0]:
                start = mr[0] + mr[2]
                end = vr[1] + mr[2]
                new_range = [start, end]
                updated_ranges.append(new_range)
                updated_range = [vr[0], mr[0] - 1]
                for mr in map_ranges:
                    if updated_range[0] >= mr[0] and updated_range[1] <= mr[1]:
                        updated_range = [updated_range[0] + mr[2], updated_range[1] + mr[2]]
                        break

        updated_ranges.append(updated_range)
    
    return updated_ranges
        

def get_locations(value_ranges, file):
    # Track current map
    current_map = []
    for line in file:
        line = line.strip()
        # If line is blank and there is a map, push the seed ranges through that map and reset map
        if len(line) <= 0 and len(current_map) > 0:
            value_ranges = process_value(value_ranges, current_map)
            current_map = []
            continue
        # If line has digits, it's a map
        if len(line) > 0 and line[0].isdigit():
            i = 0
            line_map = []
            while i < len(line):
                number = ''
                while i < len(line) and line[i].isdigit():
                    number += line[i]
                    i += 1
                line_map.append(int(number))
                i += 1
            current_map.append(line_map)
    # Process final map
    value_ranges = process_value(value_ranges, current_map)

    return value_ranges


def get_min_location(almanac):
    # Get seed ranges
    with open(almanac, 'r') as file:
        seed_ranges = get_seeds(file)
        # Iterate seed ranges and get location ranges
        locations = get_locations(seed_ranges, file)
    return min(min(location) for location in locations)

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'test_puzzleinput.txt')


print(get_min_location(puzzle_input))
