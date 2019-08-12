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

def find_length_linked_list(head): #created this function to find the length of the linked list
    cnt = 0
    p = head
    while (p is not None):
        cnt += 1
        p = p.next
    
    return cnt

# Complete the findMergeNode function below.

def findMergeNode(head1, head2):
    #calculate the length of the two LLs
    p = find_length_linked_list(head1) 
    q = find_length_linked_list(head2)

    #calculate the difference and get the absolute value
    d = p - q

    if (d < 0):
        d = d * -1
    
    #Find which one is the larger ll
    if p > q:
        larger = head1
        smaller = head2
    
    else:
        larger = head2
        smaller = head1

    cnt = 0
    #move d nodes in longer linked list
    while (cnt < d):
        larger = larger.next
        cnt += 1
    
    #then move by one step in both lls until p = q
    while (larger != smaller):
        larger = larger.next
        smaller = smaller.next
    
    return larger.data

# this is a better solution that is O(N) without the use of counters
def findMergeNodeFaster(head1, head2):
    p = head1
    q = head2

    #next node until p = q
    while(p != q):
        # if you reached the end of one list start at the beginning of the other one.
        # p
        if (p.next is None):
            p = head2
        else:
            p = p.next
        
        #q
        if (q.next is None):
            q = head1
        else:
            q = q.next
        
    return q.data


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

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
            
        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()