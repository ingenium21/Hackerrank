#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the misereNim function below.
def misereNim(s):
    ans = 0
    count = 0
    for i in range(len(s)):
        ans ^= s[i]
        if s[i] <= 1:
            count += 1

    if (count == n and ans == 1) or (count < n and ans==0):
        return "Second"
    else:
        return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
