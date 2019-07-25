# # # # Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. 
# # # # There are a number of different toys lying in front of him, tagged with their prices.
# # # #  Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.
# # # Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?
# # #Input Format:
# # #   The First Line Contains two integers, n and k, the number of priced toys and the mount Mark has to spend
# # #   The next line contains n space-sperated integers prices[i]
# # #
# #Output Format:
# #     An integer that denotes the maximum number of toys Mark can buy for his sun

# # #Sample Input:
# #     7 50
# #     1 12 5 111 200 1000 10

# #Sample output:
# #     4
# #notes:
#     Will obv need to use bubble sort, but i also need to figure out a way to do the comparisons right then and There   
#     so that I can keep this at O(N).

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    moneyLeft = k
    count = 0
    prices.sort()
        
    while (k - prices[count] >= 0):
        k = k - prices[count]
        count += 1

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
