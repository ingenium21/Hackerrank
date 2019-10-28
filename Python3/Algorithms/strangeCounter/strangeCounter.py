#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    rem = 3
    while t > rem:
        t = t-rem
        rem *= 2
    
    return (rem-t+1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

# assume a range number (rn) of the counter where it starts counting back

# for t =1 rn = 0 ...
# for t= 4 rn = 1 ...
# for t= 10 rn = 2

# if we are able to calculate this rn we know in which range t is in and the rest is just work out differences. let us define t start limits (sl) first (1, 4, 10, 22, 46,..): if you do the following, you see that the row is directly dependent of powers of 2: subtract 1 from the row:

# 1, 4, 10, 22, 46 -> 0, 3, 9, 21, 45

# divide by 3 (the whole counter ranges are divisible by 3)

# 0, 1, 3, 7, 15, ..

# can you see already? it is just 1 behind the row of powers of 2:

# 1, 2, 4, 8, 16

# now let us pack this knowledge into formula: (** = ^)

# sl = 3 * 2 ^ rn - 2

# f.e. (see above) rn = 2 -> sl (a special t) should be 10 and ...

# 3 * 2 ^ 2 - 2 = 10 .... great!

# now, to get the "range" first, we need to "reverse" (i am sorry - no native english speaker - deutsch: "Umkehrfunktion" the power function, which is log with base 2:

# sl + 2 = 3 * 2 ^ rn =>
# 2 ^ rn = (sl + 2) / 3 =>
# rn = log2 ((sl + 2) / 3)

# .... and make this an integer:

# rn = int (log2 ((sl + 2) / 3))

# Huh! To make it might be not soooo easy, but trying to explain it even more. Hope this helps figuring out to finish.