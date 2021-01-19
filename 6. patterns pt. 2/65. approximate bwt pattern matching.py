import sys


# Given a burrows-wheeler transformed string, a set of patterns, and an integer d, find 
# the positions of approximate matches (up to h-distance d away from the exact match) in
# the original string.
# run `python main.py filepath` where the file's first line has the string, the second
# has the patterns to match, and the third line has d.

def main():
    file = open(sys.argv[1], "r")
    genome = file.readline().strip()
    text = genome + "$"
    suffix_array = make_suffix_array(text)
    bwt = [text[i - 1] for i in suffix_array]
    patterns = file.readline().strip().split()
    dist = int(file.readline().strip())
    matches_by_pattern = find_patterns_in_bwt(bwt, patterns, suffix_array, genome, dist)
    matches = [str(match) for match_by_pattern in matches_by_pattern for match in match_by_pattern]
    matches.sort()
    print(" ".join(matches))

def make_suffix_array(text):
    arr = []
    for pos in range(len(text)):
        arr.append((text[pos :], pos))
    arr.sort(key = lambda x : x[0])
    return([entry[1] for entry in arr])

def find_patterns_in_bwt(bwt, patterns, suffix_array, genome, mismatches):
    forward_perm = inverse(last_to_first(bwt))
    sorted_chars = [char for char in bwt]
    sorted_chars.sort()
    match_counter = []
    for pattern in patterns:
        match_counter.append(find_approx_matches(pattern, forward_perm, sorted_chars, suffix_array, genome, mismatches))
    return(match_counter)

def find_approx_matches(pattern, forward_perm, sorted_chars, suffix_array_positions, genome, mismatches):
    exact_match_kmers = make_exact_match_kmers(pattern, mismatches)
    approx_matches = set()
    for sub_match in exact_match_kmers:
        exact_kmer = sub_match[0]
        start = sub_match[1]
        end = sub_match[2]
        exact_matches = find_pattern_matches(exact_kmer, forward_perm, sorted_chars, suffix_array_positions)
        for match_pos in exact_matches:
            (approx_match, pos) = extend_exact_match(match_pos, len(exact_kmer), pattern[0 : start], pattern[end :], genome, mismatches)
            if approx_match:
                approx_matches.add(pos)
    return(approx_matches)

def extend_exact_match(kmer_position, kmer_len, prefix, suffix, genome, distance):
    prefix_pos = kmer_position - len(prefix)
    suffix_pos = kmer_position + kmer_len
    genome_kmer_dist = hamming_dist(prefix, genome[prefix_pos : kmer_position]) + hamming_dist(suffix, genome[suffix_pos: suffix_pos + len(suffix)])
    return((genome_kmer_dist <= distance, prefix_pos))

def hamming_dist(str1, str2):
    d = abs(len(str1) - len(str2))
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            d += 1
    return(d)

def make_exact_match_kmers(pattern, mismatches):
    exact_match_kmers = []
    min_kmer_length = int(len(pattern) / (1 + mismatches))
    for i in range(mismatches):
        start = i * min_kmer_length
        end = (i + 1) * min_kmer_length
        kmer = pattern[start : end]
        exact_match_kmers.append((kmer, start, end))
    start = mismatches * min_kmer_length
    exact_match_kmers.append((pattern[start : len(pattern)], start, len(pattern)))
    return(exact_match_kmers)

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

def naive_find(text, pat, k):
    ind = []
    for i in range(len(text) - len(pat) + 1):
        if hamming_dist(text[i : i + len(pat)], pat) <= k:
            ind.append(i)
    return ind

def missing_matches(text, patterns, k):
    patterns_list = {}
    for pat in patterns:
        matches = naive_find(text, pat, k)
        if len(matches) > 0:
            patterns_list[pat] = matches
    return(patterns_list)

if __name__ == "__main__":
    main()