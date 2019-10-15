#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
# this is what happens when you don't practice for three days
# made a lot of stupid mistakes, kept getting list index out of range errors because I was 
# basically trying to reinvent the wheel
# I wound up solving it in a really clunky way, which I'm going to post
# but in the comments I will put in a neater method
def serviceLane(n, cases):
    #nice and neat method:
    #ans = []
    #for i, j in cases:
    #    ans.append(min(width[i:j+1]))
    #return ans

    #extremely neat one liner code:
    #return [min(width[x:y+1]) for x,y in cases]

    #clunky method:
    ans = []
    for i in cases:
        minwidth = n
        for j in range(i[0],i[1]+1):
            if width[j] < minwidth:
                minwidth = width[j]
        ans.append(minwidth)
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
