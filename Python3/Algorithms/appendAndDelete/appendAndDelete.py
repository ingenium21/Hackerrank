#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    commonchar = 0
    #counting what characters they have in common from start to finish
    for i in range(min(len(s),len(t))):
        if (s[i] == t[i]):
            commonchar += 1
        else:
            break
    
    #case A: is K bigger than the difference in length of the two strings
    # example: s = "hackerrank", t = "h", k = 5
    # you need a much bigger k to make those changes so we return No
    if (len(s)+len(t) - (2* commonchar) > k):
        return "No"
    #Case B: if it passes Case A, then we need to make sure that we can exactly K moves, no more, no less
    # example
    # s = "hacker", t = "hacke", k = an even number
    #or s = "hacker", t = "hacker" k = an odd number
    # k has to be equally even/odd as the number of different digits
    elif (((len(s) + len(t) - (2*commonchar)) % 2) == k % 2):
        return "Yes"
    #Case C: you could get around this even/odd problem if you have a a big enough k
    #since you can completely delete away one string adn a delete action on an empty string
    #results in another empty strin
    #example: s = "h", t = "hac", k = 5
    elif ((len(s) + len(t)) - k < 0):
        return "Yes"
    #all other cases will fail the test
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
