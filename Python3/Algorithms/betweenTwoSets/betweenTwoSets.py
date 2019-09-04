#!/bin/python3

import math
import os
import random
import re
import sys

# This is the brute force solution to this problem
# I hear theres a way to do this in O(n log(n)) complexity by finding the LCM and GCD of the arrays but meh, too annoying to care
# first it makes a list of both arrays, sorts them descending
# and then makes l = the first number which is the largest
# then while i is less than or equal to l, we use the all() function to test
# all the numbers in a to see if the ith number being considered is divisible with no remainder
# then we test all the numbers i b to see if all of them are divisible by the ith number with no remainder
# if they are they are true.  if both conditions are true then we add one to the total.  we return it when the loop is done.


def getTotalX(a, b):
    l = list(set(a) | set(b))
    l.sort(reverse=True)
    l = l[0]
    i = 0
    total = 0
    while i <= l:
        i += 1
        isAvalid = all(i % n == 0 for n in a)
        isBvalid = all(n % i == 0 for n in b)
        if isAvalid and isBvalid:
            total += 1 
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
