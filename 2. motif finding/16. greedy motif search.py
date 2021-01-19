import sys

# Given integers k and t and a set of strings DNA,
# find the (earliest if there are multiple) k-mer 
# from each string that is most probable based off
# of DNA's k-profile.
# Note: this is actually more complicated, but I'm
# typing out the description a year after I actually
# did this problem, so I'm going to come back to fix
# the description once I go through the code.
# run `python main.py filepath` where the file's first
# line contains integers k, t

def main():
    file = open(sys.argv[1], "r")
    params = file.readline().strip().split()
    k = int(params[0])
    t = int(params[1])
    dna = [line.strip() for line in file.readlines()]
    motif = greedy_motif_search(dna, k, t)
    print("\n".join(motif))

def greedy_motif_search(dna, k, t):
    best_motifs = []
    for string in dna:
        best_motifs.append(string[0:k])
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i: i+k]]
        for j in range(1, t):
            profile = make_profile(motifs)
            motifs.append(mostlikelykmer(profile, dna[j], k))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs

def make_profile(strings):
    length = len(strings[0])
    array = [0] * (len(bases_list) * length)
    for string in strings:
        for i in range(len(string)):
            base = string[i]
            array[profile_coords(base, i, length)] += (1 / len(strings))
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