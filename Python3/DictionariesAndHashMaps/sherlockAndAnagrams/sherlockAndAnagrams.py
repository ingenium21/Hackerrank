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

#suppose s = abba
# start is 0 ends at 1
# current sorted string is ['a']
# start is 1 ends at 2
# current sorted string is ['b']
# start is 2 ends at 3
# current sorted string is ['b']
# start is 3 ends at 4
# current sorted string is ['a']
# count is 2 because we have 2 instances of a = 1, 2 instances of b = 2
# dictionary is {"['a']": 2, "['b']": 2}
# start is 0 ends at 2
# current sorted string is ['a', 'b']
# start is 1 ends at 3
# current sorted string is ['b', 'b']
# start is 2 ends at 4
# current sorted string is ['a', 'b']
# count is 3 because we have 2 instances of a = 1, 2 instances of b = 2, 2 instances of ab = 3
# dictionary is {"['a']": 2, "['b']": 2, "['a', 'b']": 2, "['b', 'b']": 1}
# start is 0 ends at 3
# current sorted string is ['a', 'b', 'b']
# start is 1 ends at 4
# current sorted string is ['a', 'b', 'b']
# count is 4 because we have 2 instances of a = 1, 2 instances of b = 2, 2 instances of ab = 3, two instanced of abb = 3
# dictionary is {"['a']": 2, "['b']": 2, "['a', 'b']": 2, "['b', 'b']": 1, "['a', 'b', 'b']": 2}
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
