import sys

# Given a set of strings, build a trie containing them and return the adjacency list of 
# the trie.
# run `python main.py filepath` where the file's lines each contain a string to add to
# the trie.

def main():
    file = open(sys.argv[1], "r")
    patterns = [pattern.strip() for pattern in file.readlines()]
    trie = construct_trie(patterns)
    print_trie(trie)

bases = ['A', 'G', 'C', 'T']

def base_to_index(base):
    return(bases.index(base))

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

def print_trie(trie):
    for node in trie:
        for label in trie[node]:
            print(str(node) + "->" + str(trie[node][label]) + ":" + label)


if __name__ == "__main__":
    main()