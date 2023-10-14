import numpy as np
import pandas as pd
from random import random

class Team:
    
    def __init__(self, percentageLastSeason):
        self.score = 0
        self.victoryCnt = 0
        self.lossCnt = 0
        self.drawCnt = 0
        self.rank = percentageLastSeason/100
        self.historyScores = None
        
    def __str__(self) -> str:
        return f'Current score of team {self.__name__} is {self.score}'
    
    def victory(self):
        self.victoryCnt += 1
        self.score += 3
        
    def loss(self):
        self.lossCnt += 1
        
    def draw(self):
        self.drawCnt += 1
        self.score += 1
    
    def clear_score(self):
        self.score = 0
        self.victoryCnt = 0
        self.lossCnt = 0
        self.drawCnt = 0
        
        
        


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
                

    def calculate_probability(self, rankA, rankB, epsilon = 0.001):
        sumRanks = rankA + rankB
        victoryProbA = rankA / (sumRanks + (abs(sumRanks) / (3 * (abs(sumRanks) + epsilon))))
        victoryProbB = rankB / (sumRanks + (abs(sumRanks) / (3 * (abs(sumRanks) + epsilon))))
        drawProb = 1 - victoryProbA - victoryProbB
        return victoryProbA, victoryProbB, drawProb

    def play(self, probA, probB):
        matchResult = random()
        sectionA = probA
        sectionB = probB
        
        if matchResult < sectionA:
            pass
        elif matchResult >= sectionA and matchResult < sectionA + sectionB:
            pass
        else:
           pass 
        
    def simulate(self):
        for row in range(self.amountOfTeams):
            for col in range(self.amountOfTeams):
                if row != col:
                    listProb = self.probabilities[row][col]
                    



team1 = Team(55)
team2 = Team(89)
team3 = Team(25)

sim = Simulation([team1,team2,team3])
sim.set_matrix_of_probability()

for sim in range(31):
    