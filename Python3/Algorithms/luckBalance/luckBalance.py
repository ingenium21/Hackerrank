#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0 #we gain luck by losing, and we can only lose k amount of matches
    contests.sort(reverse=True) #we sort the array by descending order so that the max points are at the top
    for i in range(n):
        # Now we can simply loop through each pair
        if contests[i][1] == 0: #if the second item is 0, it's not important and we can lose the match for free luck
            luck += contests[i][0]
        elif contests[i][1] == 1 and k > 0: #if the second item is 1, it's important, and we can only afford to lose it for maximum point values
            luck += contests[i][0]
            k -= 1
        else:
            luck -= contests[i][0] #all that's left is important matches that we cannot lose, we subtract that amount of luck from our balance
    
    return luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
