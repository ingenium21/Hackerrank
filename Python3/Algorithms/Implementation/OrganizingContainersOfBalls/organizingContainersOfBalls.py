#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    mRow = [] #create an array of the sums of rows
    mCol = [] #cretae an array of the sums of columns

    
    #we are going to get the number of rows to know how many balls can fit in each container
    #then we get then sum of each column to get the number of each type of ball
    for i in range(n):
        mRow.append(sum(container[i]))
        total = 0
        for j in range(n):
            total += container[j][i]
        mCol.append(total)

    mRow.sort()
    mCol.sort()
    #we sort each array, if the number of types == to the number in each container, it is possible.  Else it's impossible.
    if mRow == mCol:
        return "Possible"
    else:
        return "Impossible"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
