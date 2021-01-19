import sys

# Given an integer k and text, compute the frequency
# array, in lexicographic order, of the k-mers in the text.
# run `python main.py filepath` where the first line contains
# the text, and the second contains the parameter k for kmer length.

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    k = int(file.readline().strip())
    frequency_array = count(text, k)
    print(' '.join([str(num) for num in frequency_array]))

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

def count(text, k):
    counter = make_kmer_counter(k)
    for i in range(len(text) - k + 1):
        counter[kmer_to_num(text[i : i + k])] += 1
    return counter

def top_kmers(counter):
    max_ct = 0
    indices = []
    for i in range(len(counter)):
        if counter[i] > max_ct:
            max_ct = counter[i]
            indices = []
        if counter[i] == max_ct:
            indices.append(i)
    return(map(num_to_kmer, indices))

if __name__ == "__main__":
    main()