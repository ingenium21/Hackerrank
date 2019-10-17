#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, y, x, obstacles):
    l = x - 1 #find all possible cells to the left of the queen
    r = n - x #find all possible cells to the right of the queen
    u = n - y #find all possible cells above the queen
    d = y - 1 #find all possible cells below the queen
    lu = min(l,u) #find all possible cells diagonally left-above the queen
    ld = min(l,d) #find all possible cells diagonally left-below the queen
    ru = min(r,u) #find all possible cells diagonally right-above the queen
    rd = min(r,d) #find all possible cells diagonally right-below the queen
    
    if n == 1: #if the board is 1 space large, there are no moves
        return 0

    # if there are no obstacles, just add up all of my variables
    if k == 0: 
        total = l+r+u+d+lu+ld+ru+rd
        return total
    else:
        for i in obstacles:
            #if obstacle is left/down and in the path
            if (x > i[1] and y > i[0] and x-i[1] == y-i[0]):
                ld = min(ld, x - i[1] - 1)

            #if obstacle is right/up and in the path
            if (i[1] > x and i[0] > y and i[1] - x == i[0] - y):
                ru = min(ru, i[1] - x - 1)
            
            #if obstacle is right/down and in the path
            if (i[1] > x and y > i[0] and i[1] - x == y-i[0]):
                rd = min(rd, i[1] - x - 1)
            
            #if obstacle is left/up and in the path
            if (x > i[1] and i[0] > y and x-i[1] == i[0] - y):
                lu = min(lu, x - i[1] - 1)
            
            #if obstacle is below the queen
            if (x == i[1] and y > i[0]):
                d = min(d, y - i[0] - 1)
            
            #if obstacle is above the queen
            if (x == i[1] and y < i[0]):
                u = min(u, i[0] - y - 1)
            
            #if obstacle is to the left of the queen
            if (y == i[0] and x > i[1]):
                l = min(l, x - i[1] - 1)
            
            #if obstacle is to the right of the queen
            if (y == i[0] and x < i[1]):
                r = min(r, i[1] - x - 1)
    
    return l+r+u+d+lu+ld+ru+rd

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
