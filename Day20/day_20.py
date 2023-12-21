import os

# PART 1

def build_graph(input):
    adj_list = dict()
    modules = {'broadcaster': [None, False]}
    with open(input, 'r') as file:
        for line in file:
            line = line.strip()
            i = 0
            module_type = ''
            node = ''
            # For each line, save the transmitting module name and type
            while line[i] != ' ':
                if not line[i].isalpha():
                    module_type = line[i]
                    i += 1
                node += line[i]
                i += 1
            # For all modules except the broadcaster, add to type map
            if module_type != '':
                modules[node] = [module_type, False]
            # Skip to the receiving modules
            while not line[i].isalpha():
                i += 1
            children = []
            # Add receiving modules to a list
            while i < len(line): 
                child = ''
                while i < len(line) and line[i] != ',':
                    child += line[i]
                    i += 1
                children.append(child)
                i += 2
            # Save transmitting module and its receiving modules to the adjacency list
            adj_list[node] = children
    return adj_list, modules

# Helper function to build map of input modules to conjunctions
def build_conj_map(graph, modules):
    conjunctions_map = dict()
    for key, values in graph.items():
        for value in values:
            if value in modules and modules[value][0] == '&':
                if value not in conjunctions_map:
                    conjunctions_map[value] = [key]
                else:
                    conjunctions_map[value].append(key)
    return conjunctions_map

def bf_traverse(graph, modules, conjunctions):
    highs, lows = 0, 1
    # Create and start queue with root (broadcaster) module
    queue = []
    queue.append('broadcaster')
    while len(queue) > 0:
        transmitter = queue.pop(0)
        # print(transmitter)
        # Get transmitter state
        trans_state = modules[transmitter][1] if transmitter in modules else False
        # print(trans_state)
        # Add receiving modules to queue and update their status
        for receiver in graph[transmitter]:
            if not trans_state:
                lows += 1
            else:
                highs += 1
            if receiver not in graph:
                continue
            rec_type = modules[receiver][0]
            rec_state = modules[receiver][1]
            # Flip-flop modules flip only if receiving a low pulse
            if rec_type == '%' and not trans_state:
                modules[receiver][1] = not rec_state
                # Only add them to the queue when this happens
                queue.append(receiver)
            # Conjunction modules send low pulses only if receiving all high pulses, otherwise they send low pulses
            if rec_type == '&':
                modules[receiver][1] = False if all(modules[connected_module][1] for connected_module in conjunctions[receiver]) else True
                # Always add conjunction receivers to queue
                queue.append(receiver)
    return highs, lows


def get_pulses(input):
    # Build an adjacency list for our graph and a map to track module type and state
    graph, modules = build_graph(input)
    # Init conjunctions map to keep track of all pulses being sent to each conjunction module
    conjunctions = build_conj_map(graph, modules)
    # print(graph)
    # print(modules)
    # print(conjunctions)
    # Similate 1000 button pushes and breadth first traverse the graph to get total high and low pulses
    total_highs = total_lows = 0
    for _ in range(1000):
        highs, lows = bf_traverse(graph, modules, conjunctions)
        # print(modules)
        total_highs += highs
        total_lows += lows
    # print(total_highs, total_lows)
    return total_highs * total_lows

# PART 2

def build_graph(input):
    adj_list = dict()
    modules = {'broadcaster': [None, False]}
    with open(input, 'r') as file:
        for line in file:
            line = line.strip()
            i = 0
            module_type = ''
            node = ''
            # For each line, save the transmitting module name and type
            while line[i] != ' ':
                if not line[i].isalpha():
                    module_type = line[i]
                    i += 1
                node += line[i]
                i += 1
            # For all modules except the broadcaster, add to type map
            if module_type != '':
                modules[node] = [module_type, False]
            # Skip to the receiving modules
            while not line[i].isalpha():
                i += 1
            children = []
            # Add receiving modules to a list
            while i < len(line): 
                child = ''
                while i < len(line) and line[i] != ',':
                    child += line[i]
                    i += 1
                children.append(child)
                i += 2
            # Save transmitting module and its receiving modules to the adjacency list
            adj_list[node] = children
    return adj_list, modules

# Helper function to build map of input modules to conjunctions
def build_conj_map(graph, modules):
    conjunctions_map = dict()
    for key, values in graph.items():
        for value in values:
            if value in modules and modules[value][0] == '&':
                if value not in conjunctions_map:
                    conjunctions_map[value] = [key]
                else:
                    conjunctions_map[value].append(key)
    return conjunctions_map

def bf_traverse(graph, modules, conjunctions):
    # Create and start queue with root (broadcaster) module
    queue = []
    queue.append('broadcaster')
    while len(queue) > 0:
        transmitter = queue.pop(0)
        # print(transmitter)
        # Get transmitter state
        trans_state = modules[transmitter][1] if transmitter in modules else False
        # print(trans_state)
        # Add receiving modules to queue and update their status
        for receiver in graph[transmitter]:
            if receiver == 'rx' and not trans_state:
                return True
            if receiver not in graph:
                continue
            rec_type = modules[receiver][0]
            rec_state = modules[receiver][1]
            # Flip-flop modules flip only if receiving a low pulse
            if rec_type == '%' and not trans_state:
                modules[receiver][1] = not rec_state
                # Only add them to the queue when this happens
                queue.append(receiver)
            # Conjunction modules send low pulses only if receiving all high pulses, otherwise they send low pulses
            if rec_type == '&':
                modules[receiver][1] = False if all(modules[connected_module][1] for connected_module in conjunctions[receiver]) else True
                # Always add conjunction receivers to queue
                queue.append(receiver)
    return False


def fewest_pushes(input):
    # Build an adjacency list for our graph and a map to track module type and state
    graph, modules = build_graph(input)
    # Init conjunctions map to keep track of all pulses being sent to each conjunction module
    conjunctions = build_conj_map(graph, modules)
    # print(graph)
    # print(modules)
    # print(conjunctions)
    # Similate button pushes and breadth first traverse the graph to until final module gets a low pulse
    for x in range(1000000000):
        print(x)
        if bf_traverse(graph, modules, conjunctions):
            return x + 1

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

# print(get_pulses(puzzle_input))
print(fewest_pushes(puzzle_input))
