import sys

# Given a string text, an integer k, and a profile matrix m,
# find the k-mer in text that is most probable based on the
# likelihoods given in m.
# run `python main.py filepath` where the file's first line
# is the text, the second line is the integer k, and the following 4
# lines denote the matrix m, where each column corresponds to a position
# and each entry of the column corresponds a probability (laid out as
# A, C, G, T from top to bottom).

def main():
    file = open(sys.argv[1], "r")
    dna = file.readline().strip()
    k = int(file.readline().strip())
    profile = []
    for i in range(len(bases_list)):
        probabilities = file.readline().split()
        for j in range(k):
            profile.append(float(probabilities[j]))
    print(mostlikelykmer(profile, dna, k))

def profile_coords(base, pos, k):
    return(pos + bases_list.index(base) * k)

def kmerlikelihood(kmer, profile):
    p = 1
    for i in range(len(kmer)):
        base = kmer[i]
        p = p * profile[profile_coords(base, i, len(kmer))]
    return p


def mostlikelykmer(profile, string, k):
    best_prob = -1
    best_kmer = ""
    for i in range(len(string) - k + 1):
        if kmerlikelihood(string[i: i + k], profile) > best_prob:
            best_kmer = string[i: i + k]
            best_prob = kmerlikelihood(string[i: i + k], profile)
    return best_kmer

bases_list = ['A', 'C', 'G', 'T']

if __name__ == "__main__":
    main()