#!/bin/python3
import os
import sys

sys.setrecursionlimit(2000)
class Node:
    def __init__(self, left = -1, right = -1, value = -1, depth = 1):
        self.value = value
        self.left = left
        self.right = right
        self.depth = depth
    
    def swap(self, depth):
        # i am swapping if depth is multiple of given argument
        if self.value != -1 and self.depth % depth == 0:
            self.right, self.left = self.left, self.right
    
    def __str__(self):
        return f"Node:{ self.value} left child {self.left} right child {self.right} depth {self.depth}"


traversal = []
def inoder(node):
    if node.left != -1:
        inoder(node.left)
    global traversal
    traversal.append(node.value)
    if node.right != -1:
        inoder(node.right)
    

def build_tree(indexes):
    from collections import deque
    root = Node(value = 1, left = indexes[1][0], right = indexes[1][1], depth = 1)
    mq = deque()
    mq.append(root)
    while len(mq) != 0:
        node = mq.popleft()
        if node.left != -1:
            lnode = Node(value = node.left, depth = node.depth + 1, 
                        left = indexes[node.left][0], right = indexes[node.left][1])
            node.left = lnode
            mq.append(lnode)

            
        if node.right != -1:
            rnode = Node(value = node.right, depth = node.depth + 1, 
                        left = indexes[node.right][0], right = indexes[node.right][1])
            node.right = rnode
            mq.append(rnode)


    return root

def swap_node(node, depth):
    '''
    it check whether the node has value int -1 
    if it is end of tree we do not have to process it
    '''
    if isinstance(node, Node):
        node.swap(depth)
        swap_node(node.left, depth)
        swap_node(node.right, depth)


def swapNodes(indexes, queries):
    indexes.insert(0, [])
    root_node = build_tree(indexes)
    ret = []
    global traversal
    for ele in queries:
        traversal = []
        swap_node(root_node, ele)
        inoder(root_node)
        ret.append(traversal)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    indexes = []
    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)
    result = swapNodes(indexes, queries)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()
