# Create a class Node
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# Creat the SingleLinkedList class
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # create __iter__ function so the list can be iterated

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # create a method to insert a node into the SingleLinkedList
    def insertNode(self, value, location):
        # create the new node
        newNode = Node(value)
        # check if the node has a head at all
        if self.head is None:
            # This is the first and only Node
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                # insert the new node at the head
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                # Let current node be the head
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                # Now we have the current Node, we need to insert the new Node after this current node
                # Take a reference to the next node after this current node
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traverseSL(self):
        # check if list exists
        if self.head is None:
            print("List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchNode(self, value):
        # check if list exists
        if self.head is None:
            return "List does not exist"
        else:
            # get the current head node
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
            return "The value does not exist in the list"

    def deleteNode(self, location):
        if self.head is None:
            print("List does not exist")
        else:
            if location == 0:
                # check if the head and the tail are pointing to same node
                # This is a situation where we have only one node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                # We have more than one node, check if location is first
            elif location == 1:
                # check if this is the only and last node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    # The current node next value is the tail, so set it to None and set the tail to the current value
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                # We are deleting inside the list
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                # set the current node next to the nextNode.next
                tempNode.next = nextNode.next

    def deleteEntireSLL(self):
        if self.head is None:
            print("The Single Linked list does not exist")
        else:
            self.head = None
            self.tail = None




# TEST
singleList = SingleLinkedList()
singleList.insertNode(1, 1)
singleList.insertNode(2, 1)
singleList.insertNode(3, 1)
singleList.insertNode(4, 1)
singleList.insertNode(0, 0)
singleList.insertNode(0, 3)

# Printing the newly created single linked list
print("Newly created single linked lists")
print([node.value for node in singleList])

# Printing the deleted node at location 3
print('Deletes the node at location 3')
singleList.deleteNode(3)
print([node.value for node in singleList])

# Printing the deleted entire node
print('Deletes the entire node')
singleList.deleteEntireSLL()
print([node.value for node in singleList])
