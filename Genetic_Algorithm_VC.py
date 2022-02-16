import copy
import time
import numpy as np
import random
import math
from time import strftime
from time import gmtime
from graph_manipulator import display_graph, create_graph


# Create random population --> random groups of k-size vertices.
def initialization(initial_population, amount_of_nodes, k):
    solutions = []
    for i in range(initial_population):
        sol = np.zeros(amount_of_nodes)
        samples = random.sample(range(0, amount_of_nodes), k)
        for j in range(k):
            sol[samples[j]] = 1
        solutions.append(sol)
    return solutions


# Evaluate the fitness --> defined fitness score as the function of covered edges.
# Best solution --> cost = 0 (all edges covered).
def fitness_score(solution, edges):
    cost = 0
    for edge in edges:
        if solution[edge[0]] == 0 and solution[edge[1]] == 0:
            cost += 1
    return cost


# Find the best solutions, according to the fitness_score - and pass them to the next generation, and kill the rest.
# For convergence - we pass at most 'max_population' solutions to the next generation.
def selection(edges, solutions, max_population):
    fitness_score_list = []
    output_lst = []
    for sol in solutions:
        fitness_score_list.append(fitness_score(sol, edges))
    sorted_index = np.argsort(fitness_score_list)
    for i in range(len(solutions)):
        output_lst.append(solutions[sorted_index[i]])
        if (i + 1) == max_population:
            break
    lst = output_lst
    # Return truncated-population and best score of this Generation
    return lst, fitness_score_list[sorted_index[0]]


# We combine two solutions in order to get even a better solution.
# take two solutions, find the vertices in the first solution which are not present in the second solution,
# and similarly take vertices in the second solution which are not present in the first solution and swap 50% of them.
# Swap 50% unique vertices from Solution2 into Solution1
def crossover(edges, amount_of_nodes, solutions):
    crossover_prob = 0.5
    next_generation_solutions = copy.deepcopy(solutions)
    for sol in solutions:
        new_sol = copy.deepcopy(sol)
        sol2 = solutions[random.randint(0, len(solutions) - 1)]
        unique1 = np.where(np.array(new_sol) == 1)[0].tolist()
        unique2 = np.where(np.array(sol2) == 1)[0].tolist()
        unique1 = np.setdiff1d(np.array(unique1), np.array(unique2))
        random.shuffle(unique1)
        unique2 = np.setdiff1d(unique2, unique1)
        random.shuffle(unique2)
        swap = math.ceil(crossover_prob * min(len(unique1), len(unique2)))
        for j in range(swap):
            new_sol[unique1[j]] = 1
            new_sol[unique2[j]] = 0
        next_generation_solutions.append(mutation(new_sol, edges, amount_of_nodes))
    return next_generation_solutions


# new solutions coming out from the Crossover-state change themselves slightly
# or alternatively mutate in the hope to get even better.
# In this problem, I perform two types of mutations changing 5% of the solution.
# I toss a coin and if the head comes, I perform Mutation-1
# else perform Mutation-2 both changing 5% of the solution differently.
# In Mutation-1, I take random 5% of vertices from the solution
# and replace it by some other random 5% vertices which were not in the solution before.
# In Mutation-2, I take random 5% of vertices from the solution and replace it by some other 5% vertices which can cover
# some of the edges which the current solution is fails to cover.
def mutation(new_sol, edges, amount_of_nodes):
    nodes_in_new_sol = []
    nodes_are_not_in_new_sol = []
    for i in range(amount_of_nodes):
        if new_sol[i] == 0:
            nodes_are_not_in_new_sol.append(i)
        else:
            nodes_in_new_sol.append(i)
    random.shuffle(nodes_are_not_in_new_sol)
    random.shuffle(nodes_in_new_sol)
    if random.random() <= 0.5:  # first mutation:
        swaps = min(len(nodes_in_new_sol), len(nodes_are_not_in_new_sol))
        for j in range(swaps):
            if random.random() < 0.05:
                new_sol[nodes_in_new_sol[j]] = 0
                new_sol[nodes_are_not_in_new_sol[j]] = 1
                temp = nodes_in_new_sol[j]
                nodes_in_new_sol[j] = nodes_are_not_in_new_sol[j]
                nodes_are_not_in_new_sol[j] = temp
    else:  # second mutation:
        mutate_lst = list(uncovered_edges(edges, new_sol))
        random.shuffle(mutate_lst)
        swaps = min(len(nodes_in_new_sol), len(mutate_lst))
        for j in range(swaps):
            if random.random() < 0.05:
                new_sol[nodes_in_new_sol[j]] = 0
                new_sol[mutate_lst[j]] = 1
                temp = nodes_in_new_sol[j]
                nodes_in_new_sol[j] = mutate_lst[j]
                mutate_lst[j] = temp
    return new_sol


# Return a set of edges which the given solution doesn't cover --> return a set of their vertices.
def uncovered_edges(edges, solution):
    my_list = []
    for edge in edges:
        (u, v) = edge
        if solution[u] == 0 and solution[v] == 0:
            if (random.random() < 0.5) and u not in my_list:
                my_list.append(u)
            elif v not in my_list:
                my_list.append(v)
    return set(my_list)


def genetic_algo_vc(amount_of_nodes, edges, k, initial_population, max_population, max_iterate):
    solutions = initialization(initial_population, amount_of_nodes, k)
    current_fitness_score = None
    for i in range(max_iterate):
        solutions, current_fitness_score = selection(edges, solutions, max_population)
        # check if one of the best_solutions get fitness_score = 0 --> VC solution --> covered all edges.
        if current_fitness_score == 0:
            break
        else:
            solutions = crossover(edges, amount_of_nodes, solutions)
    result = []
    solution = solutions[0]
    for j in range(len(solution)):
        if solution[j] == 1:
            result.append(j)
    return result, current_fitness_score


def find_optimal_k(amount_of_nodes, pop_init, pop_total, max_iterate, edges, start, end):
    # measure time:
    start_time = time.time()
    result_dict = {}
    l = start
    h = end
    while l <= h:
        m = int((l + h) / 2.0)
        result, cost_value = genetic_algo_vc(amount_of_nodes, edges, m, pop_init, pop_total, max_iterate)
        if cost_value == 0:
            print("Find VC but I'm not sure it's minimum VC!")
            result_dict[m] = result
            h = m - 1
        else:
            l = m + 1
    return result_dict, time.time() - start_time


def main(size, edges, my_pos):
    G, n, pop_total, pop_init, max_iterate, edges = create_graph(size, edges)
    # check if we don't have any edges in the graph:
    if len(edges) == 0:
        run_time = 0
        results = {}
    else:
        # amount_of_nodes, pop_init, pop_total, max_iterate, edges, start, end
        results, run_time = find_optimal_k(n, pop_init, pop_total, max_iterate, edges, 1, n)
    print("runtime = " + str(run_time))
    print("Genetic_Algorithm_VC results:")
    if not results:
        vc = []
    else:
        vc = results[min(results.keys())]
    # vc, fitness_score = genetic_algo_vc(n, edges, k, pop_init, pop_total, max_iterate)
    color_map = ['lightgreen' if node in vc else 'r' for node in range(n)]
    display_graph(G, my_pos, color_map, title='Genetic Algorithm: VC in green and others in red\n|VC| = {0}\nAlgorithm '
                                              'run time: {1}'.format(len(vc),
                                                                     strftime("%H:%M:%S", gmtime(math.ceil(run_time)))))
