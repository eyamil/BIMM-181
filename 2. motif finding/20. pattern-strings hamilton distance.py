import sys

# Given a pattern and a set of strings, compute
# the sum of hamming distances between the pattern 
# and the closest k-mer in each string.
# run `python main.py filepath` where the file's first
# line is the patter, and the next is the set of strings,
# where strings are separated by whitespace.

def main():
    file = open(sys.argv[1], "r")
    pattern = file.readline().strip()
    dna = file.readline().strip().split()
    print(dist_to_dna(pattern, dna))

def hamming_distance(seq_1, seq_2):
    dist = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            dist += 1
    return dist

def min_ham_dist(pattern, long_string):
    min_dist = len(pattern) + 1
    for i in range(len(long_string) - len(pattern) + 1):
        dist = hamming_distance(pattern, long_string[i:i+len(pattern)])
        if dist < min_dist:
            min_dist = dist
    return min_dist

def dist_to_dna(pattern, string_list):
    dist = 0
    for string in string_list:
        dist = dist + min_ham_dist(pattern, string)
    return dist

bases_list = ['A', 'C', 'G', 'T']

if __name__ == "__main__":
    main()