#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    ad = {n:arr.count(n) for n in set(arr)} #creates a dict of all arr values and number of instances of the value
    bd = {n:brr.count(n) for n in set(brr)} #creates a dict of all brr values and number of instances of the value

    [bd.pop(a) for a in ad if ad[a] == bd[a]]
        #for a in ad, if ad[a] has the same value as bd[a] then we pop it out of bd
        
    return sorted(bd.keys())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
