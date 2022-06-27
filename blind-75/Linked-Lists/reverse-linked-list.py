'''
https://www.youtube.com/watch?v=G0_I-ZF0S38&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=40
https://leetcode.com/problems/reverse-linked-list/
'''
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    current = head
    previous = None

    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt

    return previous