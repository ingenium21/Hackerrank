#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birdict = {1:0, 2:0, 3:0, 4:0, 5:0}
    for i in arr:
        birdict[i] += 1
    #since we know the array will always have one of these numbers, all we have to do is tell it to add it to the corresponding key
    #and we don't need to worry about sorting since we already sorted the dict ourselves.
    return(max(birdict,key=birdict.get))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
