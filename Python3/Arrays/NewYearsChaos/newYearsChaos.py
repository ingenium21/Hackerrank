#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    for pos, val in enumerate(q):
        # Because array will always be 1,2,3,4,5...end
        # and array pointer will always be arrayElement - 1 (ie. 5 -1 = 4, arr[4] => 5)
        # if 5 does not move left, then (5-1) - 4 = 0
        # if 5 moves left once, then (5-1) - 3 = 1
        # if 5 moves twice, then (5-1) - 2 = 2
        # if 5 moves three times, then (5-1) -1 = 3
        # therefore we can use that to calculate if the shift of a number required more than 2 shifts
        # say we have array 2,1,5,3,4
        # element 5 is in array position 2
        # (5-1) - 2 = 2
        # because 2 !> 2
        # then it is not too chaotic

        # No say we had array 2,5,1,3,4
        # element 5 is in array position 1
        # (5-1) -1 = 3
        # 3 > 2
        # therefore, too chaotic
        if (val-1) - pos > 2:
            return "Too chaotic"
        for j in range(max(0,val-2), pos):
            #for j in range((largest number between 0 and (value - 2)), position)
            #q = 2,1,5,3,4
            #if val = 2
            #for j in range(max(0,0), 0) = range(0,0) => returns nothing
            #moves = 0
            #if val = 1
            #for j in range(max(0,-1), 1) = range(0,1) => returns 0
                #q[0] = 2
                #is 2 > 1? yes
                #moves += 1
            #moves = 1
            if q[j] > val:
                moves+=1
    return moves

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
