#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    yesno = "YES"
    for i in range(n):
        for j in range(len(grid[i])):
            if i < n-1:
                if grid[i][j] > grid[i+1][j]:
                    yesno = "NO"
                    return yesno
    
    return yesno


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid_item = ''.join(sorted(grid_item)) #i told the driver code to sort before appending so i wouldn't have to worry about it.
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()