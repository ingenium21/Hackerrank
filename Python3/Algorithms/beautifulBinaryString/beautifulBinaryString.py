#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    switches = 0
    for i in range(len(b) -2 ):
        if b[i] == '0' and b[i+1] == '1' and b[i+2] =='0':
            switches += 1
            b = b[:i+2] + "1" +b[i+3:]
    
    return switches
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
