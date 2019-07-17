#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0
    # given array 4 3 1 2
    # for i in range n-1
    #while arr[i] does not equal i + 1 bc that would be the correct location ie.
    # the if the 0th element is 1, then nothing needs to be swapped
    #create tempVariable and assign element in location arr[arr[i] - 1]
    # so if i = 0 arr[arr[0] -1] = arr[4-1] = arr[3] so tempVar = 2
    # arr[arr[0] -1] = arr[i] so arr[3] = arr[0] so 4 goes to the location he needs to be
    # array is now 4 3 1 4
    #arr[i] = tempVar so now array is 2 3 1 4
    #swap ++
    # and so on until all swaps are complete.
    for i in range(n-1):
        while arr[i] != i+1:
            tempVar = arr[(arr[i]-1)] 
            arr[arr[i]-1] = arr[i]
            arr[i] = tempVar
            swap += 1
    return swap
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
