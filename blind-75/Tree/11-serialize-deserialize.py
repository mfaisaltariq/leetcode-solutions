'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize( root) -> str:
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    serialized = dfs(root, [])
    return ','.join(str(val) for val in serialized)

def dfs(root, serial_arr):
    if not root:
        serial_arr.append('none')
        return

    serial_arr.append(root.val)
    dfs(root.left, serial_arr)
    dfs(root.right, serial_arr)

    return serial_arr
    

def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    nodes = iter(data.split(','))
    return buildTree(nodes)

def buildTree(nodes):
    val = next(nodes)
    if val == 'none':
        return None

    node = TreeNode(str(val))
    node.left = buildTree(nodes)
    node.right = buildTree(nodes)

    return node

def printTree(root: TreeNode) -> None:
    if root is None: 
        return None

    print(root.val)
    printTree(root.left)
    printTree(root.right)

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
serialized = serialize(tree)
print(serialized)
printTree(deserialize(serialized))