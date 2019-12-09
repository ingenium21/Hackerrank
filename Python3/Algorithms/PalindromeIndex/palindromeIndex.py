#!/bin/python3

import math
import os
import random
import re
import sys
    
def isPalindrome(s):
    for i in range(len(s)):
        #if the first element does not equal the last element and so on we return false
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
# Complete the palindromeIndex function below.
def palindromeIndex(s):
    for i in range(len(s)):
        #if the low(i) element != the high(len(s) - i - 1) element we 
        #run the isPalindrome function with a substring removing the low element
        #if isPalindrome returns true then we return the low element
        #else we return the high element
        if s[i] != s[len(s) -i -1]:
            if isPalindrome(s[:i] + s[i+1:]):
                return i
            else:
                return len(s) - i - 1
    #if all lows == highs then we return -1
    return -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
