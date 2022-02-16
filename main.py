import Brute_force_Algorithm_VC
import Approximated_Algorithm_VC
import Genetic_Algorithm_VC
import graph_manipulator
import sys

if __name__ == '__main__':
    size = int(sys.argv[1])
    vertices, edges = graph_manipulator.generate_graph(size)
    print("-------------------------start-------------------------")
    print("Brute_force_Algorithm_VC start:")
    graph_pos = Brute_force_Algorithm_VC.main(vertices, edges)
    print("Approximated_Algorithm_VC start:")
    Approximated_Algorithm_VC.main(size, edges, graph_pos)
    print("\nGenetic_Algorithm_VC start:")
    Genetic_Algorithm_VC.main(size, edges, graph_pos)
    print("-------------------------end-------------------------")
