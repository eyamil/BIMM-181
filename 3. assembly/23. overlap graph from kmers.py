import sys

# Given a set of k-mers, construct the overlap graph as an adjacency list
# run `python main.py filepath` where the file's lines are the k-mers.

def main():
    file = open(sys.argv[1], "r")
    kmers = [line.strip() for line in file.readlines()]
    overlap_graph = make_overlap_graph(kmers)
    for kmer in overlap_graph:
        if overlap_graph[kmer]:
            print(kmer + " -> " + " ".join(overlap_graph[kmer]))
    
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

if __name__ == "__main__":
    main()