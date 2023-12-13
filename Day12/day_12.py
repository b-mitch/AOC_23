import os
import math

# PART 1

def get_arrangements(row, groups):
    unknowns = [i for i in range(len(row)) if row[i] == '?']
    arrangements = []
    max_gaps = len(row) - sum(groups)
    for index in unknowns:
        arrangement = ''
        i = 0
        groups_i = 0
        gaps = 0
        while i < len(row) and gaps <= max_gaps:
            if row[i] == '.' or (len(arrangement) > 0 and arrangement[-1] == '#'):
                gaps += 1
                arrangement += '.'
            elif row[i] == '?' or row[i] == '#':
                if i < index:
                    if row[i] == '?':
                        arrangement += '.'
                    if row[i] == '#':
                        arrangement += '#'
                else:
                    cont_unknowns = 1
                    while i < len(row) and (row[i] == '?' or row[i] == '#'):
                        if cont_unknowns == groups[groups_i]:
                            arrangement += '#' * cont_unknowns
                            i += cont_unknowns
                            groups_i += 1
                            break
                        cont_unknowns += 1
                        i += 1
                    i -= 1
            i += 1
        # print(i, groups_i)
        if i == len(row) and groups_i == len(groups) - 1:
            print(arrangement)
            if arrangement not in arrangements:
                arrangements.append(arrangement)
                print(arrangements)
    print(len(arrangements))
    # return arrangement_count
        

def sum_arrangements(record):
    arrangements_sum = 0
    with open(record, 'r') as file:
        for line in file:
            line = line.strip()
            i = 0
            spring_row = ''
            cont_key = []
            for char in line:
                if not char.isdigit() and char != ' ' and char != ',':
                    spring_row += char
                if char.isdigit():
                    cont_key.append(int(char))
                i += 1
            arrangements = get_arrangements(spring_row, cont_key)
    #         arrangements_sum += arrangements
    # return arrangements_sum

# PART 2

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'test_puzzleinput.txt')

print(sum_arrangements(puzzle_input))
