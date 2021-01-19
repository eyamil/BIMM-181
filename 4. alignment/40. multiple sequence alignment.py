import sys
import math
import pdb

# Longest common subsequence problem on multiple strings.
# If all the amino acids match, then assign a score of +1, and 0 otherwise.
# run `python main.py filepath` where the file's lines are all the strings
# to perform the multiple alignment on.

def main():
    file = open(sys.argv[1], "r")
    str1 = file.readline().strip()
    str2 = file.readline().strip()
    str3 = file.readline().strip()
    dp_table = do_dp(str1, str2, str3, 1, 0, 0)
    score = dp_table[len(str1)][len(str2)][len(str3)][0]
    alignment = backtrack(dp_table, str1, str2, str3, "-")
    print(score)
    print(alignment[0])
    print(alignment[1])
    print(alignment[2])

def backtrack(dp_table, str1, str2, str3, gap):
    aligned_str1 = ""
    aligned_str2 = ""
    aligned_str3 = ""
    curr = (len(str1), len(str2), len(str3))
    while (curr != (0, 0, 0)):
        prev = dp_table[curr[0]][curr[1]][curr[2]][1]
        if curr[0] - prev[0] == 1:
            aligned_str1 = str1[prev[0]] + aligned_str1
        else:
            aligned_str1 = gap + aligned_str1
        if curr[1] - prev[1] == 1:
            aligned_str2 = str2[prev[1]] + aligned_str2
        else:
            aligned_str2 = gap + aligned_str2
        if curr[2] - prev[2] == 1:
            aligned_str3 = str3[prev[2]] + aligned_str3
        else:
            aligned_str3 = gap + aligned_str3
        curr = prev
    return(aligned_str1, aligned_str2, aligned_str3)

def do_dp(str1, str2, str3, match_score, mismatch_score, gap_score):
    dp_table = [[[0] * (len(str3) + 1) for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            for k in range(len(str3) + 1):
                possible_values = []
                if i == 0 and j == 0 and k == 0:
                    possible_values.append((0, (None, None, None)))
                if i != 0:
                    prev = (i - 1, j, k)
                    possible_values.append((dp_table[i - 1][j][k][0] + gap_score, prev))
                if j != 0:
                    prev = (i, j - 1, k)
                    possible_values.append((dp_table[i][j - 1][k][0] + gap_score, prev))
                if k != 0:
                    prev = (i, j, k - 1)
                    possible_values.append((dp_table[i][j][k - 1][0] + gap_score, prev))
                if i != 0 and j != 0:
                    prev = (i - 1, j - 1, k)
                    possible_values.append((dp_table[i - 1][j - 1][k][0] + gap_score, prev))
                if j != 0 and k != 0:
                    prev = (i, j - 1, k - 1)
                    possible_values.append((dp_table[i][j - 1][k - 1][0] + gap_score, prev))
                if i != 0 and k != 0:
                    prev = (i - 1, j, k - 1)
                    possible_values.append((dp_table[i - 1][j][k - 1][0] + gap_score, prev))
                if i != 0 and j != 0 and k != 0:
                    prev = (i - 1, j - 1, k - 1)
                    alignment_score = mismatch_score
                    if str1[i - 1] == str2[j - 1] and str1[i - 1] == str3[k - 1]:
                        alignment_score = match_score
                    possible_values.append((dp_table[i - 1][j - 1][k - 1][0] + alignment_score, prev))
                dp_table[i][j][k] = max(possible_values, key = lambda x : x[0])
    return(dp_table)

if __name__ == "__main__":
    main()