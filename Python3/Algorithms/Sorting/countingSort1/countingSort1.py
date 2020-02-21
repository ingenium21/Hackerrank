#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    nums = [0]*100 #make an array of zeroes amounting to all possible numbers you know are in the array in this case, 0 <= arr[i] < 100

    for i in arr: #sort through your array and add 1 to the ith place for nums
        nums[i] += 1

    return nums

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
