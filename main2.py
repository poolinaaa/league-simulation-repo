from random import random
import math
from scipy import stats

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
        victoryProbB = 1 - victoryProbA
        return victoryProbA, victoryProbB

    def play(self, teamA, teamB, nrOfMatch, nrOfRounds, simNr):
        probA, probB = self.calculate_probability(teamA.team.rank, teamB.team.rank)
        matchResult = random()
        
        if matchResult < probA:
            teamB.change_state()
            teamA.team.victory()
            if nrOfMatch + 1 == nrOfRounds:
                teamA.team.win_championship(simNr)
            return teamA
        else:
            teamA.change_state()
            teamB.team.victory()
            if nrOfMatch + 1 == nrOfRounds:
                teamB.team.win_championship(simNr)
            return teamB

    
    def save_scores(self, nr):
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

        self.save_scores(nrOfSimulation)
        
    def stats(self):
        listOfRanks = [team.rank for team in self.listOfTeams]
        listAmountOfWonChampionships = [len(team.historyChampionshipWinner) for team in self.listOfTeams]
        r,p = stats.pearsonr(listOfRanks, listAmountOfWonChampionships)
        if r > 0 and r < 0.3:
            print('There is not relationship between (or there is really weak relationship) rank and amount of won matches')
            print(f"The correlation coefficient (Pearson's r : {r})")
        elif r >= 0.3 and r < 0.5:
            print('There is moderate relationship between rank and amount of won matches')
            print(f"The correlation coefficient (Pearson's r : {r})")
        elif r >= 0.5 and r < 0.7:
            print('There is strong relationship between rank and amount of won matches')
            print(f"The correlation coefficient (Pearson's r : {r})")
        elif r >= 0.7:
            print('There is really strong relationship between rank and amount of won matches')
            print(f"The correlation coefficient (Pearson's r : {r})")
        
    def __str__(self):
        resultWinners = []
        for team in range(self.amountOfTeams):
            resultWinners.append(f'The number of wins by the {self.listOfTeams[team].name} is {len(self.listOfTeams[team].historyChampionshipWinner)}')
        return '\n'.join(resultWinners)


team1 = Team(69,'Boston Celtics')
team2 = Team(48,'Chicago Bulls')
team3 = Team(52,'Los Angeles Lakers')
team4 = Team(26,'San Antonio Spurs')
team5 = Team(41,'Orlando Magic')
team6 = Team(16,'Detroit Pistons')
team7 = Team(70,'Milwaukee Bucks')
team8 = Team(64,'Denver Nuggets')
simulation = Simulation([team1,team2,team3,team4,team5,team6,team7,team8])

for sim in range(100):
    simulation.simulate(sim)

simulation.stats()
print()
print(simulation)
