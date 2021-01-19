import sys
import math

# Given two genome strings, find the shortest substring in the first but not the second.
# run `python main.py filepath` where the file's first line is one of the genomes,
# and the second line is the other.

def main():
    terminal_char1 = "#"
    terminal_char2 = "$"
    file = open(sys.argv[1], "r")
    text1 = file.readline().strip() + terminal_char1
    text2 = file.readline().strip() + terminal_char2
    text = text1 + text2
    trie = construct_suffix_trie(text)
    tree = make_tree_from_trie(trie)
    color_ds = {key : (False, False) for key in trie}
    color_ds = assign_tree_colors(tree, 0, text2, color_ds, "")
    nonshared_substrings = list(find_nonshared_substr(tree, 0, color_ds, ""))
    shortest_repeat = min(nonshared_substrings, key = lambda x : len(x))
    print(shortest_repeat)

def assign_tree_colors(tree, node, text2, color_ds, edge_label):
    if len(tree[node]) == 0:
        if len(edge_label) > len(text2):
            color_ds[node] = (True, False)
        else:
            color_ds[node] = (False, True)
    else:
        out_edges = iter(tree[node])
        color_tuple = (False, False)
        for edge in out_edges:
            child_node = tree[node][edge]
            color_ds = assign_tree_colors(tree, child_node, text2, color_ds, edge)
            child_color = color_ds[child_node]
            color_tuple = (color_tuple[0] | child_color[0], color_tuple[1] | child_color[1])
        color_ds[node] = color_tuple
    return(color_ds)

def find_nonshared_substr(tree, node, color_ds, base_str):
    if (len(tree[node]) == 0):
        return(set())
    else:
        outgoing_edges = iter(tree[node])
        repeat_set = set()
        if (color_ds[node][0] and (not color_ds[node][1])):
            repeat_set.add(base_str)
        for edge_label in outgoing_edges:
            repeat_set = repeat_set.union(find_nonshared_substr(tree, tree[node][edge_label], color_ds, base_str + edge_label))
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