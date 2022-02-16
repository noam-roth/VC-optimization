# VC-optimization
We implement 3 algorithms for the Vertex Cover problem:
* Brute Force algorithm
* Linear Programing algorithm
* Genetic algorithm

We create a random graph based on the number of vertices the user types, then run the three algorithms,
and present the solution (VC) of each of them, and also dispaly the run time of each of them.

### Brute Force algorithm
This is the naive approach - run on all the subgroups and search for VC.

### Linear Programing algorithm
Using Pulp library.

### Genetic algorithm
Generate solutions, create a fitness score function, and until convergence: selection - crossover - mutation.


### Compiling and Running
1. Run dependencies.bat
2. Run main.py (enter the number of vertices that you want)


