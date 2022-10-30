
import base

# Example 1
# Write a code to remove duplicates from an unsorted linked list
def removeDuplicates(linkedList):
    if linkedList.head is None:
        return 
    else:
        currentNode = linkedList.head
        visited = set([currentNode.value]) # With Buffer
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return linkedList

def removeDupsWithoutBuffer(linkedList):
    if linkedList.head is None:
        return
    currentNode = linkedList.head
    while currentNode: # ..................start from head
        runner = currentNode # ............assign runner to current node
        while runner.next: # .............. loop all the runners next values
            if runner.next.value == currentNode.value: # ........compare all next runner value with current node
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return linkedList
            

# Test Example 1
customLL = base.LinkedList()

customLL.generate(10, 0, 99)
print(customLL)

# removeDuplicates(customLL)
removeDupsWithoutBuffer(customLL)
print(customLL)


