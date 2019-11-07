#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    #ugly solution
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # newString = ""

    # for i in s:
    #     if i.isupper() == True:
    #         if i.lower() in alphabet:
    #             ind = alphabet.index(i.lower())
    #             if ind+k < len(alphabet):
    #                 newString += (alphabet[ind+k]).upper()
    #             else:
    #                 newString += (alphabet[(ind+k) % 26]).upper()
    #         else:
    #             newString += i
    #     else:
    #         if i in alphabet:
    #             ind = alphabet.index(i)
    #             if ind+k <= len(alphabet):
    #                 newString += alphabet[ind+k]
    #             else:
    #                 newString += alphabet[(ind+k) % 26]
    #         else:
    #             newString += i

    # return newString

    #cleaner solution
    alphabet = "abcdefghijklmnopqrstuvwxyz" #declare alphabet string to compare each char in the string
    newS = "" #this will be our new string
    for i in s: #loop through s, if the character is uppercase or lowercase it will return the index of that letter+k spaces, you mod it by the length of alphabet so it returns the new letter
        if i.islower():
            newS += alphabet[(alphabet.index(i)+k) % len(alphabet)]
        elif i.isupper():
            newS += (alphabet[(alphabet.index(i.lower())+k) % len(alphabet)]).upper()
        else:
            newS += i
    
    return newS

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
