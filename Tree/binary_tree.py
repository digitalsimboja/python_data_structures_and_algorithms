from base import Quueue


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Visit the root and keep to the left, when you are done, then continue with the right


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# Visit the left, visit the root, then visit the right


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# Visit the left, visit the right, then visit the root


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# Level order traversal, visit each level starting with the right, when done visit next level


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Quueue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

def searchBinaryTree(rootNode, nodeValue):
    if rootNode is None:
        return "No binary tree to search"
    else:
        customQueue = Quueue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success! Node value exists in binary tree"
            else:
                if (root.value.leftChild is not None):
                    customQueue.enqueue(root.value.leftChild)
                if (root.value.rightChild is not None):
                    customQueue.enqueue(root.value.rightChild)
        return "Node value does not exist in the binary tree"

def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Quueue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "New node successfully inserted"
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "New Node successfully inserted"

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Quueue()   
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        customQueue = Quueue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value == deepestNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild == deepestNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
                if root.value.leftChild:
                    if root.value.leftChild == deepestNode:
                        root.value.leftChild = None
                        return
                    else:
                        customQueue.enqueue(root.value.leftChild)

def deleteNodeFromBT(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQueue = Quueue()
        customQueue.enqueue(rootNode)
        
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                deepestNode = getDeepestNode(rootNode)
                root.value.data = deepestNode.data
                deleteDeepestNode(rootNode, deepestNode)
                return "Node has been successfully deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return 'Failed to delete the node'

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The BT has been successfully deleted'


# TEST


root = TreeNode('Drinks')

fanta = TreeNode('Fanta')
cola = TreeNode('Cola')

tea = TreeNode('Tea')
coffee = TreeNode('Coffee')

leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')

leftChild.leftChild = tea
leftChild.rightChild = coffee

rightChild.leftChild = fanta
rightChild.rightChild = cola

root.leftChild = leftChild
root.rightChild = rightChild





# preOrderTraversal(root)
print("Running  traversal")
# inOrderTraversal(root)
postOrderTraversal(root)

print('Performing a level order traversal')
levelOrderTraversal(root)

print('Performing binary search')
print(searchBinaryTree(root, 'Bread'))

print('Getting the deepest Node')
deepN = getDeepestNode(root)
print('The deepest node is', deepN.data)

print('Deleting the root node')
deleteDeepestNode(root, deepN)
levelOrderTraversal(root)

print('Getting the deepest Node')
deepN = getDeepestNode(root)
print('The deepest node is', deepN.data)

deleteNodeFromBT(root, "Cold")
levelOrderTraversal(root)

deleteBT(root)
levelOrderTraversal(root)

# print('Performing node insertion')
# print(insertNode(root, 'champaigne'))


