#!/bin/python3

import math
import os
import random
import re
import sys

#Using f strings since its python3
#this was deceptively simple, but basically the question sort of gave you the answer
#if you're in a leap year it almost always lands on the 12th, if not, it lands on the 13th
#so rather than do any weird calculations trying to figure out what day it was, i just told it o return one of those days
#exception being 1918, when the transition happened, they skipped 14 days so it has to return 26th of september.
def dayOfProgrammer(year):
    if year >= 1919:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            date = f"12.09.{year}"
        else:
            date = f"13.09.{year}"
    elif year == 1918:
        date = f"26.09.{year}"
    else:
        if year % 4 == 0:
            date = f"12.09.{year}"
        else:
            date = f"13.09.{year}"
    return date


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
