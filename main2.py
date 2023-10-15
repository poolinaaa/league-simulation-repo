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
        self.playCnt : int = 0 
        
    def add_teams(self, listOfTeams : list):
        self.listOfTeams = listOfTeams
        self.amountOfTeams = len(self.listOfTeams)
        self.head = TeamNode(self.listOfTeams[0])
        self.tail = self.head
        for team in range(1,len(self.listOfTeams)):
            self.tail.next = TeamNode(self.listOfTeams[team])
            self.tail = self.tail.next
    
    def eliminate_team(self, team_to_eliminate):
        if not self.head:
            return 
        
        if self.head.team == team_to_eliminate:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.team == team_to_eliminate:
                current.next = current.next.next
                return
            current = current.next
        
            
    def __str__(self):
        current = self.head
        listOfNames = []
        listOfNames.append(current.team.name)
        while current.next != None:
            listOfNames.append(current.next.team.name)
            current = current.next
        return str(listOfNames)

                    



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

    def play(self, teamA, teamB, nrOfMatch, nrOfRounds, simNr):
        probA, probB = self.calculate_probability(teamA.team.rank,teamB.team.rank)
        matchResult = random()
        
        if matchResult < probA:
            teamB.change_state()
            teamA.team.victory()
            if nrOfMatch + 1 == nrOfRounds - 1:
                teamA.team.win_championship(simNr)
            return teamB
        else:
            teamA.change_state()
            teamB.team.victory()
            if nrOfMatch + 1 == nrOfRounds:
                teamB.team.win_championship(simNr)
            return teamA
    
    def saveScores(self, nr):
        for team in range(self.amountOfTeams):
            self.listOfTeams[team].save_result(nr)
            self.listOfTeams[team].clear_score()
    
    def simulate(self, nrOfSimulation):
        listSimulation = TeamList()
        listSimulation.add_teams(self.listOfTeams)
        listSimulation.playCnt = int(self.amountOfTeams / 2)
        print(listSimulation)
        
        for match in range(int(self.numberOfMatches)):
            print(listSimulation)
            current = listSimulation.head
            for play in range(int(listSimulation.playCnt)):
                teamA = current
                teamB = current.next
                teamToRemove = self.play(teamA, teamB, match, self.numberOfMatches, nrOfSimulation)
                if teamToRemove == current:
                    if current.next.next != None:
                        current = current.next.next
                    listSimulation.eliminate_team(teamToRemove)
                else:
                    if current.next.next != None:
                        
                        current.next = current.next.next
                        current = current.next
                        listSimulation.eliminate_team(teamToRemove)
            listSimulation.playCnt = int(listSimulation.playCnt / 2)


        self.saveScores(nrOfSimulation)
        


team1 = Team(90,'tettf1')
print(team1)
team2 = Team(66,'tejfjt')
team3 = Team(25,'ftjf')
team4 = Team(50,'dgdrtgggg')

simulation = Simulation([team1,team2,team3,team4])

for sim in range(31):
    simulation.simulate(sim)
    
print(team1.historyVictoryScores)
print(team2.historyVictoryScores)
print(team3.historyVictoryScores)
print(team4.historyVictoryScores)