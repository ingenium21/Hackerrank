#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
#pretty self explanatory, sort A and sort B in reverse, loop through range n to see if each element is >= k, else break and return "NO"
def twoArrays(k, A, B):
    A.sort() 
    B.sort(reverse=True)
    for i in range(n):
        if A[i] + B[i] < k:
            return "NO"
    
    return "YES"
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()