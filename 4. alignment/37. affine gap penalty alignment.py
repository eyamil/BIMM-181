import sys
import math
import pdb

# Given two strings, compute the best global alignment between the two.
# The match/mismatch score is given by the BLOSUM62 matrix, the gap open
# penalty is -11, and the gap extension penalty is -1.
# run `python main.py filepath` where the file's two lines have the two strings.

def main():
    file = open(sys.argv[1], "r")
    str1 = file.readline().strip()
    str2 = file.readline().strip()
    scoring_matrix = read_symmetric_matrix('BLOSUM62.txt')
    dp_table = do_dp(str1, str2, scoring_matrix, -11, -1)
    score = dp_table[len(str1)][len(str2)][2][0]
    alignment = backtrack(dp_table, str1, str2, "-")
    print(score)
    print(alignment[0])
    print(alignment[1])

def backtrack(dp_table, str1, str2, gap):
    aligned_str1 = ""
    aligned_str2 = ""
    curr = (len(str1), len(str2), 2)
    while (curr != (0, 0, 2)):
        prev = dp_table[curr[0]][curr[1]][curr[2]][1]
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

def do_dp(str1, str2, scoring_matrix, gap_open_score, gap_extension_score):
    dp_table = [[[(-math.inf, (None, None, None))] * 3 for j in range(1 + len(str2))] for i in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            for k in range(3):
                possible_values = []
                # Setup: k = 0 is horizontal gap edges, k = 1 is vertical gap edges, k = 3 is match/mismatch
                if k == 0:
                    if i != 0:
                        # Case 1: extend str1 gap
                        prev = (i - 1, j, 0)
                        prev_score = dp_table[prev[0]][prev[1]][prev[2]][0]
                        possible_values.append((prev_score + gap_extension_score, prev))
                        # Case 2: open gap
                        prev = (i - 1, j, 2)
                        prev_score = dp_table[prev[0]][prev[1]][prev[2]][0]
                        possible_values.append((prev_score + gap_open_score, prev))
                    else:
                        # Base case - this should get a -inf if i == 0
                        prev = (0, j, 2)
                        possible_values.append((0, prev))
                if k == 1:
                    if j != 0:
                        # Case 1: extend str2 gap
                        prev = (i, j - 1, 1)
                        prev_score = dp_table[prev[0]][prev[1]][prev[2]][0]
                        possible_values.append((prev_score + gap_extension_score, prev))
                        # Case 2: open gap
                        prev = (i, j - 1, 2)
                        prev_score = dp_table[prev[0]][prev[1]][prev[2]][0]
                        possible_values.append((prev_score + gap_open_score, prev))
                    else:
                        # Base case - this should get a -inf if i == 0
                        prev = (i, 0, 2)
                        possible_values.append((0, prev))
                if k == 2:
                    if i != 0 and j != 0:
                        # Case 1: match/mismatch
                        prev = (i - 1, j - 1, 2)
                        prev_score = dp_table[prev[0]][prev[1]][prev[2]][0]
                        possible_values.append((prev_score + scoring_matrix[str1[i - 1]][str2[j - 1]], prev))
                    # Case 2: close str1 gap
                    prev = (i, j, 0)
                    prev_score = dp_table[prev[0]][prev[1]][prev[2]][0]
                    possible_values.append((prev_score, prev))
                    # Case 3: close str2 gap
                    prev = (i, j, 1)
                    prev_score = dp_table[prev[0]][prev[1]][prev[2]][0]
                    possible_values.append((prev_score, prev))
                dp_table[i][j][k] = max(possible_values, key = lambda x : x[0])
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