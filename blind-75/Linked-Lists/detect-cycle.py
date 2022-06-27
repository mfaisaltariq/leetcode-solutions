'''
https://www.youtube.com/watch?v=gBTe7lFR3vc&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=40
https://leetcode.com/problems/linked-list-cycle/
'''
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle( head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False