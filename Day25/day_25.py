import os
from itertools import combinations
from collections import deque
import networkx as nx

# PART 1

def build_graph(input):
    adj_list = dict()
    with open(input, 'r') as file:
        for line in file:
            line = line.strip()
            i = 0
            node1 = ''
            while line[i] != ':':
                node1 += line[i]
                i += 1
            i += 1
            if node1 not in adj_list:
                adj_list[node1] = []
            while i < len(line):
                node2 = ''
                while i < len(line) and line[i].isalpha():
                    node2 += line[i]
                    i += 1
                if node2 != '': 
                    if node2 not in adj_list[node1]:
                        adj_list[node1].append(node2)
                    if node2 not in adj_list:
                        adj_list[node2] = []
                    if node1 not in adj_list[node2]:
                        adj_list[node2].append(node1)
                i += 1
    return adj_list    

def split_graph(diagram):
    graph = build_graph(diagram)
    G = nx.Graph(graph)
    min_cut_edges = nx.minimum_edge_cut(G)
    G.remove_edges_from(min_cut_edges)
    connected_components = list(nx.connected_components(G))
    total = 1
    for graphx in connected_components:
        count = len(graphx)
        total *= count
    return total
    

# PART 2

# TESTS

puzzle_input = os.path.join(os.path.dirname(__file__), 'puzzleinput.txt')

print(split_graph(puzzle_input))
