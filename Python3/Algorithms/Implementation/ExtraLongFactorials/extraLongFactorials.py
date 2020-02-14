#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    mult = 1
    for i in range(n,0,-1):
        mult *= i

    return mult

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
