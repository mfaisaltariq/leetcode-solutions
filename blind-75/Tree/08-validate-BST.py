'''
https://leetcode.com/problems/validate-binary-search-tree/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
def isValidBST(root: Optional[TreeNode]) -> bool:
    
    return valid(root, float('-infinity'), float('infinity'))
    
    
def valid(node: TreeNode, low: float, high: float )-> bool:
    if not node:
        return True
    
    if node.val < low or node.val > high:
        return False
    
    return valid(node.left, low, node.val) and valid(node.right, node.val, high)
       
tree = TreeNode(3, TreeNode(2), TreeNode(5))
right = tree.right
right.left = TreeNode(4)
right.right = TreeNode(6)
'''
Valid BST
         3
        / \
       2   5
           / \
          4  6  
'''
print(isValidBST(tree))

tree1 = TreeNode(3, TreeNode(9), TreeNode(20))
right1 = tree1.right
right1.left = TreeNode(15)
right1.right = TreeNode(7)
'''
INVALID BST
         3
        / \
       9   20
           / \
          15  7  
'''
print(isValidBST(tree1))  