import sys

# Given integers k, L, and t, find all k-mers forming 
# an (L, t)-clump (occurring more than t-times in a stretch
# of L bases.)
# run `python main.py filepath` where the file's first line is
# the text to find clumped patterns in and the second line has
# positive integers k, L, and t (separated by whitespace) where
# k is the kmer-length, L is the maximum clump length, and t is
# the minimum number of occurrences.

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    params = file.readline().split()
    k = int(params[0])
    L = int(params[1])
    t = int(params[2])
    print(' '.join(clump_finder(text, k, L, t)))

def make_kmer_counter(k):
    return [0] * (4 ** k)

bases_list = ['A', 'C', 'G', 'T']

def kmer_to_num(kmer):
    num = 0
    for i in range(len(kmer)):
        num = num * len(bases_list) + bases_list.index(kmer[i])
    return num

def num_to_kmer(num):
    kmer = ""
    while num > 0:
        base = bases_list[num % len(bases_list)]
        kmer = base + kmer
        num = int(num / len(bases_list))
    return(kmer)

def clump_finder(text, k, L, t):
    clumped_kmers = []
    counter = make_kmer_counter(k)
    for i in range(L - k + 1):
        counter[kmer_to_num(text[i : i + k])] += 1
        if counter[kmer_to_num(text[i : i + k])] == t:
            clumped_kmers.append(text[i : i + k])
    for i in range(1, len(text) - L + 1):
        counter[kmer_to_num(text[i - 1 : i-1 + k])] += -1
        counter[kmer_to_num(text[i + L - k : i + L])] += 1
        if counter[kmer_to_num(text[i + L - k : i + L])] == t:
            clumped_kmers.append(text[i + L - k : i + L])
    return clumped_kmers

if __name__ == "__main__":
    main()