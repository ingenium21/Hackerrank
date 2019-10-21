#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    if n == m:
        return 0
    else:
        c.sort() #we sort C so that the math works
        maxdist = max(c[0], n - c[-1] -1)
        #the distance between the first city and the first station is going to be 
        #c[0] - 0
        #the distance from the last city to the last space station is (n-1) - c[-1]
        #these are the smallest possible distances you can get

        for i in range(len(c)): # iterate only through the stations array
            distance = c[i] - c[i-1] #calculate the distance from one station to the next
            maxdist = max(distance // 2, maxdist)
            #now with distance calculated we can floor divide it by 2 (so we get no remainder)
            #this will give us the distance between the middle city to either station.
            #if distance // 2 is > than maxdist, we make it the new max
    
    return maxdist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
