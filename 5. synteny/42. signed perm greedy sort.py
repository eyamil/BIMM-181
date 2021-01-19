import sys
import math

# Run a greedy sort on a signed permutation and print the intermediate steps.
# run `python main.py filepath` on a file with the signed permutation written in cycle
# notation.

def main():
    file = open(sys.argv[1], "r")
    chrom = [process_block(x) for x in file.readline().strip().lstrip("(").rstrip(")").split()]
    greedy_reversal_sort(chrom)

def process_block(str_int):
    sign = 1
    if str_int[0] == "-":
        sign = -1
    return(sign * int(str_int[1:]))

def reversal(start_index, end_index, array):
    temp_list = array[start_index : end_index]
    for i in range(len(temp_list)):
        array[start_index + i] = -temp_list[len(temp_list) - i - 1]
    return(array)

def find_block(block, array):
    if block in array:
        return(array.index(block))
    else:
        return(array.index(-block))

def chrom_to_str(array):
    chrom_str = "(" + " ".join([block_to_str(block) for block in array]) + ")"
    return(chrom_str)

def block_to_str(block):
    if block > 0:
        return("+" + str(block))
    else:
        return(str(block))

def greedy_reversal_sort(array):
    for i in range(len(array)):
        while array[i] != i + 1:
            pos = find_block(i + 1, array)
            array = reversal(i, pos + 1, array)
            print(chrom_to_str(array))
    return(array)

if __name__ == "__main__":
    main()