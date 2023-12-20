import os

# PART 1

def process_doc(doc):
    workflows = dict()
    parts = []
    # Traverse our input to build workflow map and parts list of lists
    with open(doc, 'r') as file:
        line = file.readline().strip()
        while line != '':
            next_line = file.readline().strip()
            i = 0
            # Build the key
            workflow_key = ''
            while line[i] != '{':
                workflow_key += line[i]
                i += 1
            i += 1
            # Build the value
            workflow_val = ''
            while line[i] != '}':
                workflow_val += line[i]
                i += 1
            workflows[workflow_key] = workflow_val
            line = next_line
        line = file.readline().strip()
        while line != '':
            next_line = file.readline()
            # Build part list and add each to parts
            part = []
            i = 1
            while line[i] != '}':
                rating = ''
                if line[i].isdigit():
                    while line[i].isdigit():
                        rating += line[i]
                        i += 1
                    part.append((rating))
                else:
                    i += 1
            parts.append(part)
            line = next_line

    return workflows, parts

def process_part(part, workflows):
    current_key = 'in'
    ratings = 'xmas'
    # Push part through workflows
    while True:
        current_flow = workflows[current_key]
        i = 0
        # Push part through individual workflow
        while True:
            # Check if end of the current flow (no more comparisons) has been reached
            if current_flow[i] not in ratings or (i + 1 < len(current_flow) and current_flow[i + 1].isalpha()):
                destination = ''
                while i < len(current_flow) and current_flow[i] != ',':
                    destination += current_flow[i]
                    i += 1
                if destination == 'A':
                    return sum(int(rating) for rating in part)
                if destination == 'R':
                    return 0
                current_key = destination
                break
            # Sub part type for correct current part rating
            part_index = ratings.index(current_flow[i])
            comparison = part[part_index]
            i += 1
            # Build the rest of the comparison expression
            while i < len(current_flow) and current_flow[i] != ':':
                comparison += current_flow[i]
                i += 1
            # Build the destination string
            destination = ''
            i += 1
            while i < len(current_flow) and current_flow[i] != ',':
                destination += current_flow[i]
                i += 1
            # Evaluate the comparison (EVAL OK SINCE INPUT SOURCE TRUSTED)
            result = eval(comparison)
            # If result is true, add Accepted and ignore Rejected or move to next flow
            if result:
                if destination == 'A':
                    return sum(int(rating) for rating in part)
                if destination == 'R':
                    return 0
                current_key = destination
                break
            else:
                i += 1        


def get_accepted_part_sum(doc):
    workflows, parts = process_doc(doc)
    # print(workflows)
    # print(parts)
    total = 0
    for part in parts:
        total += process_part(part, workflows)

    return total
            

# PART 2

# Helper function to get opposite of the expression
def anti(expression):
    if expression[1] == '>':
        expression = expression[0] + '<' + expression[2:]
    else:
        expression = expression[0] + '>' + expression[2:]
    return expression

def process_doc(doc):
    workflows = dict()
    # Traverse our input to build workflow map and parts list of lists
    with open(doc, 'r') as file:
        line = file.readline().strip()
        while line != '':
            next_line = file.readline().strip()
            i = 0
            # Build the key
            workflow_key = ''
            while line[i] != '{':
                workflow_key += line[i]
                i += 1
            i += 1
            # Build the value
            workflow_val = []
            antis = []
            while line[i] != '}':
                # Build the comparison expression
                comparison = ''
                # If anti destination reached, add it along with the anti comparisons to workflow
                while line[i] != '}' and line[i] != ':':
                    comparison += line[i]
                    i += 1
                if line[i] == '}':
                    workflow_val.append((antis,comparison))
                    break
                # Add it to our anti-expressions list
                antis.append(anti(comparison))
                i += 1
                # Build the destination string
                destination = ''
                while line[i] != ',':
                    destination += line[i]
                    i += 1
                # Add comparison and destination to workflow
                workflow_val.append((comparison, destination))
                i += 1
            # Add the workflow to workflows map
            workflows[workflow_key] = workflow_val
            line = next_line
        line = file.readline().strip()

    return workflows

def get_paths_helper(workflows, paths, path, wf_key):
    # Base cases
    # If 'R' reached, return to previous step
    if wf_key == 'R':
        return
    # If 'A' reached, add current path to paths and return to previous step
    if wf_key == 'A':
        paths.append(path)
        return
    
    current_wf = workflows[wf_key]
    
    if path is None:
        path = []
    # At each step in the path, add the comparison to the path and recurse comparison's destination
    for step in current_wf:
        if isinstance(step[0], list):
            for anti in step[0]:
                path.append(anti)
        else:
            path.append(step[0])
        get_paths_helper(workflows, paths, path.copy(), step[1])
        if isinstance(step[0], list):
            for anti in step[0]:
                path.remove(anti)
        else:
            path.remove(step[0])

# Helper function to start recursive creation of accepted paths
def get_paths(workflows):
    paths = []
    get_paths_helper(workflows, paths, None, 'in')
    return paths

def get_rating_range(path):
    rating_ranges = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]
    ratings = 'xmas'
    for step in path:
        rating_index = ratings.index(step[0])
        rating_range = rating_ranges[rating_index]
        lower_bound, upper_bound = rating_range[0], rating_range[1]
        operator = step[1]
        new_bound = int(step[2:])
        if operator == '>':
            if new_bound > lower_bound:
                rating_ranges[rating_index][0] = new_bound + 1
        else:
            if new_bound < upper_bound:
                rating_ranges[rating_index][1] = new_bound - 1
    return rating_ranges

def get_accepted_combos(doc):
    workflows = process_doc(doc)
    # print(workflows)
    accepted_paths = get_paths(workflows)
    # print(accepted_paths)
    rating_ranges = []
    for path in accepted_paths:
        # print(path)
        rating_ranges.append(get_rating_range(path))
    # print(rating_ranges)
    valid_ranges = []
    for ranges in rating_ranges:
        is_valid = all(rating_range[0] < rating_range[1] for rating_range in ranges)
        if is_valid and ranges not in valid_ranges:
            valid_ranges.append(ranges)
    # print(valid_ranges)
    total = 0
    available = [[0, 4001] for _ in range(4)]
    # UNSOLVED - becomes a complicated intervals problem where you have to create availability intervals based on ranges already used
    for ranges in valid_ranges:
        path_options = 1 
        print('\n')
        print(ranges)
        i = 0
        for lower, upper in ranges:
            if available[i][0] >= available[i][1]:
                i += 1
                continue
            # THIS IS WHERE IT GETS TRICKY!!
            if lower > available[i][0] and upper < available[i][1]:
                # NEED TO SPLIT THIS AVAILABILITY INTERVAL INTO TWO INTERVALS
                path_options *= (upper - lower + 1)
                available[i][0] = upper + 1
            elif lower > available[i][0] and upper > available[i][1]:
                path_options *= (upper - lower + 1)
                available[i][0] = available[i][1]

            i += 1

        total += path_options
        print(available)

    return total # solution 167409079868000

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'test_puzzleinput.txt')

# print(get_accepted_part_sum(puzzle_input))
print(get_accepted_combos(puzzle_input))
