import base

# Write code to partition a linked list around a value x, such that all nodes
# less than x comes before all nodes greater than or equal to x
def partition(linkedList, x):
    currNode = linkedList.head
    linkedList.tail = currNode
    
    while currNode:
        nextNode = currNode.next
        currNode.next = None
        if currNode.value <= x:
            currNode.next = linkedList.head
            linkedList.head = currNode
        else:
            linkedList.tail.next = currNode
            linkedList.tail = currNode
        currNode = nextNode
    if linkedList.tail.next is not None:
        linkedList.tail.next = None



# Test Example 1
customLL = base.LinkedList()

customLL.generate(10, 0, 99)
print(customLL)

partition(customLL, 30)
print(customLL)

