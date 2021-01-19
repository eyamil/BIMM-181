import sys

# Given two sequences of equal length, compute the
# hamming distance between them. This is equal to the
# minimum number of single-base deletions, insertions,
# and replacements needed to turn one sequence into the
# other.
# run `python main.py filepath` where the file's first
# line is the first sequence and the second line is the
# second sequence.

def main():
    file = open(sys.argv[1], "r")
    seq_1 = file.readline().strip()
    seq_2 = file.readline().strip()
    print(hamming_distance(seq_1, seq_2))

def hamming_distance(seq_1, seq_2):
    dist = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            dist += 1
    return dist

if __name__ == "__main__":
    main()