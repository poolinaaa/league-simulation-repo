# League simulation



## Team Class
The Team class represents individual teams in the tournament. Teams can be created with a given percentage from the last season and a name.

### First simulation
- victory(): Increases victory count and score.
- loss(): Increases loss count.
- draw(): Increases draw count and score.
- save_result(nrOfSimulation): Saves the result of a simulation.
- clear_score(): Resets scores and counts.
- calculate_average_score(simAmount): Calculates the average score over simulations.
- check_score_of_exact_simulation(nrSim): Checks the score of a specific simulation.

### Second simulation


## Simulation Class

The Simulation class conducts the tournament simulations.

- set_matrix_of_probability(): Sets up the probability matrix based on team ranks (1st simulation).
- simulate(nrOfSimulation): Simulates matches for a specified number of iterations.
- stats(simAmount): Performs statistical analysis on simulation results.
- hypothesis_testing(simAmount, alpha): Conducts hypothesis testing on the mean score. (in first simulation)
- __str__(): Displays average scores of teams (1st simulation) or displays number of wins by each team (2nd simulation).

## Getting Started

1. Create team instances with their last season's percentages and names.
2. Initialize a Simulation instance with a list of created teams.
3. Set the matrix of probabilities using set_matrix_of_probability(). (if you are going to run first simulation)
4. Run simulations using the simulate() method.
5. Analyze tournament statistics using the stats() method.
