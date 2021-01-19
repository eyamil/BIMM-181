import sys
import queue as ds

# Given a graph in adjacency list format, output a topological ordering on the nodes.
# run `python main.py filepath` where the file's lines are formatted as discussed in the
# assembly unit.

def main():
    file = open(sys.argv[1], "r")
    adj = make_adj_list([line.strip() for line in file.readlines()])
    ordering = order(adj, node_valuation)
    print(", ".join([str(node) for node in ordering]))

def node_valuation(x):
    return(x)

def str_to_node(string):
    return(int(string.strip()))

def get_all_nodes(pairings_strings):
    node_list = set()
    for line in pairings_strings:
        pairings = line.split("->")
        node_list.add(str_to_node(pairings[0]))
        for node_str in pairings[1].split(","):
            node_list.add(str_to_node(node_str))
    return node_list

def make_adj_list(pairings_strings):
    adj = {node : set() for node in get_all_nodes(pairings_strings)}
    for line in pairings_strings:
        pairings = line.split(" -> ")
        node = str_to_node(pairings[0])
        for neighbor_str in pairings[1].split(","):
            adj[node].add(str_to_node(neighbor_str))
    return adj
    
def find_source_nodes(adj_list):
    degrees = {key: 0 for key in adj_list}
    for _, to_nodes in adj_list.items():
        for to_node in to_nodes:
            degrees[to_node] += 1
    sources = []
    for node, degree in degrees.items():
        if degree == 0:
            sources.append(node)
    return (sources)

def source_dist_list(adj_list):
    distances_to_start = {node : -1 for node in adj_list}
    node_stack = ds.SimpleQueue()
    for node in find_source_nodes(adj_list):
        node_stack.put((0, node))
    while not node_stack.empty():
        (dist, top) = node_stack.get()
        if distances_to_start[top] < dist:
            distances_to_start[top] = dist
        neighbors = adj_list[top]
        for node in neighbors:
            node_stack.put((dist + 1, node))
    dist_list = {value : set() for value in distances_to_start.values()}
    for key, value in distances_to_start.items():
        dist_list[value].add(key)
    return(dist_list)

def order(adj_list, valuation):
    dist_list = source_dist_list(adj_list)
    ordering = []
    for dist in sorted(dist_list.keys()):
        ordering.extend(sorted(dist_list[dist], key = valuation))
    return(ordering)

if __name__ == "__main__":
    main()