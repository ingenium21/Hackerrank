# Function Description:
# Declare a Checker class that implements the comparator method as described. 
# It should sort first descending by score, then ascending by name. The code stub reads the input, creates a list of Player objects, uses your method to sort the data, and prints it out properly.

# Input Format:
# The first line contains an integer, n, the number of players. 
# Each of the next  lines contains a player's respective name and score , a string and an integer.

# Sample Input:
# 5
# amy 100
# david 100
# heraldo 50
# aakansha 75
# aleksa 150

# Sample Output
# aleksa 150
# amy 100
# david 100
# aakansha 75
# heraldo 50

#Notes:

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif a.name < b.name:
            return -1
        elif a.name > b.name:
            return 1
        return 0

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)