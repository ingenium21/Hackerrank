#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    peaks = 0
    seaLevel = 0
    #we know his walks start and end at sea level
    #if we make sea level a number (0)
    #assign +1 for Us
    #assign -1 for Ds
    # we know that if a D action results in a zero, it's completing a peak
    #we know if a U action results in a zero, it's completing a valley
    #constraints: 2 >= n >= 10**6
    if(2<=n and n<=10**6):
        for i in range(len(s)):
            if s[i] == 'U':
                seaLevel += 1
                if seaLevel == 0: #Here we check to see if SeaLevel resulted in 0, if it did, then a valley was completed
                    valleys += 1
                    print(valleys)
            elif s[i] == 'D':
                seaLevel -= 1
                if seaLevel == 0: #here we check to see if seaLevel resulted in 0, if it did then a peak was completed.
                    peaks += 1
            else:
                print("invalid input!")
    else:
        print("n is out of approved range!")  
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
