#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    #list to return alice's ranks
    ranks = []
    #reverse sorting the scores so highest will come first and duplicate scores will always have the same value
    lboard = sorted(set(scores), reverse = True)
    
    lind = len(lboard) #index of the leaderboard

    #we loop through the scores in the alice array
    #we run a while loop until lind <= 0 and
    #if the alice element is > than the last element in lboard
    #we subtract lind until we reach an element that alice element
    #is less than
    for a in range(len(alice)):
        while(lind>0 and (alice[a] >= lboard[lind-1])):
            lind -= 1
        #then we append the lind number +1 to account for 0th indexing
        ranks.append(lind+1)

    return ranks
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
