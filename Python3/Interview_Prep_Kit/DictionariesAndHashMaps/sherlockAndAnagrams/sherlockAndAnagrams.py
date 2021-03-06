#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    anagram_dict = {}
    count = 0
    #we need to get all possible substrings
    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            current_sorted = str(sorted(s[j:j+i]))
            if (current_sorted not in anagram_dict):
                    anagram_dict[current_sorted] = 1
            else:
                count += anagram_dict[current_sorted]
                anagram_dict[current_sorted] += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
