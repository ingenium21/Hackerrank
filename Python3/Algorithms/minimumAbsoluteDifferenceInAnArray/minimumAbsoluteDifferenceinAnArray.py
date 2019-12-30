#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    mindiff = 10**9 #maximum possible value of arr[i]
    arr.sort() #sort array in ascending order, takes O(n log n) time

    for i in range(n-1):
        #by comparing adjacent pairs in a sorted array we can find the smallest possible
        #diff in O(n Log n) time.
        if arr[i+1] - arr[i] < mindiff:
            mindiff = arr[i+1] - arr[i]

    return mindiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
