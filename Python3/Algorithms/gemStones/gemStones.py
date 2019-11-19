#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    gems = set(arr[0]) #created a new set of the first string
    for i in arr:
        gems = gems & i #using the Bitwise AND (&) operator, gems will equal any character that is both in gems and in i.
    
    return len(gems) #return the length.
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = set(input()) #I added the set command to the driver code so that it would create an array of sets.
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
