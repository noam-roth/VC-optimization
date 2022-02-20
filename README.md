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
In the running examples we call it: 'Approximation algorithm'.

### Genetic algorithm
Generate solutions, create a fitness score function, and until convergence: selection - crossover - mutation.


### Compiling and Running
1. Download python 3.8+
2. Download this repo
3. Run dependencies.bat
4. Run main.py (enter the number of vertices that you want, for example: main.py 10)


### Running Examples
![Random Graph](https://github.com/noam-roth/VC-optimization/blob/1fa2066ac5cf3770cc6041b35bec44f595cc619b/pictures/Random%20Graph%20picture.PNG)


![Brute Force](https://github.com/noam-roth/VC-optimization/blob/1fa2066ac5cf3770cc6041b35bec44f595cc619b/pictures/Brute%20Force%20Picture.PNG)


![Linear Programing](https://github.com/noam-roth/VC-optimization/blob/1fa2066ac5cf3770cc6041b35bec44f595cc619b/pictures/Approximation%20Picture.PNG)


![Genetic](https://github.com/noam-roth/VC-optimization/blob/1fa2066ac5cf3770cc6041b35bec44f595cc619b/pictures/Genetic%20Picture.PNG)
