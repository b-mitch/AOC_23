import os

# PART 1

def build_list(input):
    hailstones = []
    with open(input, 'r') as file:
        for line in file:
            line = line.strip()
            # Get the starting x and y coordinates of the hailstone
            x = y = ''
            commas = 0
            i = 0
            while commas < 2:
                if line[i] == ',':
                    commas += 1
                if line[i].isdigit():
                    if commas == 0:
                        if line[i - 1] == '-':
                            x += '-'
                        x += line[i]
                    elif commas == 1:
                        if line[i - 1] == '-':
                            y += '-'
                        y += line[i]
                i += 1
            while line[i] != '@':
                i += 1
            i += 1
            # Get the slope of the line created by the hailstone's path
            run = ''
            rise = ''
            while commas < 4:
                if line[i] == ',':
                    commas += 1
                if line[i].isdigit():
                    if commas == 2:
                        if line[i - 1] == '-':
                            run += '-'
                        run += line[i]
                    elif commas == 3:
                        if line[i - 1] == '-':
                            rise += '-'
                        rise += line[i]
                i += 1
            rise = int(rise)
            run = int(run)
            # Need to also get direction the hailstone is moving
            direction = ''
            if run > 0:
                direction = 1
            else:
                direction = -1
            slope = rise/run
            hailstones.append([int(x), int(y), slope, direction])
    return hailstones

def intersection_exists(hailstone1, hailstone2, lower, upper):
    x1, x2 = hailstone1[0], hailstone2[0]
    y1, y2 = hailstone1[1], hailstone2[1]
    m1, m2 = hailstone1[2], hailstone2[2]
    d1, d2 = hailstone1[3], hailstone2[3]
    # Check if lines are parallel and thus never intersect
    if m1 == m2:
        return False
    # Find intersection using linear algebra
    x = (m1*x1 - m2*x2 + (y2 - y1))/(m1 - m2)
    y = m1*x + (y1 - m1*x1)
    # Check intersection is within lower and upper bounds
    if x < lower or y < lower or x > upper or y > upper:
        return False
    # Check if intersection already occurred previously for either line
    if d1 > 0:
        if x < x1:
            return False
        if m1 > 0 and y < y1:
            return False
        if m1 < 0 and y > y1:
            return False
    if d1 < 0:
        if x > x1:
            return False
        if m1 > 0 and y > y1:
            return False
        if m1 < 0 and y < y1:
            return False
    if d2 > 0:
        if x < x2:
            return False
        if m2 > 0 and y < y2:
            return False
        if m2 < 0 and y > y2:
            return False
    if d2 < 0:
        if x > x2:
            return False
        if m2 > 0 and y > y2:
            return False
        if m2 < 0 and y < y2:
            return False
    return True

def count_intersections(input, lower, upper):
    hailstones = build_list(input)
    i = 0
    count = 0
    for hailstone1 in hailstones:
        for j in range(i + 1, len(hailstones)):
            hailstone2 = hailstones[j]
            if intersection_exists(hailstone1, hailstone2, lower, upper):
                count += 1
        i += 1
    return count

# PART 2

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

print(count_intersections(puzzle_input, 200000000000000, 400000000000000))
