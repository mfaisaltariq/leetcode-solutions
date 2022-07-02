'''
HARD PROBLEM 

https://www.youtube.com/watch?v=q5a5OiGbT6Q&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=42
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  if not lists or len(lists) == 0:
    return None

  while len(lists) > 1:
    merged_lists = []

    for i in range(0, len(lists), 2):
      l1 = lists[i]
      l2 = lists
      merged_lists.append(mergeLists(l1, l2))

    lists = merged_lists

  return lists[0]

def mergeLists(l1, l2) -> Optional[ListNode]:
  tmp = ListNode()
  current = tmp

  while l1 and l2:
    if l1.value < l2.value:
      current.next = l1
      l1 = l1.next
    else:
      current.next = l2
      l2 = l2.next

    if l1:
      current.next = l1
    if l2:
      current.next = l2

    return tmp.next