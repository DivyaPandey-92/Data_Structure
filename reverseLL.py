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

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    # Write your code here
    #MY LOGIC
    # cur=llist
    
    if llist is None or llist.next is None:
        return llist
    
    # if llist.next is None:
    #     return llist
    cur=llist
       
    # while cur.next.next is not None:
    # #     cur.next=cur
    # #     cur=None
    #     cur=llist.next
    #     cur.next=llist
    #     llist.next=None
    #     llist=llist.next
    #     cur=llist.next
    # return llist
        
        
    
    COPIED
    if llist == None or llist.next == None:
        return llist
    p = reverse(llist.next)
    llist.next.next = llist
    llist.next = None
    return p
if __name__ == '__main__':