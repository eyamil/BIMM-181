import sys
import random

# Given an integer k, an integer t, and a set of strings DNA
# run a randomized motif search (find motifs, build the profile,
# and repeat).
# run `python main.py filepath` where the first line of file
# has integers k and t separated by whitespace
# and subsequent lines are the set of strings DNA.

def main():
    file = open(sys.argv[1], "r")
    params = file.readline().strip().split()
    k = int(params[0])
    t = int(params[1])
    dna = [line.strip() for line in file.readlines()]
    motif = iterate_motif_search(dna, k, 1000)
    print("\n".join(motif))

def iterate_motif_search(dna, k, t):
    best_score = len(dna) * k + 1
    best_motifs = random_motif_selection(dna, k)
    for i in range(t):
        motifs = randomized_motif_search(dna, k)
        if score(motifs) < score(best_motifs):
            best_score = score(motifs)
            best_motifs = motifs
    return best_motifs
    

def randomized_motif_search(dna, k):
    best_motifs = random_motif_selection(dna, k)
    motifs = best_motifs
    while True:
        profile = make_profile(motifs)
        motifs = likelihood_motif_selection(dna, profile, k)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs

def random_motif_selection(dna, k):
    motifs = []
    for string in dna:
        pos = random.randrange(0, len(string) - k + 1)
        motifs.append(string[pos: pos + k])
    return motifs

def likelihood_motif_selection(dna, profile, k):
    motifs = []
    for string in dna:
        motifs.append(mostlikelykmer(profile, string, k))
    return motifs

def make_profile(strings):
    length = len(strings[0])
    array = [1] * (len(bases_list) * length)
    for string in strings:
        for i in range(len(string)):
            base = string[i]
            array[profile_coords(base, i, length)] += (1 / (len(strings)) + len(bases_list))
    return array

def consensus(motifs):
    consensus = ""
    for i in range(len(motifs[0])):
        counts = [0] * len(bases_list)
        for motif in motifs:
            counts[bases_list.index(motif[i])] += 1
        consensus = consensus + bases_list[counts.index(max(counts))]
    return consensus

def score(motifs):
    consensus_seq = consensus(motifs)
    score = 0
    for motif in motifs:
        score += hamming_distance(motif, consensus_seq)
    return score

def hamming_distance(seq_1, seq_2):
    dist = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            dist += 1
    return dist

def profile_coords(base, pos, length):
    return(pos + bases_list.index(base) * length)

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