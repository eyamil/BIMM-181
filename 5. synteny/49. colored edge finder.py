import sys
import math

# Given a signed permutation, write down the colored edges in the regular permutation notation.
# run `python main.py filepath` where the file's first line is a signed permutation.

def main():
    file = open(sys.argv[1], "r")
    chroms = [[process_block(x) for x in y.split()] for y in file.readline().strip().lstrip("(").rstrip(")").split(")(")]
    print(", ".join([str(x) for x in construct_edges(chroms)]))

def process_block(str_int):
    sign = 1
    if str_int[0] == "-":
        sign = -1
    return(sign * int(str_int[1:]))

def construct_edges(chroms):
    edge_list = []
    for chr in chroms:
        for i in range(len(chr)):
            fst = chr[i - 1]
            if fst < 0:
                src = start_node(-fst)
            else:
                src = end_node(fst)
            snd = chr[i]
            if snd < 0:
                dest = end_node(-snd)
            else:
                dest = start_node(snd)
            edge_list.append((src, dest))
    return(edge_list)
            

def construct_genome(chr):
    genome = []
    for block in chr:
        if block < 0:
            genome.append(end_node(-block))
            genome.append(start_node(-block))
        else:
            genome.append(start_node(block))
            genome.append(end_node(block))
    return(genome)

def start_node(x):
    return(2 * x - 1)

def end_node(x):
    return(2 * x)

if __name__ == "__main__":
    main()