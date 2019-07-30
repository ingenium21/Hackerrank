# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. 
# If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days, they send the client a notification about potential fraud. 
# The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
# Given the number of trailing days d and a client's total daily expenditures for a period of n days, find and print the number of times the client will receive a notification over all n days.
#!/bin/python3

import math
import os
import random
import re
import sys

def find_median(counts, mids):
        res = []
        for mid in mids:
                gone = 0
                for i, v in enumerate(counts):
                        gone += v #assign gone the numbers in counts
                        if gone >= mid: #if gone >= mid
                                res.append(i)
                                break
        return sum(res) / len(res)

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
        alerts = 0
        counts = [0]*201

        if d % 2 == 1:
                mids = [d // 2 + 1]
        else:
                mids = [d // 2, d // 2 + 1]
        
        for i in expenditure[:d]:
                counts[i] += 1

        for i , e in enumerate(expenditure[d:]):
                median = find_median(counts, mids)

                if e >= 2*median:
                        alerts += 1

                old = expenditure[i]
                counts[old] -= 1
                counts[e] += 1
        return alerts
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
