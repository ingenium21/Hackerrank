#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    i = 0 #our index
    # we want to iterate and loop through our array until we finally loop back around
    # easiest way to do this is the modulus operator
    # think of modulus like a clock; if n = 12, 1 % 12 = 1, and 13 % 12 = 1
    # so we will increase i by k, and then make it equal to that % n
    # until i = 0.
    # since the i will always start at 0, we must add a second conditional(e == 100) to make our while loop run the first time
    while i != 0 or e == 100:
        i = (i + k) % n
        if c[i] == 1:
            e -= 3
        else:
            e -= 1
    return e
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
