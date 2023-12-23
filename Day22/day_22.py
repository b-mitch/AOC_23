import os

# PART 1

def process_file(snapshot):
    brick_map = dict()
    brick_list = []
    with open(snapshot, 'r') as file:
        i = 0
        for line in file:
            i += 1
            brick = []
            coords1 = []
            coords2 = []
            first_half = True
            for char in line.strip():
                if char.isdigit():
                    if first_half:
                        coords1.append(int(char))
                    else:
                        coords2.append(int(char))
                if char == '~':
                    first_half = False
            brick.extend([(coords1[0],coords2[0]), (coords1[1],coords2[1]), (coords1[2],coords2[2])])
            brick_list.append(i)
            brick_map[i] = brick
    return brick_map, brick_list

def intervals_overlap(interval1, interval2):
    # Check if any edge values are shared = overlap
    for numb in interval1:
        if numb in interval2:
            return True
    # Check if inside of intervals overlap
    if (interval1[0] > interval2[0] and interval1[0] < interval2[1]) or (interval2[0] > interval1[0] and interval2[0] < interval1[1]):
        return True
    return False
    
def lower_bricks(bricks, n):
    # Traverse bricks from lowest first
    for brick1, coords1 in bricks.items():
        xr1, yr1, zr1 = coords1[0], coords1[1], coords1[2]
        # If no bricks below, drop till there is a brick below
        if brick1 > 1 and (bricks[brick1 - 1][2][1] + 1) < zr1[0]:
            level_dif = zr1[0] - bricks[brick1 - 1][2][1] - 1
            bricks[brick1][2] = (zr1[0] - level_dif, zr1[1] - level_dif)
            zr1 = bricks[brick1][2]
        # Compare brick with bricks below it
        z_dif = 0
        for brick2 in range(brick1 - 1, 0, -1):
            coords2 = bricks[brick2]
            xr2, yr2, zr2 = coords2[0], coords2[1], coords2[2]
            # If brick below blocks brick, break
            if intervals_overlap(xr1, xr2) and intervals_overlap(yr1, yr2):
                if zr1[0] - zr2[1] == z_dif:
                    z_dif = 0
                    break
            else: # Save level
                z_dif = zr1[0] - zr2[1]
        if z_dif > 0: 
            bricks[brick1][2] = (zr1[0] - z_dif, zr1[1] - z_dif)
            # Also slide all bricks above down by same amount
            for j in range(brick1 + 1, n + 1):
                zr3 = bricks[j][2]
                bricks[j][2] = (zr3[0] - z_dif, zr3[1] - z_dif)

def can_disintigrate(brick1, bricks, total_supports):
    is_supported = 0
    xr1, yr1, zr1 = bricks[brick1][0], bricks[brick1][1], bricks[brick1][2]
    brick2 = brick1 - 1 
    while brick2 > 0 and (zr1[0] == bricks[brick2][2][1]):
        brick2 -= 1
    supports = []
    while brick2 > 0 and (zr1[0] - bricks[brick2][2][1]) == 1:
        # print(brick1, brick2)
        coords2 = bricks[brick2]
        xr2, yr2 = coords2[0], coords2[1]
        if intervals_overlap(xr1, xr2) or intervals_overlap(yr1, yr2):
            supports.append(brick2)
            is_supported += 1
            if is_supported > 1:
                for support in supports:
                    if support not in total_supports:
                        total_supports.append(support)
        brick2 -= 1
    # print('BRICK',brick1,'HAS',supports,'SUPPORTS')

def count_can_disintigrate(snapshot):
    brick_map, brick_list = process_file(snapshot)
    brick_list = sorted(brick_list, key=lambda x: brick_map[x][2][0])
    print(brick_map)
    print(brick_list)
    lower_bricks(brick_map, len(brick_list))
    print(brick_map)
    # For each brick, count how many bricks support it, if greater than one, increment count by number of supports
    supports = []
    for brick in brick_list:
        can_disintigrate(brick, brick_map, supports)
    count = len(supports)
    # Account for top level bricks since they don't support anything
    count += sum(coords[2][0] == max(coords[2][0] for coords in brick_map.values()) for coords in brick_map.values())
    return count

# PART 2

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'test_puzzleinput.txt')

print(count_can_disintigrate(puzzle_input))
