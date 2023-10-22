class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        dummy = self.Node(None)
        self.head = dummy

    def push(self, data):
        node = self.head
        while node.next:
            node = node.next
        node.next = self.Node(data)

    def pop(self):
        node = self.head
        before = None
        while node.next:
            before = node
            node = node.next
        data = node.data
        before.next = None
        return data

    def size(self):
        c = 0
        node = self.head
        while node.next:
            node = node.next
            c += 1
        return c


linkedList = LinkedList()

linkedList.push(1)
linkedList.push(2)
linkedList.push(3)

linkedList.pop()

node = linkedList.head
while node.next:
    node = node.next
    print(node.data)
