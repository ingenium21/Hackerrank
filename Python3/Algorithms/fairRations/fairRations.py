#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    count = 0
    for i in range(N-1): #iterate through the array
        if B[i] % 2 == 1: #if the element is odd, you add one to it and one to the next element (i noticed that B[i] is never referened again so i removed it since it's not needed, but just pretend you add one to it)
            B[i+1] += 1
            count += 2 #increase the count by 2

    if B[N-1] %2 == 1: #if the last element of the array is odd, then this can't be completed, so we return NO
        return "NO"
    else:
        return count #if its even, then we're good and we return the count.
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
