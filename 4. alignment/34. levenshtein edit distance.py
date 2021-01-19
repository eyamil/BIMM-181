import sys
import math
import pdb

# Given two strings, compute the Levenshtein edit distance between the two.
# run `python main.py filepath` where the file's two lines have the two strings.

def main():
    file = open(sys.argv[1], "r")
    str1 = file.readline().strip()
    str2 = file.readline().strip()
    dp_table = do_dp(str1, str2, 1)
    score = dp_table[len(str1)][len(str2)]
    print(score)

def backtrack(dp_table, str1, str2, gap):
    aligned_str1 = ""
    aligned_str2 = ""
    curr = (len(str1), len(str2))
    while (curr != (0, 0)):
        prev = dp_table[curr[0]][curr[1]][1]
        if curr[0] - prev[0] == 1 and curr[1] - prev[1] == 1:
            aligned_str1 = str1[prev[0]] + aligned_str1
            aligned_str2 = str2[prev[1]] + aligned_str2
        elif curr[0] - prev[0] == 1:
            aligned_str1 = str1[prev[0]] + aligned_str1
            aligned_str2 = gap + aligned_str2
        elif curr[1] - prev[1] == 1:
            aligned_str1 = gap + aligned_str1
            aligned_str2 = str2[prev[1]] + aligned_str2
        curr = prev
    return(aligned_str1, aligned_str2)

def do_dp(str1, str2, indel_penalty):
    dp_table = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            possible_values = []
            if i == 0 and j == 0:
                possible_values.append(0)
            if i > 0 and j > 0:
                prev = (i - 1, j - 1)
                align_score = 0
                if (str1[i - 1] != str2[j - 1]):
                    align_score = 1
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
            dp_table[i][j] = min(possible_values)
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