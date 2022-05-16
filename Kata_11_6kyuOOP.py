"""https://www.codewars.com/kata/61b09ce998fa63004dd1b0b4/train/python"""

EXPERIENCE = {1: 0, 2: 83, 3: 174, 4: 276, 5: 388, 6: 512, 7: 650, 8: 801, 9: 969, 10: 1154, 11: 1358, 12: 1584,
              13: 1833, 14: 2107, 15: 2411, 16: 2746, 17: 3115, 18: 3523, 19: 3973, 20: 4470, 21: 5018, 22: 5624,
              23: 6291, 24: 7028, 25: 7842, 26: 8740, 27: 9730, 28: 10824, 29: 12031, 30: 13363, 31: 14833, 32: 16456,
              33: 18247, 34: 20224, 35: 22406, 36: 24815, 37: 27473, 38: 30408, 39: 33648, 40: 37224}
ROCKS = {'Clay': (1, 5), 'Copper': (1, 17.5), 'Tin': (1, 17.5), 'Iron': (15, 35), 'Silver': (20, 40), 'Coal': (30, 50),
         'Gold': (40, 65)}

class Miner:
    def __init__(self, xp=0):
        self.xp = xp
        if xp > 37224:
            self.level = 40
        else:
            self.level = [i for i in EXPERIENCE.items() if xp < i[1]][0][0]-1

    def mine(self, rock):
        if self.level >= ROCKS[rock][0]:
            self.xp += ROCKS[rock][1]
            if self.level < 40:
                if self.xp >= EXPERIENCE[self.level+1]:
                    self.level += 1
                    return f"Congratulations, you just advanced a Mining level! Your mining level is now {self.level}."
                return f"You swing your pick at the rock."
            else:
                return f"You swing your pick at the rock."
        else:
            return f"You need a mining level of {ROCKS[rock][0]} to mine {rock}."

    def get_info(self):
        print(f"Level {self.level}, xp = {self.xp}")


miner2 = Miner(40000)
miner2.get_info()
print(miner2.mine("Gold"))