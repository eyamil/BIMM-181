import sys
import math

# Given the set of colored edges in a graph, return the signed permutation corresponding
# to that set of colored edges.

def main():
    file = open(sys.argv[1], "r")
    edges = [process_edge(x) for x in file.readline().strip().split("), (")]
    print(construct_genome_str(edges))

def process_edge(str_pair):
    node_arr = [int(x) for x in str_pair.lstrip("(").rstrip(")").split(", ")]
    return((node_arr[0], node_arr[1]))

def construct_genome_str(edges_list):
    genome = construct_genome(edges_list)
    genome_str = ""
    for chrom in genome:
        genome_str += "(" + " ".join([block_to_str(block) for block in chrom]) + ")"
    return(genome_str)

def block_to_str(block):
    if block > 0:
        return("+" + str(block))
    else:
        return(str(block))

def construct_genome(edges_list):
    genome = []
    chrom = []
    for edge in edges_list:
        (src, dest) = edge_to_blocks(edge[0], edge[1])
        if len(chrom) == 0:
            chrom.append(src)
        if dest == chrom[-0]:
            genome.append(chrom)
            chrom = []
        else:
            chrom.append(dest)
    return(genome)

def edge_to_blocks(a, b):
    return((from_block_dir(a) * node_to_block(a), to_block_dir(b) * node_to_block(b)))

def node_to_block(a):
    return(math.ceil(a / 2))

def to_block_dir(a):
    return(2 * (a % 2) - 1)

def from_block_dir(b):
    return(1 - 2 * (b % 2))

def start_node(x):
    return(2 * x - 1)

def end_node(x):
    return(2 * x)

if __name__ == "__main__":
    main()