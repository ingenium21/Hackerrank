#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    correct = "SOS" #we know this is the correct iteration of the message
    count = 0
    for i in range(len(s)):
        #loop through the string
        #if the ith element isn't equal to the corresponding position on correct
        #you add to the count
        #you modulo i by the length of correct so that if the ith element in s is > 3 you loop back around
        if s[i] != correct[i % len(correct)]:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
