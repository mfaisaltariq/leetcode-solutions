class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val) -> None:
        if self.root is None:
            self.root = Node(val)
        else:
            self.__insert(val, self.root)

    def __insert(self, val, current):
        if val < current.val:
            if current.left is None:
                current.left = Node(val)
            else:
                self.__insert(val, current.left)

        elif val > current.val:
            if current.right is None:
                current.right = Node(val)
            else:
                self.__insert(val, current.right)

        else:
            print( "Value already exists")

    def find(self, val:int) -> bool:
        if self.root is not None:
            return self.__find(val, self.root)
        else:
            return False

    def __find(self, val:int, current:Node) -> bool:
        if current.val == val:
            return True
        elif val < current.val and current.left is not None:
            return self.__find(val, current.left)
        elif val > current.val and current.right is not None:
            return self.__find(val, current.right)
        
        return False

    def height(self) -> int:
        if self.root is not None:
            return self.__height(self.root, 0)
        else:
            return 0
    
    def __height(self, current:Node, curr_height:int) -> int:
        if current is None: return curr_height
        left_height = self.__height(current.left, curr_height+1)
        right_height = self.__height(current.right, curr_height+1)
        return max(left_height, right_height)
            

    def printInOrder(self) -> None:
        if self.root is not None:
            self.__printInOrder(self.root)

    def __printInOrder(self, current:Node) -> None:
        if current.left:
            self.__printInOrder(current.left)
        
        print(current.val)

        if current.right:
            self.__printInOrder(current.right)

    def printPreOrder(self) -> None:
        if self.root is not None:
            self.__printPreOrder(self.root)

    def __printPreOrder(self, current:Node) -> None:
        print(current.val)
        if current.left:
            self.__printPreOrder(current.left)
        if current.right:
            self.__printPreOrder(current.right)

    def printPostOrder(self) -> None:
        if self.root is not None:
            self.__printPostOrder(self.root)

    def __printPostOrder(self, current:Node) -> None:
        if current.left:
            self.__printPostOrder(current.left)
        if current.right:
            self.__printPostOrder(current.right)
        print(current.val)

def fill_tree(tree, num_elements = 100, max_val=1000):
    from random import randint
    for i in range(num_elements):
        val = randint(0, max_val)
        tree.insert(val)
    return tree

tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(12)
tree.insert(4)
tree.insert(8)
# tree.insert(15)
# tree.insert(11)
tree.printPreOrder()
print(tree.find(8))
print(tree.height())

