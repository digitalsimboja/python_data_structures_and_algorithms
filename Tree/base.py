class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
class Quueue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        else: 
            return False
    
    def enqueue(self, nodeValue):
        newNode = Node(nodeValue)
        if self.linkedList.head is None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def dequeue(self):
        if self.isEmpty():
            return 'No more queues to dequee'
        else:
            currNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head =  None
                self.linkedList.tail = None
            else:
                self.linkedList.head = currNode.next
            return currNode
