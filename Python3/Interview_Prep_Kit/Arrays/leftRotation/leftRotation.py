#!/bin/python3

import math
import os
import random
import re
import sys

def rotLeft(a, d): #this is so surprisingly stupid easy it felt like a trick question
    for i in range(d): #start loop and end at the d'th value
        f = a[0] #assign the first element of the array to f
        a.remove(f) #pop out f
        a.append(f) #push in f
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
