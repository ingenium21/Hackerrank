#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the freqQuery function below.
def freqQuery(queries):
    arr = dict() # val:count of said values    
    freq = dict() #number of counts in arr.  ie, if there are 2 5s and 2 6s in arr, then freq[2:2]
    out = []
    
    for (oper, val) in queries:
        if (oper == 1):
            #insertion
            if not(val in arr):
                arr[val] = 0 #if value isn't in arr dict, then add value to dict and give it a 0 bc we can't assign a 1 just yet
            
            if not(arr[val] in freq):
                freq[arr[val]] = 1 #if CURRENT cnt of arr[val] is not in freq, we add it and assign 1
            
            freq[arr[val]] -= 1 #then we subtract by 1, bc it's about to lose one count
            
            arr[val] += 1 #adding 1 to arr[val]
            
            if not(arr[val] in freq):
                freq[arr[val]] = 0  #if arr[val]'s NEW cnt isn't in freq, then we assign it 0
            freq[arr[val]] += 1 #we increase it by 1
        
        if (oper == 2) and (val in arr):
            #deletion
            freq[arr[val]] -= 1 #the CURRENT cnt is subtracted by 1
            arr[val] -= 1 #arr[val] is removed by 1
            freq[arr[val]] += 1 #the NEW cnt is added 1
            
            if arr[val] <= 0: #if arr[val] is less than or equal to 0 then we pop it out.
                arr.pop(val)
                
        if (oper == 3) and (val in freq):
            out.append(int(freq[val]>0)) #appends 1 if freq[val] is greater than 0, otherwise just 0
        elif(oper == 3):
            out.append(0)
    return out
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
