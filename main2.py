import numpy as np
from random import random

class Team:
    
    def __init__(self, percentageLastSeason, name):
        self.rank = percentageLastSeason/100
        self.historyVictoryScores = dict()
        self.historyChampionshipWinner = dict()
        self.victoryCnt = 0
        self.name = name
    
    def victory(self):
        self.victoryCnt += 1
        
    def save_result(self, nrOfSimulation):
        self.historyVictoryScores[nrOfSimulation] = self.victoryCnt
    
    def win_championship(self, nrOfSimulation):
        self.historyChampionshipWinner[nrOfSimulation] = 'first place'
    
    def clear_score(self):
        self.victoryCnt = 0


class TeamNode:
    
    def __init__(self, team):
        self.next = None
        self.team = team
        
class TeamList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.teamCnt = 0
        
    def add_teams(self, listOfTeams : list):
        self.listOfTeams = listOfTeams
        self.amountOfTeams = len(self.listOfTeams)
        self.head = TeamNode(self.listOfTeams[0])
        self.tail = self.head
        for team in range(1,len(self.listOfTeams)):
            self.tail.next = TeamNode(self.listOfTeams[team])
            self.tail = self.tail.next
            
    def __str__(self):
        current = self.head
        listOfNames = []
        listOfNames.append(current.team.name)
        while current.next != None:
            listOfNames.append(current.next.team.name)
            current = current.next
        return str(listOfNames)

                    
team1 = Team(14,'tettf1')
print(team1)
team2 = Team(66,'tejfjt')
team3 = Team(25,'ftjf')

teams = [team1,team2,team3]
listtt = TeamList()
listtt.add_teams(teams)
print(listtt) 

class Simulation():
    
    def __init__(self, listOfTeams : list):
        self.listOfTeams = listOfTeams
        self.amountOfTeams = len(listOfTeams)
          

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
    
    def saveScores(self, nr):
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
        self.saveScores(nrOfSimulation)