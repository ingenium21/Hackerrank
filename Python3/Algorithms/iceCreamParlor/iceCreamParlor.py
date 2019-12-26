#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    flag = 0 #this is a flag to tell if we've reached two indices that equal m
    indices = [] #our indices array
    for i in range(len(arr)): #loop through the array to get the first index
        for j in range(len(arr)): #loop a second time to find a second index when added to the first equals m
            #and it's not the same index.
            if arr[i] + arr[j] == m and i != j:
                indices += [i+1] #add them to the array, break the loops
                indices += [j+1]
                flag = 1
                break
        if flag == 1:
            break
    
    return indices


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
