#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    ones = [0,'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve',
       'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen','twenty', 'twenty one', 'twenty two', 'twenty three' , 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']

    quarters = ["%s o' clock", "quarter past %s", "half past %s", "quarter to %s"]
    
    hour = ones[h] if (m < 31) else ones[h+1]

    if m % 15 == 0:
        return(quarters[m // 15] % hour)
    elif m < 30:
        return ("%s minute"%ones[m]+"s"*(m!=1)+ " past %s"%hour)
    else:
        return ("%s minute"%ones[60-m]+"s"*(m!=59)+ " to %s"%hour)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
