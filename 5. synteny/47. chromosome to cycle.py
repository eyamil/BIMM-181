import sys
import math

# Given a chromosome written in signed permutation format, convert it to a regular permutation.
# run `python main.py filepath` where the first line is a signed permutation.

def main():
    file = open(sys.argv[1], "r")
    chrom = [process_block(x) for x in file.readline().strip().lstrip("(").rstrip(")").split()]
    print("(" + " ".join([str(x) for x in construct_genome(chrom)]) + ")")

def process_block(str_int):
    sign = 1
    if str_int[0] == "-":
        sign = -1
    return(sign * int(str_int[1:]))

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