#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    pivot = arr[0] #we choose a pivot, doesn't really matter which

    left = [] #divide into three arrays, left is for all numbers < pivot
    right = [] #nums > pivot
    equal = [] #nums == pivot

    for i in arr: #loop through the array and organize your elements in ther prospective lists
        if i == pivot:
            equal.append(i)
        elif i < pivot:
            left.append(i)
        else:
            right.append(i)
    
    left.extend(equal) #extend command lets you "merge" an array to another
    left.extend(right)
    return left

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
