import sys
import math

# Given a burrows-wheeler transformed string and a set of patterns, find the positions
# of matches in the original string.
# run `python main.py filepath` where the file's first line has the string and the second
# has the patterns to match.
# A little faster than the previous implementation by avoiding lookups.

def main():
    file = open(sys.argv[1], "r")
    bwt = file.readline().strip()
    patterns = file.readline().strip().split()
    print(" ".join([str(x) for x in count_patterns_in_bwt(bwt, patterns)]))

def count_patterns_in_bwt(bwt, patterns):
    forward_perm = inverse(last_to_first(bwt))
    sorted_chars = [char for char in bwt]
    sorted_chars.sort()
    match_counter = []
    counts = compute_counts(sorted_chars)
    first_occurrences = find_first_occurrences(sorted_chars)
    for pattern in patterns:
        match_counter.append(count_pattern_matches(pattern, forward_perm, sorted_chars, counts, first_occurrences))
    return(match_counter)

def count_pattern_matches(pattern, forward_perm, sorted_chars, counts, first_occurrences):
    top = 0
    bottom = len(forward_perm) - 1
    for pos in range(len(pattern) - 1, -1, -1):
        char = pattern[pos]
        candidates = list(filter(lambda x : sorted_chars[x] == char, forward_perm[top : bottom + 1]))
        if candidates:
            top = min(candidates)
            bottom = max(candidates)
        else:
            return(0)
    return(bottom - top + 1)

def compute_counts(sorted_chars):
    char_set = set(sorted_chars)
    index_map = {key : [0] for key in char_set}
    for i in range(1, len(sorted_chars)):
        for char in char_set:
            if char == sorted_chars[i]:
                index_map[char].append(index_map[char][-1] + 1)
            else:
                index_map[char].append(index_map[char][-1])
    return(index_map)

def find_first_occurrences(sorted_chars):
    index_map = {key : math.inf for key in set(sorted_chars)}
    for i in range(len(sorted_chars)):
        if index_map[sorted_chars[i]] > i:
            index_map[sorted_chars[i]] = i
    return(index_map)

def last_to_first(bwt):
    numbered_bwt = []
    for i in range(len(bwt)):
        numbered_bwt.append((bwt[i], i))
    numbered_bwt.sort(key = lambda x : x[0])
    permutation = [x[1] for x in numbered_bwt]
    return(permutation)

def inverse(permutation):
    inv = [0] * len(permutation)
    for i in range(len(permutation)):
        inv[permutation[i]] = i
    return(inv)

if __name__ == "__main__":
    main()