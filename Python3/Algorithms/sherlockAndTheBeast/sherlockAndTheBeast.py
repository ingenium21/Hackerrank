#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    if n % 3 == 0: #if the number is divisible by 3 right out the bat, the largest number is N number of Fives
        print(n*'5')
    else:
        numFives = n  # we start with an N number of fives
        while (numFives % 3 != 0): #while the number is not divisible by three we subtract 5 from it bc we need at least 5 threes at the end
            numFives -= 5
        if numFives < 0: #if numFives reaches -1 then we know that the number can't be decent
            print(-1)
        else:
            print(numFives*'5'+(n-numFives)*'3')

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
