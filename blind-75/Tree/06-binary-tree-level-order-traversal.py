'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List
'''
---------------- This is doesn't work for some edge cases ------------------------


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    if not root:
        return []
    else:
        res.append([root.val])
    stack = [[root]]
    
    while stack:
        nodes = stack.pop()
        
        for i, node in enumerate(nodes):
            if node.left and node.right:
                res.append([node.left.val, node.right.val])
                stack.append([node.left, node.right])
            elif node.left:
                res.append([node.left.val])
                stack.append([node.left])
            elif node.right:
                res.append([node.right.val])
                stack.append([node.right])
                
    return res
'''

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = deque([root])

    while q:
        level = []

        for i in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)

        if level:
            res.append(level)

    return res


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
print(levelOrder(tree))              
            
        