import sys

# Given a genome, build its suffix tree and return the labels of the edges.
# run `python main.py filepath` where the file's first line is the genome string, ending in
# a terminating character which isn't elsewhere in the genome string.

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    trie = construct_suffix_trie(text)
    tree = make_tree_from_trie(trie)
    for node in tree:
        for edge in trie[node]:
            print(edge)

def add_pattern_to_trie(trie, pat):
    current_node = 0
    for char in pat:
        if char in trie[current_node]:
            current_node = trie[current_node][char]
        else:
            new_node_id = len(trie)
            trie[new_node_id] = {}
            trie[current_node][char] = new_node_id
            current_node = new_node_id
    return(trie)

def construct_suffix_trie(text):
    trie = {0: {}}
    for pos in range(len(text)):
        suffix = text[pos :]
        trie = add_pattern_to_trie(trie, suffix)
    return(trie)

def make_tree_from_trie(trie):
    trie = collapse_trie_nodes(trie, 0)
    trie = remove_unreachable_nodes(trie)
    return(trie)

def collapse_trie_nodes(trie, node):
    edges = set(trie[node].keys())
    while len(edges) != 0:
        outgoing_str = edges.pop()
        curr_node = trie[node][outgoing_str]
        path_str = outgoing_str
        del trie[node][outgoing_str]
        while len(trie[curr_node]) == 1:
            outgoing_char = next(iter(trie[curr_node]))
            path_str += outgoing_char
            curr_node = trie[curr_node][outgoing_char]
        trie[node][path_str] = curr_node
        if len(trie[curr_node]) != 0:
            trie = collapse_trie_nodes(trie, curr_node)
    return(trie)

def get_reachable_nodes(trie, node):
    reachable_nodes = set()
    reachable_nodes.add(node)
    for outgoing_str in trie[node].keys():
        reachable_nodes = reachable_nodes.union(get_reachable_nodes(trie, trie[node][outgoing_str]))
    return(reachable_nodes)

def remove_unreachable_nodes(trie):
    all_nodes = set(trie)
    reachable_nodes = get_reachable_nodes(trie, 0)
    for node in all_nodes.difference(reachable_nodes):
        del trie[node]
    return(trie)

if __name__ == "__main__":
    main()