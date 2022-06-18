from xml.dom import InvalidAccessErr


class Node(object):
    def __init__(self,val):
        self.value = val
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)

    def __str__(self):
        arr = []
        current_node = self.head
        while current_node:
            arr.append(current_node.value)
            current_node = current_node.next
        return str(arr)

LL = LinkedList()
print(LL)
LL.insert(4)
LL.insert(5)
LL.insert('abc')
print(LL)

        