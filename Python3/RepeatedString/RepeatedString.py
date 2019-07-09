def repeatedString(s, n):
    #length of the string
    len_str = len(s)

    #number of times string repeats
    num_str = n // len(s)

    #We get num_str so we know how many times the strsing repeats.  For example
    #if s = 'abc' and n = 11, then we know the considered string will "abcabcabcab"
    # n // len_str = 11 // 3 = 3.   So the string repeats three times ("abcabcabc")
    # so for the remaining 2 characters, we need to determine the remainder.abs
    rem = n % len_str

    #counter to count the 'a's' in the given string
    count1 = 0

    #counter to count the 'a's' in the remaining string
    #will be used to calculate the total number of 'a's' in the string
    count2 = 0

    for i in range(len_str):
        #calculate the number occurrences of a in a given string
        if s[i] == 'a':
            count1 += 1
        #calculate the number of occurrences of 'a' in the remainder, if it exists
        if s[i] == 'a' and i < rem:
            count2 += 1

    #calculating the total number of 'a's' in the string
    total = count1*num_str + count2 

    return total

print(repeatedString("aba",11))
