import pulp
import time
from time import strftime
from time import gmtime
import math
from graph_manipulator import display_graph, create_graph


def approximate_vc(G, n):
    start_time = time.time()
    # define the problem
    prob = pulp.LpProblem("MinimumSetVertexCover", pulp.LpMinimize)
    # define the variables
    x = pulp.LpVariable.dicts("x", G.nodes(), cat=pulp.LpBinary)
    z = pulp.LpVariable.dicts("z", G.edges(), cat=pulp.LpBinary)
    prob += pulp.lpSum(x)  # define the objective function
    # define the constraints
    for (u, v) in G.edges():
        prob += x[u] + x[v] >= 1  # each edge is covered
    prob.solve()  # solve
    results = []
    for v in G.nodes():
        if pulp.value(x[v]) > 0.9:
            results.append(v)
    return {len(results): results}, time.time() - start_time


def main(size, edges, my_pos):
    G, n, pop_total, pop_init, max_iterate, edges = create_graph(size, edges)
    results, run_time = approximate_vc(G, n)
    print("runtime = " + str(run_time))
    print("Approximated_Algorithm_VC results:")
    print("nodes = {}".format(n))
    print(results)
    vc = results[min(results.keys())]
    color_map = ['lightgreen' if node in vc else 'r' for node in range(n)]
    display_graph(G, my_pos, color_map,
                  title='Approximated Algorithm: VC in green and others in red\n|VC| = {0}\nAlgorithm '
                        'run time: {1}'.format(len(vc), strftime("%H:%M:%S", gmtime(math.ceil(run_time)))))
