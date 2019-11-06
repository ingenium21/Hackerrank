#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    shiftCount = 0
    for i in range(1,len(arr)):
        key = arr[i] #we grab the ith element as the key to compare all elements
        j = i-1 #j will be assigned the element before it
        while j >= 0 and key < arr[j]: #while j is >= 0 and key < the jth element we do the shift
            arr[j+1] = arr[j] #the ith element is shifted to the jth element
            shiftCount += 1 #we count the shift
            j -= 1 #we subtract j by one two spaces before the ith element
        arr[j+1] = key #we make the original jth element equal to the ith element

    return shiftCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
