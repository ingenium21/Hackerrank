#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    d, v = {}, {} #declare two dictionaries
    for i in s:
        d[i] = d.get(i, 0) + 1 #use this one to get the number of instances of each char
    for i in d.values(): #use this to get the number of values of each char
        v[i] = v.get(i, 0) + 1
    n = len(v) #we get the lenght of v, if there's only one value, return YES
    if n == 1:
        return('YES')
    elif n == 2 and 1 in v.values(): 
        #if there are two values and one of those values occurrs once
        K = list(v.keys()) #get a list of the keys
        if v.get(1, 0) == 1 or (abs(K[0] - K[1]) == 1 and v.get(max(K)) == 1):
            #if one of those values is a 1, then return yes 
            #since you could remove that one and make it valid
            #or if abs(the difference) == 1 and only one instances of the max value
            #we return yes
            #if there's multiple instances of max then not valid, ie "aaabbccc" 
            return('YES')
    return('NO')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
