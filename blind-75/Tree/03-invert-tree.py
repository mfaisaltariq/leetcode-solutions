'''
https://www.youtube.com/watch?v=OnSn2XEQ4MY&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=60
https://leetcode.com/problems/invert-binary-tree/submissions/
'''
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTreeIterative( root: Optional[TreeNode]) -> TreeNode:
    if not root: 
        return None

    stack = [root]

    while stack:
        node = stack.pop()
        tmp = node.right
        node.right = node.left
        node.left = tmp
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root

def invertTreeRecusive( root: Optional[TreeNode]) -> TreeNode:
    if not root: 
        return None

    tmp = root.right
    root.right = root.left
    root.left = tmp
    invertTreeRecusive(root.left)
    invertTreeRecusive(root.right)

    return root




def printTree(root: Optional[TreeNode]) -> None:
    if root is None: 
        return None

    print(root.val)
    printTree(root.left)
    printTree(root.right)

tree = TreeNode(3, TreeNode(9), TreeNode(20))
right = tree.right
right.left = TreeNode(15)
right.right = TreeNode(7)
'''
         3
        / \
       9   20
           / \
          15  7  

         3
        / \
       20  9
       / \
      7   15  
'''
printTree(tree)
print('-------------------------')
# printTree(invertTreeIterative(tree))
print('-------------------------')
printTree(invertTreeRecusive(tree))