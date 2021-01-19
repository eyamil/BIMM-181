import sys

# Given a genome string and a set of patterns to match, use trie matching to find the
# locations of all the matches.
# run `python main.py filepath` where the file's first line is the genome string
# and subsequent lines have the patterns to match.

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    patterns = [pattern.strip() for pattern in file.readlines()]
    trie = construct_trie(patterns)
    print(" ".join([str(pos) for pos in trie_match(text, trie)]))

def construct_trie(patterns):
    nodes = {0: {}}
    for pattern in patterns:
        current_node = 0
        for char in pattern:
            if char in nodes[current_node]:
                current_node = nodes[current_node][char]
            else:
                new_node_id = len(nodes)
                nodes[new_node_id] = {}
                nodes[current_node][char] = new_node_id
                current_node = new_node_id
    return(nodes)

def prefix_trie_match(text, trie):
    curr_node = 0
    text_pos = 0
    while text_pos < len(text):
        if len(trie[curr_node]) == 0:
            return(True)
        elif text[text_pos] not in trie[curr_node]:
            return(False)
        else:
            curr_node = trie[curr_node][text[text_pos]]
            text_pos += 1
    return(False)
        

def trie_match(text, trie):
    match_positions = []
    for pos in range(len(text)):
        if prefix_trie_match(text[pos :], trie):
            match_positions.append(pos)
    return(match_positions)

if __name__ == "__main__":
    main()