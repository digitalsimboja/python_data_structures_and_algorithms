class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None
    

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, val):
        node = Node(val)
        node.next = None
        node.previous = None
        self.head = node
        self.tail = node

    def insertNode(self, val, location):
        # check if head exists
        if self.head is None:
            return 'List does not exist'
        else:
            newNode = Node(val)
            # check if location is first
            if location == 0:
                # link the newNode previous to None
                newNode.previous = None
                newNode.next = self.head
                # link the head next reference to the new node
                self.head.previous = newNode
                # link the newnode next to head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.previous = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.previous = tempNode
                tempNode.next = newNode
                newNode.next.previous = newNode
                tempNode.next = newNode

    def traverseDLL(self):
        if self.head is None:
            return 'List does not exist'
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def reverseTraversalDLL(self):
        if self.head is None:
            print('List does not exist')
        else:
            # assign the tempnode to the tail node
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.previous
    
    def searchNode(self, value):
        if self.head is None:
            return 'Node does not exist'
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return ('The node exists and it is:', tempNode.value)
                tempNode = tempNode.next
            return ('The node does not exist in this list ', value)
    
    def deleteNode(self, location):
        if self.head is None:
            print('List does not exist')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.previous = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                # tempNode now contains the current node before the node to be deleted
                currentNode.next = currentNode.next.next
                currentNode.next.previous = currentNode
            print('The node has been successfully deleted')
                
                


                    
                    


                    



doubleLL = DoubleLinkedList()
doubleLL.createDLL(5)
doubleLL.insertNode(0,0)
doubleLL.insertNode(1,1)
doubleLL.insertNode(2,1)
doubleLL.insertNode(3,1)
doubleLL.insertNode(4,1)

doubleLL.traverseDLL()

print([node.value for node in doubleLL])

doubleLL.reverseTraversalDLL()

print(doubleLL.searchNode(3))
print(doubleLL.searchNode(6))

doubleLL.deleteNode(-1)

print([node.value for node in doubleLL])