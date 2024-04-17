class Player:
    def __init__(self,name):
        self.__name=name# rename/ showName/ 
        self.__score=0 # + - show
        self.__hp=100 # + - show
        self.__currentStreak= 0 # + / set to 0
        self.__highestStreak=0 # setHighest streak

    #NAME 
    def setName(self,name):
        self.__name=name
    def getName(self):
        return(self.__name)
    
    #SCORE
    def _setScore(self, val):
        self.__score+=val
    def getScore(self):
        return(self.__score)

    #CurrentStreak
    def _setIncreaseCurrentStreak(self):
        self.__currentStreak+=1 
    def _setResetCurrentStreak(self):
        self.__highestStreak=self.__currentStreak
        self.__currentStreak=0
        
    def getCurrentStreak(self):
        return(self.__currentStreak)
       
    def setWin(self):
        _setScore(10)
        setIncreaseCurrentStreak()
    def setLose(self):
        _setScore(-10)
        _setResetCurrentStreak()