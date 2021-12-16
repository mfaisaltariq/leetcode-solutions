'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode(0)
    temp_tail = result
    carry, l1_val, l2_val = 0 , 0 , 0
    print('here')
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        print('here2')

        sum = l1_val+l2_val+carry
        if sum >= 10:
            carry = 1
            sum = sum - 10
        else:
            carry = 0
        print(sum, carry, 'details')
        temp_tail.next = ListNode(sum)
        temp_tail = temp_tail.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result.next

def printAll(head):
    while (head):
        print(head.val)
        head = head.next
    
node3 = ListNode(9)
node2 = ListNode(4,node3)
node1 = ListNode(2,node2)

node6 = ListNode(5)
node5 = ListNode(6,node6)
node4 = ListNode(4,node5)

# 249 + 465 = 6051

printAll(addTwoNumbers(node1,node4))

#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 9999999
# 9999
# 89990001






