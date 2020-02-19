#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    cost = 0
    c.sort(reverse=True) #sort the array in reverse
    purchases = [0] * k #create an array of purchases of length k, with zeroes, to keep track of who has purchased something

    for i in range(len(c)):
        cost += c[i]*(purchases[i%k]+1) #we have the (i%k)th person to buy the ith most expensive flower, and add that price to cost
        purchases[i%k] += 1 #then we add one to the (i%k)th purchase array so the next time they buy a flower, the florist adjusts the price

    return cost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()

# for an example of how this looks, lets say k = 3, n = 10, and c = [9, 7, 5, 3, 1, 9, 7, 5, 3, 1]
# output:
# getMinimumCost(k,c)
# old purchases: [0, 0, 0]
# cost +=  9 x ( 0 +1)
# cost =  9
# new purchases: [1, 0, 0]
# old purchases: [1, 0, 0]
# cost +=  9 x ( 0 +1)
# cost =  18
# new purchases: [1, 1, 0]
# old purchases: [1, 1, 0]
# cost +=  7 x ( 0 +1)
# cost =  25
# new purchases: [1, 1, 1]
# old purchases: [1, 1, 1]
# cost +=  7 x ( 1 +1)
# cost =  39
# new purchases: [2, 1, 1]
# old purchases: [2, 1, 1]
# cost +=  5 x ( 1 +1)
# cost =  49
# new purchases: [2, 2, 1]
# old purchases: [2, 2, 1]
# cost +=  5 x ( 1 +1)
# cost =  59
# new purchases: [2, 2, 2]
# old purchases: [2, 2, 2]
# cost +=  3 x ( 2 +1)
# cost =  68
# new purchases: [3, 2, 2]
# old purchases: [3, 2, 2]
# cost +=  3 x ( 2 +1)
# cost =  77
# new purchases: [3, 3, 2]
# old purchases: [3, 3, 2]
# cost +=  1 x ( 2 +1)
# cost =  80
# new purchases: [3, 3, 3]
# old purchases: [3, 3, 3]
# cost +=  1 x ( 3 +1)
# cost =  84
# new purchases: [4, 3, 3]
# 84