#!/bin/python3

import math
import os
import random
import re
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

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    #if llist is empty
    if head is None:
        return head
    
    #Store Head node
    temp = head

    if position == 0:
        head = temp.next
        temp = None
        return head
    
    # Find previous node of the node to be deleted 
    for _ in range(position -1 ):
        temp = temp.next
        if temp is None:
            break
    
    #is position is > number of Nodes
    if temp is None:
        return head
    if temp.next is None:
        return head
    
    #Node temp.next is the node to be deleted
    #store pointer to the next of node to be deleted
    next = temp.next.next

    # Unlink the node from linked list
    temp.next = None
    temp.next = next
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()
