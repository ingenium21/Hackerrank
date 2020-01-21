#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    #one liner solution: (1 << (len(format(l^r, 'b')))) - 1
    lxr = l ^ r #get the xor of the limits

    #we're going to loop through lxr so that we can see how many bit positions there are
    bitpos = 0
    while(lxr):
        bitpos += 1
        lxr >>=1 #this bit shift operation, shifts the number's bits once to the right, decreasing each bit value, it's a handy way to count how many bits there are.
    
    #we will loop bitpos times, maxXor = maxXor + incr, incr will increase in value by bitshifting to the left (incr <<=1 )
    maxXOR = 0
    incr = 1
    while(bitpos):
        maxXOR += incr
        incr <<= 1
        bitpos -= 1
    
    return maxXOR
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
