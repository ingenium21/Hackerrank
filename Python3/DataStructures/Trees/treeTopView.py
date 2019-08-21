class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def topView(root):
    cur = [(root, 0)]
    scores = {} #create a dict for scores

    while cur:
        #while cur is not empty
        for _ in range(len(cur)):
            node, score = cur.pop(0)
            #we pop out the first element into two seperate variables
            if not node:
                continue
            #ignore empty nodes
            if score not in scores:
                scores[score] = node.info
            #we are adding the score into the dictionary, since we only want the top view, the first node that has that score has to be shown.
            #any other nodes that have the same score are "under" the top
            #think an umbrella, top view only sees the top part of the umbrella
            cur.extend(
                [(node.left, score - 1),
                (node.right, score + 1)]
            )
    #sort the scores and print their values
    for _, value in sorted(list(scores.items())):
        print(value, end=" ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)