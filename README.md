# League simulation
This project offers a comprehensive framework for simulating sports tournaments. It uses statistical analyses to evaluate tournament results, providing insights into team performance and mean score hypotheses. Project simulates championship outcomes for a sports league based on team rankings from the previous season. The simulation assesses the relationship between a team's past performance and their championship victories.

## First simulation
The Simulation class manages the tournament simulations. It sets up a probability matrix based on team ranks and conducts match simulations using these probabilities. Additionally, it provides statistical analysis tools for tournament results, including hypothesis testing for mean scores.

Tournament Rules:

  1. Double Round-Robin: Every team competes against each other twice. 

  2. Outcome Generation: Match results are generated using a normal distribution to simulate randomness. The probability of a team winning, losing, or drawing is calculated using the following formulae:
   - The winning probability of a team A against team B is computed as:
  
          victoryProbA = rankA / (sumRanks + (abs(sumRanks) / (3 * (abs(sumRanks) + epsilon))))
  
   - The winning probability of team B against team A is similarly calculated.
   - The probability of a draw is derived from the remaining probability after accounting for the win probabilities of both teams.

  3. These probabilities are determined based on the relative ranks of the competing teams, where the rank of a team is calculated from the previous season's performance.
  4. Point System:
    Victory: When a team wins a match, they earn 3 points, contributing to their overall score.
    Loss: There is no point awarded for a loss.
    Draw: In the event of a draw, each team gains 1 point.

## Second simulation
Data structures: 
TeamNode and TeamList: These classes are used to manage a linked list of teams, organizing them for tournament simulations.

Correlation Analysis:
Statistical analysis, specifically Pearson's correlation coefficient, is applied to determine the relationship between a team's previous season ranking and their success in winning matches or championships.

This approach mirrors a classic tournament format and serves to predict championship outcomes based on the team's prior performance rankings.

Tournament rules:
  1. Power of Two Teams:
    The tournament requires the number of teams to be a power of two (e.g., 2, 4, 8, 16). This format ensures each round has an equal number of matches.
  
  2. Single Elimination:
    Teams compete in a single-elimination format, meaning if a team loses a match, they're eliminated from the tournament.
  
  3. Pairing and Rounds:
    Teams are paired up at the beginning of the tournament.
    Each round consists of matches between the paired teams.
    The number of rounds is determined by the logarithm base 2 of the total number of teams.
  
  4. Advancement:
    Winners of each match move on to the next round.
    Losers are eliminated from the tournament.

## Usage:

  Initialization: Teams are created with their respective last season rankings.
  Simulation: Simulate tournament outcomes across multiple rounds and track championship victories.
  Statistics: Analyze the correlation between team rankings and championship wins.




