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

    def __insert(self, value):
        new_node = Node(value, None)

        if self.empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *values):
        for value in values:
            self.insert(value)
        return self

    
                
    
        
    