import sys

# Find shared k-mers in two genomes.
# run `python main.py filepath` where the file has an integer parameter k, followed
# by two lines, each of which has a genome.

def main():
    file = open(sys.argv[1], "r")
    k = int(file.readline().strip())
    str1 = file.readline().strip()
    str2 = file.readline().strip()
    print("\n".join(map(lambda x : str(x), find_shared_kmers(k, str1, str2))))

def find_shared_kmers(k, str1, str2):
    shared_kmer_list = []
    str1_kmer_set = set()
    for i in range(len(str1) - k + 1):
        str1_kmer_set.add(str1[i : i + k])
    str1_kmer_dict = {key : [] for key in str1_kmer_set}
    for i in range(len(str1) - k + 1):
        str1_kmer_dict[str1[i : i + k]].append(i)
    for j in range(len(str2) - k + 1):
        substr2 = str2[j : j + k]
        if substr2 in str1_kmer_set:
            for i in str1_kmer_dict[substr2]:
                shared_kmer_list.append((i, j))
        if revcomp(substr2) in str1_kmer_set:
            for i in str1_kmer_dict[revcomp(substr2)]:
                shared_kmer_list.append((i, j))
    return(shared_kmer_list)


def revcomp(text):
    return(reverse(complement(text)))

def reverse(text):
    rev = ""
    for i in range(len(text)):
        rev = rev + text[i]
    return rev

def complement(text):
    base_list = ['A', 'C', 'G', 'T']
    comp = ""
    for i in range(len(text)):
        complement_ind = len(base_list) - (base_list.index(text[i]) + 1)
        comp = base_list[complement_ind] + comp
    return comp

if __name__ == "__main__":
    main()