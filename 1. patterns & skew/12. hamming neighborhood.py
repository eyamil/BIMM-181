import sys

# Given a k-mer and an integer d, find the set of 
# equal-length k-mers that have a hamming distance
# less than d
# run `python main.py filepath` where the file's first
# line is the k-mer and the second line is d, the maximum
# hamming distance

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    d = int(file.readline().strip())
    print('\n'.join(hamming_ball(text, d)))

bases_list = ['A', 'C', 'G', 'T']

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