import os
# PART 1

def get_win_product(matrix):
    output = 1
    c = 0
    # Iterate each column 
    while c < len(matrix[0]):
        total_time = matrix[0][c]
        record = matrix[1][c]
        win_count = 0
        # Compare hold time options and their results with the record
        for t in range(total_time + 1):
            time_remaining = total_time - t
            distance = t * time_remaining
            if distance > record:
                win_count += 1
        output *= win_count
        c += 1
    return output


def win_options_product(races):
    matrix = []
    # Convert file into matrix
    with open(races, 'r') as file:
        for line in file:
            numbers = []
            i = 0
            while i < len(line):
                number = ''
                if line[i].isdigit():
                    while i < len(line) and line[i].isdigit():
                        number += line[i]
                        i += 1
                    numbers.append(int(number))
                i += 1
            matrix.append(numbers)
    return get_win_product(matrix)


# PART 2

def get_win_count(arr):
    total_time = arr[0]
    record = arr[1]
    win_start = 0
    # Compare hold time options and their results with the record
    for t in range(total_time + 1):
        time_remaining = total_time - t
        distance = t * time_remaining
        # Once the first win is found, we now know how many total win options there are
        if distance > record:
            win_start = t
            break
    win_count = total_time - (2 * win_start) + 1
    return win_count


def win_options(race):
    arr = []
    # Convert file into list
    with open(race, 'r') as file:
        for line in file:
            i = 0
            number = ''
            while i < len(line):
                if line[i].isdigit():
                    while i < len(line) and line[i].isdigit():
                        number += line[i]
                        i += 1
                i += 1
            arr.append(int(number))
    return get_win_count(arr)

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

print(win_options(puzzle_input))
