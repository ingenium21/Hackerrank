#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort(key = lambda x: (len(str(x)), str(x))) #sorting by length of digits 
    minPairs = []
    smallestDiff = 0
    currentDiff = 0
    ind = 0

    for i in range(len(arr) - 1):
        currentDiff = abs(arr[i+1] - arr[i])
        if smallestDiff == 0:
            smallestDiff = currentDiff
            minPairs.append(arr[i+1])
            minPairs.append(arr[i])
        else:
            if currentDiff < smallestDiff:
                smallestDiff = currentDiff
                minPairs = []
                minPairs.append(arr[i+1])
                minPairs.append(arr[i])

            elif currentDiff == smallestDiff:
                minPairs.append(arr[i+1])
                minPairs.append(arr[i])

    minPairs.sort()
    return minPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
