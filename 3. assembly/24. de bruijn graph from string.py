import sys

# Given an integer k and a genome string, construct the de bruijn
# graph of the (k-1)-mers in the genome string as an adjacency list.
# run `python main.py filepath` where the file's first line has the
# integer k and the second line has the genome string.


def main():
    file = open(sys.argv[1], "r")
    k = int(file.readline().strip())
    text = file.readline().strip()
    overlap_graph = make_overlap_graph(kmer_composition(k - 1, text))
    for kmer in overlap_graph:
        if overlap_graph[kmer]:
            print(kmer + " -> " + ",".join(overlap_graph[kmer]))
    
def kmer_composition(k, text):
    kmers = set()
    for i in range(len(text) - k + 1):
        kmers.add(text[i: i + k])
    return kmers

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