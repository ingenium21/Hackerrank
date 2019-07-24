#Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

# Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
# First Element: firstElement, where  is the first element in the sorted array.
# Last Element: lastElement, where  is the last element in the sorted array.

# Sample Input:
# 3
# 1 2 3

# Sample Output:
# Array is sorted in 0 swaps.
# First Element: 1
# Last Element: 3

#Notes:
#fairly simple bubble sort challenge, the logic was in the top of the page.
#______________________________________________________________________________________________________________________________________________________

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    numSwaps = 0 #this will count the number of swaps
    for i in range(len(a)):
        for j in range(len(a) - 1 ):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                numSwaps += 1
    
    print("Array is sorted in", numSwaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n-1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
