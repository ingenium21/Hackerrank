#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    #we know the last node is the one that is out of order:
    key = arr[-1]

    index = n-2

    while((key < arr[index]) and (index >=0)):
        #while the key is less than the index's element and the index isn't -1
        #we change the index to the right of it to that index element
        #we do this until we finally find an element that is less than the key
        arr[index+1] = arr[index]
        print(*arr) #we print the array with spaces bc that's what the problem asks for
        index -= 1

    #then when we finally reach the element that is less than the key
    #we change the 
    arr[index+1] = key
    print(*arr) 
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
