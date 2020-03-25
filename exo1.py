import numpy
import math

def removeHouseToIndex(array, index, intoArray):
    while index >= 0 and len(array) > 0:
        intoArray.append(array[0])
        array.pop(0)
        index -= 1

def parcours(randomNumpy):
    array = list(randomNumpy)
    array.sort()

    positiveArr = list(filter(lambda x: x >=0, list(randomNumpy)))
    negativeArr = list(filter(lambda x: x <0, list(randomNumpy)))

    positiveArr.sort()
    negativeArr.sort(reverse=True)

    res = []
    snowplow = 0
    firstArray = positiveArr
    secondArray = negativeArr

    if len(positiveArr) < len(negativeArr):
        firstArray = negativeArr
        secondArray = positiveArr
    
    removeHouseToIndex(firstArray, 340, res)
    removeHouseToIndex(secondArray, 475, res)
    removeHouseToIndex(firstArray, len(firstArray), res)
    removeHouseToIndex(secondArray, len(secondArray), res)
    
    return res