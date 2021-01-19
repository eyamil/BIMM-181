import sys

# Given a chromosome written in regular permutation format, convert it to a signed permutation.
# run `python main.py filepath` where the first line is a regular permutation.

def main():
    file = open(sys.argv[1], "r")
    genome = [int(x) for x in file.readline().strip().lstrip("(").rstrip(")").split()]
    print(construct_chromosome_str(genome))

def construct_chromosome_str(genome):
    chr = []
    for i in range(int(len(genome) / 2)):
        block = get_block(genome[2 * i], genome[2 * i + 1])
        if block > 0:
            chr.append("+" + str(block))
        else:
            chr.append(str(block))
    return("(" + " ".join(chr) + ")")

def get_block(a, b):
    sign = 1
    if a > b:
        sign = -1
    return(int(sign * max(a, b) / 2))

if __name__ == "__main__":
    main()