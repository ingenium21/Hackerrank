l=[] #create array that will append data to

def intheorder(root):
    #do an inorder traversal, since it goes from left to right, if it's a BST, it will organize them from smallest to largest
    if(root):
        intheorder(root.left)
        global l
        l.append(root.data)
        intheorder(root.right)
        
def check_binary_search_tree_(root):
    intheorder(root) #do an inorder traveral
    for i in range(1,len(l)): #if the number to the left of the number being considered is larger, then it is not a BST.
        if(l[i]<=l[i-1]):
            return False
    return True
