import math
from itertools import combinations
import time
import networkx as nx
from time import strftime
from time import gmtime
from graph_manipulator import display_graph
import numpy as np


def is_vertex_cover(E, group):
    rows, columns = E.shape
    for i in range(rows):
        for j in range(columns):
            if E[i, j] == 1 and (i not in group and j not in group):
                return False
    return True


# V is a list of vertices, E is represent as adjacency matrix: E[i,j]=1 => then we have an edge from i to j in the graph
def brute_force_vc(V, E):
    # measure time:
    start_time = time.time()
    # check if we don't have any edges in the graph:
    if np.all((E == 0)):
        return [], time.time() - start_time
    for k in range(1, len(V)):
        # print("try combinations in size: {}".format(k))
        for group in combinations(V, k):
            # print("try the group: {}".format(group))
            if is_vertex_cover(E, set(group)):
                return group, time.time() - start_time
    return [], time.time() - start_time


def draw_graph(adjacency_matrix, my_color_map='r', title='Random Graph'):
    G = nx.from_numpy_matrix(adjacency_matrix)
    my_pos = nx.spring_layout(G, seed=100)
    display_graph(G, my_pos, my_color_map, title)
    return my_pos


def main(vertices, edges):
    my_pos = draw_graph(edges)
    vc, run_time = brute_force_vc(vertices, edges)
    print("runtime = " + str(run_time))
    print("Brute_force_Algorithm VC = {}".format(vc))
    print("Brute_force_Algorithm run time = {} sec".format(round(run_time, 5)))
    # show graph:
    color_map = ['lightgreen' if node in vc else 'r' for node in vertices]
    draw_graph(edges, color_map,
               title='Brute Force: VC in green and others in red\n|VC| = {0}\nAlgorithm run time: {1}'
               .format(len(vc), strftime("%H:%M:%S", gmtime(math.ceil(run_time)))))
    return my_pos
