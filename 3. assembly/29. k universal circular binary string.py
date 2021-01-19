import sys
import random

# Given an integer k, construct a string that, when
# circularized, contains every k-mer on the alphabet [0, 1]
# run `python main.py filepath` where the file's first line is k.

def main():
    file = open(sys.argv[1], "r")
    k = int(file.readline().strip())
    kmers = all_kmers(k - 1, ["0","1"])
    adj_list = make_overlap_graph(kmers)
    path = euler_path(adj_list, kmers[0])
    univ_str = ""
    for i in range(len(path) - 1):
        univ_str += path[i][0]
    print(univ_str)
    
def all_kmers(k, alphabet):
    if k == 0:
        return []
    if k == 1:
        return alphabet
    else:
        return str_prod(alphabet, all_kmers(k - 1, alphabet))
    
def str_prod(set1, set2):
    str_set = []
    for prefix_str in set1:
        for suffix_str in set2:
            str_set.append(prefix_str + suffix_str)
    return str_set

def make_overlap_graph(kmers):
    adj_list = {}
    for kmer in kmers:
        adj_list[kmer] = find_overlaps(kmer, kmers)
    return adj_list

def find_overlaps(pattern, kmers):
    adjacent_kmers = []
    for kmer in kmers:
        if (suffix(pattern) == prefix(kmer)):
            adjacent_kmers.append(kmer)
    return adjacent_kmers

def suffix(text):
    return(text[1 : len(text)])

def prefix(text):
    return(text[0 : (len(text) - 1)])

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