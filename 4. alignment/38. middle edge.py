import sys
import math
import pdb

# Given two amino acid strings, find the middle edge in their alignment matrix.
# run `python main.py filepath` where the file's two lines are the amino acid strings,
# with amino acids from the BLOSUM62 matrix.

def main():
    file = open(sys.argv[1], "r")
    str1 = file.readline().strip()
    str2 = file.readline().strip()
    scoring_matrix = read_symmetric_matrix(sys.argv[3])
    middle_edge = mid_edge(str1, str2, scoring_matrix, int(sys.argv[2]))
    print(str(middle_edge[0]) + " " + str(middle_edge[1]))
    
def str_reverse(string):
    reversed = ""
    for i in range(len(string)):
        reversed = string[i] + reversed
    return(reversed)

def sum_opp_alignments(mat1, mat2):
    for i in range(len(mat2)):
        for j in range(len(mat2[0])):
            mat1[i][j] = (mat1[i][j][0] + mat2[len(mat2) - i - 1][len(mat2[0]) - j - 1][0], mat1[i][j][1])
    return(mat1)

def argmax(array, key):
    best_index = 0
    for i in range(len(array)):
        if key(array[best_index]) < key(array[i]):
            best_index = i
    for i in range(len(array)):
        if key(array[best_index]) == key(array[i]):
            print("index " + str(i) + " also has same value")
    return(best_index)

def mid_edge(str1, str2, scoring_matrix, indel_penalty):
    mid_col_index = math.floor((len(str1)) / 2)
    mid_col = mid_col_score(str1, str2, mid_col_index, scoring_matrix, indel_penalty)
    best_node = argmax(mid_col[1], key = lambda x : x[0])
    dest = (mid_col_index, best_node)
    src = mid_col[1][best_node][1]
    return(src, dest)

def mid_col_score(str1, str2, col_num, scoring_matrix, indel_penalty):
    fw_col = lin_align(str1[: col_num], str2, scoring_matrix, indel_penalty)
    bw_col = lin_align(str_reverse(str1[col_num - 1 : ]), str_reverse(str2), scoring_matrix, indel_penalty)
    mid_col = sum_opp_alignments(fw_col, bw_col)
    return(mid_col)

def lin_align(str1, str2, scoring_matrix, indel_penalty):
    dp_table = [[0] * (len(str2) + 1) for i in [0, 1]]
    for i in range(len(str1) + 1):
        dp_table[0] = dp_table[1]
        dp_table[1] = [0] * (len(str2) + 1)
        for j in range(len(str2) + 1):
            possible_values = []
            if i == 0 and j == 0:
                possible_values.append((0, (None, None)))
            if i > 0 and j > 0:
                prev = (i - 1, j - 1)
                prev_lin = (0, j - 1)
                align_score = scoring_matrix[str1[i - 1]][str2[j - 1]]
                entry = (align_score + dp_table[prev_lin[0]][prev_lin[1]][0], prev)
                possible_values.append(entry)
            if i > 0:
                prev = (i - 1, j)
                prev_lin = (0, j)
                entry = (indel_penalty + dp_table[prev_lin[0]][prev_lin[1]][0], prev)
                possible_values.append(entry)
            if j > 0:
                prev = (i, j - 1)
                prev_lin = (1, j - 1)
                entry = (indel_penalty + dp_table[prev_lin[0]][prev_lin[1]][0], prev)
                possible_values.append(entry)
            dp_table[1][j] = max(possible_values, key = lambda x : x[0])
    return(dp_table)

def do_dp(str1, str2, scoring_matrix, indel_penalty):
    dp_table = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            possible_values = []
            if i == 0 and j == 0:
                possible_values.append(0)
            if i > 0 and j > 0:
                prev = (i - 1, j - 1)
                align_score = scoring_matrix[str1[i - 1]][str2[j - 1]]
                entry = (align_score + dp_table[prev[0]][prev[1]])
                possible_values.append(entry)
            if i > 0:
                prev = (i - 1, j)
                entry = (indel_penalty + dp_table[prev[0]][prev[1]])
                possible_values.append(entry)
            if j > 0:
                prev = (i, j - 1)
                entry = (indel_penalty + dp_table[prev[0]][prev[1]])
                possible_values.append(entry)
            dp_table[i][j] = max(possible_values)
    return(dp_table)

def read_symmetric_matrix(filename):
    file = open(filename, "r")
    headings = file.readline().strip().split()
    matrix = {key : {key : 0 for key in headings} for key in headings}
    for rowname in headings:
        line = file.readline().strip().split()
        for i in range(len(headings)):
            matrix[rowname][headings[i]] = int(line[i])
    return(matrix)

if __name__ == "__main__":
    main()