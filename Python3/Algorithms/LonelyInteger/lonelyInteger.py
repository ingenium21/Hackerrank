#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    #simple o(n) solution with O(n) space:
    #set_a = set(a)
    #for i in set_a:
    #    if a.count(i) == 1:
    #        return i
    
    #a slightly more complex solution with O(n) time and O(1) space:
    #using XOR, we compare each number, if a number repeats in an XOR gate, then val 
    # winds up being zero (x ^ x = 0)(0 ^ x = x)
    # for example a = [1,2,1] and val = 0
    # loop through a and you get: 0 XOR 1 = 1, 1 XOR 2 = 3, 3 XOR 1 = 2
    val = 0
    for i in a:
        val = val ^ i #^ is XOR
    
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
