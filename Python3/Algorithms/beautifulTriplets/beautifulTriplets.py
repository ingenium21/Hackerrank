#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    nums = set(arr) #create a set object of the numbers
    count = 0
    for i in arr:
        #we know what i will be, and we know what j - i needs to be
        # j - i = d
        # or i + d = j
        # and once we know that we can figure out k - j = d
        # or j + d = k
        # but we all know that j = i + d
        # so (i+d) + d = k
        # therefore we just need to find if i+d is in nums and i+d+d is is nums
        # THANKS ALGEBRA I!
        if i+d in nums and i+d+d in nums:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
