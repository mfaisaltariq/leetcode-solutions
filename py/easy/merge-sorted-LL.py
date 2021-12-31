""" 
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    merged_list = ListNode(0)
    temp_head = merged_list

    while list1 or list2:
        if list1 and list2:
            if list1.val < list2.val:
                merged_list.next = ListNode(list1.val)
                list1 = list1.next
                merged_list = merged_list.next
            else:
                merged_list.next = ListNode(list2.val)
                list2 = list2.next
                merged_list = merged_list.next
        else:
            if list1:
                merged_list.next = ListNode(list1.val)
                list1 = list1.next
                merged_list = merged_list.next
            else:
                merged_list.next = ListNode(list2.val)
                list2 = list2.next
                merged_list = merged_list.next

    return temp_head.next

def printAll(head):
    while (head):
        print(head.val)
        head = head.next


node3 = ListNode(3)
node2 = ListNode(2,node3)
node1 = ListNode(1,node2)

node6 = ListNode(6)
node5 = ListNode(4,node6)
node4 = ListNode(2,node5)

printAll(mergeTwoLists(node1, node4))