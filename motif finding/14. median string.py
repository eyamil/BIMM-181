import sys

# Given an integer k and a set of strings DNA, 
# find a median k-mer for DNA. A median k-mer m for
# a set of strings is a k-mer minimizing the sum of
# hamming distances between m and the closest k-mer
# for every string in DNA, where "closest k-mer" in
# a string refers to the k-mer in the string which has
# the lowest hamming distance to m.
# run `python main.py filepath` where the file's first line
# has the integer k, and each subsequent line contains
# a string in DNA.

def main():
    file = open(sys.argv[1], "r")
    k = int(file.readline().strip())
    dna = [line.strip() for line in file.readlines()]
    print(median_string(dna, k))

def median_string(dna_list, k):
    min_dist = k + 1
    best_string = ""
    for string in univ_string_set(k):
        if dist_to_dna(string, dna_list) < min_dist:
            min_dist = dist_to_dna(string, dna_list)
            best_string = string
        if min_dist == 0:
            break
    return best_string

def univ_string_set(length):
    if length == 0:
        return [""]
    else:
        strings = univ_string_set(length - 1)
        set = []
        for string in strings:
            for base in bases_list:
                set.append(string + base)
        return set


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