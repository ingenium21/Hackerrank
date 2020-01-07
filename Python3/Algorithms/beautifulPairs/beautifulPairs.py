#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    #you could get a lot of this done quicker and cleaner if you used the Counter() but i don't like 
    # solving stuff the easy way
    #first we're going to divide each array in their own dicts
    #we will traverse one dict and compare it to the other, if the element is in dict AND both dicts have the same value
    #we add that value to pairs, else we add the min value between the two dict elements
    #the question tripped me up, and i failed to realize that an element was going to change regardless, so for example,
    #if you have A = [1,2,3] and B=[1,2,3] the pairs answer isn't 3, but 2, because an element WILL change in B. similarly
    #if you have A = [1,2,3] and B=[1,2,4] the pairs answer will be 3
        dictA = {}
        dictB = {}
        pairs = 0
        if n == 1:
            return 0
        
        for i in range(n):
            if A[i]  in dictA:
                dictA[A[i]] += 1
            else:
                dictA[A[i]] = 1
            if B[i] in dictB:
                dictB[B[i]] += 1
            else:
                dictB[B[i]] = 1

        for i in dictA:
            if i in dictB:
                if dictB[i] == dictA[i]:
                    pairs += dictA[i]
                else:
                    pairs += min(dictA[i],dictB[i])
        
        if pairs == n:
            return pairs - 1
        else:
            return pairs + 1
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
