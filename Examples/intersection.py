import Tree.base as base

# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
# Note that the intersection is defined based on reference, not value. That is, if the kth node of
# the first linked list is the exact same node (by reference) as the jth node of the second linked list,
# then they are intersecting

def intersection(lA, lB):
    if lA.tail is not lB.tail:
        return False
    
    lenA = len(lA)
    lenB = len(lB)

    shorter = lA if lenA < lenB else lB
    longer = lB if lenA < lenB else lA
       
    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode


def addSameNode(lA, lB, value):
    node = base.Node(value)
    lA.tail.next = node
    lA.tail = node
    lB.tail.next = node
    lB.tail = node


customA = base.LinkedList()
customA.add(3)
customA.add(7)
customA.add(4)

customB = base.LinkedList()
customB.add(2)
customB.add(1)
customB.add(8)
customB.add(6)

addSameNode(customA, customB, 12)
addSameNode(customA, customB, 9)
addSameNode(customA, customB, 5)

print(customA)
print(customB)

print(intersection(customA, customB))