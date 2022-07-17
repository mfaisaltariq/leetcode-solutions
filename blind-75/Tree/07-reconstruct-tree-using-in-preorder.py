'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root

def printTree(root: Optional[TreeNode]) -> None:
    if root is None: 
        return None

    print(root.val)
    printTree(root.left)
    printTree(root.right)

printTree(buildTree([3,9,20,15,7],[9,3,15,20,7]))