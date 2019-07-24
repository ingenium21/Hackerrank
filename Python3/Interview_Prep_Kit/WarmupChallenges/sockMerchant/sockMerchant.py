#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    #setting the constraints
    CONST_MIN = 1
    CONST_MAX  = 100
    
    #check if ar meets the requirements
    if (len(ar) >= CONST_MIN and len(ar) <= CONST_MAX) \
    and isinstance(n, int) \
    and n >= CONST_MIN \
    and n <= CONST_MAX \
    and n == len(ar):
            pairs = 0
            ar.sort() #sort the array so that all pairs are next to each other
            ar.append('-1') #append -1 so that i can reach the end
            i = 0
            while i < n:
                if ar[i] == ar[i+1]: #if the Ith element in the array is equal to the one next to it
                    pairs += 1 #increase the number of pairs
                    i += 2 #skip the one next to it
                else:
                    i+=1 #don't skip the one next to it
    return pairs






if __name__ == '__main__':
    n = 7

    ar = [1,2,1,2,1,3,2]

    result = sockMerchant(n, ar)

    print(result)
