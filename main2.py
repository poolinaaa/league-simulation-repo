import numpy as np
from random import random

class Team:
    
    def __init__(self, percentageLastSeason):
        self.rank = percentageLastSeason/100
        self.historyVictoryScores = dict()
        self.historyChampionshipWinner = dict()
        self.victoryCnt = 0
        
    def __str__(self) -> str:
        return f'Current score of team {self.__name__} is {self.score}'
    
    def victory(self):
        self.victoryCnt += 1
        
    def save_result(self, nrOfSimulation):
        self.historyScores[nrOfSimulation] = self.victoryCnt
    
    def win_championship(self, nrOfSimulation):
        self.historyChampionshipWinner[nrOfSimulation] = 'first place'
        
    
    def clear_score(self):
        self.victoryCnt = 0
