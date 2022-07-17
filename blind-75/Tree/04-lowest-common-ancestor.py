'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor( root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> TreeNode:
    curr = root

    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr

tree = TreeNode(3, TreeNode(9), TreeNode(20))
right = tree.right
right.left = TreeNode(15)
right.right = TreeNode(27)
'''
         3
        / \
       9   20
           / \
          15  27  
 
'''

print(lowestCommonAncestor(tree, right.left, right.right).val)