import sys

# Given a sequence of bases, find the positions that
# minimize the skew from the start of the string.
# Skew is the count of C's minus the count of G's.
# Origins of replication tend to be nearby the positions
# of minimum skew.
# run `python main.py filepath` where the file's first line
# is the DNA sequence to find the minimum skew loci for.

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    loci = get_min_skew_loci(text)
    print(' '.join(map(str, loci)))

def get_min_skew_loci(text):
    skew = 0
    min_skew = 0
    loci = []
    for i in range(len(text)):
        if text[i] == 'G':
            skew += 1
        elif text[i] == 'C':
            skew += -1
        if skew < min_skew:
            min_skew = skew
            loci = []
        if skew == min_skew:
            loci.append(i + 1)
            # offset by 1 since length of text from 0 to i is i + 1
    return loci

if __name__ == "__main__":
    main()