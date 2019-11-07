#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    string = "hackerrank"
    if len(s) < len(string):
        return "NO"
    #loop through s until you have removed each letter from string sequentially, if you have done so successfully, then the string is a subsequence in s
    #also break the loop if string becomes empty early, no need to keep looping.
    for i in s:
        if i == string[0]:
            string = string[1:]    
        if len(string) == 0:
            return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
