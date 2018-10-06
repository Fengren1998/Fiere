import random as rng

class GenesysDice:
    def __init__(self, sides, positive=True):
        self.sides = sides
        self.positive = positive
        if self.positive == True:
            self.triumph = 0
            self.success = 0
            self.advantage = 0
        else:
            self.despair = 0
            self.failure = 0
            self.threat = 0

    def reset(self):
        if self.positive == True:
            self.triumph = 0
            self.success = 0
            self.advantage = 0
        else:
            self.despair = 0
            self.failure = 0
            self.threat = 0

class GenesysDiceRoller:
    success = 0
    failure = 0
    advantage = 0
    threat = 0
    triumph = 0
    despair = 0
    net_success = 0
    net_advantage = 0
    proficiency_dice = GenesysDice(12)
    ability_dice = GenesysDice(8)
    boost_dice = GenesysDice(6)
    setback_dice = GenesysDice(6, False)
    difficulty_dice = GenesysDice(8, False)
    challenge_dice = GenesysDice(12, False)
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
    def roll_dice(self, dice_pool):
        self.success = 0
        self.failure = 0
        self.advantage = 0
        self.threat = 0
        self.triumph = 0
        self.despair = 0
        self.net_success = 0
        self.net_advantage = 0
        self.boost_dice.reset()
        self.setback_dice.reset()
        self.ability_dice.reset()
        self.difficulty_dice.reset()
        self.proficiency_dice.reset()
        self.challenge_dice.reset()

        for roll in range(dice_pool[0]):
            stored_side = self.dice_physics(6)
            self.sort_result(self.boost[stored_side], self)
            self.sort_result(self.boost[stored_side], self.boost_dice)
        for roll in range(dice_pool[1]):
            stored_side = self.dice_physics(6)
            self.sort_result(self.setback[stored_side], self, False)
            self.sort_result(self.setback[stored_side], self.setback_dice, False)
        for roll in range(dice_pool[2]):
            stored_side = self.dice_physics(8)
            self.sort_result(self.ability[stored_side], self)
            self.sort_result(self.ability[stored_side], self.ability_dice)
        for roll in range(dice_pool[3]):
            stored_side = self.dice_physics(8)
            self.sort_result(self.difficulty[stored_side], self, False)
            self.sort_result(self.difficulty[stored_side], self.difficulty_dice, False)
        for roll in range(dice_pool[4]):
            stored_side = self.dice_physics(12)
            self.sort_result(self.proficiency[stored_side], self)
            self.sort_result(self.proficiency[stored_side], self.proficiency_dice)
        for roll in range(dice_pool[5]):
            stored_side = self.dice_physics(12)
            self.sort_result(self.challenge[stored_side], self, False)
            self.sort_result(self.challenge[stored_side], self.challenge_dice, False)

        self.determine_result()

    def dice_physics(self, sides):
        bounces = rng.randint(sides, sides + 4)
        result = rng.randint(1, sides)
        for roll in range(bounces):
            result = rng.randint(1, sides)
        return result - 1

    def sort_result(self, number, target, positive=True):
        if(positive == True):
            if(number == 1):
                target.success += 2
            elif(number == 2):
                target.success += 1
            elif(number == 3):
                target.success += 1
                target.advantage += 1
            elif(number == 4):
                target.advantage += 1
            elif(number == 5):
                target.advantage += 2
            elif(number == 6):
                target.triumph += 1
        else:
            if(number == 1):
                target.failure += 2
            elif(number == 2):
                target.failure += 1
            elif(number == 3):
                target.failure += 1
                target.threat += 1
            elif(number == 4):
                target.threat += 1
            elif(number == 5):
                target.threat += 2
            elif(number == 6):
                target.despair += 1

    def determine_result(self):
        self.net_advantage = (self.advantage - self.threat)
        self.net_success = (self.success - self.failure)
