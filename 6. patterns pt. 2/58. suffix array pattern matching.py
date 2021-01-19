import sys
import math

# Given a string, use the suffix array to pattern match in the string. Prints positions 
# of matches.
# run `python main.py filepath` where the file's first line is the string
# and the subsequent lines are patterns to match.

def main():
    terminal_char = sys.argv[2]
    file = open(sys.argv[1], "r")
    text = file.readline().strip() + terminal_char
    patterns = [pattern.strip() for pattern in file.readlines()]
    suffix_array = make_suffix_array(text)
    print(" ".join([str(pos) for pos in multiple_pattern_search(text, suffix_array, patterns)]))
    

def make_suffix_array(text):
    arr = []
    for pos in range(len(text)):
        arr.append((text[pos :], pos))
    arr.sort(key = lambda x : x[0])
    return([entry[1] for entry in arr])

def multiple_pattern_search(text, arr, queries):
    match_set = set()
    for query in queries:
        match_set = match_set.union(search_suffix_array(text, arr, query))
    return(match_set)

def search_suffix_array(text, arr, query):
    min_ind = 0
    max_ind = len(arr) - 1

    def lower_lex_bound(index):
        return(query > text[index :])

    def equal_lex_bound(index):
        if len(text) - index - 1 >= len(query):
            return(query == text[index : index + len(query)])
        else:
            return(False)
    
    min_ind = find_bounds_in_array(arr, lower_lex_bound, min_ind, max_ind)[0]
    if not equal_lex_bound(arr[min_ind]):
        return([])
    max_ind = find_bounds_in_array(arr, equal_lex_bound, min_ind, max_ind)[1]
    return(arr[min_ind : max_ind + 1])


def find_bounds_in_array(array, condition, min_ind, max_ind):
    while min_ind <= max_ind:
        mid_ind = int((min_ind + max_ind) / 2)
        if condition(array[mid_ind]):
            min_ind = mid_ind + 1
        else:
            max_ind = mid_ind - 1
    return((min_ind, max_ind))

if __name__ == "__main__":
    main()