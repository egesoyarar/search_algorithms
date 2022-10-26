class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def createLeaf(value, parent: Tree, side):
    newLeaf = Tree(value)  
    if side:  
        parent.left = newLeaf
    else:
        parent.right = newLeaf

    return newLeaf