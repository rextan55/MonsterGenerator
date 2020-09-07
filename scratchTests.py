from monsterlist import *
from monsterTest
import json
import random

monlis = monsterlist
def xpformat(ml):
    rawChallenge = ml["Challenge"]
    splitChallenge = rawChallenge.split()
    #XP parser
    xpValue = splitChallenge[1]
    xpValue = xpValue.replace('(', '').replace(')', '').replace(',', '')
    intChallenge = int(xpValue)

    return intChallenge


    #CR parser
def crformat(ml):
    rawChallenge = ml["Challenge"]
    splitChallenge = rawChallenge.split()
    rawcr = splitChallenge[0]
    splitChallenge = rawChallenge.split()
    x = '/'
    if x in rawcr:
        rawcr = rawcr.replace(x, ' ')
        rawcr = rawcr.split()
        num = int(rawcr[0])
        den = int(rawcr[1])
        cr = (float(num / den))

        return cr
    else:
        cr = int(rawcr)
        return cr


def appender(x):
    newlist = []

    for monster in x:
        newmonster = monster.copy()
        monsterxp = xpformat(monster)
        monstercr = crformat(monster)
        newmonster['xp'] = monsterxp
        newmonster['cr'] = monstercr
        newlist.append(newmonster)

    print(newlist)

    with open("monsterlist2.py" , "w") as fout:
        json.dump(newlist, fout)
