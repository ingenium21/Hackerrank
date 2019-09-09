#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#code is ugly but it works so wgaf
def pageCount(n, p):
    rightPage = 1 #first page will always be the right page
    leftPage = 0
    startTurns = 0
    endTurns = 0
    if p == n or p == 1: #no point in doing anything if p is the first or last page
        return 0

    elif n % 2 == 0: #if n is even we know the last page will be a left page, add 2 to rightPage for every turn until it's no longer less than p
        while(rightPage < p):
            rightPage += 2
            leftPage = rightPage - 1
            startTurns += 1

        leftPage = n #then we do it again but this time from the last page, subtract 2 for every turn until it's no longer gt p
        while(leftPage > p):
            leftPage -= 2
            rightPage = leftPage + 1
            endTurns += 1
    
    else: #all that's left is to figure out odd numbered books
        while(rightPage < p): #same thing here
            rightPage += 2
            leftPage = rightPage - 1
            startTurns += 1

        rightPage = n 
        leftPage = rightPage - 1
        if leftPage == p: #we add this conditional in case p is the second to last page on an odd numbered book
            return 0
        else:
            while(leftPage > p):
                rightPage -= 2
                leftPage = rightPage - 1
                endTurns += 1
    
    if startTurns < endTurns: #we add this conditional to determine the lowest number of turns and return that
        return startTurns
    else:
        return endTurns


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
