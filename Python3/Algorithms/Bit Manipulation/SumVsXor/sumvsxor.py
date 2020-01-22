#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    #simple solution that doesn't pass test cases with large numbers:
    # count = 0
    # for i in range(n+1):
    #     if n^i == n + i:
    #         count += 1
    # return count
    unset_bits = 0 #use to keep track of count of unset bits in bin(n)
    while(n > 0):

        if n & 1 == 0:
            unset_bits += 1
        n >>= 1
    
    return (1 << unset_bits)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
