import sys
import math

# Given two signed permutations, compute the 2-break distance between them.
# run `python main.py filepath` where the file has two lines, each being a 
# signed permutation in cycle notation.

def main():
    file = open(sys.argv[1], "r")
    chroms_1 = [[process_block(x) for x in y.split()] for y in file.readline().strip().lstrip("(").rstrip(")").split(")(")]
    chroms_2 = [[process_block(x) for x in y.split()] for y in file.readline().strip().lstrip("(").rstrip(")").split(")(")]
    block_graph_1 = chroms_to_graph(chroms_1)
    block_graph_2 = chroms_to_graph(chroms_2)
    print(count_blocks(block_graph_1) - count_cycles(block_graph_1, block_graph_2))

def process_block(str_int):
    sign = 1
    if str_int[0] == "-":
        sign = -1
    return(sign * int(str_int[1:]))

def count_blocks(adj_list):
    return(int(len(adj_list) / 2))

def count_cycles(adj_list_1, adj_list_2):
    alternator = 0
    edges_by_color = (adj_list_1, adj_list_2)
    node_set = set(adj_list_1.keys())
    cycle_count = 0
    # Go through each cycle, counting once:
    while len(node_set) != 0:
        cycle_count += 1
        curr_node = node_set.pop()
        node_set.add(curr_node)
        # Go through the cycle, removing nodes:
        while curr_node in node_set:
            alternator = 1 - alternator
            node_set.remove(curr_node)
            curr_node = edges_by_color[alternator][curr_node]
    return(cycle_count)

def chroms_to_graph(chroms):
    node_set = set()
    for chr in chroms:
        for block in chr:
            if block < 0:
                block = - block
            node_set.add(start_node(block))
            node_set.add(end_node(block))
    adj_list = {node : 0 for node in node_set}
    for chr in chroms:
        for i in range(len(chr)):
            src_block = chr[i - 1]
            dest_block = chr[i]
            edge = signed_blocks_to_edge(src_block, dest_block)
            adj_list[edge[0]] = edge[1]
            adj_list[edge[1]] = edge[0]
    return(adj_list)

def signed_blocks_to_edge(src_block, dest_block):
    if src_block < 0:
        src_node = start_node(-src_block)
    else:
        src_node = end_node(src_block)
    if dest_block < 0:
        dest_node = end_node(-dest_block)
    else:
        dest_node = start_node(dest_block)
    return((src_node, dest_node))

def start_node(x):
    return(2 * x - 1)

def end_node(x):
    return(2 * x)

if __name__ == "__main__":
    main()