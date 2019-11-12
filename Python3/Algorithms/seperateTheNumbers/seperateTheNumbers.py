#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    # Complete this function
    if s[0] == s: #if the string is one element, then it's not beautiful
        print('NO')
    
    for i in range(1,len(s)):
        #the for loop is to determine the digits we will use, we start with 1 digit
        stack = [] #we create a stack to append the numbers
        stack.append(s[:i]) #s[:1] will return us the first digit, s[:2] the first two digits, etc etc
        while len(''.join(stack)) < len(s): #we join the stack and determine the length of it, if it's less than len(s) then we continue
            stack.append(str(int(stack[-1])+ 1)) #we keep appending 1+ the last number until we reach len(s)
        
        if ''.join(stack) == s: #if the joined stack is identical to s, then we print 'YES' and the first element of the stack which is the lowest number
            print('YES', stack[0])
            break #make sure to break so it doesn't keep going
        if i == len(s) -1: #if i winds up equalling len(s) -1 then that means stack[0] is going to be the whole string, so it never found any beautiful numbers.  so we print 'NO' 
            print('NO')

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
