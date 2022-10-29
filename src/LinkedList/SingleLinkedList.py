# Create a class Node
class Node:
    def __init__(self, value = None):
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
                self.head.next = newNode
                newNode.next = self.head
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                # Let current node be the head 
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                # Now we have the current Node, we need to insert the new Node after this current node
                # Take a reference to the next node after this current node
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode





# TEST
singleList = SingleLinkedList()
singleList.insertNode(0,1)
print([node for node in singleList])