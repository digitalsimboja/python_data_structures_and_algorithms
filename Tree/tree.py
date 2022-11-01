class TreeNode:
    def __init__(self, data=None, children=[]):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)



root = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])

fanta = TreeNode('Fanta', [])
cola = TreeNode('Fanta', [])

tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])

root.addChild(cold)
root.addChild(hot)

cold.addChild(fanta)
cold.addChild(cola)

hot.addChild(tea)
hot.addChild(coffee)


print(root)