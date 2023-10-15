import numpy as np
from random import random
import math

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
        self.state = 'winner'
    
    def change_state(self):
        self.state = 'loser'
       
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


class Simulation():
    
    def __init__(self, listOfTeams : list):
        self.listOfTeams = listOfTeams
        self.amountOfTeams = len(listOfTeams)
        self.numberOfMatches = math.log2(self.amountOfTeams)

    def calculate_probability(self, rankA, rankB):
        victoryProbA = rankA / (rankA + rankB)
        print(victoryProbA)
        victoryProbB = 1 - victoryProbA
        print(victoryProbB)
        return victoryProbA, victoryProbB

    def play(self, teamA, teamB):
        probA, probB = self.calculate_probability(teamA.team.rank,teamB.team.rank)
        matchResult = random()
        
        if matchResult < probA:
            teamB.change_state()
            teamA.team.victory()
        else:
            teamA.change_state()
            teamB.team.victory()

    
    def saveScores(self, nr):
        for team in range(self.amountOfTeams):
            self.listOfTeams[team].save_result(nr)
            self.listOfTeams[team].clear_score()
    
    def simulate(self, nrOfSimulation):
        listSimulation = TeamList()
        listSimulation.add_teams(self.listOfTeams)
        listSimulation.teamCnt = self.amountOfTeams
        
        for match in range(int(self.numberOfMatches)):
            current  = listSimulation.head

            while current.next != None:
                listOfNames.append(current.next.team.name)
                current = current.next
       
            
        
        self.saveScores(nrOfSimulation)