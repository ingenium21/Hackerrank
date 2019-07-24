#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def _get_hourglass_sum(matrix,row,col):
    sum = 0
    sum += matrix[row-1][col-1] #element up and to the left
    sum += matrix[row-1][col] #element directly above center
    sum += matrix[row-1][col+1] #element up and to the right
    sum += matrix[row][col] #main center element
    sum += matrix[row+1][col-1] #element below and to the left
    sum += matrix[row+1][col] #element directly below center
    sum += matrix[row+1][col+1] #element below and to the right
    return sum


def hourglassSum(arr):
    #because -9 <= arr[i][j] <= 9, this means that a cell can only be
    #between or equal to -9 and 9, so the min hourglass sum is -63
    max_hourglass_sum = -63

    #creating a double for loop that skips the first and last row since they can't create hourglasses
    for i in range(1,5):
        for j in range (1,5):
            current_hourglass_sum = _get_hourglass_sum(arr,i,j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum

    return max_hourglass_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
