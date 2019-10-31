#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    stack = [] #create a stack array
    for i in s: #iterate through the array
        if i in stack and i==stack[-1]: #if the ith element is in stack and it == the last element in stack, then we pop it out of stack
            stack.pop()
        else: #if it's not in the stack or it's not in the last element of the stack then we append it
            stack.append(i)
    
    if len(stack) == 0:
        return "Empty String"
    else:
        return ''.join(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
