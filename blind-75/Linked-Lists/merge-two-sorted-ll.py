'''
https://leetcode.com/problems/merge-two-sorted-lists/submissions/
https://www.youtube.com/watch?v=XIdigk956u0&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=41
'''

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    tmp_head = ListNode()
    current = tmp_head

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return tmp_head.next