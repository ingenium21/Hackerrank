#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
#this was one of those dumb math geometry problems disguised as a prgoramming problem.  
def surfaceArea(A):
    H, W = len(A), len(A[0])
    area = 2 * H * W
    for i in range(H):
        for j in range(W):
            area += A[i][j] if i == 0 else abs(A[i][j] - A[i - 1][j])
            area += A[i][j] if j == 0 else abs(A[i][j] - A[i][j - 1])
            area += A[i][j] if i == H - 1 else 0
            area += A[i][j] if j == W - 1 else 0
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
