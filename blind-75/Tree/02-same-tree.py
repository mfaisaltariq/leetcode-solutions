'''
https://www.youtube.com/watch?v=vRbbcKXCxOw&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=59
https://leetcode.com/problems/same-tree/
'''
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree( p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q: 
        return True
    if (not p or not q) or (p.val != q.val):
        return False
    else:
        return (isSameTree(p.left, q.left) and isSameTree(p.right,q.right))

tree = TreeNode(3, TreeNode(9), TreeNode(20))
right = tree.right
right.left = TreeNode(15)
right.right = TreeNode(7)

tree1 = TreeNode(3, TreeNode(9), TreeNode(20))
right1 = tree1.right
right1.left = TreeNode(15)
right1.right = TreeNode(7)

print(isSameTree(tree, tree1))