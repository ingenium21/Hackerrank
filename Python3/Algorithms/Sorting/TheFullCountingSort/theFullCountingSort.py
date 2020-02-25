#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    numDict = {} #declaring a dict to store and organize the number as the key and string as the value
    maxNum = 0 #to help find the largest key
    output = [] #self explanatory
    for i in range(len(arr)):
        #run through the array, splitting the key into numI and value into linI
        numI = int(arr[i][0])
        linI = arr[i][1]

        if i < n/2: #if we're in teh first half of the array, we change linI to a dash (-)
            linI = "-"
        
        if numI > maxNum: #we use this to find the largest key
            maxNum = numI
        
        if numI in numDict: #this if, else statement is to add the key/value to numDict
            numDict[numI].append(linI)
        else:
            numDict[numI] = [linI]
        
    for i in range(maxNum + 1):
        #we go in order from 0 - maxNum + 1
        #if i is in numdict
        #we run through each array element corresponding to that number and append it to output
        if i in numDict:
            for j in numDict[i]:
                output.append(j)

    print(" ".join(output)) #we print the output in the format the question wants us to.

    
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
