import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

def huffman_hidden():#builds the tree and returns root
    q = Queue.PriorityQueue()

    
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key) ))
    
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0' )
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj ))
        
    root = q.get()
    root = root[2]#contains root object
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    result = []
    head = root
    #we shall loop through s and look for any 1s and 0s
    #if we see a 1, then we go right in the tree
    #if we see a 0, then we go left in the tree
    #since a letter will always be at the end of the tree
    #we will check if .left and .right are null, then we append the letter
    for i in s:
        if i == '1':
            head = head.right
        if i == '0':
            head = head.left

        if head.right==None and head.left==None:
            result.append(head.data)
            head = root

    print(''.join(result))


ip = input()