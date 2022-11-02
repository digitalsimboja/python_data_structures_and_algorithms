from unittest import result
import Tree.base as base

# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds two numbers and returns the sum as a linked list

def sumList(l1, l2):
    node1 = l1.head
    node2 = l2.head
    carry = 0
    linkedList = base.LinkedList()

    while node1 or node2:
        result = carry
        if node1:
            result += node1.value
            node1 = node1.next
        if node2:
            result += node2.value
            node2 = node2.next
        linkedList.add(int(result % 10))
        carry = result / 10
    return linkedList

listA = base.LinkedList()
listA.add(7)
listA.add(1)
listA.add(6)

listB = base.LinkedList()
listB.add(5)
listB.add(9)
listB.add(2)

print(listA)
print(listB)

print(sumList(listA, listB))