#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    # O(1) solution: 
    # we are using 32Bits of unsigned integers, which means the largest number is 2**32-1
    # in binary that's '1111111...' 32 times.
    # now all we need to do is use the bitwise XOR command between n and flipper.   All 0s will be flipped to 1s and all 1s will be flipped to 0s.
    flipper = (2**32)-1
    return n ^ flipper
    
    # less efficient solution requires turning n into a binary string, replacing all the 1s with 2s, the 0s with 1s, and then the 2s with 0s.

    # binstr = '{:032b}'.format(n) #use this to turn your number into a 32bit binary string

    # #we use the replace() method to replace all the 1s with 2s, all the 0s with 1s, and then all the 2s with 0s.
    # binstr = binstr.replace('1','2').replace('0','1').replace('2','0')
    
    # #we return the binary string converted back into an int using base 2.
    # return int(binstr,2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
