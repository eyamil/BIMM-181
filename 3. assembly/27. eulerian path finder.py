import sys
import random

# Given an adjacency list, find an eulerian path through the graph it represents.
# run `python main.py filepath` where the file's lines are in the format
# n -> w,x,y,...,z where n is the starting node, and there are directed edges
# from n to w, x, y, and so on.
# There must be an eulerian path to find for this script to work.

def main():
    file = open(sys.argv[1], "r")
    adj = make_adj_list([line.strip() for line in file.readlines()])
    (sources, sinks) = find_unbalanced_nodes(adj)
    print("->".join(euler_path(adj, sources[0])))
    
def get_all_nodes(pairings_strings):
    node_list = set()
    for line in pairings_strings:
        pairings = line.split("->")
        node_list.add(pairings[0])
        for node in pairings[1].split(","):
            node_list.add(node)
    return node_list

def make_adj_list(pairings_strings):
    adj = {node : [] for node in get_all_nodes(pairings_strings)}
    for line in pairings_strings:
        pairings = line.split(" -> ")
        node = pairings[0]
        adj[node] = pairings[1].split(",")
    return adj

def find_unbalanced_nodes(adj_list):
    degrees = {key: 0 for key in adj_list}
    for from_node, to_nodes in adj_list.items():
        degrees[from_node] -= len(adj_list[from_node])
        for to_node in to_nodes:
            degrees[to_node] += 1
    sources = []
    sinks = []
    for node, degree in degrees.items():
        if degree > 0:
            sinks.append(node)
        elif degree < 0:
            sources.append(node)
    return (sources, sinks)

def euler_path(adj_list, start_node):
    edge_count = sum([len(adj_list[key]) for key in adj_list])
    path = [start_node]
    while (edge_count - (len(path) - 1) > 0):
        new_path = traverse_path(adj_list, path[random.randrange(0, len(path))])
        path = join_paths(path, new_path)
    return path

def join_paths(path_1, path_2):
    insertion_index = path_1.index(path_2[0])
    path_1.pop(insertion_index)
    for i in range(len(path_2)):
        path_1.insert(insertion_index + i, path_2[i])
    return path_1

def traverse_path(adj_list, start):
    path = []
    current_node = start
    path.append(current_node)
    while (len(adj_list[current_node]) > 0):
        current_node = adj_list[current_node].pop()
        path.append(current_node)
    return path

if __name__ == "__main__":
    main()