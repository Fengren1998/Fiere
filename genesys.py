import random as rng

class GenesysDiceRoller:
    success = 0
    failure = 0
    advantage = 0
    threat = 0
    triumph = 0
    despair = 0
    netSuccess = 0
    netAdvantage = 0
    boost = [0,0,2,3,5,4]
    setback = [0,0,2,2,4,4]
    ability = [0,2,2,1,4,4,3,5]
    difficulty = [0,2,1,4,4,4,5,3]
    proficiency = [0,2,2,1,1,4,3,3,3,5,5,6]
    challenge = [0,2,2,1,1,4,4,3,3,5,5,6]
    '''
    0 n/a
    1 XX    FF
    2 X     F
    3 XA    FT
    4 A     T
    5 AA    TT
    6 TP    DR
    '''
    def rollDice(self, dicePool):
        self.success = 0
        self.failure = 0
        self.advantage = 0
        self.threat = 0
        self.triumph = 0
        self.despair = 0
        self.netSuccess = 0
        self.netAdvantage = 0
        for roll in range(dicePool[0]):
            self.sortResult(self.boost[self.dicePhysics(6)])
        for roll in range(dicePool[1]):
            self.sortResult(self.setback[self.dicePhysics(6)], False)
        for roll in range(dicePool[2]):
            self.sortResult(self.ability[self.dicePhysics(8)])
        for roll in range(dicePool[3]):
            self.sortResult(self.difficulty[self.dicePhysics(8)], False)
        for roll in range(dicePool[4]):
            self.sortResult(self.proficiency[self.dicePhysics(12)])
        for roll in range(dicePool[5]):
            self.sortResult(self.challenge[self.dicePhysics(12)], False)
        self.determineResult()

    def dicePhysics(self, sides):
        bounces = rng.randint(4, 10)
        result = rng.randint(1, sides)
        for roll in range(bounces):
            result = rng.randint(1, sides)
        return result - 1

    def sortResult(self, number, positive=True):
        if(positive == True):
            if(number == 1):
                self.success += 2
            elif(number == 2):
                self.success += 1
            elif(number == 3):
                self.success += 1
                self.advantage += 1
            elif(number == 4):
                self.advantage += 1
            elif(number == 5):
                self.advantage += 2
            elif(number == 6):
                self.triumph += 1
        else:
            if(number == 1):
                self.failure += 2
            elif(number == 2):
                self.failure += 1
            elif(number == 3):
                self.failure += 1
                self.threat += 1
            elif(number == 4):
                self.threat += 1
            elif(number == 5):
                self.threat += 2
            elif(number == 6):
                self.despair += 1

    def determineResult(self):
        self.netAdvantage = (self.advantage - self.threat)
        self.netSuccess = (self.success - self.failure)
