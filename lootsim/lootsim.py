import random
import json

def makeLoot():
    loot = {'iron': 0, 'gold': 0, 'tnt': 0, 'diamonds': 0}
    for i in range(random.randrange(5, 9)):
        itemNum = random.randrange(0, 35)
        if itemNum < 20:
            loot['iron'] += random.randrange(1, 5)
        elif itemNum < 30:
            loot['gold'] += random.randrange(1, 5)
        else:
            loot['tnt'] += random.randrange(1, 3)
    for i in range(random.randrange(1, 5)):
        itemNum = random.randrange(1, 4)
        if itemNum == 1:
            loot['diamonds'] += random.randrange(1, 3)
    return loot


def checkLoot():
    thresholds = json.load(open('thresholds.json'))
    loot = makeLoot()
    valid = True
    for item in loot.keys():
        if not thresholds[item]['min'] <= loot[item] <= thresholds[item]['max']:
            valid = False
    return valid

def sim():
    totalValid = 0
    for i in range(100000):
        if checkLoot():
            totalValid += 1
    print(str(totalValid/1000) + '% chance')


sim()
