#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
#pretty self explanatory
def bonAppetit(bill, k, b):
    actual = (sum(bill) - bill[k])/2
    if b == actual:
        print("Bon Appetit")
    else:
        print(int(b-actual))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
