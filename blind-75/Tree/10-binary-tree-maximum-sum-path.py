'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

def maxPathSum( root: Optional[TreeNode]) -> int:
    return sumDFS(root)[1]


def sumDFS(node: TreeNode) -> int:
    if not node:
        return 0, float('-inf')

    left_max, sum_left_subtree = sumDFS(node.left)
    right_max, sum_right_subtree = sumDFS(node.right)

    left_max = max(left_max, 0)
    right_max = max(right_max, 0)

    res = max(sum_left_subtree, sum_right_subtree, node.val + left_max + right_max)

    return [node.val + max(left_max, right_max), res]
    




tree = TreeNode(-10, TreeNode(9), TreeNode(20))
right = tree.right
right.left = TreeNode(15)
right.right = TreeNode(7)
left = tree.left
left.left = TreeNode(5)
'''
         -10
        / \
       9   20
           / \
          15  7  

'''
print(maxPathSum(tree))  