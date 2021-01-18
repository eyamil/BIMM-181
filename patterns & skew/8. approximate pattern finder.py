import sys

# Given a pattern p, text, and an integer k, find all
# matches to p in text with up to k mismatch bases.
# run `python main.py filepath` where the file's first
# line is the pattern, the second line is the text,
# and the third is the number of mismatches to tolerate.

def main():
    file = open(sys.argv[1], "r")
    pat = file.readline().strip()
    text = file.readline().strip()
    k = int(file.readline().strip())
    print(' '.join(map(str, find(text, pat, k))))

def find(text, pat, k):
    ind = []
    for i in range(len(text) - len(pat) + 1):
        if hamming_distance(text[i : i + len(pat)], pat) <= k:
            ind.append(i)
    return ind

def hamming_distance(seq_1, seq_2):
    dist = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            dist += 1
    return dist

if __name__ == "__main__":
    main()