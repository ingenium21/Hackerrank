class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #if the root is empty, add the new node
        if self.root == None:
            self.root = Node(val)
        
        #assign self.root to variable 'root'
        root = self.root
        while root is not None:
            if val > root.info:
                if root.right:
                    root = root.right
                    #if val is greater than the root, we check if root.right exists
                    #if it does, then there's no need to check root.left and we make
                    #root.right the new root, since root is not empty, it will continue
                    #to run the loop until it does
                else:
                    root.right = Node(val)
                    break
                    #if it's empty, then we add the node and break
            elif val < root.info:
                if root.left:
                    root = root.left
                    #if val is less than the root, we check if root.left exists
                    #if it doesn't, we add  a new node and break just like above
                else:
                    root.left = Node(val)
                    break
            else:
                break


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
