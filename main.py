class Team:
    
    def __init__(self, percentageLastSeason):
        self.score = 0
        self.victoryCnt = 0
        self.lossCnt = 0
        self.drawCnt = 0
        self.rank = percentageLastSeason/100
        
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
    
    def clearScore(self):
        self.score = 0
        self.victoryCnt = 0
        self.lossCnt = 0
        self.drawCnt = 0
        
        
        
def probability(rankA, rankB, epsilon):
    victoryProbA = rankA / (rankA + rankB + (abs(rankA + rankB) / (3 * (abs(rankA + rankB) + epsilon))))
    victoryProbB = rankB / (rankB + rankA + (abs(rankB + rankA) / (3 * (abs(rankB + rankA) + epsilon))))
    drawProb = 1 - victoryProbA - victoryProbB
    return victoryProbA, victoryProbB, drawProb

