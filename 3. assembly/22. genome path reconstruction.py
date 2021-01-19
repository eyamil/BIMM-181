import sys

# Given the k-mers from a genome string in order,
# reconstruct the genome string.
# run `python main.py filepath` where each line in
# the file is a k-mer in the genome string, and all
# the lines are in order.

def main():
    file = open(sys.argv[1], "r")
    kmers = [line.strip() for line in file.readlines()]
    print(reconstruct(kmers))

def reconstruct(kmers):
    genome = kmers[0]
    for kmer in kmers[1:]:
        genome += kmer[len(kmer) - 1]
    return(genome)

if __name__ == "__main__":
    main()