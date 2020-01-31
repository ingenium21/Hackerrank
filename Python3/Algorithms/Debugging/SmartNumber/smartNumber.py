import math

def is_smart_number(num):
    #this is more of a math problem.  Think hard back to 5th grade math days and remember that the only numbers
    #who have an odd number of factors are perfect squares.  1, number, and int(sqrt(num))
    val = int(math.sqrt(num))
    if val**2 == num:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")



