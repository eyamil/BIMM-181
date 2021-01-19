import sys
import random

# Given an adjacency list, find an eulerian cycle through the graph it represents.
# run `python main.py filepath` where the file's lines are in the format
# n -> w,x,y,...,z where n is the starting node, and there are directed edges
# from n to w, x, y, and so on.
# There must be an eulerian cycle to find for this script to work.

def main():
    file = open(sys.argv[1], "r")
    adj = make_adj_list([line.strip() for line in file.readlines()])
    print("->".join(euler_cycle(adj, list(adj.keys())[0])))
    
def make_adj_list(pairings_strings):
    adj = {}
    for line in pairings_strings:
        pairings = line.split(" -> ")
        node = pairings[0]
        adj[node] = pairings[1].split(",")
    return adj

def euler_cycle(adj_list, start_node):
    edge_count = sum([len(adj_list[key]) for key in adj_list])
    cycle = [start_node]
    while (edge_count - (len(cycle) - 1) > 0):
        new_cycle = traverse_cycle(adj_list, cycle[random.randrange(0, len(cycle))])
        cycle = join_cycles(cycle, new_cycle)
    return cycle

def join_cycles(path_1, path_2):
    insertion_index = path_1.index(path_2[0])
    path_1.pop(insertion_index)
    for i in range(len(path_2)):
        path_1.insert(insertion_index + i, path_2[i])
    return path_1

def traverse_cycle(adj_list, start):
    path = []
    current_node = start
    path.append(current_node)
    while (len(adj_list[current_node]) > 0):
        current_node = adj_list[current_node].pop()
        path.append(current_node)
    return path

if __name__ == "__main__":
    main()