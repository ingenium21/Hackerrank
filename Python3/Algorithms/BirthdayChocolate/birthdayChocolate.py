#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        #By using s[x:y] we can iterate the exact number of sets of elements we want to sum
        #since the question calls for m to be the number of elements summed we just call the sum function
        # and tell it to sum s[i:m+i] which will tell it to go from ith to the m+ith element.
        if sum(s[i:m+i]) == d:
            count += 1
    return count

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
