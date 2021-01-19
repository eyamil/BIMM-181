import sys
import math

# Given a signed permutation, count the number of breakpoints in the permutation.
# run `python main.py filepath` where the file has a signed permutation written in cycle
# notation.

def main():
    file = open(sys.argv[1], "r")
    chrom = [process_block(x) for x in file.readline().strip().lstrip("(").rstrip(")").split()]
    print(str(compute_breakpoints(chrom)))

def compute_breakpoints(blocks):
    blocks.insert(0, 0)
    blocks.append(len(blocks))
    num_breakpoints = 0
    for i in range(len(blocks) - 1):
        if blocks[i] + 1 != blocks[i + 1]:
            num_breakpoints += 1
    return(num_breakpoints)

def process_block(str_int):
    sign = 1
    if str_int[0] == "-":
        sign = -1
    return(sign * int(str_int[1:]))

if __name__ == "__main__":
    main()