'''
https://www.youtube.com/watch?v=hTM3phVI6YQ&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=58
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

''' BFS SOLUTION'''
def maxDepth( root: Optional[TreeNode]) -> int:
    level = 0
    q = deque([root])

    while q:

        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        level += 1

    return level

''' DFS SOLUTION Recursive'''
def maxDepthDFSRecursive( root: Optional[TreeNode]) -> int:
    if root:
        return _depth(root, 0)
    else:
        0

def _depth(current, depth):
    if current is None: return depth
    left_depth = _depth(current.left, depth+1)
    right_depth = _depth(current.right, depth+1)
    return max(left_depth, right_depth)

''' DFS SOLUTION Iterative'''
def maxDepthDFSIterative( root: Optional[TreeNode]) -> int:
    if root is None: return 0
    res = 0
    stack = [[root, 1]]
    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth+1])

    return res

tree = TreeNode(3, TreeNode(9), TreeNode(20))
right = tree.right
right.left = TreeNode(15)
right.right = TreeNode(7)

print(maxDepth(tree))
print(maxDepthDFSRecursive(tree))
print(maxDepthDFSIterative(tree))