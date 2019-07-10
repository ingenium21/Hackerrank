#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    pos = 0
    while pos < n-1:
        if pos+2 < n and c[pos+2] == 0:
            pos = pos + 2
            jumps += 1
        elif c[pos+1] == 0:
            pos += 1
            jumps += 1
        else:
            print("there are no possible moves")
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
