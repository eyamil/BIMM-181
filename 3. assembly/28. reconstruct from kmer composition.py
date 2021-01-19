import sys
import random

# Given an integer k and the k-mer composition of a genome, 
# reconstruct the genome.
# run `python main.py filepath` where the file's first line
# is k and the following lines have the k-mer composition,
# with one k-mer on each line.

def main():
    file = open(sys.argv[1], "r")
    k = int(file.readline().strip())
    kmers = [line.strip() for line in file.readlines()]
    adj_list = make_overlap_graph(kmers)
    (sources, _) = find_unbalanced_nodes(adj_list)
    reconstruction = euler_path(adj_list, sources[0])
    genome = reconstruction[0]
    for i in range(1, len(reconstruction)):
        genome += reconstruction[i][k - 1]
    print(genome)
    
def make_overlap_graph(kmers):
    adj_list = {}
    for kmer in kmers:
        adj_list[kmer] = find_overlaps(kmer, kmers)
    return adj_list

def find_overlaps(pattern, kmers):
    adjacent_kmers = []
    for kmer in kmers:
        if suffix(pattern) == prefix(kmer):
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