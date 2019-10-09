#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.

def timeInWords(h, m):
    hour = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve"
    }
    tens = {
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    tenthMinute = {
        2: "twenty",
        3: "thirty",
        4: "twenty",
        5: "ten"
    }

    firstMinute = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten"
    }
    
    if m == 0:
        return "%s o' clock" % hour[h]
    elif m == 1:
        return "one minute past %s" % hour[h]
    elif m == 15:
        return "quarter past %s" % hour[h]
    elif m == 30:
        return "half past %s" % hour[h]
    elif m == 45:
        h += 1
        return "quarter to %s" % hour[h]
    elif m == 59:
        h += 1
        return "one minute to %s" % hour[h]
    else:
        if m <= 10:
            return "%s minutes past %s" % (firstMinute[m],hour[h])
        if m <= 19:
            return "%s minutes past %s" % (tens[m], hour[h])
        elif m < 30 and m % 10 == 0:
            return "%s minutes past %s" % (tenthMinute[(m // 10)], hour[h])
        elif m < 30 and m % 10 != 0:
            return "%s %s minutes past %s" % (tenthMinute[(m // 10)], firstMinute[(m % 10)], hour[h])
        elif m < 40:
            h += 1
            return "%s %s minutes to %s" % (tenthMinute[(60 - m) // 10], firstMinute[(60 - m) % 10], hour[h])
        elif m <= 40 and m % 10 == 0:
            h += 1
            return "%s minutes to %s" % (tenthMinute[(m // 10)], hour[h])
        elif m <= 40 and m % 10 != 0:
            h += 1
            return "%s %s minutes to %s" % (tenthMinute[(m // 10)], firstMinute[(m % 10)], hour[h])
        elif m < 50:
            h += 1
            return "%s minutes to %s" % (tens[(60 - m)], hour[h])
        elif m >= 50 and m % 10 == 0:
            h += 1
            return "%s minutes to %s" % (tenthMinute[(m // 10)], hour[h])
        else:
            h += 1
            return "%s minutes to %s" % (firstMinute[60 - m], hour[h])


                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
