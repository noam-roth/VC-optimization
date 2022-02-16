import matplotlib.pylab as plt
import networkx as nx
import numpy as np


def display_graph(G, my_pos, my_color_map, title):
    plt.figure(figsize=(10, 7))
    plt.title(title)
    nx.draw(G, my_pos, node_color=my_color_map, node_size=600, with_labels=True)
    plt.show()


def create_graph(my_nodes, my_edges):
    # creates graph in nx format from given adjacency matrix
    nodes = my_nodes
    edges = []
    # convert 'my_edges' format:
    for i in range(nodes):
        for j in range(i):
            if my_edges[i, j] == 1:
                edges.append((i, j))
    G = nx.Graph()
    G.add_nodes_from(list(range(0, nodes)))
    G.add_edges_from(edges)
    # values for genetic algo:
    n = nodes
    pop_total = int(50 * max(1, round(n / 5.0)))  # max population allowed in the environment
    pop_init = int(20 * max(1, round(n / 5.0)))
    max_iterate = int(7 * max(1, round(n / 5.0)))
    print("nodes = {}, pop_total = {}, pop_init = {}, max_iterate = {}".format(n, pop_total, pop_init, max_iterate))
    return G, n, pop_total, pop_init, max_iterate, edges


def generate_graph(size):
    vertices = [i for i in range(size)]
    # create an adjacency matrix --> binary symmetric matrix (undirected graph)
    edges = np.random.randint(0, 2, (size, size))
    edges ^= edges.T
    print("vertices = {}".format(vertices))
    print("edges:\n{}\n\n".format(edges))
    return vertices, edges
