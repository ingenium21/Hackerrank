#!/bin/python3

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    a = llist1
    b = llist2

    while (a != None and b != None):
        if (a.data != b.data):
            return False #if at any point a and b aren't equal, return a false which returns a 0
        a = a.next
        b = b.next
    
    #if linked lists are identical, then a and b will be both null at this point so that will return a true
    return (a == None and b==None)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
