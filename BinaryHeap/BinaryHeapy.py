class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0 # Number of elements in the heap
        self.maxSize = size + 1
    
def peek(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def sizeHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])

def heapifyInsertNode(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        # Check if the current value is smaller than the parent
        # Minimum heap implies the parent must be smaller than the children
        if rootNode.customList[index] < rootNode.custonList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.custonList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyInsertNode(rootNode, parentIndex, heapType)
    # Maximum heap implies that the parent must be greater than the children
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.custonList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyInsertNode(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return " The binary heap is full"
    else:
        rootNode.customList[rootNode.heapSize + 1] = nodeValue
        rootNode.heapSize += 1
        heapifyInsertNode(rootNode,rootNode.heapSize, heapType)
    return "The value is successfully inserted"

def heapifyExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChildIndex = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp 
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChildIndex = leftIndex
            else:
                swapChildIndex = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChildIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChildIndex]
                rootNode.customList[swapChildIndex] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChildIndex = leftIndex
            else:
                swapChildIndex = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChildIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChildIndex]
                rootNode.customList[swapChildIndex] = temp
        heapifyExtract(rootNode, swapChildIndex, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyExtract(rootNode, 1, heapType)
        return extractNode

def deleteEntireBH(rootNode):
    rootNode.customList = None


newBinaryHeap = Heap(6)
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
extractNode(newBinaryHeap, 'Min')
levelOrderTraversal(newBinaryHeap)