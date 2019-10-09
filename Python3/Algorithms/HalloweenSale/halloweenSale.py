#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    #here is a simple O(n) implementation using a while loop
    # count = 0
    # while (s >= p):
    #     s -= p
    #     p = max(p-d,m)
    #     count += 1
    # return count

    
    # Here is a O(1) implementation using linear arithmetic
    #I'll be honest, I have no idea how this solution works
    #I found it in a comment section and really wish the guy who wrote it explained it.
    kmax = ((p-m) // d)
    fmax = (kmax+1)*p-((kmax+1)*kmax*d) / 2

    if (s >= fmax):
        return int(kmax+1 + (s-fmax)/m)
    else:
        b = p*1.0/d - 0.5
        g = b - ((b*b-2/d*(s-p))**0.5)
        return int(math.ceil(g))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
