#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    lhite = {}
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    tall = 1
    ans = 0
    #created a dict so i can reference each leter height
    #then used this for loop below to assign each letter their corresponding height
    for i in range(len(h)):
        lhite[alph[i]] = h[i]

    #used this for loop to find the tallest letter
    for i in range(0,len(word)):
        if tall < lhite[word[i]]:
            tall = lhite[word[i]]
    
    #then simply multiplied the tallest letter by the length of the word
    ans = tall * len(word)
    
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

