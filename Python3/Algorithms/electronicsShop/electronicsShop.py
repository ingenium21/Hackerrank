#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #sort the keyboards in reverse order
    keyboards.sort(reverse=True)
    drives.sort()
    cur = -1 #current
    #we reversed the keyboards so that we can find the largest number possible as quickly as possible
    #using these two loops we're able to add the two arrays and break whenever we get too big.
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i]+drives[j] > b:
                break
            elif keyboards[i]+drives[j] > cur:
                cur = keyboards[i]+drives[j]
    return cur


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
