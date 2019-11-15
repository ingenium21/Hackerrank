#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    array = [0]*(max(arr)+1) #declare an array of 0s equal to the max number + 1, this is to account for any 0s in the array
    for i in arr:
        #we loop through arr, whenever we encounter a number, we add 1 to array[thatNumber], this keeps track of how many times that number shows up
        array[i] += 1

    stack = [] #we create a third array, i called it stack because it's kinda stacky, but not really
    for i in range(len(array)):
        #we loop through array, every time we find a non-zero integer, that means that it shows up in arr so we add thatNumber*array[thatNumber] times
        #for example, if array = [0,3,2,0], then we know that arr had 3x[1] and 2x[2], sor sorted the stack would end up looking like this: [1,1,1,2,2]
        if array[i] != 0:
            stack += [i]*array[i]
    
    return stack
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
