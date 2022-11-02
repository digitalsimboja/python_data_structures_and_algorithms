from platform import node


class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return 'The Binary Tree is full'
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return 'Successfully inserted'
    
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return 'Success!'
            else: 
                return 'Not Found!'
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)
    
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.inOrderTraversal(index*2 + 1)
        print(self.customList[index])
    
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])
    
    def deleteNode(self, nodeValue):
        if self.lastUsedIndex == 0:
            return 'No element to delete'
        for i in range(1, self.lastUsedIndex +1):
            if self.customList[i] == nodeValue:
                self.customList[i] == self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return 'The element is successfully deleted'
    
    def deleteBT(self):
        self.customList = None
        
        
