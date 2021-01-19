import sys

# Given a burrows-wheeler transformed string and a set of patterns, find the positions
# of matches in the original string.
# run `python main.py filepath` where the file's first line has the string and the second
# has the patterns to match.

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
    for pattern in patterns:
        match_counter.append(count_pattern_matches(pattern, forward_perm, sorted_chars))
    return(match_counter)

def count_pattern_matches(pattern, forward_perm, sorted_chars):
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