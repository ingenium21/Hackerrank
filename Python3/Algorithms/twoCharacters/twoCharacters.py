#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations #we're gonna need this to easily combo the strings

def alternate(s):
    if len(s) <=1: #if the length is <= 1 there's no alternating so return 0
        return 0
    
    stringSet = set(s) #create a set of s
    longest = 0 #use this to keep track of the longest alternating string of two characters

    for char1,char2 in combinations(stringSet,2):
        #combinations() will create an object of every possible 2 letter combo
        temp = [i for i in s if (i == char1 or i == char2)]
        #we create a temporary array that stores every element that equals said combo
        if all(x != y for x,y in zip(temp, temp[1:])):
            #here's where it gets a little tricky
            #using zip() we assign two variables to compare the elements of temp and temp[1:] which is the rest of the string after the first element
            #if temp[0] != temp[1], and temp[1] != temp[2]...then the all() method returns true
            longest = max(longest, len(temp))
            #if the all method returns true, then we assign longest to the max between the current longest and the length of temp
    return longest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
