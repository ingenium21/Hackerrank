#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    dictChar = {}
    for i in s:
        if i in dictChar:
            dictChar[i] += 1
        else:
            dictChar[i] = 1
    
    odds = 0
    for i in dictChar:
        if dictChar[i] & 1: # if num bitwiseAND 1 is true, then the last binary digit is a 1 and that means the number is odd
            odds += 1
    
    if odds > 1:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
