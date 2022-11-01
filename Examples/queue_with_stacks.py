# Implement a queue using two stacks
# Stack 1, the items are added as with the first item at the lower end of stack
# To enqueue and item, you simply add the item to the top of stack
# To dequeue an item, you pop the top item into a second stack until you reach the first item in the firts stack
# Then the first item  in the first stack becomes the top item in the second stack
# Then pop the item at the top of the second stack
# Finally, pop all items from the second stack into the first stack

from numpy import insert


class Stack:
    def __init__(self):
        self.list = []
    
    def __len__(self):
        return len(self.list)
    
    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop()
    
class QueueViaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    
    def enqueue(self, item):
        self.inStack.push(item)
    
    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result

customQueue = QueueViaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
customQueue.enqueue(5)

print(customQueue.dequeue())

