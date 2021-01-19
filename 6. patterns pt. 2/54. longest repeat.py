import sys
import math

# Given a genome string, find the longest repeat in it.
# run `python main.py filepath` where the file's first line is the genome string (no 
# special terminal character)

def main():
    terminal_char = sys.argv[2]
    file = open(sys.argv[1], "r")
    text = file.readline().strip() + terminal_char
    trie = construct_suffix_trie(text)
    tree = make_tree_from_trie(trie)
    longest_repeat = max(list(find_all_repeats(tree, 0, "")), key = lambda x : len(x))
    print(longest_repeat)
    
def find_all_repeats(tree, node, base_str):
    if len(tree[node]) == 0:
        return(set())
    elif len(tree[node]) == 1:
        edge_label = next(iter(tree[node]))
        return(find_all_repeats(tree, tree[node][edge_label], base_str + edge_label))    
    else:
        outgoing_edges = iter(tree[node])
        repeat_set = set()
        repeat_set.add(base_str)
        for edge_label in outgoing_edges:
            repeat_set = repeat_set.union(find_all_repeats(tree, tree[node][edge_label], base_str + edge_label))
        return(repeat_set)

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