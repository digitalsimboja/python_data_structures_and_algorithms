from operator import index
from os import link
import base

# Implement an algorithm to find all the elements nth to the last element of a singly linked list
def traverseKthToLast(linkedList, location):
    if linkedList.head is None:
        return
    else:
        kthLists = []
        if location == 0:
            currNode = linkedList.head
            while currNode:
                kthLists.append(currNode.value)
                currNode = currNode.next
        elif location == 1:
            kthLists.append(linkedList.tail.value)
        else:
            currNode = linkedList.head
            index = 0
            while index < location - 1:
                currNode = currNode.next
                index += 1
            nextNode = currNode.next
            while nextNode:
                kthLists.append(nextNode.value)
                nextNode = nextNode.next
            
    return kthLists

# Implement an algorithm to find the nth from the last element of a singly linked list
def findKthFromLast(linkedList, n):
    if linkedList.head is None:
        return
    else:
        pointer1 = linkedList.head
        pointer2 = pointer1
        space = 0
        while space < n - 1:
            pointer2 = pointer2.next
            space += 1
        while pointer2:
            if pointer2.next is None:
                return pointer1.value
            else:
                pointer1 = pointer1.next
                pointer2 = pointer2.next


# Test
customLL = base.LinkedList()

customLL.generate(10, 0, 99)

print(customLL)

# print(traverseKthToLast(customLL, 6))

print(findKthFromLast(customLL, 8))

