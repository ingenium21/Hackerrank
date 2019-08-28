#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        #if the grade is less than 38 there is no rounding up
        # question asks to round up if the value of the grade and the 
        # multiple of 5 is less than 3, round up
        # but you can make it easier if you just make sure that 
        # grade % 5 is > 2.
        # to round up you get the grade + (5 - (grade % 2))
        if grades[i] >= 38:
            if grades[i] % 5 > 2:
                grades[i] = grades[i] + (5 - grades[i] % 5)

    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
