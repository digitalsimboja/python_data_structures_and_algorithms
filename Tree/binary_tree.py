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
