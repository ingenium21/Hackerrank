#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    mini = n #we know n is the largest minimum possible
    ob = {} #we create an object to store the indiex of each element

    #we loop through the array
    for i in range(n):
        #we use a try/except statement to find the last known index for the element in the dictionary
        #then we subtract it, if it's smaller than the last minimum, then we make mini equal to it
        try:
            mini = min(i-ob[a[i]], mini) #mini equals the minimum value between the element i and the last known index of the same element
            ob[a[i]] = i #we then change the last known position of the element
            if mini == 1: #if mini ever equals, 1, the code doesn't need to go further bc nothing will be shorter than that
                break
        except:
            ob[a[i]] = i #except is for what to do when an exception is thrown, in this case, it means that ob[a[i]] doesn't exist, so we add it
    
    if mini == n: #if mini is the same value as initialized then no elements are repeating, we return -1
        return -1
    else:
        return mini


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
