import sys

# Given integers k and d, and a set of strings DNA, find all
# (k, d) motifs, where a (k, d) motif is a k-mer appearing in
# in every string in DNA with at most d mismatches (for each 
# appearance).
# run `python main.py filepath` where the first line in filepath
# has parameters k and d (separated by whitespace), and each
# following line has one of the strings in DNA.

def main():
    file = open(sys.argv[1], "r")
    params = file.readline().strip().split()
    k = int(params[0])
    d = int(params[1])
    dna = [line.strip() for line in file.readlines()]
    possible_motifs = enumerate_motifs(dna, k, d)
    print(" ".join(possible_motifs))

bases_list = ['A', 'C', 'G', 'T']

def enumerate_motifs(dna_strings, k, d):
    patterns = set()
    for i in range(len(dna_strings)):
        for j in range(len(dna_strings[i]) - k + 1):
            pattern = dna_strings[i][j: j+k]
            for neighbor in hamming_ball(pattern, d):
                if present_in_all(dna_strings, neighbor, d):
                    patterns.add(neighbor)
    return patterns

def present_in_all(dna_strings, pat, d):
    for string in dna_strings:
        if not find(string, pat, d):
            return False
    return True

def find(text, pat, d):
    for i in range(len(text) - len(pat) + 1):
        if hamming_distance(text[i : i + len(pat)], pat) <= d:
            return True
    return False

def hamming_distance(seq_1, seq_2):
    dist = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            dist += 1
    return dist


def hamming_ball(text, dist):
    neighbors = []
    for radius in range(dist + 1):
        neighbors.extend(hamming_circle(text, radius))
    return neighbors
        

def hamming_circle(text, dist):
    if dist > len(text):
        return []
    elif dist == 0:
        return [text]
    elif len(text) == 1:
        return exclude_base(text[0])
    else:
        neighbors = str_prod([text[0]], hamming_circle(text[1 : len(text)], dist))
        neighbors.extend(str_prod(exclude_base(text[0]), hamming_circle(text[1 : len(text)], dist - 1)))
        return(neighbors)

def str_prod(prefixes, suffixes):
    prod = []
    for i in range(len(prefixes)):
        for j in range(len(suffixes)):
            prod.append(prefixes[i] + suffixes[j])
    return prod

def exclude_base(s):
    candidates = list(bases_list)
    candidates.remove(s)
    return candidates

if __name__ == "__main__":
    main()