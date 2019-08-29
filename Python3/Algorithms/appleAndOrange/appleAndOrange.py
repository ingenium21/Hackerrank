#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #s = first num in range of house
    #t = last num in range of house
    #a = position of apple tree
    #b = position of orange tree
    #apples = array of apple drop positions from tree, neg is left, pos is right
    #oranges = array of orange drop positions from tree, neg is left, pos is right
    houseApp = 0 #counter for apples
    houseOra = 0 #counter for oranges

    #we loop through the apples array and add it to the position of the apple tree
    #the result will give us a number.  If the number is between s and t
    #then the number falls on the house and we add 1 to the counter
    for i in range(len(apples)):
        if (apples[i] + a) >= s and (apples[i]+a) <= t:
            houseApp += 1

    #we loop through the oranges array and add it to the position of the orange tree
    #the result will give us a number.  If the number is between s and t
    #then the number falls on the house and we add 1 to the counter
    for i in range(len(oranges)):
        if (oranges[i] + b ) >= s and (oranges[i] + b) <= t:
            houseOra += 1
    print(houseApp)
    print(houseOra) 
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
