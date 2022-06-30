'''
https://leetcode.com/problems/reorder-list/
https://www.youtube.com/watch?v=S5bfdUTrKLM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=44
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
def reorderList( head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow, fast = head, head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    current = slow.next
    previous = slow.next = None
    
    while current:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
        
    first_half, second_half = head, previous
    printList(first_half)
    printList(second_half)
    
    while second_half:
        tmp1, tmp2 = first_half.next, second_half.next
        first_half.next = second_half
        second_half.next = tmp1
        first_half, second_half = tmp1, tmp2

    print('here')
    printList(head)

def printList(head):

    current = head
    while current:
        print(current.val)
        current = current.next

l4 = ListNode(4)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1,l2)
reorderList(l1)


