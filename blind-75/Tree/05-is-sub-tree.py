'''
https://www.youtube.com/watch?v=OnSn2XEQ4MY&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=60
https://leetcode.com/problems/invert-binary-tree/submissions/
'''
# Definition for a binary tree node.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot :
        return True
    if not root:
        return False
    
    if _isSubtree(root, subRoot):
        return True
    
    return (isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot))
    
    
    
def _isSubtree(root, subRoot) -> bool:
    if not root and not subRoot: 
        return True
    if (not root or not subRoot) or (root.val != subRoot.val):
        return False
    else:
        return (_isSubtree(root.left, subRoot.left) and _isSubtree(root.right,subRoot.right))
        
        
tree = TreeNode(3, TreeNode(9), TreeNode(20))
right = tree.right
right.left = TreeNode(15)
right.right = TreeNode(7)

subTree = TreeNode(20, TreeNode(15), TreeNode(7))
'''
         3
        / \
       9   20
           / \
          15  7  

       20
       / \
      15   7  
'''
print(isSubtree(tree, subTree))