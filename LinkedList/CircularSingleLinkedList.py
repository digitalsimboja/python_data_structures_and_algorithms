from hashlib import new
import tarfile


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# Creat the SingleLinkedList class
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # create __iter__ function so the list can be iterated

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            
    
    def createCircleSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
    
    def insertCircularSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "New node successfully inserted"

    def traverseCircularSLL(self):
        if self.head is None:
            return 'Not does not exist'
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
    
    def searchNodeInCSL(self, value):
        if self.head is None:
            return 'List does not exist'
        else:
            node = self.head
            while node:
                if node.value == value:
                    return node.value
                node = node.next
                if node  == self.tail.next:
                    return 'Node is not found'
    
    def deleteNode(self, location):
        if self.head is None:
            print('Node does not exist')
        else:
            if location == 0:
                # If we have only one node
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                 # If we have only one node
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


    def deleteEntireCSL(self):
        self.head = None
        self.tail.next = None
        self.tail = None




circleSLL = CircularLinkedList()
circleSLL.createCircleSLL(0)
circleSLL.insertCircularSLL(1, 1)
circleSLL.insertCircularSLL(2, 1)
circleSLL.insertCircularSLL(3,1)
circleSLL.insertCircularSLL(0, 0)

print([node.value for node in circleSLL])

circleSLL.traverseCircularSLL()
print('Searching for a node in the circular linked list')
print(circleSLL.searchNodeInCSL(4))

circleSLL.deleteNode(3)
print([node.value for node in circleSLL])

