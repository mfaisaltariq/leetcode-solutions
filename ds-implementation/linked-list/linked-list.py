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

    def remove(self, data):
        if not self.head:
            raise Exception("Error: Linked List is empty")
            
        current_node = self.head

        while current_node.next:
            if current_node.next.value == data:
                temp = current_node.next
                current_node.next = temp.next
                return
            current_node = current_node.next

    def reverse(self):
        if self.head is None:
            raise Exception("Error: Linked List is empty")
        if self.head.next is None:
            raise Exception("Error: Linked List contains only 1 element")

        current_node = self.head
        previous = None
        while current_node:
            nxt = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = nxt
        self.head = previous

    def __str__(self):
        arr = []
        current_node = self.head
        while current_node:
            arr.append(current_node.value)
            current_node = current_node.next
        return str(arr)

LL = LinkedList()
print(LL)
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.insert(6)
LL.insert('abc')
print(LL)
LL.remove(5)
LL.reverse()
print(LL)
        