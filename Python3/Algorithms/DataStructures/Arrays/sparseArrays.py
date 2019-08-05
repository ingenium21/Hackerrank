# Problem

# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.
# For Example, given input strings = ['ab','ab','abc'] and queries = ['ab','abc','bc'], we find 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'.
# for reach query, we add an element to our return array, results = [2,1,0]

# Function Description

# Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

# matchingStrings has the following parameters:

# strings - an array of strings to search
# queries - an array of query strings

# input format:

# The First line contains an intenger, n, the size of strings

# each of the next n lines contains a string strings[i]

# the next line contains q, the size of queries

# each of the next q lines contains a string queries[i]

# Contraints:
# 1 <= n <= 1000
# 1 <= q <= 1000
# 1 <= |strings[i],queries[i]| <= 20

# Output format:
# Return an integer array of the results of all queries in order.

# Sample Input:
# 4
# aba
# baba
# aba
# xzxb
# 3
# aba
# xzxb
# ab

# Sample Output:
# 2
# 1
# 0

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    result = []
    for j in range(queries_count):
        instance = 0
        for i in range(strings_count):
            if queries[j] == strings[i]:
                instance += 1
        result.append(instance)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
