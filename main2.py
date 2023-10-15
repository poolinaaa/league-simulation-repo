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
    
    def appendingElement(self,element: Team):
        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.tail = element
        

        
            
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
        probA, probB = self.calculate_probability(teamA.team.rank, teamB.team.rank)
        matchResult = random()
        
        if matchResult < probA:
            teamB.change_state()
            print(teamB.state)
            teamA.team.victory()
            if nrOfMatch + 1 == nrOfRounds:
                teamA.team.win_championship(simNr)
            return teamA
        else:
            teamA.change_state()
            print(teamA.state)
            teamB.team.victory()
            if nrOfMatch + 1 == nrOfRounds:
                teamB.team.win_championship(simNr)
            return teamB

    
    def saveScores(self, nr):
        for team in range(self.amountOfTeams):
            self.listOfTeams[team].save_result(nr)
            self.listOfTeams[team].clear_score()
    
    
    def simulate(self, nrOfSimulation):
        listSimulation = TeamList()
        listSimulation.add_teams(self.listOfTeams)

        for match in range(int(self.numberOfMatches)):
            current = listSimulation.head
            listNextRound = TeamList()
            while current and current.next:
                teamA = current
                teamB = current.next
                winner = self.play(teamA, teamB, match, self.numberOfMatches, nrOfSimulation)
                listNextRound.appendingElement(winner)
                current = current.next.next

            listSimulation = listNextRound

        self.saveScores(nrOfSimulation)

    


team1 = Team(90,'tettf1')
print(team1)
team2 = Team(66,'tejfjt')
team3 = Team(25,'ftjf')
team4 = Team(50,'dgdrtgggg')
team5 = Team(95,'tetf1')
print(team1)
team6 = Team(64,'tejt')
team7 = Team(5,'ff')
team8 = Team(55,'dgdrtg')
simulation = Simulation([team1,team2,team3,team4,team5,team6,team7,team8])

for sim in range(10):
    simulation.simulate(sim)
    
print(team1.historyVictoryScores)
print(team2.historyVictoryScores)
print(team3.historyVictoryScores)
print(team4.historyVictoryScores)
print(team5.historyVictoryScores)
print(team6.historyVictoryScores)
print(team7.historyVictoryScores)
print(team8.historyVictoryScores)