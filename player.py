class Player:
    def __init__(self,name):
        self.name=name# rename/ showName/ 
        self._score=0 # + - show
        self._currentStreak= 0 # + / set to 0
        self._highestStreak=0 # setHighest streak
        self._previousTurnWin=False
    #SCORE
    def setWin(self):
        self._score+=1
    def setLose(self):
        self._score-=1
    def getScore(self):
        return(self._score)

    #CurrentStreak
    def setIncreaseCurrentStreak(self):
        self._currentStreak+=1 
    def setResetCurrentStreak(self):
        self._currentStreak=0
    def getCurrentStreak(self):
        return(self._currentStreak)

    def rename(self,name):
        self.name=name

    

