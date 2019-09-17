#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
openLi = ["[","{","("] #create array of the openers
closedLi = ["]","}",")"]  #create array of the closers; notice how each bracket is in the same index as the openers
def isBalanced(s):
    #we're going to declare an empty stack and then iterate through s
    #if the element is in the open list, then we append it to the stack
    #when we get to a closer, then we simply have to check that the corresponding opener is the last element that was appended
    stack = []
    for i in s:
        if i in openLi:
            stack.append(i)
        elif i in closedLi:
            pos = closedLi.index(i) #we grab the index so that we can check the index of the opener
            if ((len(stack) > 0) and (openLi[pos] == stack[len(stack) - 1])): #if the length of the stack is not empty and the open List's index is the same as the last element
                stack.pop() #pop it out
            else:
                return "NO" #otherwise it's unbalanced
    if len(stack) == 0: #in the end, if it's balanced, the stack should be empty.  If it isn't, it's unbalanced.
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
