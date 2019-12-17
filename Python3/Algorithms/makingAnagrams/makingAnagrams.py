#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    for i in s1:
        #loop through s1, if that char is in s2, we replace that character in both s1 & s2 with null
        #once we're done, we are left with all the excesses
        #we add them up to return the number of deletions needed
        if i in s2:
            s1=s1.replace(i,"",1)
            s2=s2.replace(i,"",1)
    
    return(len(s1)+len(s2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
