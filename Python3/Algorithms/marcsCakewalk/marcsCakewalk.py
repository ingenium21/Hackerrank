#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    miles = 0
    calorie.sort(reverse=True) #sort in decending so that Marc eats the most calorific cupcake first.
    for i in range(len(calorie)):
        miles += (2**i * calorie[i])

    return miles
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
