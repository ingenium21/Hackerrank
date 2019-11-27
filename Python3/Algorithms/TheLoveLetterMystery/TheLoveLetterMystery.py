#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    length = len(s)
    start = 0
    end = length - 1
    count = 0
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #create a array of your letters

    while (start < end):
        #if it needs to be a palindrome then the start == end, start +1 == end -1, etc.etc.
        #so we check each letter at both ends start going in until they've over taken each other
        #if we get to a point where the letter from the left is different from the letter from the right
        #then we get the index of that letter in alpha and subtract it from the other letter's index in alpha, that's the amount of changes you'll need to get them equal
        #add that number to count
        #you use the absolute value in the chance that the letter needs to go the other way in the alpha array.  Ex: s = 'cda', you need to change a to c, if you don't use the absolute value, you'll get a negative number.
        if s[start] != s[end]:
            count += abs((alpha.index(s[end]) - alpha.index(s[start])))
        start += 1
        end -= 1
    
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
