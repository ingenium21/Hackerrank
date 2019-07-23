#Function should return the number of triplets forming a geometric progression for a given r as integer
#input format:
# n r
# n separated integers in arr[i]

#sample input:
# 4 2
# 1 2 2 4

# Sample output:
# 2

#notes:
# how am I going to make it iterate through the array looking for all possible geo progresses...
################################
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    second = dict() 
    third = dict()
    count = 0

    for i in arr:
        # if i is in third, then the triplet already completed and we need to increment the count
        if i in third:
            count += third[i]
        #if i is in second, then it is the second number of the triplet, successor needs to be added in case of a potential triplet
        if i in second:
            if i*r in third:
                third[i*r] += second[i] #if second i*r is in third, then we increase third's i*r by the value of second[i]
            else:
                third[i*r] = second[i]
        # else i is the first element of the triplet, so successor needs to be added or incremented in the r2 dict in case of potential triplet
        if i*r in second:
            second[i*r] += 1
        else:
            second[i*r] = 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
