#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    count = 0
    pageNum = 0
    #chapter = 0 You don't really need a variable for chapter, but I used it to help organize my process and debug
    for i in range(len(arr)): #loop through the array
        #chapter += 1
        pageNum += 1 #starting at page 1
        problem = 0 #we declare variables for each problem number and it's index, the index will be useful bc we don't exactly know how many problems are in each page (k)
        probIndex = 0
        for j in range(0,arr[i]): #second loop that counts from 0 to arr[i], we don't need to worry about starting at 1, but if you prefer that, make sure you also +1 the second range
            problem += 1 #adds one to the problem number
            probIndex += 1 #adds one tot he index
            if problem == pageNum:
                count += 1 #if the problem number is == to the page number, it's beautiful or whatever, increase the count
            if probIndex == k and problem != arr[i]: 
                #this is where it got a little tricky
                #once the problem index reached k, it was time to turn the page
                #however there was an instance when probIndex reached K AND it was the end of the problems, so it turned the page twice
                #so i added that second conditional
                pageNum += 1
                probIndex = 0

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
