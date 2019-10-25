#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    l1 = []

    for i in range(n):
        temp = 0
        temp = (i*a) + (n-i-1)*b
        l1.append(temp)
    
    ans = []
    ans = list(set(l1))
    ans.sort()
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
