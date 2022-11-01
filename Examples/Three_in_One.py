# Use a single list to implement three stacks

class MultiStack:
    def __init__(self, stackSize):
        self.numberstacks = 3
        self.customList = [0] * (stackSize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stackSize
    
    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
    
    def isEmpty(self, stacknum):
        if self.sizes == 0:
            return True
        else: 
            return False
    
    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    
    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return 'The stack is full'
        else:
            self.sizes[stacknum] += 1
            self.customList[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            value = self.customList[self.indexOfTop(stacknum)]
            self.customList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
    
    def peek(self, stacknum):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            print(self.customList)
            value = self.customList[self.indexOfTop(stacknum)]
            return value