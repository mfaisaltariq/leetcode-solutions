'''
https://www.youtube.com/watch?v=XVuQxVej6y8&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=43
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    tmp_head = ListNode(0, head)

    left = tmp_head
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return tmp_head.next