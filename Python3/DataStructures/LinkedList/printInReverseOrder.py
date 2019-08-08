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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

# Complete the reversePrint function below.

# Let's take an example Linked List: 1->2->3 Walking through the code, the function ReversePrint is given a link to the head of our Linked List, which is 1. 
# We see that head is not equal to null so we move to the second line of the code, which is the first recursive call to head.next, which is 2. 
# Again we see that this new "head" is not equal to null, so we do a second recursive call, this time passing the node that contains 3. 
# We see that this new "head" is not equal to null, so we do a third recursive call on head.next, which is null in this case. 
# So we return, since we hit our base case. We are now back in our second recursive call, and we move to the line of code that comes after the recursive call, which is the print statement. 
# We print 3. Since this recursive call is now complete, we move back to the first recursive call, and print 2. 
# Finally, we are back in our initial function call, and we print 1. Therefore, successfully printing our Linked List in reverse order.

def reversePrint(head):
    if head is None:
        return
    else: 
        reversePrint(head.next) 
        print(head.data)

if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)
