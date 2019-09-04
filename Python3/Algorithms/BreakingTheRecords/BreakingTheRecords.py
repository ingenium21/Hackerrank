#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    recordHigh = scores[0]
    recordLow = scores[0]
    countHigh = 0
    countLow = 0
    for i in range(1, len(scores)):
        if recordHigh < scores[i]:
            recordHigh = scores[i]
            countHigh += 1
        elif recordLow > scores[i]:
            recordLow = scores[i]
            countLow += 1

    a = [countHigh, countLow]
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
