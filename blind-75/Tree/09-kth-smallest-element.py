'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

def kthSmallest( root: Optional[TreeNode], k: int) -> int:
    counter = 0
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        counter += 1
        if counter == k:
            return curr.val

        curr = curr.right






tree = TreeNode(3, TreeNode(2), TreeNode(20))
right = tree.right
right.left = TreeNode(15)
right.right = TreeNode(27)
'''
         3
        / \
       2   20
           / \
          15  27  

'''
print(kthSmallest(tree, 3))  