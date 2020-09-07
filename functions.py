import random
from monsterlist2 import *



#xpTotal = input("How much XP do you want to grant?")
#partyLevel = input("What is the average party level?")
#Monster Spawner



def diceRoll(max, rolls):
    results = []
    for x in range(rolls):
        results.append(random.randint(1, max))
    return results


def hpCalculator(monster):
    splitlist = monster['Hit Points'].split()
    parsehp = splitlist[1].replace('(', '').replace(')', '').replace('d', ' ')
    parsehp = parsehp.split()
    multiple = int(parsehp[0])
    max = int(parsehp[1])
    results = diceRoll(max, multiple)
    sumres = sum(results)
    if len(splitlist) > 2:
        extra = splitlist[3].replace(')','')
        extra = int(extra)
        truehp = sumres + extra
    else:
        truehp = sumres
    return truehp



def monsterGenerator(totalxp, pl):
    totalxp = int(totalxp)
    equalcr = []
    monstersSpawned = []
    #make list of possible monsters based on challenge rating
    for i in monsterlist:
        if i["cr"] == (int(pl) + 1):
            equalcr.append(i)

        elif  i["cr"] == (int(pl)):
            equalcr.append(i)

        elif i["cr"] == (int(pl) - 1):
            equalcr.append(i)

        else:
            continue

    #Random add monsters into monstersSpawned
    monstersSpawned.append(random.choice(equalcr))
    xpsum = sum(i['xp'] for i in monstersSpawned)

    #stop when enough monsters based on requested XP
    while xpsum <= totalxp:
        monstersSpawned.append(random.choice(equalcr))
        xpsum = sum(i['xp'] for i in monstersSpawned)


    #print out the names only
    f = 0
    quicklist = []
    while f < len(monstersSpawned):
        name = monstersSpawned[f]['name']
        hp = hpCalculator(monstersSpawned[f])
        xp = monstersSpawned[f]['xp']
        quicklist.append('name: ' + str(name) + ' hp: ' + str(hp) + ' ' + 'xp: ' + str(xp))
        f += 1
    quicklist = '\n'.join(quicklist)
    print(quicklist)
    return quicklist
