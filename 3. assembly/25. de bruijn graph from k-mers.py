import sys

# Given all the k-mers, construct the de bruijn graph.
# run `python main.py filepath` where the file's lines
# are the k-mers to build the de bruijn graph out of.

def main():
    file = open(sys.argv[1], "r")
    kmers = [line.strip() for line in file.readlines()]
    overlap_graph = kmer_edge_graph(kmers)
    for kmer in overlap_graph:
        if overlap_graph[kmer]:
            print(kmer + " -> " + ",".join(overlap_graph[kmer]))

def suffix(text):
    return(text[1 : len(text)])

def prefix(text):
    return(text[0 : (len(text) - 1)])

def kmer_edge_graph(kmers):
    adj_list = {}
    prefix_set = set([prefix(kmer) for kmer in kmers])
    for kmer_prefix in prefix_set:
        adj_list[kmer_prefix] = []
    for kmer in kmers:
        adj_list[prefix(kmer)].append(suffix(kmer))
    return(adj_list)

if __name__ == "__main__":
    main()