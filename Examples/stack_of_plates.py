# Imagine a stack of plates. If it gets too high, it might topple. 
# Implement a data structure SetOfStacks that mimics this

class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def __str__(self):
        values = [str(x) for x in self.stacks]
        return ''.join(values)
    
    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()
    
    def pop_at(self, stacknum):
        if len(self.stacks[stacknum]) > 0:
            return self.stacks[stacknum].pop()
        else:
            return None
    

customStack = PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
print(customStack.pop())
print(customStack.pop_at(0))

print(customStack)