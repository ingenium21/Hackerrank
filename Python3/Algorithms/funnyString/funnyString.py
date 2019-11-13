#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    ascii = [ord(c) for c in s] #get the ascii value of each char in the string
    differ = [] #this will be the array of diffs from i to i+1
    revDiffer = [] #and this is the reverse order of diffs
    for i in range(len(ascii)-1):
        #we loop through the array length - 1, 
        differ.append(abs(ascii[i+1] - ascii[i])) #we append the diffs
        revDiffer.append(abs(ascii[len(ascii)-i-1] - ascii[len(ascii)-i-2])) #we append the diffs in reverse order
    
    if differ == revDiffer: #compare the diff arrays
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
