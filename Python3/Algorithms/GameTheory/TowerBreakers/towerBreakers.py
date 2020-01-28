#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the towerBreakers function below.
def towerBreakers(n, m):
    # If M == 1, then player 2 wins, because all of the towers begin at minimum height.

    # Otherwise, if the number of towers is even, then player 2 wins. This is because 
    # player 2 can play a "mirror strategy". For every move that player 1 makes, player 2
    # makes the same move on another tower. Evenutally, player 2 has made the last validmove.

    # If the number of towers is odd, then player 1 immediately removes the "odd" tower by reducing its height to 1. 
    # player 2 is then stuck being "mirrored" by player 1.

    return 2 if m==1 or n% 2 == 0 else 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
