class Node(object):
    
    def __init__(self, data, parent):
        self.left = None
        self.right = None
        self.value = data
        self.parent = parent

    
class BinarySearchTree(object):
    
    def __init__(self, root):
        self.root = root

    def empty(self):
        return self.root == None

        
    
        
    