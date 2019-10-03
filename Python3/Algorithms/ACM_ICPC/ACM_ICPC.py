#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations #we could try iterating and manually making combinations of each string, but itertools is faster and easier

# Complete the acmTeam function below.
def acmTeam(topic):
    combos = list(combinations(topic,2)) #this makes 
    
    knowledge = [] #we will be making an array for total knowledge for every two team combo
    
    for x in combos:
        knowledge.append(bin(int('0b' + x[0], 2) | int('0b' + x[1], 2)).count('1')) #this particular string appends the total knowledge number to knowledge
        #what bin() does is combine each of two combos, and counts the total number of 1s
    maximum = max(knowledge)
    ans = []
    ans.append(maximum)
    ans.append(knowledge.count(maximum))

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
