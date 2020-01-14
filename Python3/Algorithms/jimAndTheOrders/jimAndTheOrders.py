#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    t = {} #create a dictionary of all the times
    for i in range(len(orders)):
        #we know the first number is the order number and the second is the prep time so we add em up and put them in t 
        #with their corresponding customer number, we add 1 to i in t[i+1] since the customer no. starts at 1
        t[i+1] = orders[i][0] + orders[i][1]
    sorted_t = sorted(t, key=t.get) #creates an array of the sorted t keys sorted by another key, t.get().  The "key" in the code specifically is asking how to sort the keys in the dict

    return sorted_t
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
