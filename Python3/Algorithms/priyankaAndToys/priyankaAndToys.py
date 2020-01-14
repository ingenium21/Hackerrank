#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    count = 0 #number of containers needed
    maxweight = 0 #max weight allowed in your container
    w.sort() #sort the array, ascending, to help evaluate the number of containers easier.

    for i in w:
        if i > maxweight or maxweight == 0:
            count += 1
            maxweight = i+4
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
