import sys

# Given a burrows-wheeler transformed string and a set of patterns, find the positions
# of matches in the original string.
# run `python main.py filepath` where the file's first line has the string and the second
# has the patterns to match.
# The partial suffix array actually made things worse - maybe because the CPU is looking
# ahead to load things? In any case, I turned it off because memory isn't a limiting
# factor for this problem set.

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip() + "$"
    suffix_array = make_suffix_array(text)
    bwt = [text[i - 1] for i in suffix_array]
    patterns = [pattern.strip() for pattern in file.readlines()]
    matches_by_pattern = find_patterns_in_bwt(bwt, patterns, suffix_array)
    matches = [str(match) for match_by_pattern in matches_by_pattern for match in match_by_pattern]
    matches.sort()
    print(" ".join(matches))

def make_suffix_array(text):
    arr = []
    for pos in range(len(text)):
        arr.append((text[pos :], pos))
    arr.sort(key = lambda x : x[0])
    return([entry[1] for entry in arr])

def find_patterns_in_bwt(bwt, patterns, suffix_array):
    forward_perm = inverse(last_to_first(bwt))
    sorted_chars = [char for char in bwt]
    sorted_chars.sort()
    match_counter = []
    for pattern in patterns:
        match_counter.append(find_pattern_matches(pattern, forward_perm, sorted_chars, suffix_array))
    return(match_counter)

def find_pattern_matches(pattern, forward_perm, sorted_chars, suffix_array_positions):
    top = 0
    bottom = len(forward_perm) - 1
    for pos in range(len(pattern) - 1, -1, -1):
        char = pattern[pos]
        candidates = list(filter(lambda x : sorted_chars[x] == char, forward_perm[top : bottom + 1]))
        if candidates:
            top = min(candidates)
            bottom = max(candidates)
        else:
            return([])
    suffix_positions = [suffix_array_positions[i] for i in candidates]
    return(suffix_positions)

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