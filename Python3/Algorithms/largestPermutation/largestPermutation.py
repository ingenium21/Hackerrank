#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr, n):
    sortedArr = sorted(arr, reverse=True) # declare a reverse sorted array

    arrDict = {} 
    for j, item in enumerate(arr):
        arrDict[item] = j #dictionary to record item and index
    
    for i, item in enumerate(sortedArr):
        if arr[i] != item:
            k -= 1 #we spend a swap
            j = arrDict[item] #we make a temp variable (j) of the item
            arr[i], arr[j] = item, arr[i] #this is the actual swap code
            #we update the dictionary afterwards
            arrDict[item] = i
            arrDict[arr[j]] = j
            if 0 == k:
                return arr
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr, n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
