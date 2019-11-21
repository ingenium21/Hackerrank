#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    stack = [0] #create a stack with a random character that isn't A or B
    dels = 0 #number of deletions you'll need
    for i in s:
        #go through each s, if the ith element doesn't equal the last letter, add it to the stack
        #else, you skip it and add 1 to dels.
        if i != stack[-1]:
            stack.append(i)
        else:
            dels += 1
    
    return dels

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
