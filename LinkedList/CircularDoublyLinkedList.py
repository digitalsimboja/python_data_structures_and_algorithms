from pickle import NONE


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next == self.tail.next:
                break

    def createCircularDLL(self, val):
        node = Node(val)
        self.head = node
        self.tail = node
        node.previous = node
        node.previous = node
        node.next = node
        return "The circular doubly linked list is created successfully"

    def insertCDLL(self, val, location):
        if self.head is None:
            return 'Node does not exist'
        else:
            newNode = Node(val)
            if location == 0:
                newNode.next = self.head
                newNode.previous = self.tail
                self.head.previous = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.previous = self.tail
                self.head.previous = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                newNode.next = currentNode.next
                newNode.previous = currentNode
                newNode.next.previous= newNode
                currentNode.next = newNode
            return 'The node is successfully inserted'

    def traverCDLL(self):
        if self.head is None:
            return 'The node does not exist'   
        node = self.head
        while node:
            print(node.value)
            if node == self.tail:
                break
            node = node.next   

    def reverseTraversalCLL(self):
        if self.head is None:
            return 'There is no list to traverse'
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.previous

    def searchNode(self, nodeValue):
        if self.head is None:
            return 'There is no list to search'
        else:
            node = self.head
            while node:
                if node.value == nodeValue:
                    return node.value
                if node == self.tail:
                   return 'Node does not exist'
                node = node.next
    
    def deleteNode(self, location):
        if self.head is None:
            return 'There is no node to delete'
        else:
            if location == 0:
                # There are two cases here
                # Case 1: One and only one node
                if self.head == self.tail:
                    self.head.next = None
                    self.head.previous = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.previous = self.tail
                    self.tail.next = self.head
            if location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.previous = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = self.head
                    self.head.previous = self.tail
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.previous = currentNode
            print('Node has been successfully deleted')
    
    def deleteEntireNode(self):
        if self.head is None:
            return 'The node does not exist'
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.previous = None
                tempNode = tempNode.next
            self.head = None
            self.head = None                    

        

circularDLL = CircularDLL()
print(circularDLL.createCircularDLL(5))

print(circularDLL.insertCDLL(0,0))
print(circularDLL.insertCDLL(1,1))
print(circularDLL.insertCDLL(2,2))

circularDLL.traverCDLL()
print([node.value for node in circularDLL])

circularDLL.reverseTraversalCLL()
print(circularDLL.searchNode(4))

circularDLL.deleteNode(0)
circularDLL.deleteNode(1)
circularDLL.deleteNode(2)
print([node.value for node in circularDLL])