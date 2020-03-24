import numpy
import sys

sys.setrecursionlimit(100000)

## At each step, we have two choices :
    # going to nearest positiv number,
    # or to nearest negativ number,
## Tried to use recursion to get the best path with at each step, choosing negativ
## or positiv by comparing the average wainting.

## Didn't work, maximum depth recursing limit exceed

def calcul(positiv, negativ, actualNode, actualDist, totalDist, totalNumber):
    if len(positiv) == 0 and len(negativ) == 0: # last node
        print('lastnode')
        print(totalDist / totalNumber)
        print(actualNode)
        print(" ")
        return ((totalDist / totalNumber), list())

    if len(positiv) == 0: # no more positiv
        actualDist += abs(negativ[0] - actualNode)
        actualNode = negativ[0]
        totalDist += actualDist
        copyNegativ = list(negativ)
        copyNegativ.pop(0)
        return (calcul(positiv, copyNegativ, actualNode, actualDist, totalDist, totalNumber)[0], negativ)

    if len(negativ) == 0: # no more negativ
        actualDist += abs(positiv[0] - actualNode)
        actualNode = positiv[0]
        totalDist += actualDist
        copyPositiv = list(positiv)
        copyPositiv.pop(0)
        return (calcul(copyPositiv, negativ, actualNode, actualDist, totalDist, totalNumber)[0], positiv)

    #positiv path
    actualDist1 = actualDist + abs(positiv[0] - actualNode)
    positivNode = positiv[0]
    totalDist1 = totalDist + actualDist1
    copyPositiv = list(positiv)
    copyPositiv.pop(0)
    positivPath = calcul(copyPositiv, negativ, positivNode, actualDist1, totalDist1, totalNumber)

    #negativ path
    actualDist2 = actualDist + abs(negativ[0] - actualNode)
    negativNode = negativ[0]
    totalDist2 = totalDist + actualDist2
    copyNegativ = list(negativ)
    copyNegativ.pop(0)
    negativPath = calcul(positiv, copyNegativ, negativNode, actualDist2, totalDist2, totalNumber)
    if positivPath[0] < negativPath[0]:
        res = positivPath[1]
        res.insert(0, positivNode)
        return (positivPath[0], res)
    else:
        res = negativPath[1]
        res.insert(0, negativNode)
        return (negativPath[0], res)

def parcours(randomNumpy):
    array = list(randomNumpy)
    array = randomNumpy.sort()

    positiveArr = list(filter(lambda x: x >=0, list(randomNumpy)))
    negativeArr = list(filter(lambda x: x <0, list(randomNumpy)))

    positiveArr.sort()
    negativeArr.sort(reverse=True)

    res = calcul(positiveArr, negativeArr,0, 0,0,len(list(randomNumpy)))

    return res[1]