#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    #brute Force Solution:
    #arr = [0]*n
    #for i in queries:
    #    for j in range(i[0], i[1] + 1):
    #        arr[j - 1] += i[2]
    #return max(arr)
    #loops through the whole thing and adds the value k, too innefficient

    #use differnce array
    diffArr = [0 for i in range(n+1)]
    for i in queries:
        diffArr[i[0] - 1] += i[2]
        diffArr[i[1]] -= i[2]

    maxval = 0
    tsum = 0
    for j in diffArr:
        tsum += j
        if tsum > maxval:
            maxval = tsum
    return maxval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
