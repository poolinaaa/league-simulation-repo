import numpy as np
from random import random
from scipy import stats

class Team:
    
    def __init__(self, percentageLastSeason):
        self.score = 0
        self.victoryCnt = 0
        self.lossCnt = 0
        self.drawCnt = 0
        self.rank = percentageLastSeason/100
        self.historyScores = dict()
        
    def __str__(self) -> str:
        return f'Current score is {self.score}'
    
    def victory(self):
        self.victoryCnt += 1
        self.score += 3
        
    def loss(self):
        self.lossCnt += 1
        
    def draw(self):
        self.drawCnt += 1
        self.score += 1
    
    def save_result(self, nrOfSimulation):
        self.historyScores[nrOfSimulation] = self.score
        
    def clear_score(self):
        self.score = 0
        self.victoryCnt = 0
        self.lossCnt = 0
        self.drawCnt = 0
    
    def calculate_average_score(self, simAmount):
        self.averageScore = (sum([score for score in self.historyScores.values()]))/simAmount 
        
class Simulation():
    
    def __init__(self, listOfTeams : list):
        self.listOfTeams = listOfTeams
        self.amountOfTeams = len(listOfTeams)
        
    def set_matrix_of_probability(self):
        
        self.probabilities = np.zeros(shape=(self.amountOfTeams,self.amountOfTeams), dtype = list)
        
        for row in range(self.amountOfTeams):
            for col in range(self.amountOfTeams):
                pA, pB, pD = self.calculate_probability(self.listOfTeams[row].rank, self.listOfTeams[col].rank)                
                self.probabilities[row][col] = [pA, pB, pD]
        print(self.probabilities)   

    def calculate_probability(self, rankA, rankB, epsilon = 0.001):
        sumRanks = rankA + rankB
        victoryProbA = rankA / (sumRanks + (abs(sumRanks) / (3 * (abs(sumRanks) + epsilon))))
        print(victoryProbA)
        victoryProbB = rankB / (sumRanks + (abs(sumRanks) / (3 * (abs(sumRanks) + epsilon))))
        print(victoryProbB)
        drawProb = 1 - victoryProbA - victoryProbB
        return victoryProbA, victoryProbB, drawProb

    def play(self, probA, probB, teamA, teamB):
        matchResult = random()
        sectionA = probA
        sectionB = probB
        
        if matchResult < sectionA:
            self.listOfTeams[teamA].victory()
            self.listOfTeams[teamB].loss()
        elif matchResult >= sectionA and matchResult < sectionA + sectionB:
            self.listOfTeams[teamA].loss()
            self.listOfTeams[teamB].victory()
        else:
            self.listOfTeams[teamA].draw()
            self.listOfTeams[teamB].draw() 
    
    def save_scores(self, nr):
        for team in range(self.amountOfTeams):
            self.listOfTeams[team].save_result(nr)
            self.listOfTeams[team].clear_score()
    
    def simulate(self, nrOfSimulation):
        for row in range(self.amountOfTeams):
            for col in range(self.amountOfTeams):
                if row != col:
                    listProb = self.probabilities[row][col]
                    self.play(listProb[0],listProb[1], teamA=row, teamB=col)
                else:
                    continue
        self.save_scores(nrOfSimulation)

    
    def stats(self, simAmount, alpha=0.05):
        self.meanScoreOfSimulations = []
        for nrOfSim in range(simAmount):
            sumScores = 0
            for team in range(self.amountOfTeams):
                sumScores += self.listOfTeams[team].historyScores[nrOfSim]
            result = sumScores / self.amountOfTeams
            self.meanScoreOfSimulations.append(result)
        self.hypothesis_testing(simAmount,alpha)

      
    def hypothesis_testing(self, simAmount, alpha):
        #h0 mean of sample is less than 2.5(N-1)
        #h1 mean of sample is greater than 2.5(N-1)
        meanValOfSim = sum(self.meanScoreOfSimulations)/simAmount
        test25N1 = 2.5*(self.amountOfTeams-1)

        t1, p1 = stats.ttest_1samp(self.meanScoreOfSimulations, test25N1, alternative='less')

        if p1 > alpha :
            #h0 mean of sample is greater than 2.5(N-1)
            print(f'There is {100 - alpha*100}% confidence that mean of average score (which is {meanValOfSim}) is greater than 2.5(N-1) = {test25N1}')
        else:
            #h0 mean of sample is less than 2.5(N-1)
            #h0 rejected
            print(f"On confidence level {100 - alpha*100}% mean of average score (which is {meanValOfSim}) is less than {test25N1}.")
                
team1 = Team(14)
team2 = Team(66)
team3 = Team(25)
team4 = Team(70)
team5 = Team(89)
team6 = Team(20)
team7 = Team(5)
team8 = Team(78)
team9 = Team(2)



simulation = Simulation([team2,team8,team9,team1,team4,team5,team3,team6,team7])
simulation.set_matrix_of_probability()

for sim in range(31):
    simulation.simulate(sim)
    
simulation.stats(31)


