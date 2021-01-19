import sys

# Given a burrows-wheeler transformed string, recover the original string.
# run `python main.py filepath` where the file's first line has the string.

def main():
    file = open(sys.argv[1], "r")
    bwt = file.readline().strip()
    print(reconstruct_text(bwt))

def get_alph_ordering(bwt):
    char_array = [char for char in bwt]
    char_array.sort()
    labelled_char_array = [(char_array[0], 0)]
    for pos in range(1, len(char_array)):
        if char_array[pos] == char_array[pos - 1]:
            labelled_char_array.append((char_array[pos], labelled_char_array[pos - 1][1] + 1))
        else:
            labelled_char_array.append((char_array[pos], 0))
    return(labelled_char_array)

def number_bwt_positions(bwt):
    numbering_graph = {}
    numbered_text = []
    for pos in range(len(bwt)):
        if bwt[pos] in numbering_graph:
            numbering_graph[bwt[pos]] += 1
        else:
            numbering_graph[bwt[pos]] = 0
        numbered_text.append((bwt[pos], numbering_graph[bwt[pos]]))
    return(numbered_text)

def reconstruct_text(bwt):
    bwt_graph = {}
    numbered_text = number_bwt_positions(bwt)
    sorted_letters = get_alph_ordering(bwt)
    for i in range(len(bwt)):
        bwt_graph[sorted_letters[i]] = numbered_text[i]
    text = ""
    curr_node = (sorted_letters[0][0], 0)
    for i in range(len(bwt)):
        text = curr_node[0] + text
        curr_node = bwt_graph[curr_node]
    return(text)

if __name__ == "__main__":
    main()