
stack = [0] #declare a stack
for i in range(int(input())): #the first input will be the number of queries it expects
    n = list(map(int, input().split()))
    if n[0] == 1: #if the first number is a 1, then you append the next number
        stack.append(max(n[1],stack[-1])) # you append it to the end so the last element always has the largest number
    elif n[0] == 2: #if the first number is a 2, you pop out the top element
        stack.pop()
    else: #print the stack if its a three or not 1/2
        print(stack[-1])