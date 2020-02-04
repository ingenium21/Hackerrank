#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ","")
    sRows = math.floor(len(s)**0.5) #square root of length s's floor
    sCols = math.ceil(len(s)**0.5) #square root of length s's ceiling
    
    encodedPhrase = ""
    for i in range(sCols):
        #we know that we have sCols number of columns.  
        #so if we were looking for the first letter of each column, we simply would look for 0, 0+8, 0+8+8...until we reached len(s)
        #we wrap that in a loop, add it to a string Object(encodedPhrase) and separate them with spaces.
        sIndex = i
        while sIndex < len(s):
            encodedPhrase = encodedPhrase + s[sIndex]
            sIndex += sCols
        encodedPhrase = encodedPhrase + " "
    
    return encodedPhrase

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
