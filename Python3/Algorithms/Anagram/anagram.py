#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    count = 0 #to count the number of changes
    dict1 = {} #using dicts to control for repeating letters
    dict2 = {}
    if len(s) % 2 != 0: #if the length of the string is odd, then we can't split it so we return -1
        return -1
    
    else:
        for i in range(len(s)//2):
            #going in from both sides, we're going to assign each character from the 
            #front to dict1 and each character from the back to dict2 until we reach
            #the middle
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1
            if s[len(s)-i-1] not in dict2:
                dict2[s[len(s)-i-1]] = 1
            else:
                dict2[s[len(s)-i-1]] += 1

    for i in dict2:
        #for each character in dict2, we check if it's in dict1, if it is then we check
        #if they're the same number, if they're not then we add the difference to count
        if i in dict1:
            if dict2[i] > dict1[i]:
                count += (dict2[i] - dict1[i])
        else:
            #if it isn't in dict1 then we add the number of that character to count
            count += dict2[i]
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
