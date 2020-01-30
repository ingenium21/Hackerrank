#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimbleGame function below.
def nimbleGame(s):
    xor = 0
    for i in range(len(s)):
        if s[i] > 0:
            if s[i] % 2 == 0: xor ^= 0
            else: xor ^= i
    
    if xor != 0: return "First"
    else: return "Second"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = nimbleGame(s)

        fptr.write(result + '\n')

    fptr.close()
