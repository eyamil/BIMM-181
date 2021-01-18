import sys

# Given text and integers k, d, find the most frequent k-mers with
# up to d mismatches in the text.
# run `python main.py filepath` where the file's first line is the
# text, and the second line has k and d, separated by whitespace.

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    params = file.readline().strip().split()
    k = int(params[0])
    d = int(params[1])
    print(k,d)
    frequency_array = exact_count(text, k)
    approx_freq_array = calc_approx_matches(frequency_array, k, d)
    print(' '.join(top_kmers(approx_freq_array, k)))

def make_kmer_counter(k):
    return [0] * (4 ** k)

bases_list = ['A', 'C', 'G', 'T']

def kmer_to_num(kmer):
    num = 0
    for i in range(len(kmer)):
        num = num * len(bases_list) + bases_list.index(kmer[i])
    return num

def num_to_kmer(num, k):
    kmer = ""
    for i in range(k):
        base = bases_list[num % len(bases_list)]
        kmer = base + kmer
        num = int(num / len(bases_list))
    return(kmer)

def exact_count(text, k):
    counter = make_kmer_counter(k)
    for i in range(len(text) - k + 1):
        counter[kmer_to_num(text[i : i + k])] += 1
    return counter

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

def calc_approx_matches(frequency_array, k, dist):
    match_array = [0] * len(frequency_array)
    for i in range(len(frequency_array)):
        kmer = num_to_kmer(i, k)
        for radius in range(dist + 1):
            for neighbor in hamming_circle(kmer, radius):
                match_array[i] += frequency_array[kmer_to_num(neighbor)]
    return match_array

def top_kmers(counter, k):
    max_ct = 0
    indices = []
    for i in range(len(counter)):
        if counter[i] > max_ct:
            max_ct = counter[i]
            indices = []
        if counter[i] == max_ct:
            indices.append(i)
    return [num_to_kmer(index, k) for index in indices]

if __name__ == "__main__":
    main()