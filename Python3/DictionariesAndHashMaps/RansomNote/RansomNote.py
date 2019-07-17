#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    #O(N^2) solution: 
    #loop through every word in ransom
    #remove it from magazine if the word is found
    # for word in ransom:
        # if word in magazine:
            # magazine.remove(word)
        # else:
            # return print("No")
    # return print("Yes")

    #for a O(N) solution, we can use hash tables.
    #we want to create a hash table that counts all instances of characters
    #creating an empty hash table
    mag_hash = {}
    for letter in magazine:
        if letter in mag_hash: #if that letter is already in the hash table
            mag_hash[letter] += 1 #add one to it's instance
        else:
            mag_hash[letter] = 1 #otherwise just set it to one
    
    #now we want to cycle through every letter in note
    for letter in note:
        #if the letter in question is in hash table and it doesn't equal 0
        if letter in mag_hash and mag_hash[letter] > 0:
            mag_hash[letter] -= 1 #subtract 1 from the count of it
        else:
            return print("No") #if it does equal 0 then that means we're missing an instance of that letter or the letter isn't in mag_hash, either way it's a fail.
    return print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
